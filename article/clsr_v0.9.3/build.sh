#!/usr/bin/env bash
# Rebuild figures, Word manuscript, LaTeX sources and PDFs, ancillary Word files, and run the gate.
# Single source: manuscript.md. Needs: python3 (matplotlib, python-docx, pillow), pandoc >= 3.1,
# pdflatex and xelatex with elsarticle (texlive-publishers), soffice (only for the docx->pdf QA render).
set -euo pipefail
cd "$(dirname "$0")"
export REVIEW_CODE="${REVIEW_CODE:-$(cd .. && pwd)/review_code}"

build_named() {
  # Author-only camera-ready preview with names; never part of the submission upload.
  mkdir -p author_only build/tex_named
  rm -f build/tex_named/*.aux build/tex_named/*.out
  pandoc manuscript.md -s --template build/elsarticle.latex --lua-filter build/filter.lua \
    -V classoption=5p,twocolumn -V twocol=true -V named=true -o build/tex_named/manuscript_named.tex
  ln -sfn ../../Figures build/tex_named/Figures
  ( cd build/tex_named
    for i in 1 2 3; do pdflatex -interaction=nonstopmode -halt-on-error manuscript_named.tex >/dev/null; done )
  cp build/tex_named/manuscript_named.pdf author_only/Preview_two_column_NAMED.pdf
  [ "$(pdftotext author_only/Preview_two_column_NAMED.pdf - | grep -c 'Author preview, not the anonymised submission')" -ge 1 ] \
    || { echo "named preview footer missing"; exit 1; }
}

if [ "${1:-}" = "named" ]; then
  echo "== named author preview (not for submission)"
  build_named
  echo "build OK"
  exit 0
fi

echo "== figures"
for f in figures_src/fig*.py; do python3 "$f"; done

echo "== reference docx"
pandoc -o build/reference_default.docx --print-default-data-file reference.docx
python3 build/make_reference_docx.py build/reference_default.docx build/reference.docx

echo "== Manuscript_anonymised.docx"
pandoc manuscript.md -o build/tmp.docx --reference-doc build/reference.docx \
  --lua-filter build/filter.lua --no-highlight --resource-path=.
python3 build/post_docx.py build/tmp.docx Manuscript_anonymised.docx

echo "== LaTeX (elsarticle): two-column preview and single-column review"
pandoc manuscript.md -s --template build/elsarticle.latex --lua-filter build/filter.lua \
  -V classoption=5p,twocolumn -V twocol=true -o manuscript.tex
pandoc manuscript.md -s --template build/elsarticle.latex --lua-filter build/filter.lua \
  -V classoption=preprint,review,12pt -V linenumbers=true -o manuscript_review.tex
mkdir -p build/tex build/tex_xe
rm -f build/tex/*.aux build/tex/*.out build/tex_xe/*.aux build/tex_xe/*.out
cp manuscript.tex manuscript_review.tex build/tex/
cp manuscript.tex manuscript_review.tex build/tex_xe/
ln -sfn ../../Figures build/tex/Figures
ln -sfn ../../Figures build/tex_xe/Figures
# PDFs are built with pdfLaTeX (Elsevier's route); xelatex is run as a second compile check.
( cd build/tex
  for f in manuscript manuscript_review; do
    pdflatex -interaction=nonstopmode -halt-on-error "$f.tex" >/dev/null
    pdflatex -interaction=nonstopmode -halt-on-error "$f.tex" >/dev/null
    pdflatex -interaction=nonstopmode -halt-on-error "$f.tex" >/dev/null
  done )
( cd build/tex_xe
  for f in manuscript manuscript_review; do
    xelatex -interaction=nonstopmode -halt-on-error "$f.tex" >/dev/null
    xelatex -interaction=nonstopmode -halt-on-error "$f.tex" >/dev/null
  done )
cp build/tex/manuscript.pdf Preview_two_column.pdf
cp build/tex/manuscript_review.pdf Manuscript_anonymised.pdf
for pdf in Preview_two_column.pdf Manuscript_anonymised.pdf; do
  n=$(pdftotext "$pdf" - 2>/dev/null | tr "\f" "\n" | grep -cE '^\[[0-9]+\] ')
  [ "$n" -ge 39 ] || { echo "references missing in $pdf ($n)"; exit 1; }
done

echo "== named author preview (author_only/, not for submission)"
build_named
for pdf in Preview_two_column.pdf Manuscript_anonymised.pdf; do
  [ "$(pdftotext "$pdf" - | grep -ciE 'abbasia|ferreira|author preview')" -eq 0 ] || { echo "name leaked into $pdf"; exit 1; }
done

echo "== ancillary Word files"
python3 build/make_ancillary_docx.py

echo "== concordance gate"
python3 concordance_gate.py
echo "build OK"

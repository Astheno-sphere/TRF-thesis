-- Format-specific handling for the single-source manuscript.md
-- docx: keep everything (keywords paragraph shown in body).
-- latex: drop docx-only blocks, render figures/tables/listing as full-width floats with
--        the caption text exactly as written in manuscript.md (caption* avoids double numbering).

local function latex(blocks)
  return pandoc.write(pandoc.Pandoc(blocks), 'latex')
end
local function inl(inlines)
  return pandoc.write(pandoc.Pandoc({pandoc.Plain(inlines)}), 'latex')
end


-- ---- Algorithm blocks ------------------------------------------------------------------
-- Source form (manuscript.md): a Div.algorithm holding a caption paragraph and a CodeBlock.alg.
-- One line per row:  kind | text | source lines in trf_checker.py [| comment]
-- kind: H (Input/Output header), 0 or 1 (numbered line at that indent), if (numbered condition;
-- the following kind-1 lines are its body). The source-line field is read by concordance_gate.py.
local function split_bar(line)
  local f = {}
  for part in (line .. ' | '):gmatch('(.-) | ') do table.insert(f, part) end
  return f
end

local function alg_rows(el)
  local cap, code
  for _, b in ipairs(el.content) do
    if b.t == 'Para' then cap = b.content elseif b.t == 'CodeBlock' then code = b.text end
  end
  local rows = {}
  for line in code:gmatch('[^\n]+') do
    local f = split_bar(line)
    table.insert(rows, {kind = f[1], text = f[2], src = f[3], note = f[4]})
  end
  return cap, rows
end

local function md_inlines(text)
  return pandoc.read(text, 'markdown').blocks[1].content
end

function algorithm_latex(el)
  local cap, rows = alg_rows(el)
  local out = {
    '\\begin{algorithm*}[!tbp]',
    '\\captionsetup{justification=raggedright,singlelinecheck=false}',
    '\\hrule height 0.8pt\\vspace{3pt}',
    '{\\algcapfont\\raggedright ' .. inl(cap) .. '\\par}',
    '\\vspace{2pt}\\hrule height 0.5pt\\vspace{3pt}',
    '\\small\\linespread{1.05}\\selectfont\\begin{algorithmic}[1]'}
  local open = false
  local function close() if open then table.insert(out, '\\EndIf'); open = false end end
  for _, r in ipairs(rows) do
    local note = r.note and (' \\Comment{' .. inl(md_inlines(r.note)):gsub('\n', ' ') .. '}') or ''
    if r.kind == 'H' then
      local kw, rest = r.text:match('^%*%*(%a+):%*%*%s+(.*)$')
      local cmd = (kw == 'Input') and '\\Require' or '\\Ensure'
      table.insert(out, cmd .. ' ' .. (inl(md_inlines(rest)):gsub('\n', ' ')))
    elseif r.kind == 'if' then
      close()
      table.insert(out, '\\If{' .. (inl(md_inlines(r.text)):gsub('\n', ' ')) .. '}')
      open = true
    else
      local body = r.text
      local ret = body:match('^%*%*return%*%*%s+(.*)$')
      local t
      if ret then t = '\\State \\Return ' .. (inl(md_inlines(ret)):gsub('\n', ' '))
      else t = '\\State ' .. (inl(md_inlines(body)):gsub('\n', ' ')) end
      if r.kind == '0' and open then table.insert(out, '\\EndIf'); open = false end
      table.insert(out, t .. note)
    end
  end
  if open then table.insert(out, '\\EndIf') end
  table.insert(out, '\\end{algorithmic}')
  table.insert(out, '\\vspace{2pt}\\hrule height 0.8pt')
  table.insert(out, '\\end{algorithm*}')
  return pandoc.RawBlock('latex', table.concat(out, '\n'))
end

local TAB = pandoc.RawInline('openxml', '<w:r><w:tab/></w:r>')

local function alg_docx(el)
  local cap, rows = alg_rows(el)
  local blocks = {pandoc.Div({pandoc.Para(cap)}, pandoc.Attr('', {}, {['custom-style'] = 'Alg Title'}))}
  local n = 0
  for i, r in ipairs(rows) do
    local last = (i == #rows)
    local inls, style
    if r.kind == 'H' then
      local kw, rest = r.text:match('^%*%*(%a+):%*%*%s+(.*)$')
      inls = {pandoc.Strong({pandoc.Str(kw .. ':')}), TAB}
      for _, x in ipairs(md_inlines(rest)) do table.insert(inls, x) end
      style = 'Alg Head'
    else
      n = n + 1
      inls = {pandoc.Str(tostring(n)), TAB}
      local body = r.text
      if r.kind == 'if' then
        table.insert(inls, pandoc.Strong({pandoc.Str('if')})); table.insert(inls, pandoc.Space())
        for _, x in ipairs(md_inlines(body)) do table.insert(inls, x) end
        table.insert(inls, pandoc.Space()); table.insert(inls, pandoc.Strong({pandoc.Str('then')}))
        style = 'Alg L0'
      else
        for _, x in ipairs(md_inlines(body)) do table.insert(inls, x) end
        style = (r.kind == '1') and 'Alg L1' or 'Alg L0'
      end
      if last then style = style .. ' End' end
      if r.note then
        table.insert(inls, TAB)
        table.insert(inls, pandoc.Emph(md_inlines(r.note)))
      end
    end
    table.insert(blocks, pandoc.Div({pandoc.Para(inls)}, pandoc.Attr('', {}, {['custom-style'] = style})))
  end
  return blocks
end

if not FORMAT:match 'latex' then
  function Div(el)
    if el.classes:includes('algorithm') then return alg_docx(el) end
  end
end

if FORMAT:match 'latex' then
  function Div(el)
    if el.classes:includes('docxonly') then return {} end
    if el.classes:includes('references') then
      -- v0.9.1 fix: the v0.9 code used table.unpack() in the middle of a table constructor,
      -- which Lua truncates to its first value, so only [1] reached the PDF. Emit a real
      -- thebibliography (elsarticle numbered style) with one \\bibitem per entry instead.
      local out = {'\\begin{thebibliography}{17}', '\\setlength{\\itemsep}{1pt}', '\\raggedright'}
      local n = 0
      for _, b in ipairs(el.content) do
        if b.t == 'Para' then
          local txt = inl(b.content)
          local num, rest = txt:match('^{%[}(%d+){%]}%s+(.*)$')
          if not num then error('reference without [N] label: ' .. txt:sub(1, 60)) end
          n = n + 1
          if tonumber(num) ~= n then error('reference out of order: ' .. num) end
          table.insert(out, '\\bibitem{r' .. num .. '} ' .. rest)
        end
      end
      table.insert(out, '\\end{thebibliography}')
      return pandoc.RawBlock('latex', table.concat(out, '\n'))
    end
    if el.classes:includes('algorithm') then return algorithm_latex(el) end
  end

  function Header(el)
    -- elsarticle's thebibliography prints its own "References" heading
    if el.identifier == 'references' then return {} end
  end

  function Figure(el)
    -- v0.9.1: figures are drawn at final print size. A 90 mm figure (width=90mm in
    -- manuscript.md) is a single-column float at natural size; others span both columns.
    local img
    el.content:walk({Image = function(i) img = i end})
    local src = img.src:gsub('%.png$', '.pdf')
    local cap = pandoc.utils.blocks_to_inlines(el.caption.long)
    local single = (img.attributes.width == '90mm')
    local env = single and 'figure' or 'figure*'
    local w = single and '\\figwsingle' or '\\textwidth'
    return pandoc.RawBlock('latex',
      '\\begin{' .. env .. '}[!tbp]\n\\centering\n\\includegraphics[width=' .. w .. ']{' .. src .. '}\n' ..
      '\\caption*{' .. inl(cap) .. '}\n\\end{' .. env .. '}')
  end

  function Table(el)
    local cap = pandoc.utils.blocks_to_inlines(el.caption.long)
    local ncol = #el.colspecs
    local spec = {}
    for _, cs in ipairs(el.colspecs) do
      local a = cs[1]
      if ncol == 3 then table.insert(spec, '>{\\raggedright\\arraybackslash}X')
      elseif a == 'AlignRight' then table.insert(spec, '>{\\raggedleft\\arraybackslash}X')
      else table.insert(spec, '>{\\raggedright\\arraybackslash}X') end
    end
    local function row(r)
      local cells = {}
      for _, c in ipairs(r.cells) do
        table.insert(cells, (latex(c.contents):gsub('\n+$', ''):gsub('\n', ' ')))
      end
      return table.concat(cells, ' & ') .. ' \\\\'
    end
    local out = {'\\begin{table*}[!tbp]', '\\captionsetup{justification=raggedright,singlelinecheck=false}',
                 '\\caption*{' .. inl(cap) .. '}', '\\small',
                 '\\begin{tabularx}{\\textwidth}{' .. table.concat(spec) .. '}', '\\toprule'}
    for _, r in ipairs(el.head.rows) do table.insert(out, row(r)) end
    table.insert(out, '\\midrule')
    for _, b in ipairs(el.bodies) do for _, r in ipairs(b.body) do table.insert(out, row(r)) end end
    table.insert(out, '\\bottomrule'); table.insert(out, '\\end{tabularx}'); table.insert(out, '\\end{table*}')
    return pandoc.RawBlock('latex', table.concat(out, '\n'))
  end
end

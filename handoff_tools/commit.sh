#!/usr/bin/env bash
# Gated commit: runs the trail inspector first and refuses to commit if any check FAILs.
# Usage: bash handoff_tools/commit.sh "<ID>: message"
# Added 3 Oct 2026 after P03 was committed with check 3 failing.
set -uo pipefail
cd "$(dirname "$0")/.."
python3 handoff_tools/register_sync.py >/dev/null
out=$(python3 handoff_tools/trail_check.py 2>&1)
if echo "$out" | grep -q '^\[FAIL\]' || ! echo "$out" | grep -q '^TRAIL INTACT'; then
  echo "$out" | tail -5
  echo "$out" | grep -A6 '^\[FAIL\]'
  echo "REFUSED: trail_check has FAILs or did not finish; nothing committed."
  exit 1
fi
git add -A
git commit -q -F - <<MSG
$1

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01NcQq1nsLTRuJVxEX8DbgE6
MSG
python3 handoff_tools/register_sync.py >/dev/null
if ! git diff --quiet; then git add -A; git commit -q --amend --no-edit; fi
git log --oneline -1
python3 handoff_tools/trail_check.py 2>&1 | tail -1

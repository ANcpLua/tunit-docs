#!/usr/bin/env bash
# Markdown summary of what changed in TUnit between two release tags, from the GitHub API.
# Usage: scripts/whats-new.sh v1.67.0 v1.68.4 > WHATSNEW.md   (needs gh, authenticated, and jq)
set -euo pipefail

old="$1"
new="$2"
repo="thomhurst/TUnit"
compare="$(gh api "repos/$repo/compare/$old...$new")"

echo "# TUnit $old → $new"
echo
echo "Compare: https://github.com/$repo/compare/$old...$new"
echo

echo "## Releases"
echo
# Every release after $old up to and including $new, oldest first; dependency bumps dropped.
gh api "repos/$repo/releases" --paginate --jq '.[].tag_name' |
  { echo "$old"; echo "$new"; cat; } | sort -uV |
  awk -v o="$old" -v n="$new" '$0==o{on=1; next} on{print} $0==n{exit}' |
  while read -r tag; do
    echo "### $tag"
    echo
    gh api "repos/$repo/releases/tags/$tag" --jq '.body' |
      grep -E '^\* ' | grep -v 'chore(deps)' || echo "_only dependency updates_"
    echo
  done

echo "## Public API"
echo
# The PublicAPI snapshots are TUnit's own record of every public member; net10.0 is enough.
api="$(jq -r '.files[] | select(.filename | test("^tests/TUnit.PublicAPI/.*DotNet10_0\\.verified\\.txt$"))
  | "#### \(.filename | sub("^tests/TUnit.PublicAPI/Tests\\."; "") | sub("_Has_No_API_Changes.*"; ""))\n\n```diff\n\(.patch // "(patch too large — open the compare link)")\n```\n"' <<<"$compare")"
echo "${api:-No public API change.}"
echo

echo "## Library code (src/)"
echo
jq -r '[.files[] | select(.filename | startswith("src/"))] as $f
  | if ($f | length) == 0 then "No change under `src/` — the packages are code-identical."
    else ($f[] | "- `\(.filename)` (+\(.additions) −\(.deletions))") end' <<<"$compare"
echo

echo "## Commits"
echo
jq -r '"\(.total_commits) commits; dependency bumps not listed.\n",
  (.commits[] | .commit.message | split("\n")[0] | select(test("^chore\\(deps\\)") | not) | "- \(.)")' <<<"$compare"

# The compare endpoint returns at most 300 files and 250 commits.
jq -r 'if (.files | length) >= 300 or (.commits | length) < .total_commits
  then "\n> Truncated by the GitHub compare API; the compare link above has the full list." else empty end' <<<"$compare"

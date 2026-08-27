#!/usr/bin/env bash
# Install the dbtips-kol-videos skill so Claude Code can find it.
#
#   ./install.sh                    -> ~/.claude/skills          (all your projects)
#   ./install.sh /path/to/project   -> <project>/.claude/skills  (that project only)
#   ./install.sh --copy [target]    -> copy instead of symlink
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL="dbtips-kol-videos"
SRC="$REPO/skills/$SKILL"

MODE=link
if [[ "${1:-}" == "--copy" ]]; then MODE=copy; shift; fi

if [[ -n "${1:-}" ]]; then
  DEST_DIR="${1%/}/.claude/skills"
else
  DEST_DIR="$HOME/.claude/skills"
fi
DEST="$DEST_DIR/$SKILL"

[[ -d "$SRC" ]] || { echo "error: $SRC not found" >&2; exit 1; }
mkdir -p "$DEST_DIR"

if [[ -e "$DEST" || -L "$DEST" ]]; then
  echo "error: $DEST already exists — remove it first:" >&2
  echo "    rm -rf '$DEST'" >&2
  exit 1
fi

if [[ "$MODE" == link ]]; then
  ln -s "$SRC" "$DEST"
  echo "linked $DEST -> $SRC"
  echo "(git pull in $REPO now updates this install)"
else
  cp -R "$SRC" "$DEST"
  echo "copied $SRC -> $DEST"
fi

echo
echo "Next:"
echo "  1. Install prerequisites (see README.md): aganitha-ie-tools, yt-dlp, baml-py"
echo "  2. cd '$SRC' && baml-cli generate     # builds baml_client/, not committed"
echo "  3. Export GEMINI_API_KEY, AACT_DB_USER, AACT_DB_PASSWORD"

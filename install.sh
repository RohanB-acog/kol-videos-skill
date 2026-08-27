#!/usr/bin/env bash
# Install the dbtips-kol-videos skill so Claude Code can find it.
#
#   ./install.sh                    -> ./.claude/skills          (current project)
#   ./install.sh /path/to/project   -> <project>/.claude/skills  (that project)
#   ./install.sh --global           -> ~/.claude/skills          (every project)
#
#   --copy   copy instead of symlink
#   --force  replace an existing install at the destination
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL="dbtips-kol-videos"
SRC="$REPO/skills/$SKILL"

MODE=link
SCOPE=project
FORCE=0
TARGET=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --copy)   MODE=copy;      shift ;;
    --global) SCOPE=global;   shift ;;
    --force)  FORCE=1;        shift ;;
    -h|--help) sed -n '2,9p' "${BASH_SOURCE[0]}" | sed 's/^# \{0,1\}//'; exit 0 ;;
    -*) echo "error: unknown option $1" >&2; exit 2 ;;
    *)  TARGET="$1"; shift ;;
  esac
done

if [[ "$SCOPE" == global ]]; then
  [[ -z "$TARGET" ]] || { echo "error: --global takes no path" >&2; exit 2; }
  DEST_DIR="$HOME/.claude/skills"
  WHERE="user level — available in EVERY project"
else
  BASE="$(cd "${TARGET:-$PWD}" && pwd)"
  DEST_DIR="$BASE/.claude/skills"
  WHERE="project scope — available only in $BASE"
fi
DEST="$DEST_DIR/$SKILL"

[[ -d "$SRC" ]] || { echo "error: $SRC not found" >&2; exit 1; }

if [[ -e "$DEST" || -L "$DEST" ]]; then
  if [[ "$FORCE" == 1 ]]; then
    rm -rf "$DEST"
  else
    echo "error: $DEST already exists. Re-run with --force to replace it." >&2
    exit 1
  fi
fi

mkdir -p "$DEST_DIR"
if [[ "$MODE" == link ]]; then
  ln -s "$SRC" "$DEST"
else
  cp -R "$SRC" "$DEST"
fi

echo "Installed at $WHERE"
echo "  $DEST"
[[ "$MODE" == link ]] && echo "  (symlink — git pull in $REPO updates it)"
echo
echo "It is a dotfile directory: 'ls -l' will not show it, use 'ls -la'."
echo "Restart Claude Code for the skill to be picked up."
echo
echo "Next:"
echo "  1. Install prerequisites (see README.md): aganitha-ie-tools, yt-dlp, baml-py"
echo "  2. cd '$SRC' && baml-cli generate     # builds baml_client/, not committed"
echo "  3. Export GEMINI_API_KEY, AACT_DB_USER, AACT_DB_PASSWORD"

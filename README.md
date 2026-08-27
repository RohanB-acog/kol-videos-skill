# kol-videos-skill

The `dbtips-kol-videos` Claude Code skill: builds the
`/market-intelligence/kol-videos/` payload for a disease — identifies key opinion
leaders, finds their recorded talks, reads the transcripts, and emits the
13-field KOL record schema the dossier endpoint consumes.

The skill itself lives in [`skills/dbtips-kol-videos/`](skills/dbtips-kol-videos);
its contract and procedure are documented in
[`SKILL.md`](skills/dbtips-kol-videos/SKILL.md) and
[`references/SETUP.md`](skills/dbtips-kol-videos/references/SETUP.md).

## Install (for someone cloning this repo)

```bash
git clone git@github.com:RohanB-acog/kol-videos-skill.git
cd kol-videos-skill

# Scope it to one project (recommended) -> <project>/.claude/skills/
./install.sh /path/to/project

# Or make it available everywhere -> ~/.claude/skills/
./install.sh
```

**The two are different places.** With no argument the skill installs at user
level (`~/.claude/skills/`) and is available in every project — nothing appears
inside the repo you ran it from. Pass a project path to scope it to that project
instead. Whichever you pick, Claude Code has to be restarted to notice it.

`install.sh` symlinks the skill into place, so `git pull` here updates every
install. Pass `--copy` before the path if you'd rather have an independent copy.

Verify: start `claude` in the target project and `dbtips-kol-videos` should be
in the skills list.

To move an install from one scope to the other, delete the old link first:

```bash
rm ~/.claude/skills/dbtips-kol-videos          # or <project>/.claude/skills/...
./install.sh /path/to/project
```

## Prerequisites

Install these once; the skill shells out to them and a missing one stops a run
rather than producing an empty result.

```bash
uv tool install --index https://pypi.aganitha.ai/simple 'aganitha-ie-tools[all]==0.36.0'
uv tool install yt-dlp
pip install baml-py==0.214.0
```

`uv` itself: `curl -LsSf https://astral.sh/uv/install.sh | sh`.

Aganitha's internal PyPI needs auth — run `atk login` first if the
`aganitha-ie-tools` install 401s.

## Build the typed client

`baml_client/` is a build artifact and is **not** committed — every clone must
generate it once, and again after any change to `baml_src/`:

```bash
cd skills/dbtips-kol-videos
baml-cli generate
```

A stale client accepts the old shape and silently drops fields the new one
added.

## Credentials

Export these (or put them in an env file and point `AGANITHA_ENV_FILES` at it):

| Variable | Needed by | Notes |
|---|---|---|
| `GEMINI_API_KEY` | `tools/extract.py` | Required. |
| `AACT_DB_USER`, `AACT_DB_PASSWORD` | trial-people, bridge | Required for the clinical-authority signal. Free registration at aact.ctti-clinicaltrials.org. Without them, trial investigators never enter the candidate pool and the shortlist skews toward people who publish. |
| `NCBI_API_KEY`, `NCBI_API_EMAIL` | PubMed | Optional. 3 → 10 req/s. |
| `OPENALEX_MAILTO` | OpenAlex | Optional. Faster pool. |

## Smoke test

```bash
cd skills/dbtips-kol-videos
uv run tools/candidates.py --search-name "gout" --out /tmp/candidates.json --videos /tmp/videos.json
```

If that returns resolved experts and videos, the install is good. Tunables that
change what a run retrieves are listed in `references/SETUP.md`.

## What is not in this repo

`baml_client/`, `out/`, and the per-disease `run_*/` working directories are
gitignored — they are build artifacts and run scratch, not part of the skill.

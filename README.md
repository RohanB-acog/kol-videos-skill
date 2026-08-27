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

./install.sh                    # this project      -> ./.claude/skills/
./install.sh /path/to/project   # another project   -> <project>/.claude/skills/
./install.sh --global           # every project     -> ~/.claude/skills/
```

**Scope matters and the two locations look nothing alike.** The default is
project scope: the skill lands in `.claude/skills/` inside the target project.
`--global` puts it in `~/.claude/skills/` instead, where it is available
everywhere but nothing appears in the repo.

`.claude` is a dotfile directory, so `ls -l` will not list it — use `ls -la`.
Restart Claude Code after installing; it reads the skills list at startup.
Verify by starting `claude` in the target project and looking for
`dbtips-kol-videos` in the skills list.

Other flags: `--copy` installs an independent copy rather than a symlink (with a
symlink, `git pull` in this repo updates every install). `--force` replaces an
existing install at the destination — needed when moving between scopes:

```bash
rm ~/.claude/skills/dbtips-kol-videos   # drop a previous --global install
./install.sh /path/to/project
```

## Prerequisites

Install these once; the skill shells out to them and a missing one stops a run
rather than producing an empty result.

```bash
uv tool install --index https://pypi.aganitha.ai/simple 'aganitha-ie-tools[all]==0.36.0'
uv tool install yt-dlp
uv tool install baml-py==0.214.0
```

`uv` itself: `curl -LsSf https://astral.sh/uv/install.sh | sh`.

**No virtualenv is needed.** `uv tool install` gives each tool its own isolated
environment and puts the entry point on your PATH, and the scripts in `tools/`
declare their dependencies inline (PEP 723), so `uv run tools/foo.py` builds a
throwaway environment per invocation. There is nothing to activate.

Check the install with `uv tool list` — it should show `aganitha-ie-tools`,
`baml-py`, and `yt-dlp`.

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

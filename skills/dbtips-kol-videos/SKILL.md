---
name: dbtips-kol-videos
description: Build the /market-intelligence/kol-videos/ payload for a disease — identify the key opinion leaders, find their recorded talks, read the transcripts, and emit the 13-field KOL record schema the dossier endpoint consumes. Use when asked to generate, refresh, or QC KOL videos for a disease dossier.
---

# dbtips KOL videos

Produces the payload stored under `/market-intelligence/kol-videos/` in
`cached_data_json/disease/<disease>.json`.

**This file is yours.** `references/` is generated and is replaced wholesale on
upgrade — never hand-edit inside it. Re-run `aganitha-ie-skill-creator` with the
same facets to upgrade.

## Contract

A bare JSON list of records — no disease wrapper — each with exactly these 13
keys, every value a string or null:

```
search_name  video_id  title  kol_name  affiliation  expertise  opinion
video  publications  published_date  view_count  channel_name  duration_seconds
```

Two properties of the data that decide correctness:

- **`kol_name` is the identity key.** One person must appear under exactly one
  spelling across every record, because consumers group on this string. Getting
  it wrong splits a person in two, and no downstream fix can undo that.
- **`opinion` may legitimately be null** — a video with no extractable stance is
  a finding, not a failure. Emit the null and say why in the run record. Do not
  substitute the description to fill the field; that is what produces marketing
  copy in place of a clinician's view.

## Procedure

1. **Verify tools.** `aganitha-ie-people`, `yt-dlp`, `baml-cli`, and a built
   `baml_client/`. See `references/SETUP.md`. A missing tool stops the run.
2. **Candidates and video discovery.**
   ```bash
   uv run tools/candidates.py --search-name "<disease>" \
       --out candidates.json --videos videos.json
   ```
   Read the `resolve_disease_notes` it returns. If the disease did not resolve
   to a MeSH heading, the trial signal is thin and the run is a floor.
3. **Gate on the transcript.** A video with no captions is not analysed: no
   classification, no extraction, no record. `tools/extract.py` exits 3 and says
   `no_transcript`. Count it in `videos_considered` so the denominator stays
   honest, and never let a fetch failure become a null-opinion record — the two
   are different states and only one is a fact about the video.
4. **Extract.** One call per transcript segment, not per video: the full
   transcript is kept and split at `DBTIPS_KOL_CHUNK_CHARS` with
   `DBTIPS_KOL_CHUNK_OVERLAP` repeated across each boundary. Each segment is
   analysed with the running extraction carried forward, so a stance developed
   over a whole talk accumulates rather than being re-derived from a fragment.
   Truncating instead would discard the back of a long talk — which is where the
   argument usually is, since the introduction is at the front.
   ```bash
   uv run tools/extract.py <video_id> --search-name "<disease>" \
       --candidates candidates.json > out/<video_id>.json
   ```
5. **Validate every extraction.** `uv run tools/validate.py out/<video_id>.json`
6. **Assemble.** Keep only records from videos assessed `video_type == "KOL
   interview"` **and** `discusses_disease == true`. Concatenate their `records`
   arrays into one list and write it under the endpoint key.
7. **Report** what was examined, not only what was found: videos considered,
   how many had transcripts, how many yielded records, and every expert with no
   video — recorded as absent, not dropped.

## Decision points

Resolved without a person, because this runs headless under `build_dossier.py`:

- **A KOL named in a transcript but absent from `candidates.json`.** Emit them,
  take the spelling from title or description rather than captions, and log an
  assumption.
- **Transcript affiliation disagrees with the candidate record.** Emit the
  candidate's; log a conflict carrying both readings.
- **No transcript available.** Set `transcript_available` false. Do not let a
  fetch failure become an empty finding about the video.
- **A record whose `opinion` would be null despite a transcript.** Keep it and
  say so: captions existed, the video simply carried no stance. That is a
  finding. Only absent captions cause a drop, and that happens at step 3.

## Known limits

- `aganitha-ie-people videos` searches the **person**, not the disease, so a KOL
  absent from the shortlist is unreachable no matter how much they are on
  camera. Widen `DBTIPS_KOL_SHORTLIST` before concluding coverage is complete.
- Without `AACT_DB_USER` / `AACT_DB_PASSWORD` the clinical signal is absent
  entirely and the shortlist skews toward people who publish.
- Auto-captions mistranscribe names constantly. The canonical spelling from the
  candidate stage always wins over one heard in a transcript.
- Grant signal is NIH-only. Absence there says nothing about a non-US expert.

## Note on the current consumer

`frontend-locked-new/.../kolCard.tsx` dereferences `opinion.length` with no null
guard, so a null `opinion` crashes its card view. **That is a bug in that
component, not a constraint on this skill.** Fix it there. Suppressing valid
records here to avoid it trades a visible crash for silent data loss, and leaves
the next consumer with the same trap.

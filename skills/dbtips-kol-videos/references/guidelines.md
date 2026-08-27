<!-- guideline-set 06baa528522f · cut 2026-08-20 · 96 guidelines · selection: source_types=[video-and-recordings, literature, trial-registries]; access=[networked]; industries=[biomedical, biopharma]; formats=[video, audio, html] -->

# Guidelines — dbtips KOL videos

Generated snapshot. **Never hand-edit.** Regenerate by re-running
 with the same facets; this directory is replaced wholesale.

---

# A prevalence figure travels with four facts or it is not a finding

`a-burden-figure-is-four-facts-or-it-is-noise` · MUST · output-contract

**Rule.** Never emit a prevalence, incidence or burden number on its own. Every
value carries, as structure and not as surrounding prose, four things:

1. **What was measured, and by what test.** The metric and its diagnostic
   threshold — body-mass index at or above 30, fasting glucose ≥ 7.0 mmol/L,
   two clinic readings above 140/90 — and whether the estimate is **crude or
   age-standardised**.
2. **In whom.** Country or region, age band, sex, and every other dimension that
   defined who was counted, including the ones that look like defaults.
3. **Over what period.** The year or window the estimate refers to, which is
   not the year it was published.
4. **How uncertain.** The interval and what kind it is; where the source
   published none, that absence, stated.

The four are a unit. A value separated from them cannot be compared to anything,
and the separation usually happens in the last step, when a carefully assembled
table is summarised into a sentence.

**Prevents.** Two figures being called a disagreement, a trend, or a market when
they are answers to different questions. Crude and age-standardised obesity
prevalence for 2016 differ by more than 10% relative in **69 of 199 countries**,
and the sign flips with the age structure — Italy's crude estimate is 23% above
its age-standardised one, Malawi's is 18% below. Neither number is wrong; a
chart mixing them is. The same failure produces a screening-detected prevalence
compared against a symptomatic one, an adult figure against an all-ages figure,
and a point estimate quoted to three digits whose interval spans a factor of two.

**Applies when.** Any epidemiological quantity, from any source — an agency
dashboard, a modelled global estimate, a registry study, a systematic review.
It applies hardest where the source is authoritative, because an authoritative
number is the one most likely to be quoted onward without its qualifiers.

**Verify.** Every value in the output can be traced to all four facts without
consulting the source again. A reader can tell, from the record alone, whether
any two values in it may be put on the same axis. A summary that reduces a value
to a single number states the four facts alongside it or does not make the
comparison.

**Source.** Stated 2026-08-16 while building WHO GHO access. The API returns a
row whose fields carry all four, and every one of them is easy to drop on the
way to a sentence.

---

# What a document calls its sections is not a value for a controlled field

`a-document-s-own-grouping-is-not-a-category` · MUST · extraction

**Rule.** When assigning a category from a controlled vocabulary, derive it from
what the item is, not from the heading, panel name, order set, or section title
the document filed it under. Capture the document's own grouping separately if
it is worth keeping.

The same holds for the wording of a title. Classify by what was done and why,
not by the verb the document chose: a procedure titled as excisional may still
be diagnostic, and the stated purpose decides.

**Prevents.** A source's local filing convention leaking into a field consumers
filter on. Two documents group the same item differently, so the category stops
partitioning anything — and because each individual assignment looks defensible,
this is found only when someone tries to use the field.

**Applies when.** Every controlled-vocabulary field populated from a document
that has its own organising scheme.

**Verify.** Group the corpus by category and by the source's own section names.
If the two match closely, the header is being copied rather than the item
classified.

**Source.** Harvested from clinical-ingest's lab extractor, where a panel is
assigned per analyte from a fixed taxonomy — never the document's own order-set
name — after two real leaks of exactly that kind.

---

# A missing credential is not a source decision — ask for it

`a-missing-credential-is-not-a-source-decision` · MUST · acquisition

**Rule.** When the source the run needs is unreachable because a credential is
absent, **stop and ask for the credential**, naming the variables required and
the exact page where the user obtains them. Do not substitute a different
source, a different access path, or a narrower subset of the same source, and do
not proceed on whatever happens to be reachable without authentication.

Most sources worth using have two doors: an authenticated one built for volume,
and an open one built for looking up a single record. They are not the same
source with different keys — they differ in coverage, in freshness, in which
fields exist, and in whether the joins the question needs are possible at all.
Walking through the open door because the key is missing answers a different
question under the name of the one that was asked.

The user chose the source ([[consumer-selects-sources]]). Swapping it is a
scope decision made on their behalf, and one they cannot see in the output.
Asking costs a message; a credential is usually a free registration.

If the user, having been asked, says to proceed anyway, that is their decision to
make. Then the substitution is explicit and must be recorded as one — which
source was used, which was intended, and what the difference costs
([[record-scope-narrowing]], [[report-skipped-sources]]).

**Prevents.** An answer indistinguishable from the real one and built on
something thinner. A per-record lookup API cannot compare hundreds of records,
so the fallback quietly becomes a small sample presented as a landscape; a free
tier silently truncates; an unauthenticated view omits the fields that were the
point. Nothing in the output marks any of this, and the person reading it has no
way to know the source changed.

**Applies when.** Any run against a source requiring authentication, including
one whose public tier appears to answer the same question. Most acute where the
open path exists and looks serviceable — that is what makes the substitution
tempting rather than obviously wrong.

**Verify.** For every run, either the intended source was reached, or the run
stopped and asked, or the output names the substitution and its cost. A result
that mentions no credential problem and no substitution should have come from
the intended source.

**Source.** Stated 2026-08-12 for the AACT mirror of ClinicalTrials.gov, whose
public instance is free but requires registration at
`https://aact.ctti-clinicaltrials.org/users/sign_up`, and whose REST alternative
is built for single-trial lookup and cannot support the joined, many-trial
queries the registry work depends on.

---

# Trials with no results are a population you can count, and they are not a random sample

`a-missing-result-is-measurable-and-not-random` · SHOULD · triangulation

**Rule.** When a landscape rests on reported results, establish how many
relevant trials reported nothing, and treat that group as data rather than as
the part you could not reach. Non-reporting correlates with unfavourable
outcomes, so the trials missing from an evidence base are systematically the
ones that would have changed it.

Three states, and collapsing them loses the whole signal:

- **Not due** — the trial is outside the reporting requirement, or its deadline
  has not arrived. An absence here is expected and carries no information
  ([[expected-absence-is-not-a-gap]]).
- **Due and reported**, on time or late. Lateness is itself a signal.
- **Due and never reported.** This is a positive finding about the trial and its
  sponsor, not a gap in your search ([[capture-stated-negatives]]).

**Where to get it.** The FDAAA TrialsTracker, from the Bennett Institute at
Oxford, computes this for trials covered by the US FDA Amendments Act and
publishes it at `fdaaa.trialstracker.net/api/`. Per trial it gives
`results_due`, `has_results`, `has_exemption`, `status` (reported,
reported-late, overdue) and `days_late`; per sponsor it aggregates across their
portfolio. Roughly 50,000 trials, refreshed daily.

Two limits worth carrying. Its status is a **derived label, not a registry
field** — an inference from registry data under the project's stated method, so
record it as their determination rather than as a fact from the registry
([[carry-the-trigger-for-a-derived-label]], [[mark-a-secondary-mention]]). And
its scope is FDAAA, so it says nothing about trials outside that law: a trial
absent from the tracker is out of scope, not compliant.

The project also argues a position about non-reporting. That argument is worth
reading and is not a finding — attribute it
([[mine-commentary-for-analysis-not-just-news]]).

**Prevents.** An evidence base that looks complete because everything in it is
real. If a third of the relevant trials never reported, a summary of the
remainder is not a summary of the evidence, and its bias points one way. The
sponsor-level view catches the sharper version: a company whose portfolio
reports poorly will look better in any landscape built from published results
than one that reports everything.

**Applies when.** Any claim about what the evidence shows for an indication,
mechanism, or agent — as opposed to what one named trial found.

**Verify.** The output states how many relevant trials had no reported results
and how many of those were due. A landscape that reports only what it found has
not established its own denominator ([[record-what-was-in-scope]]).

**Source.** Stated 2026-08-12. API and field names checked the same day;
the service reported 49,862 trials and a sponsor record updated the previous day.

---

# A name no vocabulary knows, that the corpus does know, is a rename in flight

`a-name-no-vocabulary-knows-is-not-a-rare-disease` · MUST · source-selection

**Rule.** When a term resolves to nothing in every controlled vocabulary you
consult *and yet returns records in the corpus*, do not report the record count.
That combination is not a rare condition — it is the signature of a subject
renamed faster than the vocabularies were revised, and the count you are holding
is a rounding error against the real one.

Look for the bridge in **co-occurrence inside the matched records**: what else
those records name alongside the unknown term. During a changeover, authors and
sponsors write the old name beside the new one on the same record, and that
co-listing is the only machine-readable link that exists before the vocabularies
catch up. It disappears once adoption completes, which is when it stops being
needed.

**Rank the leads; do not pick one.** A co-listed term may be the former name, a
comorbidity, a parent category or a co-enrolled population, and at the counts
involved these are indistinguishable by frequency. Where the corpus separates
what the author wrote from what an indexer assigned, prefer the author's own
strings — an assigned hierarchy attaches every ancestor, which co-occurs with
the record without being its subject. Confirm the rename against the literature
that announced it, then resolve the established name and query **both**
([[resolve-the-query-term-before-you-trust-a-zero]],
[[a-record-matching-a-disease-is-not-about-it]]).

**Prevents.** Two silent failures at once, in opposite directions. Querying the
new name returns a handful of records and presents a major disease as a rare one.
Querying the established name — the correct, current, fully-resolved query —
silently drops every record filed under the new name alone, and those are the
newest records in the field, so the loss falls entirely on what is happening
now. Neither run reports an error; both look like clean answers.

**Applies when.** Any vocabulary-backed source, at any time a subject is being
renamed — which is continuous somewhere in a field. Nomenclature bodies revise
on their own schedule and a consensus rename reaches a registry the day it is
announced and an ontology months later. Suspect it whenever a plausible,
current, well-formed term resolves to nothing.

**Verify.** For any term that resolved to nothing in every vocabulary, the run
record shows either the co-occurrence lookup and what it returned, or an explicit
statement that the corpus had no records for it either. A run that reports a
record count for an unresolved term, without saying that it resolved nowhere,
has published a number it cannot support.

**Source.** Measured 2026-08-15. PCOS was renamed *polyendocrine metabolic
ovarian syndrome* by global consensus published in The Lancet earlier that year.
Neither EFO nor MeSH returned anything for the new name or its acronym, while
AACT already carried trials under it. A query on the new name returned 2 trials;
the disease has 1,059. A query on PCOS could not see the newest of them —
recruiting, listing only the new name, carrying no MeSH terms at all. One trial
listed both names, and that co-listing was the entire bridge.

---

# A preprint carries no review, and the record must say so in a field

`a-preprint-is-not-evidence-until-it-says-which` · MUST · extraction

**Rule.** Mark every record with its review status as structure, never as an
inference from where it was found. A preprint is unreviewed; a published paper
has been through review of unstated quality; a Google Scholar hit may be either
and the source does not say. Those are three different values, and the third is
`unknown`, not `false`.

For a preprint, also carry whether a **published version exists**. That is the
question worth asking about a preprint and it is not answerable from the
preprint record alone: a preprint with a published version has been reviewed and
the reviewed text may differ from what is indexed; a preprint without one, after
long enough, may have failed review or been abandoned. Both readings matter and
neither is available from a date and a server name.

Never mix reviewed and unreviewed records into one evidence table without the
column present.

**Prevents.** An unreviewed claim being counted as evidence because it appeared
in a list beside reviewed work. The failure is entirely one of presentation: the
retrieval was correct, the record was correct, and the table lost the one
distinction that decides how much the reader should believe it.

It also prevents the opposite error of discarding preprints wholesale. In a fast
field the preprint is often the only account of the newest work, and in rare
disease it is sometimes the only account at all — excluded silently, that is a
recall failure the output cannot show.

**Applies when.** Any retrieval that spans more than one index, and any output
that places records from different sources in one list. Also whenever a citation
count is used, since preprint and published versions accumulate citations
separately and neither figure is the total.

**Verify.** Every record has an explicit review-status value. Preprints carry a
published-version field that is either populated or explicitly unchecked. No
table mixes the categories without a visible column, and no count aggregates
across them without saying so.

**Source.** Stated 2026-08-17 while building preprint retrieval through Europe
PMC, which returns bioRxiv, medRxiv, Research Square and SSRN records in the same
shape as peer-reviewed ones.

---

# A rate needs a denominator that can carry it

`a-rate-needs-a-denominator-that-can-carry-it` · MUST · extraction

**Rule.** Before reporting a proportion, a percentage, or a "most common"
ranking, check the denominator it rests on. Where the denominator is too small
to support the claim, **withhold the claim and keep the underlying counts**,
stating why the rate was not computed.

Report the numerator and denominator together — `2/4`, never `50%`. A percentage
strips exactly the information a reader needs to judge it, and one derived from
a handful of subjects reads identically to one derived from thousands.

**Withholding a claim is not deleting data.** The row stays, with its counts and
its denominator; only the derived rate and any ranking built on it are held back,
with the reason recorded. Filtering the small groups out upstream instead
destroys the evidence and silently changes the population every later number is
computed over ([[capture-stated-negatives]],
[[do-not-invent-rows-for-unmeasured-members]]).

Rankings are the sharpest case. "Most common adverse event" computed across arms
of wildly different sizes is decided by the smallest arms, where one additional
patient moves the rate by tens of points.

**Prevents.** A confident percentage that one patient would overturn, and a
"most frequent" claim that ranks a 3-patient arm above a 300-patient one. These
survive review because the output shows a clean number with no denominator
attached, and they are most damaging where they matter most — small
rare-disease cohorts and early-phase dose groups, exactly where readers are
hungriest for a signal.

**Applies when.** Any proportion, rate, incidence, response percentage or
frequency ranking, from any source. Small arms are not an edge case: 15% of the
adverse-event rows in ClinicalTrials.gov have five or fewer subjects at risk.

**Verify.** Every reported rate carries its numerator and denominator. Every
withheld rate carries the reason it was withheld and still shows its counts. An
output containing bare percentages has not applied this rule.

**Source.** Carried over from the angiosarcoma case portal's
`clinical-trials-ingest`, which excludes arms with five or fewer subjects at risk
from "most common adverse event" claims while keeping the rows themselves, and
records a `no_qualifying_reason` when it does.

Measured 2026-08-12 against the AACT mirror: of 11,958,347 adverse-event rows
carrying a subjects-at-risk figure, **1,795,751 — 15.0% — rest on five or fewer
subjects**, and 4,815,629 on twenty or fewer.

---

# A record that matches a disease is not a record about it

`a-record-matching-a-disease-is-not-about-it` · MUST · extraction

**Rule.** Matching a query term is not the same as being about the term. Before
counting a matched record into a landscape, decide whether the disease is the
subject or one entry in a list, record which, and report the two populations
separately.

The measure that works is **how large a share of the record's declared subject
the queried term occupies**, not whether the term appears. In a trial registry
that is the fraction of the trial's listed conditions the disease accounts for;
in a paper it is whether the disease is the study population or one of many
mentioned. Basket, umbrella, platform and agnostic designs enrol a mechanism
across many tumour types, and each one matches every disease it lists.

**Keyword detection on the design name does not work.** The words `basket`,
`umbrella` and `platform` are terms of art that sponsors mostly do not put in
the title. The titles say "Rare Tumors", "Rare Solid Tumors", "Agnostic Therapy
in Rare Solid Tumors". Search for the design name and you will find almost none
of them.

Neither population is the wrong answer, and neither should be silently dropped.
A basket trial is genuinely a treatment option for the disease and belongs in a
patient-facing answer; it is not evidence of a dedicated development programme
and must not be counted as one in a competitive read. **Report both counts and
say which question each answers.**

**Prevents.** A rare-disease landscape inflated several-fold, in the direction
nobody checks. Every basket trial listing the disease is counted as a programme
in it, so a field with a handful of dedicated trials reports dozens, and the
conclusion — that the area is active and competitive — is the opposite of the
truth. The same error makes a "no dedicated trials exist" finding impossible to
reach, because the dedicated count is never computed separately.

**Applies when.** Any count, landscape, or competitive read keyed on a disease.
Most severe in rare disease and oncology, where basket designs are common and
the dedicated population is small enough that a few baskets dominate it, and
where the answer is most likely to be used for a decision.

**Verify.** The output reports the matched total and the dedicated subset as two
numbers, states the rule used to separate them, and names the borderline records.
A single trial count for a rare disease, with no dedicated subset beside it, has
not made the distinction.

**Source.** Carried over from the angiosarcoma case portal's
`clinical-trials-ingest`, whose `classify_relevance()` tags every record
`dedicated` or `basket-umbrella` on a majority-share heuristic and which names
never dropping that tag as its first non-negotiable.

Measured 2026-08-12 against the AACT mirror, on the 91 trials indexed to MeSH
`hemangiosarcoma`: only **18 carry angiosarcoma as at least half their listed
conditions — 73 of 91, 80%, list it as a minority**. Thirty list more than five
conditions and eight list more than twenty, topping out at 94 conditions
(`NCT02834013`, "Nivolumab and Ipilimumab in Treating Patients With Rare
Tumors") and 41 (`NCT06638931`, "Agnostic Therapy in Rare Solid Tumors"). **Not
one of the 91 contains `basket`, `umbrella` or `platform` in its brief title**,
which is why the share measure is the rule and keyword matching is not.

---

# The structured columns of a registry are the index, not the content

`a-registry-record-is-mostly-prose` · SHOULD · extraction

**Rule.** Treat a trial registry as a set of documents with a structured index
in front of them, and extract from the prose. Phase, status, and enrolment are
already structured and need no extraction; what needs reading is everything
written in English by a human.

Where the content actually is:

- **Eligibility criteria** — a free-text block, sometimes thousands of words,
  carrying the real patient definition: biomarker requirements, prior-therapy
  limits, washout periods, organ-function thresholds. The structured age and sex
  columns beside it capture almost none of this.
- **Outcome definitions** — what was actually measured, how, and over what
  window. Two trials reporting "overall response rate" may be measuring
  different things, and only the definition text says so.
- **Arm and intervention descriptions** — dose, schedule, route, and combination
  structure, written as prose per arm rather than as fields.
- **Titles and summaries** — where the design intent is stated plainly, often
  more plainly than in the eventual publication.
- **Condition and intervention names as submitted** — non-standard, sponsor-
  chosen, and the reason exact-match querying needs
  [[resolve-the-query-term-before-you-trust-a-zero]].
- **Results sections**, where posted — adverse-event tables and outcome
  measures with their own descriptive text.

Keep the submitted wording alongside anything you normalise
([[preserve-the-surface-form]]), and record which registry field each value came
from, because a value from an outcome definition and one from a title carry very
different authority ([[provenance-on-every-value]]).

**Prevents.** Producing a trial landscape that is a table of phases and statuses
— information already available from any registry front-end, and none of the
reason anyone asked. The comparison a researcher actually wants is whether two
trials enrolled the same patients and measured the same endpoint, and both of
those live only in the prose.

**Applies when.** Any registry extraction beyond counting trials.

**Verify.** For a set of trials, the extraction can answer whether their
eligibility criteria differ materially. If it can only report phase and status,
the prose was not read.

**Source.** Stated 2026-08-11: the valuable data in ClinicalTrials.gov is
English — indications, drug names, inclusion and exclusion criteria, endpoint
definitions, arm and intervention descriptions, and results documents.

---

# The same trial result is published several times, and the versions disagree

`a-result-has-a-disclosure-history` · MUST · triangulation

**Rule.** A trial result is not one number with one date. It surfaces in stages,
each with different completeness, independence, and delay, and later stages
routinely restate earlier ones differently. Record which stage a number came
from, its data cutoff, and what the earlier stages said.

The usual order:

1. **Company press release** — first, often within weeks of database lock, and
   the version most people will quote. Topline only: the endpoints that read
   well, little method, no protocol. Findable through the wires and financial
   news sites as much as through the company.
2. **Conference abstract, poster, or presentation** — more detail, still curated
   and often under an embargo that shaped the press release. The deck carries
   numbers that appear nowhere else for a year or more
   ([[mine-decks-for-science-not-just-status]]).
3. **Registry results posting** — structured and legally required in several
   jurisdictions, but frequently late, sometimes absent, and posted without
   narrative. In AACT this is `outcomes`, `outcome_measurements`,
   `outcome_analyses`, `reported_events` and `baseline_measurements`.
4. **Peer-reviewed publication** — full method and analysis population at last,
   and the authority for the result ([[prefer-the-authoritative-version]]). It
   arrives late, and trials that read badly are published less often and later,
   so the published set is not the conducted set.
5. **Independent synthesis** — Cochrane reviews and other meta-analyses. The
   most careful reading available and the least current, and a synthesis rather
   than a source ([[synthesis-is-not-independent-corroboration]]).

**Expect the versions to differ**, and treat a difference as a finding rather
than an error to reconcile ([[report-disagreement]]). Legitimate causes are
common: a later data cutoff, a switch from investigator assessment to blinded
review, a different analysis population, or a rounding and framing choice in the
release. Record all readings with their stage and cutoff; do not overwrite an
earlier number with a later one silently.

**Getting from a trial to its publications.** The registry usually links them:
in AACT, `study_references` carries `pmid`, `citation` and `reference_type`,
and `documents` and `provided_documents` carry URLs for protocols, statistical
analysis plans and results documents. Follow those before searching, and note
that a missing link is not evidence of no publication.

**Prevents.** Reporting a press-release number as the trial's result years after
the publication revised it, or carrying two versions of one result as two
independent findings. The reverse also matters: ignoring the earlier stages
loses everything about a trial whose results were presented and never published,
which is a large share of them.

**Applies when.** Any extraction of a trial outcome, and every comparison
involving one.

**Verify.** For each reported result, the record names the disclosure stage and
the data cutoff. If a value has neither, it cannot be placed in this sequence and
its agreement or disagreement with any other source means nothing.

**Source.** Stated 2026-08-11: results appear first in company press releases,
then conference presentations and trade press, then peer-reviewed publications,
then independent meta-analyses. AACT table names checked against its data
dictionary.

---

# A retracted paper returns from every query and reads exactly like evidence

`a-retracted-paper-is-still-in-every-search-result` · MUST · extraction

**Rule.** Check retraction status on every record before it enters a result set,
and carry the status as a field rather than dropping the record silently. A
retraction removes nothing from an index: the paper still matches the query,
still has an abstract, still has citations — many of them accrued after the
retraction — and nothing in the text says it was withdrawn.

Check **both** available signals, because they disagree. PubMed records it as a
publication type on the retracted article (`Retracted Publication`, and
separately `Expression of Concern`); OpenAlex carries an `is_retracted` boolean.
A paper flagged by either must not be cited as evidence.

Return the record with the flag rather than filtering it out. A dropped record
is invisible, and the reader cannot tell whether it was never found or found and
excluded ([[record-what-was-in-scope]]).

**Prevents.** Building a conclusion on withdrawn work. This is not rare and it is
not confined to obscure venues: retracted papers continue to be cited for years,
and citation counts — the usual proxy for importance — actively favour the
notorious ones, so a relevance ranking that weights citations promotes exactly
the papers most likely to be retracted.

Also prevents the quieter failure of a corpus that was silently filtered, where
a later reader cannot audit what was removed or why.

**Applies when.** Any retrieval from a literature index, including one done to
support something else — a burden estimate, a KOL list, a trial's published
results. It applies hardest to older, highly-cited work, which is where both the
retraction risk and the citation weight concentrate.

**Verify.** Every record in the output carries a retraction field with an
explicit value, including `false`. No record was removed from the set without a
count and a reason appearing in the notes. Any figure quoted from a flagged
paper is either removed or labelled.

**Source.** Stated 2026-08-17 while building literature retrieval: PubMed marks
retraction as a publication type that a caller has to ask for, and a record
fetched without checking it is indistinguishable from a sound one.

---

# A link to a search is not evidence that anything was found

`a-search-url-is-not-a-citation` · MUST · provenance

**Rule.** A URL containing a query — a term parameter, a search path, a results
page — never stands as provenance. Provenance points at a specific, stable
resource: the abstract, the grant record, the study page, the profile, the
video. If no specific URL can be found after genuinely looking, record that it
was not found.

A search link may still be offered as a navigation aid, but only where the
record already states the reference is unresolved. It supplements a declared
gap; it never fills one.

**Prevents.** The most common way an agent fabricates evidence while appearing
to cite it. A search URL looks like a citation, passes a link check, and proves
nothing — results change, and the item may never have been in them. Unlike a
missing citation, which is visible, this one survives review because it is
clickable.

**Applies when.** Every provenance record. Most acutely where a claim is about a
person or an organisation rather than a document, since those are the hardest to
pin to a stable page and the easiest to gesture at with a search.

**Verify.** Scan the output's URLs for query parameters and search paths. Each
hit is either a declared-unresolved navigation aid or a defect.

**Source.** Harvested from kol-finder, which names this "the most common way
agents fake evidence while appearing to link sources." The navigation-aid
carve-out resolves a conflict with media-deep-ingest, which builds a search link
for citations it has already recorded as unresolved.

---

# Registry IDs are standardised; the names everyone actually uses are not

`a-trial-has-a-codename-and-an-id` · MUST · entity-resolution

**Rule.** A trial has a registry identifier and a sponsor-assigned codename, and
almost nothing outside the registry uses the identifier. Papers, conference
abstracts, investor decks, press releases and analyst commentary all say
KEYNOTE-189 or CheckMate-227 or DESTINY-Breast04. Resolve between the two before
searching either, and carry both on every record.

Three properties that break naive matching:

- **A codename prefix is a programme, not a trial.** One prefix spans dozens or
  hundreds of numbered trials across indications. Matching on the prefix alone
  gathers an entire development programme; matching on the full codename gets
  one trial, and only if the numbering is written the same way.
- **The numbering is written inconsistently** — hyphenated, spaced, zero-padded
  or not, sometimes with a suffix for a sub-study or a cohort. Treat it as a
  fuzzy string, not a key.
- **A codename is not unique across companies**, and a trial run jointly can
  appear under each partner's naming scheme.

The registry usually records the codename somewhere — an acronym field, the
brief title, or the official title — but not reliably and not in a dedicated
column, so recovering it means reading text
([[a-registry-record-is-mostly-prose]]).

**Prevents.** Failing to connect the paper, the deck, and the registry record
for one trial, and therefore counting it as three pieces of evidence — or
missing it entirely when a landscape assembled from registry IDs is checked
against commentary that only ever uses codenames. This is the same molecule
problem one level up ([[search-every-name-a-drug-has]]).

**Applies when.** Any work that crosses between the registry and anything
written about it, which is most trial intelligence.

**Verify.** For each trial in the output, both the registry identifier and the
codename are present, or the record says the codename could not be found. A
landscape keyed only on NCT numbers cannot be reconciled with any external
source by anyone.

**Source.** Stated 2026-08-11: companies refer to their trials by codename, and
trial IDs are the only standardised part.

---

# Nothing found by one reading strategy is a reason to try another, not a finding

`a-zero-result-may-be-the-parser` · MUST · extraction

**Rule.** When a parse that should have produced records produces none, try the
other layouts that source type is known to use before concluding the content is
absent. Record which strategies were attempted.

**Prevents.** Reporting that a note lists no medications, when the medications
were in a bulleted list and the run only tried a table parser. The output is
empty, well-formed, and confidently wrong — and the same document type routinely
arrives in both layouts from the same system.

**Applies when.** Any source class that renders the same content more than one
way: tables versus lists, multi-column versus single-column, a structured export
versus a printed view. Distinct from [[tool-failure-is-not-a-finding]], which
concerns a tool that errored; here the tool succeeded and found nothing.

**Verify.** For any empty section in the output, the run record lists the
strategies tried.

**Source.** Harvested from clinical-ingest's oncology-note extractor: "If the
medication section yields 0 records from a table approach, fall back to the
bulleted-list parser before concluding there are no medications."

---

# An announcement dates a claim, not a programme

`an-announcement-dates-a-claim-not-a-programme` · MUST · triangulation

**Rule.** A pipeline disclosure is evidence that someone made a claim on a date.
It is not evidence that the programme exists now. Record the source, the date
and the wording, and never carry a stage forward as a current fact.

Everything about a pre-registry asset comes from an interested party. A company
press release, a pipeline page, an investor deck and a filing are all the
developer's own account of itself, written to an audience it is raising money
from. That does not make them false — a 10-K carries disclosure obligations —
but it makes them claims with an author, a date and a purpose.

**"Preclinical" and "development candidate" have no regulatory definition.** No
authority certifies either term, and a company chooses when to apply it. Two
companies using the same phrase may be years apart in reality, and the same
company may use it for a molecule and for a research programme with no molecule
in it.

**Assets are discontinued silently.** A programme is announced with a press
release and dropped without one; it simply stops appearing on the pipeline page.
So the absence of recent news is not evidence of continuation, and a candidate
list assembled from announcements will always over-count what is live. Where the
question is whether a programme is still running, the last dated evidence is the
answer to report, not a current status.

**Prevents.** Reporting a company's marketing language as an assessed
development stage; treating a three-year-old press release as a live programme;
counting one asset twice because it appears under a code name in a filing and a
generic name in a release; presenting a candidate landscape as complete when it
was assembled from the sources that happen to publish.

**Verify.** For each candidate, can you state who claimed it, on what date, and
in what words? Does the reported stage quote the source rather than assert one?
If the most recent evidence is older than a year, does the output say so? If a
route did not run — no search key, no filings coverage for a private or foreign
company — does the output say the picture is partial rather than presenting what
the other routes found as the whole?

---

# A missing interval is missing information, not a precise estimate

`an-estimate-without-an-interval-is-not-a-precise-one` · MUST · output-contract

**Rule.** Carry the uncertainty a source published, and where it published none,
record that absence explicitly rather than leaving the field empty. An empty
uncertainty field and a genuinely tight interval are indistinguishable
downstream, and the empty one gets read as the tight one.

Do not manufacture what the source withheld: no interval invented from a sample
size, no standard error assumed, no "±" attached because a figure looks like it
should have one. And do not silently drop the bounds that were published —
carrying the point estimate alone through one transformation is how a modelled
figure with a two-fold interval becomes a planning assumption.

Say what kind of interval it is when the source says, and say that it did not
when it does not. WHO's GHO returns `Low` and `High` on most estimates and
nowhere states the coverage level in the API; that is reportable as published
bounds of unstated coverage, which is neither a 95% confidence interval nor
nothing.

**Prevents.** A modelled estimate being treated as a measurement. Global burden
figures for rare and under-diagnosed conditions routinely carry intervals wide
enough to change a decision, and those are precisely the figures most likely to
be quoted as a single number because the interval is inconvenient. Also prevents
the reverse error of discarding an estimate for being uncertain when the
interval, stated, would still have supported the conclusion.

**Sometimes the interval disqualifies the estimate.** Carrying it is the
minimum, not the end. For survey data there is a published rule: NCHS's *Data
Presentation Standards for Proportions* (Parker et al., Vital Health Stat
2(175), 2017) set a minimum denominator, a minimum effective sample size, and
limits on the absolute and relative width of the confidence interval, and return
present / footnote / **do not present**. A correctly computed NHANES figure —
obesity among Asian non-Hispanic women 70+, 13.9% — fails it, because its
interval is wider than the estimate. Subgroup cells are where a market-sizing
question pushes and where this bites; apply the same test to any survey-derived
subgroup, whatever the source.

**Applies when.** Any published estimate, at every step that moves it —
extraction, aggregation, comparison, and the final summary. The last one is
where it is usually lost.

**Verify.** Every value in the output has an uncertainty field that is either
populated with the source's bounds or explicitly marked as not published by the
source. No output contains an interval that cannot be traced to a source that
stated it ([[a-burden-figure-is-four-facts-or-it-is-noise]],
[[never-invent-an-identifier]]).

**Source.** Stated 2026-08-16 while building WHO GHO access, where `Low` and
`High` are present on most rows, absent on some, and never labelled.

---

# An extraction vocabulary stays open

`an-extraction-vocabulary-stays-open` · MUST · extraction

**Rule.** Where a field takes one of a set of values, publish the set as a
**starting vocabulary, not a closed one**. When a case does not fit, do not
force it into the nearest value and do not drop it: record it as unclassified,
carry the source's own wording verbatim, and propose the value the set is
missing.

Three things travel together for every such field — the value chosen, the
verbatim text it was chosen from, and whether the chosen value actually fits
([[carry-the-trigger-for-a-derived-label]], [[preserve-the-surface-form]]).

**A residual value is not the same as an open vocabulary.** "Other" absorbs the
unmatched case and hides it; unclassified plus the verbatim text keeps it
readable and countable. If a value recurs, it has earned a place in the set, and
that is the mechanism by which the vocabulary grows.

**Where the consuming project's contract is closed, the mismatch is reported,
not coerced.** A schema that permits only its own enum still gets a valid
document; what it must not get is a wrong value chosen to satisfy it
([[never-invent-a-schema]]). Say plainly that a case did not fit.

**Prevents.** The novel case disappearing into the nearest familiar bucket. In
practice the unmatched cases are the interesting ones — the trial stopped for a
reason nobody had a category for, the finding that does not resemble the
previous hundred — and forcing them into an existing value produces a clean
distribution that is quietly wrong. It also destroys the evidence that the
vocabulary needs extending, so the same loss repeats every run.

**Applies when.** Any field with a controlled set of values: classifications,
statuses, outcomes, document types, reasons.

**Verify.** The output has an unclassified bucket that is allowed to be
non-empty, each entry carrying the verbatim text; and a proposed-values list
naming what recurred. A run where every record matched an existing value, on a
corpus not seen before, is more likely to have coerced than to have fitted.

**Source.** Stated 2026-08-12, generalising the trial-outcome vocabulary in the
trial-registry skill, where the categories a result can fall into — met all
endpoints, met the primary, failed the primary, stopped for safety, stopped for
other reasons — are a starting set that real conclusions will exceed.

---

# Build the co-authorship and affiliation graph before ranking researchers

`build-the-coauthorship-graph` · SHOULD · source-selection

**Rule.** Assemble co-author lists and their affiliations across the retrieved
corpus, then use the graph structure — who publishes with whom, which
institutions recur, which groups are productive on this specific topic — to rank
whose output to mine.

**Prevents.** Ranking by citation count, which surfaces reviews and decade-old
landmark papers rather than the groups currently generating data. The question
is usually "who is doing this work now," and citation counts answer a different
question.

**Applies when.** [[rank-by-social-graph]] applies — the question is topic-shaped
and the field is too large to read exhaustively.

**Verify.** The run records the researchers and institutions it selected and the
graph evidence for each.

**Source.** Stated in the project vision — "mapping and using social graphs to
identify high-quality researchers and research institutions."

---

# An explicitly stated absence is data — record it

`capture-stated-negatives` · MUST · extraction

**Rule.** When a source states that something was looked for and not found, was
normal, or did not occur, capture that as a finding. Do not skip a section
because its content is negative, and do not let a negative reading fall out of
the output as though the source never addressed it.

**Prevents.** The most damaging ambiguity in extracted evidence: a consumer
cannot tell "the source examined this and reported nothing" from "the source
never examined this." Those support opposite conclusions. A report stating no
metastatic disease and a report that omitted the question look identical once
the negative is dropped, and the gap is unrecoverable afterwards.

**Applies when.** Every source with a structured or conventional set of things
it addresses — a radiology report's organ sections, a trial's safety endpoints,
a datasheet's property table, a paper's negative results.

**Verify.** For a document with explicitly normal sections, those sections
appear in the output with their stated content. A run whose output contains only
positive findings dropped the negatives.

**Source.** Harvested from clinical-ingest's imaging extractor — every
anatomical section is captured "including sections with normal findings. Do not
skip normal sections."

---

# Take the source's own conclusion as written

`capture-the-source-s-conclusion-verbatim` · SHOULD · extraction

**Rule.** Where a document states its own impression, conclusion, or summary,
capture it verbatim rather than condensing it. Summarise elsewhere if a short
form is needed; do not replace the original with the summary.

**Prevents.** Losing a hedge. Conclusions are where sources are most careful —
"consistent with", "cannot exclude", "in this subgroup only" — and condensing
strips exactly those qualifications, converting a guarded finding into a
confident one while every number stays correct.

**Applies when.** Any source with an authored conclusion: report impressions,
paper discussions, executive summaries, guideline recommendations.

**Verify.** Compare a captured conclusion against the source, word for word.

**Source.** Harvested from clinical-ingest's imaging extractor — all impression
items verbatim, "Do not condense or truncate. Every numbered impression item is
clinically important."

---

# A caveat printed next to a value is part of the value

`carry-the-source-s-own-qualifier` · MUST · extraction

**Rule.** When a source qualifies a value — approximately, estimated,
preliminary, research use only, not validated, pending confirmation — that
qualifier travels with the value. It is captured from the document, not
inferred, and it is not our confidence assessment.

**Prevents.** A preliminary result being read as final, or a figure the vendor
marked as not clinically validated being used as though it were. The source did
the honest thing and said so; dropping the qualifier is where the dishonesty
enters, and it happens by omission rather than by any wrong number.

**Applies when.** Every extracted value. Qualifiers hide in footnotes,
asterisks, and status fields more often than in the sentence carrying the
number.

**Verify.** For a document with a footnoted or status-qualified value, the
qualifier is present in the output attached to that value. Distinct from
[[keep-confidence-tiers-in-the-output]], which concerns confidence we assigned.

**Source.** Harvested from clinical-ingest — a tumour mutational burden
footnoted as research use only stays flagged as such, and an approximate lesion
measurement is captured with the qualifier.

---

# A label we assigned carries the evidence that produced it

`carry-the-trigger-for-a-derived-label` · MUST · provenance

**Rule.** Any classification, bucket, tag, or category the run assigns records
what caused it — the matched heading, the matched text span, the rule that
fired. This is provenance for derived values, and it is required wherever
[[provenance-on-every-value]] is required for extracted ones.

**Prevents.** A count of records in a category that nobody can audit or correct.
Without the trigger, a rule matching the wrong thing produces a plausible number
and there is no way to find out, because the only evidence of the mistake was
discarded at the moment it was made.

**Applies when.** Every derived label, including ones that only ever appear as
part of an aggregate.

**Verify.** Take any labelled record and recover why it was labelled. Take any
category count and list the triggers behind it.

**Source.** Harvested from literature-search-ingest — every rule-derived label
carries its matched trigger, and a bucket count never drops it.

---

# Two trials reporting the same endpoint are usually not measuring the same thing

`carry-what-makes-a-result-comparable` · MUST · triangulation

**Rule.** A result is only meaningful with the things that make it
interpretable. Carry all of them on every extracted outcome, and refuse to place
two numbers side by side until they are present for both:

- **The endpoint as defined**, not its name. "Overall response rate" differs by
  criteria — RECIST 1.1, iRECIST, Lugano — and "progression-free survival"
  differs by whether progression was called by the investigator or by blinded
  independent review. The definition text is in the registry
  ([[a-registry-record-is-mostly-prose]]).
- **The analysis population** — intention-to-treat, per-protocol, safety, or a
  biomarker-selected subset. The same trial reports different numbers for each.
- **The timepoint and data cutoff**, since survival endpoints move.
- **The comparator and the backbone**, because an effect measured against
  placebo and one measured against active therapy are different quantities
  ([[read-the-arms-to-know-what-is-under-test]]).
- **The statistic and its uncertainty** — hazard ratio, odds ratio, median
  difference, with the interval and the method. AACT holds these in
  `outcome_analyses` as `param_type`, `param_value`, the confidence limits and
  `method`.
- **The assay or instrument version** where one is involved
  ([[record-the-source-s-method-version]]).

**Cross-trial comparison is not a controlled comparison.** Populations,
eras, standards of care and assessment methods all differ, and none of it is
randomised. Where a run puts numbers from separate trials next to each other,
say plainly that the comparison is indirect and what differs between the
populations. That sentence is part of the output, not a caveat to be trimmed.

Where the necessary context is missing, the honest result is that the two are
not comparable ([[mark-what-a-human-would-have-confirmed]]) — not a comparison
with a footnote.

**Prevents.** The most consequential error this whole pack exists to stop: a
clean table of response rates across competing agents, every number correctly
transcribed, that ranks them on differences created by their assessment
methods and enrolment criteria rather than by the drugs. It looks like the
deliverable everyone wanted, and it is confidently wrong in a way no
spot-check of individual values will reveal.

**Applies when.** Any output placing outcomes from more than one trial in the
same table, chart, or sentence.

**Verify.** Take any two numbers compared in the output and check that endpoint
definition, analysis population, cutoff and comparator are recorded for both. A
comparison table with a single column of values and no context columns has this
defect by construction.

**Source.** Stated 2026-08-11: collating reported results across trials is the
hardest part of registry work.

---

# Check a name against every record, not just the ones in front of you

`check-naming-against-the-whole-corpus` · SHOULD · entity-resolution

**Rule.** Before naming a measurement, parameter, or series, check the name
against the whole existing corpus rather than against the current document or
the current date. Reuse an existing name verbatim when it refers to the same
thing.

**Prevents.** One quantity splitting into two series under two spellings, so a
trend line breaks in half and neither half looks wrong. The split happens across
documents, so a check scoped to the document in hand cannot see it — which is
why it is the more common failure and the harder one to notice.

**Applies when.** Any extraction that appends to an accumulating dataset, or
that will be joined with earlier runs.

**Verify.** Group the corpus by name and look for near-duplicates that differ
only in spelling, spacing, or case.

**Source.** Harvested from clinical-ingest — naming "must be checked against the
full existing dataset (every date), not just the current document's date."

---

# The consumer selects the source classes; never run the full ensemble by default

`consumer-selects-sources` · MUST · source-selection

**Rule.** A skill runs the source classes and methods the consumer enabled. When
the consumer has not chosen, ask or use a stated narrow default. Do not widen a
run because more sources might help.

**Prevents.** A question answerable from two databases spending an hour crawling
video, trade press, and patents. The cost is invisible to the consumer until the
bill or the wait arrives, and the extra sources usually add nothing to a narrow
question.

**Verify.** The run's parameters name the enabled source classes explicitly.
There is no code path that reaches a source the consumer did not enable.

**Source.** Stated as a project requirement — "sources/capabilities in our
skills are selectable by consumers, not wasting compute when scope is simpler."

---

# Compare across sources or methods before treating a value as established

`corroborate-before-establishing` · MUST · triangulation

**Rule.** A value that came from one source read by one method is unconfirmed.
Where the value matters, obtain a second reading — another source, or another
method on the same source ([[use-more-than-one-method]]) — and compare.

**Prevents.** A transcription error, a units mismatch, or a misread table cell
propagating into the answer with nothing to catch it. Single-source extraction
has no error-detection mechanism at all; it can only be wrong quietly.

**Applies when.** The value is load-bearing. Corroboration for every incidental
value is not affordable and is not required.

**Verify.** The provenance record shows the readings that were compared, not
only the value that survived.

**Source.** Stated in the project vision — "mining of content will never be
perfect with just any one source and approach."

---

# Identify a repeated document by its content, never by its name or path

`dedup-on-content-not-filename` · MUST · acquisition

**Rule.** When checking whether a document has already been processed, hash its
content. Do not match on filename, path, or folder. Treat a name-based match as
a hint that still requires a content check.

Run the check before the expensive work, not after. Re-processing a document and
discarding the result at write time pays the full cost of the extraction for
nothing.

**Prevents.** Re-extracting hundreds of documents because an export reorganised
its folders or a tool appended a copy suffix, and — worse in the other direction
— skipping a genuinely new document because it happens to share a name with one
already processed.

**Applies when.** Any corpus delivered more than once: repeated exports,
refreshed downloads, a directory a consumer points at on successive runs.

**Verify.** Rename a processed file and re-run. It is still recognised as
already processed.

**Source.** Harvested from clinical-ingest — its triage step hashes file content
only, "never filename or path, because snapshot exports reorganize folders even
when the bytes are identical."

---

# Everything derived from one physical sample carries the same identity for it

`derivatives-of-one-sample-share-its-identity` · MUST · entity-resolution

**Rule.** When several records describe tests, assays, or measurements performed
on one physical specimen, batch, or lot, they all carry the same identifier and
the same wording for it. Check what earlier records called that sample before
naming it again.

**Prevents.** A sample's results scattering into unlinked groups. Histology, a
molecular panel, and an immunohistochemistry result from one biopsy end up under
three phrasings of the same site, and nothing can then show that they describe
one specimen — so a reviewer cannot tell that the negative marker and the
mutation came from the same tissue.

**Applies when.** Any chain of derived work on a physical thing: a specimen and
its assays, a formulation batch and its property measurements, a compound lot
and its test results. Distinct from [[check-naming-against-the-whole-corpus]] in
what it links — that governs the name of a *quantity*, this the identity of a
*sample*.

**Verify.** Group records by sample identifier. Two groups describing the same
physical thing means the identity drifted.

**Source.** Harvested from clinical-ingest's pathology and procedure extractors,
which reuse the tissue tag verbatim "for every record drawn from the same
physical specimen — histology plus any downstream molecular test run on that
same specimen."

---

# Check what this document prints rather than what its type usually omits

`do-not-assume-a-type-never-carries-a-field` · SHOULD · extraction

**Rule.** Do not encode a belief that a document type never carries a field and
skip looking for it. Check each document. Where a type genuinely never carries
something, that is recorded under [[expected-absence-is-not-a-gap]] — but it must
be established, not assumed.

**Prevents.** A whole category of values never being extracted because an early
sample lacked them. The rule that skips the check also removes the evidence that
would overturn it, so the assumption survives indefinitely and the gap is
invisible in the output.

**Applies when.** Any extraction rule phrased as "this type has no X."

**Verify.** For a rule asserting a type never carries a field, find the sample
it was drawn from and check a document from a different source or period.

**Source.** Harvested from clinical-ingest's lab extractor, correcting its own
earlier claim that percentage differential fields have no reference range —
false for the repo's real documents. "Never assume an analyte category is
rangeless."

---

# If the fields that identify a record cannot be determined, do not create it

`do-not-create-an-ambiguous-record` · MUST · extraction

**Rule.** A record needs the fields that establish what it is — typically its
subject, its date or conditions, and its kind. If any of those is ambiguous, do
not write a partial record. Report it as not captured, with what was ambiguous.

**Prevents.** A record that cannot be deduplicated, joined, or corrected,
because nothing identifies it. Unlike a missing record, it actively damages the
dataset: it will not merge with the real record when that arrives, so the same
fact ends up present twice under different partial identities.

**Applies when.** Every record written. Distinct from
[[never-fabricate-to-fill-a-field]], which concerns a missing *attribute*; this
concerns a missing *identity*.

**Verify.** Every record in the output can be matched against a re-extraction of
the same source.

**Source.** Harvested from clinical-ingest's cross-type event scan — where date,
type, and title cannot all be confidently determined, "do not create the
record."

---

# When a source counts a group but measures some of it, do not manufacture the rest

`do-not-invent-rows-for-unmeasured-members` · MUST · extraction

**Rule.** Where a document reports a group and gives values for only part of it,
record the measured members and record the group's stated size. Do not create a
record per member, and do not distribute or estimate values across the
unmeasured ones.

**Prevents.** Turning one measurement into ten. A source reporting roughly ten
lesions with the largest measured yields exactly one measurement; ten rows imply
ten observations that were never made, and any count or average over them is
fabricated at scale rather than one value at a time.

**Applies when.** Any source that enumerates loosely and measures selectively —
lesion counts, sample batches, cohort subgroups, product ranges.

**Verify.** Count records against measurements stated in the source. More
records than measurements means members were manufactured.

**Source.** Harvested from clinical-ingest's imaging extractor — for a group
descriptor, create one row for the measured anchor and note the group size; "Do
not create rows for the unmeasured members."

---

# A value mentioned in a document is not automatically a value about its subject

`do-not-mix-levels` · MUST · extraction

**Rule.** Separate what a document asserts about its own subject from what it
merely mentions. A population statistic, a reference range, a comparison case, a
figure quoted from another study, a drug named as used in someone else's trial —
none of these are observations about the subject of the document.

**Prevents.** A trial's published response rate being recorded as this patient's
response, or a reference range being captured as a measured value. The number is
real and correctly transcribed, which is what makes the error survive review:
nothing about the value looks wrong, only its attachment.

**Applies when.** Any document that discusses context alongside its own findings
— which is nearly all of them. Clinical notes cite literature, papers cite prior
work, decks show competitor data.

**Verify.** For any extracted value, point at the sentence establishing that the
document asserts it about its subject rather than reporting it about something
else.

**Source.** Harvested from clinical-ingest's shared scans, which exclude
population toxicity tables, reference ranges, trial-context treatments, and
values from case comparisons.

---

# Gate an expensive pass behind a cheap check that says it is warranted

`escalate-cost-only-on-evidence` · SHOULD · extraction

**Rule.** Before running a costly extraction pass, run the cheapest check that
could rule it out. Only escalate when that check says the expensive work will
find something.

**Prevents.** Downloading a ninety-minute recording and running scene detection
across it to find slides, on a talk that is one continuous camera shot of a
speaker. The cost is paid on every video in a corpus, and most of them are
talking heads.

**Applies when.** Any pass whose cost is materially higher than the check that
predicts its value — full-text retrieval behind an abstract scan, OCR behind a
text-layer probe, frame extraction behind a handful of sampled stills.

**Verify.** The run record shows the cheap check ran, what it concluded, and
whether the expensive pass followed from it.

**Source.** Harvested from media-deep-ingest, which checks the description for a
linked deck, then samples six frames, and only then downloads the video.

---

# Separate a field this source type never carries from one we failed to get

`expected-absence-is-not-a-gap` · MUST · output-contract

**Rule.** When a field is absent because documents of this kind do not have it,
record it as not applicable. Reserve "missing" for a field the source should
have carried and we could not read. The two must be distinguishable in the
output.

**Prevents.** A conference deck being flagged forever as missing a DOI, when
decks are not indexed and never have one. Reviewers learn that the flags are
noise and stop reading them, which is how a real missing value gets ignored.

**Applies when.** Every source class with structurally absent fields — decks and
posters without DOIs, preprints without volume or page numbers, unindexed
citations without a resolvable identifier.

**Verify.** Count the flagged-missing fields in a run. If the count is dominated
by fields that this source type never carries, the distinction is not being
made.

**Source.** Harvested from literature-ingest — "No DOI/PMID: expected for this
doc type; not a gap, do not flag as missing" — and from media-deep-ingest, where
an unresolved conference-abstract citation is the normal outcome.

---

# Fetch the artifacts that accompany a document, not only the document

`fetch-companion-artifacts` · MUST · acquisition

**Rule.** A publication is not one file. Supplementary data files, appendices,
and linked datasets are separate artifacts and must be fetched explicitly.

**Prevents.** Extracting a summary table from a paper while the per-experiment
values sit in a supplementary spreadsheet nobody downloaded. The paper often
reports one aggregate where the supplement holds the fifty measurements the
question actually needs.

**Applies when.** Any source that publishes accompanying files — journals,
preprint servers, regulatory filings, conference proceedings.

**Verify.** For each document processed, the run records how many accompanying
artifacts existed and how many it retrieved. Zero retrieved with a non-zero
count is a finding, not a silent pass.

**Source.** Stated in the project vision — "supplementary data in publications."

---

# Write down what counts as the disease before you retrieve anything

`fix-the-disease-boundary-before-you-count` · MUST · source-selection

**Rule.** Before the first query, record the disease's boundary as structure: the
names to search, the endpoint that answers the question, the **metric families**
that count and the adjacent ones that do not, the case definitions and their
thresholds, what must be excluded, which sources are preferred, and the traps
already known. Emit that block with the results and check every candidate figure
against it before accepting one.

The block is the reusable half of the work. The next run on the same disease
starts from it instead of rediscovering the boundary, and a run that turns up a
new trap adds it.

**The field that does the work is metric family**, because it is the one a
careful record of value, population, period and uncertainty does not contain.
Three groups, and members of different groups never share an axis:

- what **is** the disease under the stated case definition;
- the **adjacent state** a search returns and a reader confuses with it;
- **risk-attributable burden**, which is a modelled counterfactual about
  something else entirely.

**Prevents.** Two figures being compared when they agree on every recorded facet
and are about different things. WHO publishes obesity as `NCD_BMI_30A` and
overweight-including-obesity as `NCD_BMI_25A` — two characters apart, same year,
same age band, same standardisation, same publisher, both correct — and global
prevalence reads 16.2% or 44.6% depending which you took. Nothing in the four
facts separates them. The same shape recurs everywhere: hyperuricaemia for gout,
thyrotoxicosis for Graves', short sleep duration for sleep apnoea, steatotic
liver disease for MASLD, high-BMI-attributable DALYs for obesity prevalence.

It also prevents the quieter failure of a run that was correct but
unreproducible, because the judgements that shaped it — which definition, which
exclusions, which source won a conflict — were made silently and left in nobody's
notes.

**Applies when.** Any run that will produce a number about how common something
is, from any source. It applies hardest where the disease has a moving case
definition, a neighbouring risk state, a paediatric variant with a different
rule, or a recent rename — which between them cover most of a therapeutic area.

**Verify.** The output contains the profile, and every accepted figure names the
metric family, case definition and measurement basis it was admitted under. Any
two figures placed on one axis agree on metric family, case definition,
population, standardisation and measurement basis, or the difference is stated in
the same sentence as the numbers. Absence is recorded as searched-and-not-found
rather than left blank ([[a-burden-figure-is-four-facts-or-it-is-noise]],
[[a-source-that-does-not-cover-a-disease-reports-no-burden-for-it]]).

**Source.** Asked for by an analyst using the burden skill, 2026-08-16, who had
built the same discipline by hand for obesity and wanted it enforced rather than
remembered. The 2.75-fold overweight/obesity figure was measured the same day.

---

# Judge a source by what it is, not by the file type it arrived as

`format-is-not-credibility` · SHOULD · extraction

**Rule.** Record the credibility of a source from its content and provenance —
who produced it, whether it was reviewed, what it reports. Do not derive it from
the format. The format is already recorded separately.

**Prevents.** Every slide deck being tagged as a conference abstract, when the
same file type covers an invited expert lecture, a grand-rounds teaching
session, and a deck presenting an already peer-reviewed paper. A consumer
filtering on credibility gets a category that means nothing.

**Applies when.** Any output carrying a quality, tier, or evidence-level field.

**Verify.** Group the corpus by format and by credibility. If the two groupings
are identical, credibility is being read off the format.

**Source.** Harvested from literature-ingest — quality tier "reflects the
credibility of the content, not the fact that it's slides."

---

# A parser that covers part of a document is composed with handling for the rest

`handle-what-a-partial-parser-left` · MUST · extraction

**Rule.** When a deterministic parser reports that it covered only part of a
document, treat its output as one region handled and continue with the
remainder. Do not treat a successful partial parse as a completed extraction,
and do not discard the reliable part in order to reread the whole document a
second way.

**Prevents.** Losing everything outside a parser's clean region. A structured
report often mixes one well-formed table with free narrative and two irregular
sub-layouts; a parser built for the table succeeds, returns rows, and the
narrative measurements silently never appear. The run looks clean because the
part that was parsed was parsed correctly.

**Applies when.** Any document mixing structured and unstructured regions, and
any tool that reports its own coverage. Distinct from
[[layered-methods-add-never-overwrite]], which orders methods by reliability over
the same content; this divides one document into regions.

**Verify.** For a document handled by a partial parser, the run record names
which regions it covered and how the rest was handled.

**Source.** Harvested from clinical-ingest's echocardiography extractor, whose
fast path always reports partial coverage — "complementary, not alternatives."

---

# A value known to be weaker must stay marked weaker all the way out

`keep-confidence-tiers-in-the-output` · MUST · output-contract

**Rule.** Confidence, provisional status, and known method limitations travel
with a value through every downstream step. A value produced by a prototype
method, a partial-coverage parser, or an unvalidated rule is never presented
alongside validated values without that distinction.

**Prevents.** A statistic from a prototype classifier appearing in a summary
table next to measured values, with the caveat left behind two transformations
ago. Aggregation is where confidence is most often dropped and where its loss
does the most damage, because the reader sees only the total.

**Applies when.** Every step that copies, joins, or summarises extracted values.

**Verify.** Take any aggregate in the output and determine the weakest input
that contributed to it. If you cannot, the tier was dropped somewhere.

**Source.** Harvested from literature-search-ingest — statistics marked lighter-
weight or unvalidated "must stay labeled as such, never presented as equal-
confidence to validated fields."

---

# A looser later method may add what an earlier one missed, never replace it

`layered-methods-add-never-overwrite` · MUST · extraction

**Rule.** When methods are layered from strict to loose — structured metadata,
then text patterns, then a model's reading — each later layer may only fill gaps
the earlier ones left. It never overwrites, downgrades, or re-labels what a
stricter method already determined.

**Prevents.** A text-pattern layer clobbering a label that came from the
source's own structured metadata, replacing a fact with a guess. Because the
looser layer runs later and matches more, it wins every collision unless the
rule is explicit.

**Applies when.** Any pipeline running more than one extraction or
classification method over the same content. Distinct from
[[use-more-than-one-method]], which runs methods to compare them; this governs
which one wins when they are ordered by reliability rather than compared.

**Verify.** For any value produced by more than one layer, the recorded method
is the strictest one that produced it, not the last one that ran.

**Source.** Harvested from literature-search-ingest — "never let a later
classification step overwrite or downgrade an earlier step's label."

---

# The locator is precise enough to return to the exact place

`locators-must-be-precise` · MUST · provenance

**Rule.** Record the page and region for a PDF, the slide and shape for a
presentation, the timestamp for a recording, the sheet and cell for a
spreadsheet, the table and row for structured text. A document-level citation is
not a locator.

**Prevents.** A reviewer given "found in the 2024 annual report" spending twenty
minutes searching a 180-page document for one number, and giving up. A locator
that costs more to use than to re-extract is not doing its job.

**Verify.** Hand a locator to someone who has not seen the run. They reach the
value in under a minute without searching.

**Source.** Derived from [[provenance-on-every-value]] and recorded in the vision.

---

# Do not treat the literature as the default or sufficient source

`look-beyond-the-literature` · SHOULD · source-selection

**Rule.** Before defaulting to papers, work out which source class would carry
this particular fact *first*, and search that one too. Publication is the last
step in a long chain of disclosure, not the first, so for anything commercial
the literature is usually the slowest witness available.

Match the question to where the answer surfaces earliest:

| The question is about | Where it appears first |
|---|---|
| Whether a programme is alive, dead, or partnered | Quarterly and annual reports, R&D-day decks, trade press |
| Mechanism, target rationale, in vivo data for an unpublished programme | R&D-day and investor decks — often the only public record that will ever exist, see [[mine-decks-for-science-not-just-status]] |
| A trial's design, sites, or enrolment status | Trial registries, then conference abstracts |
| Headline efficacy or safety before a paper | Conference presentations and their recordings; the deck usually predates the manuscript by a year or more, and for a private company may replace it entirely |
| Formulation, composition, or manufacturing detail | Patent applications — the examples and property tables, not the claims |
| Who is actually doing the work now | Grant awards, conference programmes, trial investigator lists |
| Why a company changed direction | Earnings calls and their transcripts; trade press covering them |
| Regulatory position | Agency filings, advisory-committee materials, approval letters |
| Why a subgroup, dose, or combination was chosen — or why something failed | Trade-press analysis and expert blogs; the reasoning spans studies and is in none of them, see [[mine-commentary-for-analysis-not-just-news]] |

**Named starting points, biopharma.** These are examples rather than a
catalogue, and they are where commercial and clinical-development news lands
before it is written up anywhere citable:

- **Endpoints News** — deal, pipeline, and personnel coverage; frequently first
  on a programme being cut.
- **STAT News** — clinical and policy reporting, and the outlet most likely to
  do original investigative work rather than restating a release.
- **Fierce Pharma** and **Fierce Biotech** — broad commercial and R&D coverage
  respectively; high volume, useful for establishing that something happened and
  when.
- **BioSpace** — company, financing, and hiring signals, which often move before
  any scientific disclosure.
- **BioCentury** and **Evaluate** — analytical rather than reportorial;
  competitive-landscape framing and forecast context.
- **Scrip** and **Pink Sheet** — commercial strategy and regulatory policy,
  both usually subscription-gated.

Independent expert blogs sit alongside these and do something different — they
argue rather than report. **In the Pipeline** (Derek Lowe), **Century of
Biology** (Elliot Hershberg), and **Asimov Press** are the standing examples.
Their value is analysis that spans studies: stratification, dose rationale,
class toxicity, repurposing, why something failed. See
[[mine-commentary-for-analysis-not-just-news]], which is about reading all of
this for its argument rather than its news.

For biomedical and consumer-care questions the equivalent outlets differ, and
the same reasoning applies: find the trade publication whose readers are the
people making the decision, because they are served first.

Distinguish outlets that do **original reporting** from those that restate a
press release. Two aggregators carrying the same announcement are one source,
not corroboration — see [[synthesis-is-not-independent-corroboration]].

**Prevents.** Reporting a programme as active a year after it was quietly
dropped, because the discontinuation appeared in one line of a quarterly report
and a trade-press item and was never written up. The same failure gives a
competitive landscape that is a year stale, and a formulation summary missing
the detail that exists only in a patent example table. Published literature
lags and omits by design: negative results often go unpublished entirely, and
commercial decisions are disclosed to investors long before they reach a
journal, if they ever do.

**Applies when.** The question concerns commercial programmes, timelines,
competitive position, regulatory status, or anything a company would disclose
to investors or a conference before publishing. Also when a literature search
returns suspiciously little on an active area — that is usually a signal the
activity is real and unpublished, not that it is absent
([[capture-stated-negatives]] is about a source stating an absence; this is
about mistaking silence for one).

**Verify.** The run record names the non-literature source classes it consulted,
or states why the question did not warrant any
([[report-skipped-sources]]). A run that answered a commercial question from
papers alone has not applied this rule, whatever it found.

**Source.** Stated in the project vision — intelligence "not just in scientific
literature but also in" R&D-day presentations, performance reports, recordings,
trade press, patents, social media, and research databases. Outlets named
2026-08-11.

---

# A value read from a document that repeats it is marked as second-hand

`mark-a-secondary-mention` · MUST · provenance

**Rule.** Prefer the document that originated a value. When it is unavailable
and another document repeats the value, extract it rather than dropping it — and
mark it as taken from a repeating source, so it can be verified against the
original later.

**Prevents.** Two failures pulling in opposite directions. Dropping the value
because the primary source was not in the corpus loses data that was plainly
present. Recording it as primary hides that it passed through a summarising step
where a unit, a qualifier, or a decimal place can have been lost.

**Applies when.** Any corpus where the same fact appears in a report and in a
document summarising that report — a lab result inside a consult note, a trial
result inside a review, a figure inside a slide deck.

**Verify.** For any value, the record says whether it came from the document
that produced it or one that repeated it.

**Source.** Harvested from clinical-ingest's shared scans — the primary document
is always preferred, but data present in a secondary one is "never silently
dropped," and the source type is always flagged.

---

# Text we generated is marked as generated, and never mixed with quoted text

`mark-generated-prose` · MUST · output-contract

**Rule.** Any prose the run produced — a summary, a synthesis, a narrative
description — is labelled as generated and kept distinguishable from text quoted
from the source. Where an output has both, the boundary between them is
explicit.

**Prevents.** A model's paraphrase being read and later quoted as the source's
own words. The paraphrase carries the same provenance record as the quotation,
so it inherits the citation's authority, and a downstream reader has no way to
see that the source supports the topic but not the phrasing.

**Applies when.** Every output containing prose we wrote. See
[[no-interpretation-in-extraction]] for the separate question of whether that
prose should contain conclusions at all.

**Verify.** Take any sentence of output and determine whether the source wrote
it or we did.

**Source.** Harvested from literature-ingest, where a flag is set true whenever
any summary field was generated and false only when the body is verbatim source
text.

---

# Distinguish structure the source provided from structure we inferred

`mark-inferred-structure` · MUST · extraction

**Rule.** When a document's own structure is used — publisher chapters, declared
sections, a real table — mark it as coming from the source. When the structure
was proposed by reading the content — topic-shift boundaries, inferred column
groupings, reconstructed table borders — mark it as inferred, and never present
it as the source's own.

A third origin matters as much as the first two: an element a person supplied —
a corrected boundary, a hand-added timestamp, a reviewer's label — is neither
the source's nor ours, and is marked as theirs.

**Prevents.** Agent-proposed chapter boundaries in a recording being read as the
speaker's own outline, so a reader treats "the presenter devoted a section to
safety" as a fact about the talk when it is a fact about our segmentation. The
same failure applies to any reconstructed table: a column grouping we guessed
looks identical in the output to one the document declared.

**Applies when.** Any output carrying structure — sections, chapters, tables,
groupings — where some of it may not be the source's.

**Verify.** For every structural element in the output, determine from the
record alone whether the source declared it or we proposed it.

**Source.** Harvested from media-deep-ingest, which marks every chapter as
creator-authored or inferred and always lists inferred ones for review.

---

# A decision taken without a human is an assumption, not a finding

`mark-what-a-human-would-have-confirmed` · MUST · output-contract

**Rule.** When a run reaches a point where a person would have been asked and no
person is there, take the best-supported option, record what was chosen and on
what basis, and mark it as assumed. Never present it as confirmed, and never
resolve it by inventing a value — [[never-fabricate-to-fill-a-field]] still binds.

**Prevents.** An unattended run producing output indistinguishable from a
reviewed one. Every value carries the same provenance and the same confidence,
so a consumer trusts a defensible guess exactly as much as a checked fact — and
the assumptions are precisely the places where a checked fact would most often
have differed.

**Applies when.** Any run without a person available at a decision point:
scheduled pipelines, batch processing, a generated skill running in a project
that chose not to elicit.

**Verify.** Filter the output to assumed values. A run that made no assumptions
either had a person at every decision point or is not marking them.

**Source.** Harvested from clinical-ingest and literature-ingest, whose
unattended mode writes what can be written and marks anything the interactive
gate would have raised — "auto mode relaxes who confirms, never what's allowed."

---

# Match an open-vocabulary label by word, not by equality

`match-an-open-vocabulary-label-by-word-not-by-equality` · MUST · entity-resolution

**Rule.** Where a field is free text written by a submitter, never retrieve on
string equality alone. Match the term at **word boundaries** so a qualified
label still matches, report which spellings were hit, and keep exact and lexical
matches distinguishable in the output.

Submitters qualify a label with everything the record is about: site, stage,
age group, resectability, recurrence. `Cutaneous Angiosarcoma`,
`adult angiosarcoma`, `Angiosarcoma of Skin`, `Unresectable Angiosarcoma` are
all the disease, and none of them equals `angiosarcoma`. Equality retrieves the
bare form and nothing else, and the loss is invisible because the bare form
returns plenty.

**Word boundaries, not substrings.** `\msarcomas?\M` must not match
`osteosarcoma`. Bare substring matching over an open vocabulary is a different
and worse error — see [[search-every-name-a-drug-has]] for what it costs.

**Discover the variants, do not guess them.** The set of qualified spellings is
a property of the corpus, so query it: return every matching label with its
record count. Asking a user to imagine `Angiosarcoma of Skin` is asking them to
do retrieval by memory.

**A word match is not a relevance judgement.** A record whose text reads
"not including angiosarcoma" contains the word. Where matching moves beyond the
labelled field into titles, summaries or eligibility prose, that pass is
**review-only**: return the surrounding text, flag apparent negation, and never
let it enter a matched count without a decision ([[capture-stated-negatives]],
[[no-interpretation-in-extraction]]).

**Prevents.** A recall gap that no zero-check catches. The query returns a
plausible number, every returned record is correct, and the missing ones are
missing for a reason nobody sees. It is worst in rare disease, where the
qualified variants can outnumber the bare form and each one carries few records.

**Applies when.** Any retrieval keyed on a human-written label — registry
condition and intervention names, author keywords, patent classifications,
free-text diagnosis fields.

**Verify.** The output states the match rule used, lists the spellings actually
matched with counts, and separates exact from lexical matches. A run reporting a
single count against a single string did not check.

**Source.** Measured 2026-08-12 against the AACT mirror, prompted by a curated
angiosarcoma corpus that carried trials this skill's own query missed. Exact
equality on the resolved names returned 32 trials and the MeSH index 91; word
matching on `angiosarcomas?` and `hemangiosarcomas?` returned 62, and the union
**102** — 11 trials that are in neither the MeSH index nor any exact spelling,
spread across 18 qualified labels including `adult angiosarcoma` (9 trials),
`childhood angiosarcoma` (4) and `cutaneous angiosarcoma` (3). Running every
resolved exact spelling did not recover them; only word matching did. In the
same corpus a trial titled "...Not Including Angiosarcoma" carries the condition
`Cutaneous Sarcoma` only, so it is correctly absent from the label match and
correctly present, flagged, in the review-only text pass.

---

# Match the consumer's declared shape, or be self-describing

`match-shape-or-self-describe` · MUST · output-contract

**Rule.** A run operates in one of two modes and says which. Either the consumer
declared a target shape in BAML and the output is typed to it, or the output is
a self-describing payload — field meanings, units, and the question each value
answers carried inline. Neither mode is a fallback for the other.

**Prevents.** Two distinct failures. A pipeline that silently accepts a shape it
did not expect and corrupts everything downstream. And an exploratory result
that arrives as opaque keys the analyst has to reverse-engineer from our source
code before they can use it.

**Applies when.** Every run. The mode is chosen by the consumer, not inferred
from the question.

**Verify.** For declared mode: a shape mismatch fails the run loudly rather than
degrading. For self-describing mode: hand the payload to an engineer with no
access to this pack and ask them to map it to a target schema. If they need our
source, the payload is not self-describing.

**Source.** Stated in the vision conversation — consumer specifies shape via
BAML, or receives a self-descriptive payload to transform.

---

# Read conflict-of-interest, acknowledgement, and funding statements as data

`mine-declaration-sections` · SHOULD · extraction

**Rule.** Extract the declared relationships from conflict-of-interest
statements, acknowledgement sections, and funding declarations: who paid, who
provided material, who advised, which company employs which author.

**Prevents.** Missing the commercial relationship that explains a result. These
sections are skipped as boilerplate by every text pipeline that treats a paper
as title-abstract-body, and they carry the industry ties, material transfers,
and funding sources that appear in no other public record.

**Applies when.** The question concerns who is working on a topic, who funds it,
or whether a reported result carries a commercial interest.

**Verify.** For a paper with a non-empty COI statement, the run emits the
declared parties, not a flag saying a statement was present.

**Source.** Stated in the project vision — "conflict of interest and
acknowledgement statements in research publications declaring affiliations and
funding providers."

---

# Leave a field empty and flag it rather than inventing a value

`never-fabricate-to-fill-a-field` · MUST · extraction

**Rule.** When a value cannot be read from the source, emit nothing for it and
record it as not captured. This holds even when a downstream schema requires the
field: a record that cannot be written truthfully is skipped and surfaced, never
completed with a plausible value so that it validates.

**Prevents.** A record that passes every check and is false. This is worse than
a missing record, because validation is exactly what a downstream consumer
trusts — a fabricated dose, coverage depth, or effect size that satisfies the
schema will be read as measured. Nothing downstream can detect it.

**Applies when.** Every extraction, including unattended runs. An unattended run
may relax who confirms a value; it may never relax whether a value was read.

**Verify.** For any empty field in the output, the run record says it was not
captured. For any skipped record, the run record says which required field could
not be read.

**Source.** Harvested from the never-fabricate rule carried by clinical-ingest,
literature-ingest, media-deep-ingest, and literature-search-ingest — the one
rule all four state independently.

---

# "Current" means what the consumer pointed at, not what a name implies

`never-infer-authority-from-a-name` · MUST · acquisition

**Rule.** When more than one candidate could be the authoritative version of a
corpus or a document, ask which. Never decide by parsing dates out of folder or
file names, by comparing naming patterns, or by taking the most recent-looking
one.

**Prevents.** Extracting from last quarter's export because this quarter's was
named under a convention that changed, or because a re-export left two folders
that both look current. The run succeeds and every value in it is stale, with
nothing in the output to show it.

**Applies when.** Any handed-over corpus with more than one plausible candidate,
and any source whose naming convention is outside our control — which is all of
them.

**Verify.** The run record names the corpus it used and states that the consumer
identified it, rather than that the run selected it.

**Source.** Harvested from clinical-ingest, whose snapshot convention had
already changed once: "never something inferred by parsing or comparing dates
embedded in folder names, and never a guess when more than one candidate
exists."

---

# Never emit a presentation format or a schema this pack invented

`never-invent-a-schema` · MUST · output-contract

**Rule.** Output is structured data. Not a report, not a formatted table, not
prose. And not a domain schema this pack defined and expects consumers to adopt
— the consumer's declared shape or a self-describing payload, nothing between.

**Prevents.** A consumer parsing our markdown to get their numbers back. Every
presentation choice we make becomes a compatibility constraint we cannot change,
and a domain schema we invent becomes one every consumer has to translate out
of.

**Applies when.** Every run, including runs an analyst reads directly. Rendering
for a human is the consumer's job even when the consumer is a person.

**Verify.** The output parses as data without heuristics. No field exists solely
to control how something displays.

**Source.** Stated as a project requirement — "output format is generic enough
for consumers to then transform into formats of their need."

---

# Never invent an identifier; unresolved is a valid recorded state

`never-invent-an-identifier` · MUST · entity-resolution

**Rule.** When no confident match exists, emit the original string with the
resolution marked as unresolved and the candidates considered. Do not choose the
nearest match to avoid an empty field.

**Prevents.** A wrong accession that is worse than no accession, because it
looks authoritative and joins silently to the wrong entity downstream. An empty
resolution stops a consumer; a wrong one does not, and the error surfaces much
later with no trace back to here.

**Verify.** Unresolved entities appear in the output with their candidates. A
run with a hundred percent resolution rate on messy source text is a symptom,
not an achievement.

**Source.** Derived from [[provenance-on-every-value]] and the vision's provenance
requirement.

---

# Report what the source says, never what it means for a particular case

`no-interpretation-in-extraction` · MUST · output-contract

**Rule.** Extraction output states what the source said and where. It does not
characterise what that implies for a specific patient, programme, or decision.
If the source itself draws a conclusion, record that the source drew it; do not
extend it.

**Prevents.** An unreviewed inference travelling with a provenanced extract and
inheriting its authority. The provenance is real, so the interpretation looks
sourced — and a reader has no way to see that the citation supports the finding
but not the conclusion drawn from it.

**Applies when.** Every output, and most urgently in the summary-shaped ones. A
narrative summary is where the pressure to interpret is highest and where the
addition is least visible.

**Verify.** Take any sentence of output and point at the span of source it came
from. A sentence with no such span is interpretation.

**Source.** Harvested from media-deep-ingest, whose artifacts are source-only by
construction — "what the video says, never what it means for any specific
patient." Matches the vision's exclusion of judgment.

---

# Check whether a file bundles several documents before treating it as one

`one-file-may-be-several-documents` · MUST · format-handling

**Rule.** Before extracting, check whether the file contains more than one
document — several reports issued under one order, several exhibits in one
filing, several assays in one export. Each component has its own identifier,
date, and content, and each is extracted or cross-referenced on its own.

**Prevents.** Extracting the first component and stopping. The output is
well-formed and describes a real document, so nothing signals that two further
reports sat below it in the same PDF — and the components buried later are often
the molecular results that carry the decision.

**Applies when.** Any source that bundles: pathology reports carrying downstream
molecular panels, regulatory filings with exhibits, supplementary archives,
combined lab exports, conference proceedings shipped as one PDF.

**Verify.** For a bundling file, the run record lists the components found and
what happened to each.

**Source.** Harvested from clinical-ingest's pathology extractor — one PDF "may
contain multiple embedded components under one order number," each with its own
case ID and result section.

---

# Trial phase is a set, not a value — and most often it is not a phase at all

`phase-is-not-one-value-and-not-always-a-phase` · MUST · extraction

**Rule.** Never treat phase as a single categorical value. Before counting,
grouping, or filtering on it, settle three things and record what you settled.

**One trial can carry several phases.** A seamless design registers as
first-in-human and expansion together, and the registry stores that as a set:
`["PHASE1", "PHASE2"]`, not `"PHASE1/2"`. Decide whether such a trial counts
once in each bucket, once in a combined bucket, or once at its highest phase —
every one of those is defensible, none is the default, and the totals differ
substantially between them. State which you used.

**Not-applicable and unrecorded are different, and both are enormous.** In
ClinicalTrials.gov today, `NA` is the single most common value at roughly
234,000 studies — more than any real phase — and a further ~142,000 studies
carry no phase field at all. `NA` is an assertion that the concept does not
apply: observational studies, device and behavioural trials, expanded access.
Missing is an absence of information. Collapsing them into one "unknown" bucket
merges a positive statement with a gap, and dropping both silently discards
more than half the registry ([[expected-absence-is-not-a-gap]],
[[capture-stated-negatives]]).

**The spelling depends on the access path.** The v2 API returns a normalised
enum — `PHASE1`, `PHASE2`, `EARLY_PHASE1`, `NA` — while the AACT mirror's
`studies.phase` is a single text column carrying the older human-readable forms
with combinations written out. Same registry, same trial, different string.
Normalise on the way in and keep the original
([[preserve-the-surface-form]]), or a query written against one path silently
returns nothing against the other.

`EARLY_PHASE1` is a real distinct value, not a synonym for phase 1. Other
registries — EU CTIS, jRCT, ChiCTR — use their own vocabularies again, so a
multi-registry landscape needs an explicit mapping rather than string equality.

**Phase is also sponsor-declared and registered once.** It reflects what the
sponsor called the trial when they registered it, not necessarily what it became.

**Prevents.** A phase distribution that is confidently wrong. Count naively and
a seamless phase 1/2 trial vanishes from both buckets or appears in neither
total; treat `NA` as missing and an observational corpus disappears; write the
query against AACT's spelling after testing it on the API and get zero rows
back. Each of these produces a clean-looking chart with no error anywhere in it.

**Applies when.** Any grouping, counting, filtering, or comparison keyed on
phase — which is nearly every trial landscape.

**Verify.** The output states how multi-phase trials were counted, how `NA` and
missing were each handled, and how many trials fell in each. If the phase
counts sum to the trial count exactly, multi-phase trials were probably
collapsed without anyone deciding to.

**Source.** Stated 2026-08-11, and checked the same day against the
ClinicalTrials.gov v2 API: `NA` 234,113 studies, `PHASE2` 89,699, `PHASE1`
65,361, `PHASE3` 49,629, `PHASE4` 35,636, `EARLY_PHASE1` 6,433, with 141,765
studies missing the field, and combined designs stored as arrays such as
`["PHASE1", "PHASE2"]`.

---

# Take a platform's own captions and metadata before transcribing media

`prefer-platform-captions` · MUST · acquisition

**Rule.** Video and audio platforms expose captions, descriptions, chapter
markers, and structured metadata separately from the media stream. Fetch those
first. Transcribe only what they do not cover.

**Prevents.** Paying for transcription of a ninety-minute webinar that already
had accurate publisher-supplied captions, and getting a worse result — machine
transcription mangles the drug names, gene symbols, and author names that the
publisher's captions spell correctly.

**Applies when.** Any video or audio source, including YouTube and Google Drive.

**Verify.** The run records whether captions were available and whether it used
them. Transcription with captions available needs a recorded reason.

**Source.** Stated in the project vision — "youtube and google drive videos have
captions and metadata that can be mined."

---

# When the same work exists in a more authoritative form, extract that

`prefer-the-authoritative-version` · SHOULD · source-selection

**Rule.** A slide deck, a recorded talk, or a press summary presenting a study
is a condensed rendering of it, not the record. Where the underlying paper,
abstract, or filing is available, extract from that and treat the derived form
as supplementary — useful for what it adds, such as commentary or unpublished
context, not as the source of the numbers.

Where two artifacts are the same document at different fidelity — a photographed
copy and a text-native export — surface both to the consumer rather than
silently preferring one. Higher fidelity is usually right, but not when the
copies differ in content as well as quality.

**Prevents.** Recording a rounded figure read off a slide when the paper states
it to three significant figures with a confidence interval, and inheriting the
presenter's simplifications as if they were the study's own.

**Applies when.** Any source that presents work published elsewhere.

**Verify.** For a value taken from a derived form, the run record says whether
an authoritative version was looked for and what was found.

**Source.** Harvested from literature-ingest — "If the same work exists as a
full paper or abstract, prefer that source and treat the deck as supplementary"
— and from clinical-ingest's better-version conflict handling.

---

# An amendment does not erase what it amended

`preserve-both-versions-of-an-amended-document` · MUST · extraction

**Rule.** When a document carries an addendum, correction, or revision, keep
both the original text and the amended text, and record which is current. The
current value is the amended one; the original stays available.

An amendment can also add rather than revise. A critical value may appear only
in an addendum and nowhere in the original, so the whole document is read before
it is treated as extracted.

**Prevents.** Losing the fact that a finding changed. A corrected radiology
impression or a retracted figure is itself important information — knowing a
value was revised, and from what, is often more useful than the revision.
Keeping only the latest also makes it impossible to explain why an earlier
extraction disagreed.

**Applies when.** Any source class that issues corrections: clinical reports
with addenda, papers with errata, filings with amendments, guidance with
revisions.

**Verify.** For an amended document, both versions are recoverable from the
output and the current one is identifiable.

**Source.** Harvested from clinical-ingest's imaging extractor — both the
original and the addendum impression are preserved, with the addendum used as
the current description.

---

# Normalise the name, but keep the one the document used

`preserve-the-surface-form` · MUST · entity-resolution

**Rule.** When an entity is mapped to a standard name or identifier, retain the
string the source actually printed alongside it. The normalised form is for
joining; the surface form is what makes the extraction checkable against the
document.

**Prevents.** An extraction nobody can verify. A reviewer holding the source
searches for the brand name printed on the page and cannot find it in the
output, because it was silently replaced by the generic. It also destroys the
evidence for a resolution that turns out to be wrong — the only clue would have
been the original string.

**Applies when.** Every resolution step. See [[resolve-against-authorities]] for
which authority to map to.

**Verify.** For any resolved entity, recover the exact text the document used.

**Source.** Harvested from literature-ingest — use standard names, "but include
brand names in the document body if present" — and from clinical-ingest, which
keeps the verbatim measurement phrase beside the normalised value.

---

# A degraded artifact makes every value from it lower-confidence

`propagate-source-quality-to-values` · MUST · extraction

**Rule.** When the artifact is a scan, an image-only export, a machine-generated
transcript, or anything else read through a lossy step, mark every value taken
from it accordingly. The judgment is made once about the artifact and applied to
all of its values, not re-argued per field.

**Prevents.** A dose OCR'd off a photographed page sitting in the same table, at
the same apparent confidence, as one read from a publisher's text layer. A
consumer ranking or filtering by confidence cannot tell them apart, and the
transposed digit looks exactly as trustworthy as the correct one.

**Applies when.** Any artifact classified as degraded — see
[[classify-pdf-before-extracting]] for the PDF case. Machine-generated captions
are the same situation for a recording.

**Verify.** For a known scanned document, every value extracted from it carries
the degraded marking. One unmarked value means the classification did not
propagate.

**Source.** Harvested from clinical-ingest and literature-ingest, which elevate
every value from an image-only document, and from media-deep-ingest, which flags
machine-generated captions as lower confidence than creator-supplied ones.

---

# Every extracted value carries its source, locator, and method

`provenance-on-every-value` · MUST · provenance

**Rule.** No value is emitted without the artifact it came from, a locator
inside that artifact, and the method that produced it. A value missing any of
the three is a defect, not a lower-confidence result.

**Prevents.** An answer nobody can check. The first question any scientist asks
of an extracted number is where it came from, and a pipeline that cannot answer
produces output that cannot be used for a decision anyone is accountable for.

**Applies when.** Every value, every run, including values the consumer did not
explicitly ask for.

**Verify.** Take any value in any output and follow it back to the exact place
in the source. If any step requires guessing, the rule was not followed.

**Source.** Stated in the vision conversation as a non-negotiable.

---

# Use the social graph to decide whose work to mine

`rank-by-social-graph` · SHOULD · source-selection

**Rule.** Where the question is about a topic rather than a named party,
identify the researchers and institutions producing quality work on it first,
then mine their output. See [[build-the-coauthorship-graph]] for how the graph is
built.

**Prevents.** A keyword sweep that returns a thousand papers of unknown value
and no way to rank them. Ranking by citation count alone favours old work and
review articles over the labs currently producing the data.

**Applies when.** The question is topic-shaped and the field is larger than the
run can read exhaustively.

**Verify.** The run records which researchers or institutions it selected and on
what basis.

**Source.** Stated in the project vision — mapping social graphs to identify
high-quality researchers and institutions for a given topic.

---

# When several sources give the same attribute, use a stated precedence

`rank-evidence-for-a-contested-attribute` · SHOULD · extraction

**Rule.** Where more than one candidate exists for an attribute — a date, a
dose, a concentration — rank the evidence by authority, take the best available,
and record which tier it came from. A weaker tier used as a floor is marked as a
floor, not presented as measured.

**Prevents.** Silently taking whichever candidate the parser met first. A
treatment dated from the note that mentions it, rather than the administration
record, shifts a timeline by days — and the value looks equally solid either way
because nothing records which kind of evidence produced it.

**Applies when.** Any attribute a corpus states more than once at different
removes from the event. Distinct from [[report-disagreement]], which concerns
readings that conflict; here they do not conflict, they differ in authority.

**Verify.** For any such attribute, the record names the evidence tier used.

**Source.** Harvested from clinical-ingest's oncology-note rules, which rank an
explicit cycle date range above an administration record above the note's own
date, and require the weakest tier to be flagged.

---

# A windowed export is one series split for display — read all of it

`read-every-window-of-a-paginated-export` · MUST · extraction

**Rule.** When an export paginates its content across tables, pages, or date
windows, read every window and merge them. State how much of the stated total
was visible, and flag a window that is cut off.

**Prevents.** Reporting the first page as the whole series. The extracted values
are all correct and the trend they describe is wrong, because the earlier points
that would change its direction were in window two. Nothing in a single-window
extraction looks partial.

**Applies when.** Any source that splits one logical result set for display —
paginated exports, multi-table reports, result sets capped per request. Distinct
from [[report-partial-retrieval]], which concerns a source that stopped giving;
here the source gave everything and the document divided it.

**Verify.** Compare the record count against the total the document states. A
mismatch with no truncation flag means windows were missed.

**Source.** Harvested from clinical-ingest's trend-export extractor, whose real
documents split into numbered table windows and state their own date bounds.

---

# Read the slides in a recording, not only the audio

`read-slides-not-just-audio` · SHOULD · format-handling

**Rule.** Extract and read frames from recorded talks. Slides carry citations,
identifiers, and QR codes that the speaker never reads aloud.

**Prevents.** Losing the reference list for every claim in a conference
presentation. The speaker says "as we showed previously"; the slide carries the
citation, and often a QR code linking to the poster or preprint that holds the
underlying data.

**Applies when.** Any recording of a presentation, lecture, or webinar.

**Verify.** The run records how many distinct slides it detected and whether it
decoded any QR or barcode content.

**Source.** Stated in the project vision — "videos of lectures often provide
slides with citations in text or QR codes."

---

# An intervention list is not a list of drugs under test

`read-the-arms-to-know-what-is-under-test` · MUST · extraction

**Rule.** The intervention list contains everything administered. What a trial
is actually testing has to be read from the arm structure together with the arm
and intervention descriptions — and sometimes it cannot be determined at all,
in which case say so rather than guessing.

**What the flat list mixes together.** KEYNOTE-189 (NCT02578680) lists eight
interventions: pembrolizumab, cisplatin, carboplatin, pemetrexed, folic acid,
vitamin B12, dexamethasone and saline solution. One is under test, three are
chemotherapy backbone, three are premedication and supplementation, and one is
the placebo. Query the list flat and the trial counts as evidence of activity in
dexamethasone.

Alongside the agent under test, expect **backbone therapy** given in every arm,
a **comparator** — a competitor's drug here is being beaten, not developed —
**placebo or vehicle**, sometimes named as a drug, **premedication and
supportive care**, and **named regimens** like FOLFOX or R-CHOP that may arrive
as one row for the whole combination or one row per component.

**What varies between arms is not always one agent.** Differencing the arms is
sometimes informative and is not a rule:

- **One agent differs** — the add-on-to-standard-of-care design, as above.
- **Several differ** — two regimens compared head to head, where the subject is
  each combination rather than any single component.
- **The dose differs** and nothing else. Intervention names can be identical
  across arms.
- **The schedule differs** — same agent, same dose, different frequency or
  duration.
- **The route or formulation differs** — intravenous against subcutaneous of one
  molecule, which is also a naming problem
  ([[search-every-name-a-drug-has]]).
- **The sequence differs** — same agents, different order.
- **Nothing differs in the names.** NCT03590054 has three arms all listing
  abexinostat and pembrolizumab; they are dose-escalation and expansion cohorts,
  and the distinction exists only in the arm labels. It is an abexinostat trial,
  and no amount of set arithmetic over intervention names will say so.
- **There is one arm.** Single-arm studies are common in early oncology and
  offer nothing to difference.

In the last several cases the answer is in prose — arm labels, arm descriptions,
intervention descriptions, the title
([[a-registry-record-is-mostly-prose]]). Read it.

**How to attribute.** Record, per trial, which intervention plays which role and
what evidence assigned it ([[carry-the-trigger-for-a-derived-label]]).
Sponsor and code-name conventions help: an intervention carrying a company code
is usually the investigational one. Where the arms, the descriptions and the
naming still do not settle it, record the role as undetermined rather than
defaulting to "under test" ([[mark-what-a-human-would-have-confirmed]]).

This is [[do-not-mix-levels]] inside a single record: a drug present in a
document is not thereby a drug the document is about.

**Prevents.** A competitive landscape assembled from intervention names, which
credits every backbone cytotoxic with thousands of trials, credits a competitor
for trials where their drug was the control arm, and dilutes the count for the
agent actually under study. Combination designs dominate oncology, so this is
the normal case there rather than an edge one.

**Applies when.** Any count, ranking, or attribution keyed on a drug in a source
that records combinations.

**Verify.** For each drug attribution, the record names the evidence that
assigned the role — a differing agent, a stated dose or schedule comparison, a
single-arm subject, a code name, or the description text. An attribution
traceable only to the intervention list is unverified. Two cheap smells: a
landscape whose top agents are cytotoxics or dexamethasone has this bug, and a
run that produced no undetermined roles at all has probably defaulted them.

**Source.** Stated 2026-08-11 and corrected the same day after over-generalising
from a single example. Arm structures checked against NCT02578680 and
NCT03590054 via the ClinicalTrials.gov v2 API.

---

# Say how much of a source was actually used

`record-scope-narrowing` · SHOULD · output-contract

**Rule.** When only part of a source was relevant and extracted, record what
fraction was used and on what basis. A summary drawn from six of sixty slides is
a summary of those six.

**Prevents.** A consumer reading a partial extract as a representation of the
whole document, and concluding that the source did not discuss something it
covered at length in the part we skipped.

**Applies when.** Any source broader than the question — a landscape review, a
conference deck spanning a field, an annual report where one programme is
relevant.

**Verify.** For any summarised source, recover from the run record how much of
it was in scope.

**Source.** Harvested from literature-ingest's scope-discipline rule for decks
covering more than the question asked.

---

# Record the method that produced the value

`record-the-method` · MUST · provenance

**Rule.** Name the parser, the model, the prompt version, and the route taken —
text layer, OCR, figure extraction, caption, transcript. Where a value survived
triangulation, record every reading and every method that contributed
([[corroborate-before-establishing]]).

**Prevents.** A conflict nobody can explain. Method is usually the explanation:
two values differ because one came from OCR of a scan and the other from a text
layer. Without the method recorded, an investigable defect looks like an
irreducible disagreement between sources.

**Verify.** For any conflicting pair in an output, the methods are visible and
different methods are distinguishable from different sources.

**Source.** Stated in the vision as part of the provenance envelope.

---

# The assay, instrument, or edition the source used is provenance too

`record-the-source-s-method-version` · SHOULD · provenance

**Rule.** Capture the method the source used to produce a value — assay name and
version, instrument, analysis pipeline, guideline edition, protocol. This is
separate from [[record-the-method]], which records how *we* extracted it.

**Prevents.** Pooling values that are not comparable. Two tumour mutational
burden figures from different panel versions, two property measurements under
different test standards, or two staging calls under different guideline
editions look like a series and are not one. Without the version, the
incomparability is invisible and the trend line is fiction.

**Applies when.** Any value produced by an instrument, assay, model, or
standardised procedure — which covers most quantitative extraction in
biomedical, biopharma, and formulation work.

**Verify.** For any two values of the same quantity, determine whether they were
produced the same way.

**Source.** Harvested from clinical-ingest's genomics extractors, which capture
assay name, panel version, and pipeline version alongside every variant.

---

# Record what was examined, not only what was found

`record-what-was-in-scope` · MUST · provenance

**Rule.** Capture the boundary of the search alongside its results: which genes
a panel covered, which years a query spanned, which sections a document
contained, which page range an export displayed. The denominator is part of the
finding.

**Prevents.** A negative being read as evidence when it is only silence. A
hereditary panel that did not include a gene and one that included it and found
nothing are opposite results, and without the panel's gene list they are
indistinguishable — as are a literature search filtered to the last five years
and one that found nothing older.

**Applies when.** Every run, and every source that declares its own coverage: an
assay's panel, a query's filters, a report's section list, an export's stated
date bounds. See [[capture-stated-negatives]] for the related case where the
source states an absence explicitly.

**Verify.** For any absent result, determine from the output whether it was
outside the scope examined or inside it and not found.

**Source.** Harvested from clinical-ingest's germline extractor, which captures
the full panel gene list untruncated because "future re-analysis depends on
knowing exactly what was covered," and from its trend-export extractor, where
the document states its own date filter.

---

# Use a refinement loop where the cost is justified

`refine-in-a-loop` · MAY · extraction

**Rule.** Where a first extraction is incomplete or internally inconsistent, run
a propose-review-refine loop: extract, check the result against the source, and
re-extract what failed the check. Bound the loop by iteration count and by cost.

**Prevents.** Accepting a first-pass extraction that missed half a table because
the table spanned a page break. A review pass that reads the extraction back
against the document catches structural misses that no single forward pass will.

**Applies when.** The extraction is high-value, the source is difficult, and the
consumer has not constrained cost. Do not loop by default — the loop multiplies
cost for a gain that is often zero on a clean source.

**Verify.** The run records how many iterations ran and what changed on each. A
loop that ran three iterations and changed nothing after the first is a
configuration to fix.

**Source.** Stated in the project vision — "the looping technique, where needed
and where costs are justified, to iteratively refine what's extracted."

---

# The same fact in two documents is one value with two sources

`repeated-sightings-add-a-source` · MUST · output-contract

**Rule.** When a value already extracted is found again in another document, add
the second document to that value's provenance rather than emitting a second
value. The output expresses corroboration as multiple sources on one record, not
as multiple records.

**Prevents.** Double-counting. A count of how many studies report an effect, or
how many times a lesion was measured, becomes a count of how many documents
mentioned it — and because each duplicate is individually correct, nothing in
the data looks wrong.

**Applies when.** Any run over a corpus where documents repeat each other, which
is every real corpus. Distinct from [[report-disagreement]]: this is what to do
when readings *agree*.

**Verify.** Count distinct values in the output and distinct facts in the
corpus. A gap means repetition became duplication.

**Source.** Harvested from clinical-ingest and literature-ingest, whose writers
merge a repeated document into an existing record's sources rather than
appending a row.

---

# Report disagreement; never reconcile it silently

`report-disagreement` · MUST · triangulation

**Rule.** When readings conflict, the conflict is part of the output. Do not
average, do not pick the majority, do not prefer the more recent source without
saying so. Emit both values with their provenance and mark them as conflicting.

**Prevents.** Destroying the single most informative signal the run produced. A
conflict between two sources on an efficacy value is frequently the finding — it
means a units error, a different assay, a different population, or a party
reporting selectively. Averaging produces a number that no source supports and
that nobody can trace.

**Applies when.** Any time two readings of the same value differ, including
differences in unit, precision, or qualifier.

**Verify.** Search the output for values with more than one reading. Each shows
all readings. There is no code path that collapses them.

**Source.** Stated in the vision conversation as a non-negotiable.

---

# Say when a source was searched but not exhausted

`report-partial-retrieval` · MUST · output-contract

**Rule.** When retrieval from an enabled source ended for any reason other than
running out of results — throttled, timed out, quota spent, stopped at a page
cap, credential rejected mid-run — record that per source, with the reason.
Complete and truncated are different results and must be distinguishable.

**Prevents.** A throttled run being read as a complete survey. This is the
failure [[report-skipped-sources]] prevents, one level further in: there the
source was never consulted, here it was consulted and not exhausted. The second
is more dangerous, because the output shows real results from that source and
therefore looks like it worked. A consumer who cannot tell "found three" from
"got three before being cut off" will treat absence of evidence as evidence of
absence.

**Applies when.** Every run. Truncation is normal under
[[respect-source-rate-limits]], not exceptional, so this is not an error path.

**Verify.** For any source in the run record, determine whether its results are
complete or truncated, and if truncated, why. If the record shows only what was
found, the rule was not followed.

**Source.** Derived from [[respect-source-rate-limits]] and
[[report-skipped-sources]].

---

# Report the source classes the run did not use

`report-skipped-sources` · MUST · source-selection

**Rule.** Output names what was skipped, alongside what was searched. Skipped
because the consumer disabled it, and skipped because it was unavailable, are
different states and must be distinguishable.

**Prevents.** A consumer reading an answer as complete when three source classes
were never touched. Absence of evidence gets read as evidence of absence, and
the consumer has no way to know which one they are looking at.

**Verify.** Take any output and list the sources not consulted. If you cannot,
the rule was not followed.

**Source.** Derived from consumer-selects-sources and recorded in the vision as
a non-negotiable.

---

# State what the run did, not only what it found

`report-what-the-run-did` · MUST · output-contract

**Rule.** Every output carries the run record: source classes enabled and
skipped ([[report-skipped-sources]]), methods applied, artifacts retrieved and
failed, iterations run, and unresolved entities ([[never-invent-an-identifier]]).

**Prevents.** A consumer treating a thin result as a finding about the world
when it is a finding about the run. "We found two studies" and "we searched one
source class and found two studies" support entirely different decisions.

**Verify.** From the output alone, reconstruct what the run attempted. If
attempts and results are indistinguishable, the rule was not followed.

**Source.** Derived from [[report-skipped-sources]] and the vision's selectability
requirement.

---

# A company name matches too much and too little at the same time

`resolve-a-company-not-a-name` · MUST · entity-resolution

**Rule.** Resolve sponsors and assignees to organisations, not to strings.
String matching fails in both directions simultaneously, and a landscape built
on it is wrong in ways that look plausible.

**Too much.** Two unrelated companies can share a name. The standing example:
in ClinicalTrials.gov, `Merck Sharp & Dohme LLC` is the US Merck & Co, while
`Merck KGaA, Darmstadt, Germany` is a separate German company with different
assets and territories. A substring match on "Merck" merges competitors into one
entity. The German company registers under several variants of its own, and the
US one appears with acquired subsidiaries spelled out in the name field —
`Cubist Pharmaceuticals LLC, a subsidiary of Merck & Co., Inc. (Rahway, New
Jersey USA)`, and in one real record two levels deep,
`ArQule, Inc., a subsidiary of Merck Sharp & Dohme LLC, a subsidiary of Merck &
Co., Inc.`. The corporate hierarchy is free text inside the name, written
inconsistently, sometimes with unclosed brackets.

**Too little.** A wholly-owned subsidiary need not mention its parent at all.
Genentech registers uniformly as `Genentech, Inc.` and never as Roche, so
grouping by sponsor string splits one organisation's portfolio in two — and
nothing in the data hints that it should be joined.

Also expect: national operating entities registering separately, CROs and
academic centres registering on a company's behalf, name changes after
rebranding, and sponsor changes mid-programme after an acquisition, which leaves
one asset under two sponsors across its own trials.

Resolve against an organisation identifier where one exists — ROR for research
institutions, a company register or GRID/Wikidata for corporates
([[resolve-against-authorities]]) — and keep the string as recorded
([[preserve-the-surface-form]]). Where you cannot resolve confidently, say so
rather than guessing ([[never-invent-an-identifier]]).

**Prevents.** A competitive landscape that merges two rivals or splits one, both
of which change the answer to "who is ahead" without changing anything visibly
wrong in the data. The Merck case merges two companies that compete in the same
indications; the Genentech case hides the scale of a single portfolio.

**Applies when.** Any grouping, counting, or ranking by sponsor, assignee,
affiliation, or funder.

**Verify.** Group by resolved organisation and by raw string, and compare the
counts. If they match, no resolution happened.

**Source.** Stated 2026-08-11, with sponsor strings checked the same day against
the ClinicalTrials.gov v2 API.

---

# Resolve a person on the whole record, never on one field

`resolve-a-person-on-the-whole-record` · MUST · entity-resolution

**Rule.** Decide that two mentions are the same person from the **totality of
what is known about each**, not from any single field. Never merge on a matching
name alone. Never split on a differing affiliation alone. Record the confidence
and the evidence that produced it, and leave a cluster unresolved rather than
guessing ([[keep-confidence-tiers-in-the-output]]).

**The signals that actually discriminate**, strongest first:

- **A shared persistent identifier** — ORCID, OpenAlex or Scopus author id.
  Near-decisive when present, and absent from most sources.
- **A cross-source bridge.** The principal investigator on a trial and an author
  of the paper reporting that trial are very likely one person. Bridges like this
  are the only hard evidence linking a registry name to a literature name, since
  neither carries the other's identifiers.
- **Co-author overlap.** People who publish with the same people are usually the
  same person ([[build-the-coauthorship-graph]]).
- **Topic overlap**, by normalised concept rather than free text.
- **Affiliation history overlap** — the set over time, not a point-in-time match.
- **Temporal plausibility.** A career spanning sixty years is a merge, not a
  prodigy.

**Name rarity modulates all of it.** A distinctive surname carries evidence a
common one cannot: the same two matching fields that confirm one person leave
another wide open. Estimate rarity from the corpus itself rather than assuming.

**Affiliation moves, so a mismatch is not disconfirming.** It is a fact about a
date ([[verify-affiliation-currency]]). Institution *strings* also vary without
the institution changing, so normalise them before comparing, and treat an
unnormalised mismatch as no information at all.

**A name field may not hold a person.** Registries and programmes put role
titles, departments and companies where a name belongs. Detect and set these
aside rather than ranking them.

**Prevents.** Two failures, and the quiet one is the split. A person recorded
under four name variants has their evidence divided four ways, so the strongest
expert in a field ranks below people with a single tidy spelling — and nothing in
the output looks wrong, because every record is individually correct. The merge
is louder but rarer: two people fused into one with fabricated breadth of
signal, which is exactly what [[rank-by-breadth-of-signal]] then rewards.

**Applies when.** Any counting, ranking, or profiling keyed on people —
investigators, authors, speakers, inventors, committee members.

**Verify.** Every person in the output carries an identity confidence, the
identifiers resolved, and the name variants merged into them. Unresolved clusters
appear as unresolved. A run that produced one record per distinct name string did
not resolve anything.

**Source.** Measured 2026-08-12 against the AACT mirror of ClinicalTrials.gov.
One sarcoma investigator appears as `Nicolas PENEL, MD` (5 trials),
`Nicolas PENEL, PhD` (3), `PENEL Nicolas, MD` (3) and `Nicolas Penel, MD` (2):
**four strings, thirteen trials, one person**, whose best single entry is 5 — so
counting name strings ranks him nowhere and merging ranks him first. Note the
credential itself differs between variants, so even that field is unstable. His
one institution appears as `Centre Oscar Lambret`, `Centre Oscar Lambret - France`
and `Oscar Lambret Center`.

Registry-wide, 32,995 official names carry more than one affiliation, and the
most polysemous are not people at all: `Study Director` appears with 181
affiliations, `Medical Director` with 178, `Trial Manager` with 96.

---

# Resolve entities against the authority for their domain

`resolve-against-authorities` · SHOULD · entity-resolution

**Rule.** Map extracted entities to identifiers from the recognised authority:
UniProt for proteins, ChEMBL and PubChem for compounds, CAS for registered
substances, MONDO and Orphanet for disease, SNOMED CT for clinical findings,
LOINC for laboratory results, RxNorm for medicinal products, ROR for
institutions. Record which authority and which version answered.

**Prevents.** Two extractions of the same protein under a gene symbol and a
protein name never joining, so a consumer counting evidence finds two weakly
supported entities instead of one well supported one. String matching across
sources fails on exactly the entities that appear most often.

**Applies when.** The entity type has an authority and the consumer will join
across sources or runs.

**Verify.** Resolved values carry the authority name, the identifier, and the
authority version or access date.

**Source.** Set as in-scope in the vision conversation.

---

# In an exact-match source, an unresolved term and an empty result look identical

`resolve-the-query-term-before-you-trust-a-zero` · MUST · source-selection

**Rule.** Where a source matches controlled terms exactly — a registry keyed on
MeSH, a database keyed on an ontology identifier — resolve the user's wording to
that vocabulary *before* querying, and record which term was actually used. A
query built from an unresolved or wrongly-resolved term returns nothing, and
nothing is indistinguishable from a real absence.

Concretely: resolve the disease to its ontology and MeSH terms, resolve the drug
to its preferred name and synonyms, and expand where the vocabulary is
hierarchical — a query on a parent term will not return trials indexed under its
children unless you ask for them. Record every term tried, including the ones
that resolved to nothing
([[record-what-was-in-scope]], [[never-invent-an-identifier]]).

**Prevents.** Reporting that no trials exist for an indication because the
user's phrasing was not the indexed one — "lung cancer" against a corpus indexed
under "Carcinoma, Non-Small-Cell Lung", or a brand name against a registry that
records the generic. The query succeeded, the result set is empty, and the
output says the field is clear. This failure is silent, confident, and
completely wrong, and it is the single most likely way to produce a
catastrophically misleading landscape.

**Applies when.** Any source whose matching is exact rather than fuzzy —
registries, ontology-backed databases, controlled-vocabulary indexes. Also any
free-text search where the returned count is suspiciously low.

**Verify.** The run record lists every term queried, what it resolved from, and
its result count. A zero-result run that does not name the terms it tried has
reported an absence it cannot support.

**Source.** Stated 2026-08-11 while building registry access: AACT matches
condition and intervention names exactly and lower-cased, so the resolution step
decides the answer.

---

# Stay inside a source's rate limit, and back off rather than retry

`respect-source-rate-limits` · MUST · acquisition

**Rule.** Keep requests within the ceiling configured for that source, and never
run concurrency above it. On a 429 or an equivalent throttling response, honour
`Retry-After` and back off; do not retry immediately, and do not retry in a
tighter loop. Where a source publishes its remaining quota in response headers,
read it rather than assuming the configured ceiling is still accurate.

The ceiling itself is configuration, not part of this guideline. A vendor's
published limit changes without notice, and a number frozen into a snapshot goes
wrong in both directions — a run that gets blocked, or one that crawls for no
reason. The consuming project supplies the numbers, the same way it supplies
credentials.

**Prevents.** Getting the engagement's API key or IP blocked partway through a
run. The cost is not the failed run: a blocked key can take days to restore and
usually belongs to the client or to Aganitha rather than to this project, so
every other engagement sharing it stops too. Retrying hard on a 429 is what
converts a few minutes of throttling into a multi-day ban on most services.

**Applies when.** Any source reached over a network, including archives and
search interfaces, not only metered commercial APIs.

**Verify.** The run record shows, per source, the ceiling that was in force, how
many requests were made, and every backoff event. A run against a metered source
with no ceiling recorded was not configured, it was guessed.

**Source.** Stated 2026-08-10 — rate limits must be honoured by both the driver
and by generated project skills.

---

# When a document does not identify its own subject, record that

`say-when-the-subject-came-from-context` · MUST · provenance

**Rule.** If a document carries no identifier for what it is about — no subject
name, no accession, no compound label — and the attribution comes from the
folder it arrived in, the batch it belonged to, or what the consumer said,
record that the attribution is contextual rather than from the document.

**Prevents.** A record silently attached to the wrong subject. A page with no
identifier looks exactly like one that has been positively matched, so a
misfiled document contaminates a cohort or a compound series with nothing to
trace. Recording the basis is what makes the error findable later.

**Applies when.** Any corpus where documents arrive grouped rather than
individually identified — clinical exports, supplementary file bundles, batch
downloads, scanned folders.

**Verify.** For any record, determine whether its subject was stated in the
document or inherited from context.

**Source.** Harvested from clinical-ingest's lab extractor, whose exports
routinely carry no name, date of birth, or record number: "identity linked by
folder/date context. Verify this record belongs to the correct patient."

---

# A document carries several dates — record which one the record is anchored to

`say-which-date-you-used` · MUST · provenance

**Rule.** Where a source states more than one date, capture the one the record
is anchored to and say which it is. Keep the others. Do not collapse them into
an unlabelled date field.

**Prevents.** Series that cannot be compared and timelines that are quietly
wrong. A specimen collected in June and reported in August is one event with two
dates, and a cohort mixing collection dates with report dates has an artificial
spread nobody can see. The same applies to submitted against published, priority
against grant, and last-updated against first-issued.

**Applies when.** Nearly every source class. Specimens have collection and
report dates; papers have submission, acceptance, and publication; patents have
priority, filing, and grant; living references have a last-revised date and no
publication date at all.

**Verify.** For any dated record, name which of the source's dates it uses.

**Source.** Harvested from clinical-ingest's germline extractor — the collection
date anchors the record, the signed date is captured separately and flagged when
later — and from literature-ingest, which takes a living reference's
last-updated date as its year.

---

# One molecule, many names — resolve to the set, never to one

`search-every-name-a-drug-has` · MUST · entity-resolution

**Rule.** A drug carries several names simultaneously, and every source records
whichever one its author happened to use. Resolve to the whole set before
searching, query all of it, and record which name returned what.

The name classes, and why each one exists:

- **Company code** — assigned before anything else, and the only name an early
  programme has. `mRNA-1273`, `LY3437943`, `BMS-986165`.
- **More than one company code for the same molecule.** A candidate that is
  licensed, co-developed, or acquired picks up the new owner's code alongside
  the originator's. Two codes, one molecule, and in a trial landscape they look
  like two competing programmes unless someone links them.
- **INN or USAN** — the durable generic name, `elasomeran`. It is the best
  identifier available, and it does not exist until it is assigned, so an
  investigational molecule may have none at all.
- **Brand names, plural** — `Spikevax`. Brands vary by market for the same
  molecule and the same company, so a European filing and a US one can look
  unrelated.
- **Brands of generic equivalents** — one off-patent ingredient carries many
  marketed names, none of which is the one the trial used.
- **Salt, ester, and hydrate forms** — the name changes, the active moiety does
  not.
- **Route and formulation variants** — the same active ingredient given
  intravenously and subcutaneously is a different product and often a different
  trial programme. Whether those count as one drug depends on the question:
  they are one molecule for a mechanism question and two products for a
  competitive one. **Decide which question you are answering and record the
  decision** rather than letting the search settle it by accident.

**Where to resolve.** RxNorm is authoritative for marketed and approved
products and gives ingredient, brand, precise-ingredient and dose-form
relationships cheaply — for pembrolizumab it returns the INN, both brands, the
biosimilar-suffixed form, a combination product, and dose forms that separate
the intravenous product from the subcutaneous one.

Its coverage is uneven, though, in a way worth knowing before you trust an empty
answer: vaccines, biologics and company codes are frequently absent altogether,
where MeSH carries the full chain. **Query both, and treat a thin result from
either as a gap in that vocabulary rather than a fact about the molecule.**

**Beware the approximate matcher.** When an exact lookup finds nothing, RxNav
offers approximate candidates ranked by string similarity, and those are not
resolutions. Asked for `Spikevax` or `MK-3475` it returns candidates that are
**dead concepts carrying no name, no term type and no relationships** — for
`MK-3475`, four of them with identical scores, which is a matcher discriminating
nothing. A pipeline that stores the top candidate has invented an identifier for
a molecule RxNorm does not name ([[never-invent-an-identifier]]), and the failure
is worse than an empty result because it looks like success. Accept an
approximate candidate only if it resolves to actual names; otherwise report that
the vocabulary has no entry.

RxNorm is weak-to-absent for investigational molecules, which is exactly where
code names live — so for anything pre-approval expect to reach RxNorm and find
nothing, and fall back to the source's own recorded names, sponsor documents,
and search. An empty RxNorm result for a phase 1 asset is the normal case and is
not evidence the drug does not exist ([[tool-failure-is-not-a-finding]] for the
adjacent case where the lookup itself failed).

Keep every surface form found ([[preserve-the-surface-form]]), and treat two
names established to be one molecule as one entity thereafter, the way
[[derivatives-of-one-sample-share-its-identity]] treats work derived from one
specimen.

**Prevents.** Two failures that both pass review. Searching a brand name
against a registry that indexed the company code returns zero, and zero reads as
"nobody is developing this" — see
[[resolve-the-query-term-before-you-trust-a-zero]]. And counting a licensed
molecule twice, once per company code, inflates a competitive landscape with a
rival that does not exist and hides that the two programmes are the same asset.

**Applies when.** Any search or count keyed on a drug name, in any source.
Most dangerous for early-stage assets, where the code name is the only name and
the naming is least standardised.

**Verify.** For each drug in the output, the run record lists every name
searched and its result count, and states whether route or formulation variants
were treated as one drug or several. A drug represented by a single name string
was not resolved.

**Source.** Stated 2026-08-11: the same drug is referred to by company code
names — more than one where a candidate is licensed — by INN, by brand name, by
the brands of generic equivalents, and by different names for the same active
ingredient given by a different route.

Measured 2026-08-12 against the AACT mirror of ClinicalTrials.gov, on trials
indexed to the MeSH heading `carcinoma, non-small-cell lung`. The INN
`pembrolizumab` returns 444 trials, the brand `keytruda` 35, the company code
`mk-3475` 9; the union is 464. So the INN — the strongest single identifier
available, and the one an analyst would reasonably pick — misses **20 trials, 4%
of the landscape**. Those trials name the drug only as `Keytruda`, `KEYTRUDA®`,
`EU-Keytruda®`, `EU sourced Keytruda`, `Keytruda-EU`, or
`Keytruda Injectable Product`. The market and route qualifiers are the same
variation described above, appearing here inside the drug name string itself
rather than as a separate field, so no amount of exact matching on a normalised
name recovers them.

Measured the same day, on the whole intervention table rather than one
indication: the brand `Keytruda` alone matches **138 trials**, while the name set
resolved from it — adding `pembrolizumab` and `mk-3475` — matches **2,528**. The
seed name finds **5% of its own landscape**, and the 95% it misses carries no
marker distinguishing it from a real absence. Resolving a drug and then searching
only the string that was typed is this rule failing one step further down the
pipeline than it is usually described.

Seeding `Spikevax` and `mRNA-1273` returns `TAK-919` in the same MeSH concept —
the licensing case above, surfaced by the vocabulary rather than assumed — along
with the formulation variants `mRNA-1273.211` and `mRNA-1273.214`, which are
separate trial populations.

Checked the same day against RxNav and MeSH: RxNorm resolves `Keytruda` and
`zanidatamab` to full name sets, and has **no live concept for `Spikevax` or
`MK-3475`** — the exact lookup returns nothing, and the approximate candidates
offered instead, rxcui 2601548 and 203435, have no properties at all. MeSH
carries both chains, and gives `pembrolizumab`, `MK-3475`, `Keytruda`,
`lambrolizumab` and `SCH-900475` under one heading — *two* company codes for the
one molecule, which is the licensing case described above.

---

# The public registry is not the only registry

`sponsors-run-their-own-registers` · SHOULD · source-selection

**Rule.** Large sponsors maintain their own study registers, and they hold
material the public registries do not. Check the sponsor's register for any
trial that matters, and record whether you did.

GSK, Pfizer, Novartis, Roche and their peers publish these under transparency
commitments. What they add beyond ClinicalTrials.gov varies by sponsor, and
typically includes result summaries written for different audiences, protocols
and statistical analysis plans, clinical study report synopses, plain-language
summaries, and a route for requesting patient-level data. For a trial where the
registry posting is thin and no paper exists, the sponsor's register is
sometimes the only substantive account.

**They are built for reading, not for mining.** These are JavaScript
applications with search forms rather than APIs — GSK's register serves about
five thousand characters of text behind seventeen scripts on its landing page,
with the content arriving after execution. Expect to drive a browser or work
from the sitemap rather than to fetch and parse. Budget for that before
promising coverage, and treat a sponsor register as a per-trial follow-up rather
than something to sweep ([[escalate-cost-only-on-evidence]]).

Check the site's terms and its robots file before any automated access — GSK's
permits crawling outside a private path and publishes a sitemap, and others
differ. This is the open access-terms question in `docs/vision.md`, and until it
is settled, record what was accessed and how.

Coverage is per sponsor and partial: a register covers that sponsor's own
trials, and only from whenever their commitment began. Absence from one proves
nothing ([[expected-absence-is-not-a-gap]]).

**Prevents.** Concluding no results exist for a trial whose sponsor published a
full summary on their own site. It also loses the documents that make a result
interpretable — the protocol and the analysis plan — which is precisely what
[[carry-what-makes-a-result-comparable]] demands and the public registry
frequently lacks.

**Applies when.** Any trial from a large sponsor where the registry posting is
thin, no publication is linked, or the protocol and analysis plan matter.

**Verify.** For trials whose results the output relies on, the record says
whether the sponsor's own register was checked and what it held.

**Source.** Stated 2026-08-12, with the GSK study register checked the same day
for how it serves content.

---

# Suspect the extraction before believing that sources disagree

`suspect-extraction-first` · SHOULD · triangulation

**Rule.** When readings conflict, first check whether the extraction was wrong —
wrong cell, wrong column header, wrong arm, lost unit prefix, footnote ignored.
Only after the extraction is confirmed correct is the disagreement a genuine
difference between sources.

**Prevents.** Reporting a real disagreement between two companies when the truth
is that one parser read the adjacent column. The most common cause of a
conflicting value is our own error, and recording it as a source conflict hides
a bug we could have fixed.

**Applies when.** Any conflict surfaced by [[report-disagreement]].

**Verify.** The conflict record states whether the extraction was re-checked and
what the re-check found.

**Source.** Stated in the project vision — "triangulating extracted information
to identify and fix issues in extraction."

---

# A source restating another's result is not a second reading of it

`synthesis-is-not-independent-corroboration` · MUST · triangulation

**Rule.** Before treating two sources as agreeing, establish that they are
independent. A review, guideline, press summary, or talk that cites a study is
carrying that study's result, not confirming it. Trace a value to the work that
produced it and count that once.

**Prevents.** Manufactured confidence. A finding restated across a guideline,
two reviews, and a conference deck looks like four-way corroboration and is one
study — and the more influential the original, the more restatements it
accumulates, so the appearance of consensus grows with citation count rather
than with evidence.

**Applies when.** Any corroboration step over a corpus containing tertiary
material. [[corroborate-before-establishing]] assumes independent readings; this
is what establishes that they are independent.

**Verify.** For any corroborated value, list the distinct works behind it. If
two sources trace to the same study, they counted once.

**Source.** Harvested from literature-ingest's clinical-reference extractor,
which classes tertiary syntheses separately from primary research precisely
because they report no new results of their own.

---

# Who registered a trial is not who is developing the drug

`the-sponsor-is-not-the-developer` · MUST · extraction

**Rule.** The sponsor field says who takes regulatory responsibility for that
trial. It does not say who discovered the molecule, who owns it, or who will
commercialise it. Treat developer attribution as an inference to be made and
evidenced, never as a field to be read.

The sponsor can be, and often is, none of the above:

- **An academic centre or investigator** running an investigator-initiated
  trial, with the company supplying drug and appearing only as a collaborator —
  or nowhere at all.
- **A CRO or a national affiliate** registering on the sponsor's behalf.
- **A licensee rather than the originator**, so the trial sponsor and the
  molecule's discoverer are different companies, each with their own code name
  for it ([[search-every-name-a-drug-has]]).
- **A partner in a co-development**, where lead sponsor and collaborator
  reflect who filed rather than who contributes what.
- **The acquirer**, on trials begun by a company that no longer exists — while
  the earlier trials for the same asset still carry the old sponsor.

Build the attribution from more than the field: lead sponsor and collaborators
together, the same asset's other trials and who sponsored those, the intervention
naming — a company code name in the intervention text is strong evidence of
origin — and, where it matters, the disclosure sources that state a licensing
deal outright ([[look-beyond-the-literature]],
[[mine-decks-for-science-not-just-status]]). Record which of these supported the
conclusion ([[carry-the-trigger-for-a-derived-label]]), and where the evidence
is thin, say the developer is undetermined rather than defaulting to the
sponsor.

**Prevents.** Crediting a molecule to the wrong company, which corrupts exactly
the questions a landscape is built to answer: who is ahead, who to partner with,
who to watch. Reading the field naively also systematically over-credits large
sponsors, who register more trials, and erases originators who licensed early —
the two errors point the same way and reinforce each other.

**Applies when.** Any claim about who is developing, who owns, or who is
competing on an asset — as opposed to who ran a particular trial.

**Verify.** For each developer attribution, the record names the evidence. An
attribution that traces only to the lead sponsor field is a restatement of that
field, not a finding.

**Source.** Stated 2026-08-11: working out the developer of a drug from a
sponsors list is tricky.

---

# A missing or failing tool says nothing about the document

`tool-failure-is-not-a-finding` · MUST · extraction

**Rule.** Separate "the document does not contain this" from "we could not
look." A non-zero exit from a parser, an absent binary, a timeout, or an
unconfigured dependency is a fact about the environment. Never record it as a
negative result about the content, and never let it satisfy a check.

**Prevents.** A text extractor exiting because the PDF tool is not installed,
and that being recorded as "no text layer — treat as scanned," which routes a
clean digital document through OCR and degrades every value from it. The run
looks successful and the output is quietly worse.

**Applies when.** Every tool invocation. It matters most where a tool's failure
mode and a real negative result produce the same empty output.

**Verify.** For every empty or negative result in the run record, the reason is
recorded and distinguishes an environment failure from a genuine absence.

**Source.** Harvested from clinical-ingest — "an exit 3 is a missing dependency,
not a classification result, so it never implies anything about the document."

---

# Never force a record into the nearest category

`unclassified-is-a-valid-outcome` · MUST · extraction

**Rule.** A record that does not confidently match any category stays
unclassified and is reported as such. Do not assign the closest category, and do
not drop the record.

A catch-all category is not an escape from this. Assigning something to Other or
General because nothing else fits well is a last resort that must be recorded as
one, never a default taken for convenience.

**Prevents.** Destroying the meaning of every category at once. If unmatched
records are pushed into the nearest bucket, the buckets stop describing anything
— and the pressure to do it is strongest exactly when the unclassified pile is
large, which is when the distortion is worst.

**Applies when.** Every classification step. The same reasoning as
[[never-invent-an-identifier]], applied to categories instead of identifiers.

**Verify.** The output reports an unclassified count. A run over a messy corpus
that classified everything did not classify, it assigned.

**Source.** Harvested from literature-search-ingest, where 6,472 of 7,181
retrieved records stayed deliberately unclassified rather than being forced into
one of four buckets.

---

# An unrecognised document is extracted at low confidence, not skipped

`unknown-type-is-captured-not-dropped` · SHOULD · extraction

**Rule.** When a document does not match any known type, do not guess a type and
do not discard it. Extract what can be read using generic handling, mark it as
unrecognised and low-confidence, and record enough about it that a recurring
pattern can be promoted to a real type later.

**Prevents.** Two failures at once. Forcing a wrong type applies the wrong
extraction rules and produces confident nonsense; dropping the document loses it
silently, and the documents that fail to classify are often the novel ones worth
the most.

**Applies when.** Any corpus with heterogeneous or evolving document types,
which in practice means any handed-over corpus.

**Verify.** The run record lists unrecognised documents with what was extracted
from each. A run over a varied corpus that recognised every document is
suspicious rather than clean.

**Source.** Harvested from clinical-ingest — an unrecognised document is
captured at needs-review confidence with a generic extractor and flagged, so a
future session can promote it if the pattern recurs.

---

# Apply more than one method to a source that matters

`use-more-than-one-method` · SHOULD · extraction

**Rule.** Where a value is load-bearing for the answer, extract it by at least
two methods — a different parser, a different prompt, a different modality of
the same artifact. Hand both results to triangulation
([[corroborate-before-establishing]]).

**Prevents.** A single method's systematic error passing as fact. One parser
drops the footnote that qualifies the number; one prompt reads a control arm
value as the treatment arm. With one method there is nothing to notice the error
against.

**Applies when.** The value materially changes the answer, and the cost of a
second pass is small relative to the cost of being wrong. Not every value earns
this.

**Verify.** The provenance record for the value names more than one method
([[record-the-method]]).

**Source.** Stated in the project vision — "ensemble approaches, applying
multiple sources, methods and tools."

---

# An affiliation is a fact about a date, not a property of a person

`verify-affiliation-currency` · MUST · entity-resolution

**Rule.** Treat an institutional affiliation as time-bound. When recording where
someone works, confirm it against a current profile or their most recent output,
and record the date the affiliation was observed. A historical affiliation is
kept as historical, not corrected away.

**Prevents.** Attributing current work to a former employer. Researchers move,
and an affiliation harvested from a paper is accurate for that paper and
possibly years stale — so a map of which institutions are active on a topic can
be a map of where those people used to be, with every individual record
technically correct.

**Applies when.** Any extraction of affiliations, including those taken from
author lists, funding records, and conference programmes.

**Verify.** For any affiliation, recover the date it was observed and the source
that stated it.

**Source.** Harvested from kol-finder — "Confirm currency — researchers move.
Check their faculty profile or most recent paper affiliation."

---

# Confirm required tools are present before starting, and stop if they are not

`verify-tools-before-running` · MUST · acquisition

**Rule.** At the start of a run, check that the tools the selected methods need
are installed and configured. If one is missing, stop and say which, rather than
silently falling back to a weaker method. Record in the run record which tools
were available.

**Prevents.** A run that completes with a fraction of the intended extraction
because a parser was absent, reported as a finished run. Silent degradation is
undetectable downstream: the output has the right shape and less in it.

**Applies when.** Every run. It matters most for skills that instruct an agent
to use tools from the surrounding environment rather than shipping them, where
the same instructions produce different results on two machines.

**Verify.** The run record lists the tools the run required and which were
found. A run that used a fallback method says which tool's absence caused it.

**Source.** Harvested from clinical-ingest, literature-ingest, and media-deep-
ingest, each of which opens with a preflight tooling check and stops rather than
working around a missing dependency.

---

# A stopped trial is not a failed drug, and four different things look alike

`why-a-trial-stopped-is-usually-not-about-the-drug` · MUST · extraction

**Rule.** Never read a trial's status as a verdict on the intervention. Separate
the status values, read the stated reason, and classify the reason before using
it for anything.

**The statuses mean different things.** Terminated means enrolment began and
stopped. Withdrawn means nobody was ever enrolled — there is no data and there
never was. Suspended is a pause the sponsor expects to lift. And **Unknown is a
fact about the record, not the trial**: it marks a study whose sponsor stopped
updating, and it is the second most common status in ClinicalTrials.gov at
roughly 96,000 studies, against 34,000 terminated and 17,000 withdrawn. Counting
Unknown as stopped, or as running, are both wrong.

**The stated reason is free text and mostly is not scientific.** Read
`why_stopped` and classify it:

- **Business or strategic** — "Company decision", "adjustments in the company's
  strategy", a device no longer manufactured, a merger, a portfolio
  reprioritisation, funding withdrawn.
- **Operational** — slow recruitment, low inclusion rates, inability to enrol,
  staffing changes at the site, a component becoming unavailable. Recruitment
  failure is the single most common reason and says nothing about efficacy.
- **Scientific** — futility at interim, no objective response, a changed
  benefit-risk assessment, a data monitoring committee stopping the study.
- **Uninformative** — "Company decision" and its relatives assert only that
  someone decided. Record it as unclassifiable rather than filing it under
  business, which is a guess ([[unclassified-is-a-valid-outcome]]).

**Never classify on a bare keyword match — check for negation first.** A reason
that explicitly *denies* a safety cause still contains the word "safety":
"terminated for business reasons, not due to any safety concern" contains both
`safety` and `concern`, and a keyword rule files it as a scientific stop, which
is the exact inversion of what the sponsor wrote. The same holds for "no safety
signal was observed" and "not related to toxicity". Require that the term not be
negated within the surrounding clause before it counts, and where the text is
short and ambiguous, leave it unclassified rather than guessing
([[capture-stated-negatives]]).

In a sample of terminated trials the reasons split roughly evenly across those
first three, so most stopped trials stopped for reasons unrelated to whether the
drug works. Carry the verbatim reason with any classification you assign
([[carry-the-trigger-for-a-derived-label]],
[[capture-the-source-s-conclusion-verbatim]]).

Where the reason matters commercially, the registry field is often terse and the
real account is elsewhere — a call transcript, trade press, or a sponsor's own
register ([[look-beyond-the-literature]]).

**Prevents.** Inverting a competitive read. A programme dropped because the
sponsor exited the therapeutic area is evidence about the sponsor, not the
mechanism — and treating it as a signal that the target does not work is exactly
backwards, since the asset may be available to license. The complementary error
is treating a futility stop as a business decision and continuing to count a
dead mechanism as live.

**Applies when.** Any use of trial status or termination as evidence about a
drug, target, or mechanism.

**Verify.** For each stopped trial in the output, the verbatim reason is present
and its classification is recorded — including "unclassifiable". A run that
classified every reason has over-read the terse ones.

**Source.** Stated 2026-08-12, with status counts and real `why_stopped` values
checked the same day against the ClinicalTrials.gov v2 API.

The negation guard is carried over from the angiosarcoma case portal's
`clinical-trials-ingest`, where a keyword rule labelling early stops as safety
signals was found misreading text that explicitly denied a safety cause. Their
fix — requiring the term not be negated within a short window — was a real bug
caught in validation, not a hypothetical.
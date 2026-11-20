# Audit log

| Date (UTC) | Scope | Result | Coverage limitations |
| --- | --- | --- | --- |
| 2026-11-20 | Tracker initialization | Four initial Issues, including SNX's Cataclysm/Classic item report (#1). | No Discord channel history reviewed at setup time. |
| 2026-11-20 | **First partial Discord browser audit**: visible message windows in Bug Reports (Nov 19–20), Questions & Help (Nov 19–20), visible Suggestions Forum topic previews (Nov 9–20) | Created **14 Issues**: #5–#11 (seven potential bugs) and #12–#18 (seven suggestions); grouped two melee-range proposals in #12; kept all unverified pending evidence. | **Not a full historical audit.** Browser readout reflects only loaded message windows and visible forum previews; archived topics, older messages, most thread replies, exact message links and screenshot contents were not comprehensively available. Attachments were not republished. |

| 2026-11-20 | **Changelog comparison**: visible official releases 0.7.0–0.7.4 (Nov 17–20) against open Issues | Updated #1, #6–#10, #12, #15; closed #15 as shipped in 0.7.4; #9 probable correction pending retest. [Details](CHANGELOG_CROSSCHECK_2026-11-20.md). | Releases before Nov 17 and full Nov 10–20 historical community messages were **not accessible in loaded browser context**. |

## Items intentionally not opened as active bugs

- **AZS_GetLocalTime UTC issue:** A Nov 20 reply says changelog version 0.7.4 has corrected local-time behavior. This was not independently tested; leave in audit notes unless evidence of a regression appears.
- **Time Fracture / Deep Freeze Echo:** A participant explains the absence of Echo as intended, due to balance and minimum cooldown limits. Treat as balance discussion rather than confirmed bug.
- **Suggestions Forum topic about changing the Cataclysm last-arena model:** Only the title was visible; no rationale or thread content was available, so no Issue created.
- Generic support questions about resetting graphics, transferring progress, or target prioritization were not converted into bugs without an identified defect.

## Next audit

Load older Bug Reports and Questions & Help message history and open the Suggestions Forum threads individually (including archived ones), inspect available attachments in context, acquire original Discord message permalinks, and check against all current Issues before creating new ones.

For every further audit, record: checked time range; channels/threads reached; created/updated/merged counts; screenshot review and redaction; and inaccessible segments. Do not describe an incomplete snapshot as exhaustive.

## Historical review follow-up — 2026-11-20

**Coverage status: partial.** Requested start: Nov 10 inclusive (Europe/Paris).

| Source | Evidence captured | Outstanding verification |
| --- | --- | --- |
| Bug Reports | 197 unique visible messages, from the channel welcome on Nov 16 at 00:09 to Nov 20 at 08:35. | The beginning was reached. The Discord thread panel listed no threads. Some attachments still require visual inspection. |
| Questions & Help | 105 unique visible messages, from the channel welcome on Nov 16 at 00:08 to Nov 20 at 11:57. | The beginning was reached. The Discord thread panel listed no threads. Several screenshots and support references still require visual inspection or classification. |
| Suggestions Forum | 71 observed topics created in the window out of 75 indexed topics. 16 in-window threads opened. Forum listing checked under activity and creation-date ordering. | 55 identified in-window threads still require opening. Exhaustive historical activity on older topics, archived or restricted topics, and thread attachments is unverified. One direct-link attempt in a new tab led to Discord sign-in. |
| Official changelogs | 41 posts covering 0.6.1–0.7.4 from Nov 12 to Nov 20, from the beginning of the visible channel. | Earlier Nov 10–11 releases were not visible in this channel. Release notes establish the published changes. Retests remain separate. |
| GitHub | Matched observations against the 18 Issues present at the start, including their comments. Created #19–#44 and enriched existing matching Issues. | #3 remains open for full coverage. The project listed #5, #6 and #7 under Needs Review and #15 and #23 under Done. Pending cards and priorities are tracked below. |

The prior source date on #13 was corrected. Item identification from the image narrowed #11 to Deathbringer’s Will. The launcher reports were split by symptom: #10 for slow transfer/browser loading and #22 for an update that can stop and launch the preceding version. The supporting media and exact Discord member-area message links stay out of the public repository.

### Published corrections and related changes

| Release | Match and disposition |
| --- | --- |
| 0.6.4 | Level-up cards pause co-op revive and preserve progress. #25 checks whether the report concerned a different card type or current-build behavior. |
| 0.6.8 | Preserve stored level-ups after jewelry choices, persist interface scale, and keep Hurricane and related effects ticking during co-op cards. Correct the Ashen Band of Destruction's upgrade wording and Echo's misleading overflow above 100%. Fix two known long-run FPS mechanisms. #35 retains the current-build performance retest. |
| 0.6.8 / 0.6.9 | Correct Fire Cat's white shop texture and, separately, buried enemies and ground placement. Skin persistence on co-op rejoin and the later Lady Deathwhisper report need separate verification. 0.6.9 also corrects missing or stale armory gear for the documented cases. |
| 0.7.0 / 0.7.1 | Improve rerolls and limit multiple healing rings/trinkets in offers. Show remaining files at the end of an update and fix a first-start crash. #20 and #22 retain the narrower symptoms. |
| 0.7.2 / 0.7.3 | Correct inaccessible guardian lairs, Pandaren helms, Cataclysm minimap artwork and Vashj’ir pursuit. Version 0.7.3 also makes shirts hideable and restores the starting shirt. #24 (Uldum marker overlay) and #26 (guardian presence) call for separate tests. |
| 0.7.4 | Publishes Netherwind Blizzard visual following (#23, closed), Vashj’ir spawning depth and swimming speed (#9, retest), local time API and racial/passive API (#15), Death Knight HD elf eyes, Elementium Signet icon, Dragon Soul boundaries/rescue, and ground-effect projection onto high walls. |
| 0.7.4 | Daily and weekly quests and a Badge of Justice cosmetic vendor now match the core forum proposal. Exact rewards and optional constraints in the discussion still require design review if pursued. |

The Dragon Soul thread contained three image posts. The inspected image showed the character below the normal battlefield. Version 0.7.4 documents a narrower starting arena and return after falls. A current-build recurrence is needed to establish the reported position still occurs. Time Fracture’s portal Echo behavior was explained as intentional for balance. Individual account, moderation, and access-support cases were kept out of the public game tracker.

See the [priority tracker](PRIORITIES.md) for triage and retest items.

## Forum backlog reviewed — 2026-11-20

- Opened the 55 previously pending topics, reaching **71/71 indexed topics within the Paris-time window**, and checked four older visible topics for follow-ups. Matched displayed reply counts in the opened backlog, including all 14 visible entries in mobile feedback. The newest and oldest cards came from the chronological listing. Its available display controls did not provide a separate inventory of archived or restricted topics.
- Created **14 Issues, #45–#58**, and updated **8 existing Issues** including the audit tracker. Mobile graphics-device loss (#45) and touch talent tooltips (#47) are distinct. The former includes a photographed device-loss diagnostic and needs a current-build retest. The Auto Shot screenshot shows a question-mark icon on both the upgrade card and the spell strip (#7). The Hunter comparisons need a controlled damage test (#8).
- Confirmed released changes for controller jump (0.6.4), the delayed boss while a treasury portal remains open (0.6.6), and the **Owned** shop filter, mobile minimap controls, and in-run jewelry banish (0.7.0). The proposed pre-run item exclusions are tracked in #48. The shirt-thread reply acknowledges the fix documented in 0.7.3. The 0.7.4 Endless mode partly addresses requests for additional endgame challenge (#58).
- Deduplicated capped crit, cooldown and capped buff-effect reward offers into #51. #44 now carries additional accidental-selection evidence, #43 separates achievement placement from intended progression, and #41 and #39 record the related Affliction and starter-spell examples. Kept community Discord setup and title-only ideas in the review notes.
- **Still partial for the full audit.** The corpus of listed forum topics has been opened. Attachment content is only partially inspected. A few title-only or attachment-only posts need content follow-up, and coverage of archives outside the visible forum listing is unverified. Public updates contain anonymized technical summaries.

## Issue sources and image review

Added and verified direct Discord message or forum links on all 54 audit Issues (#5–#58). Forum and message access remains subject to Discord permissions. The approved gameplay crops are embedded in the Auto Shot (#7) and Deathbringer’s Will (#11) Issues. The Hunter comparison (#8) includes player identifiers and needs redaction. The mobile graphics report (#45) links directly to its original image message. Remaining evidence, archive coverage and Kanban checks are tracked in #3.

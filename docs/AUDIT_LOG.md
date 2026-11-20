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

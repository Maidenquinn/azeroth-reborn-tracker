# On-demand Discord audit workflow

**Operating mode:** the moderator asks ChatGPT to audit the community's Discord channels when desired. No bot, cron task, or background monitoring.

## Sources
- Bug Reports: https://discord.com/channels/1567264381929259189/1571654342023581696
- Suggestions Forum: https://discord.com/channels/1567264381929259189/1569325066553000006

## Procedure for each audit
1. Read the accessible Discord channel messages and suggestion forum threads, including follow-up replies and attached images where available. The moderator may need to open Discord in a browser or provide an export, since a channel URL alone grants no access.
2. Read open and closed GitHub Issues to establish which items are already tracked.
3. Extract potentially meaningful bug reports and suggestions. Record source URL and date, observable evidence, symptoms, mode/class/version if known, steps to reproduce if documented, and screenshots only if approved for public use.
4. Deduplicate multiple reports describing the same root issue, retaining additional approved source links and frequency indicators. Mark uncertain matches for review.
5. For bugs, write actual vs expected behavior and a provisional priority with rationale. For suggestions, consider benefit, game fit, scope, potential risks and possible refinements; make a recommendation, not a unilateral decision.
6. Sanitize and publish new GitHub Issues, update existing Issues where new corroboration or progress evidence appears, and avoid overwriting historical context.
7. Update issue states only when a reliable staff/developer statement or verification supports it. Unconfirmed reports stay in Needs Review.
8. Report audit coverage (date range, channels/threads reviewed, inaccessible sections), Issues created/updated, duplicates merged, items needing developer attention, and outstanding evidence.

## Suggested user request

> Audit the Reborn Discord Bug Reports channel and Suggestions forum since our last review. Analyze replies and attached screenshots if accessible, deduplicate against all GitHub Issues in Maidenquinn/azeroth-reborn-tracker, and create/update only appropriate tickets. List coverage gaps and what changed. Do not publish personal/private content.

## Restrictions

- The GitHub repository is public. Do not publish unapproved private Discord content, media, personal identifiers or secrets.
- Do not claim complete Discord coverage if older messages, archived forum threads or attachments were not accessible.
- No continuous automation is promised; follow-up audits require a new user request.

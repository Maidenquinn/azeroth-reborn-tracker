# Azeroth Survivors: Reborn — Community Tracker

Community-maintained bug reports and suggestions for Azeroth Survivors: Reborn.

> Unofficial community tracker. Only SNX and the game developers confirm implementation, acceptance, testing or rejection.

## Quick links

- **[Live GitHub Projects Kanban](https://github.com/users/Maidenquinn/projects/1/views/1)** · [All Issues](../../issues)
- [Report a bug](../../issues/new?template=bug_report.yml) · [Suggest an improvement](../../issues/new?template=feature_request.yml)
- [Manual audit guide](docs/MANUAL_REVIEW.md) · [Review checklist](docs/REVIEW_CHECKLIST.md) · [Audit log](docs/AUDIT_LOG.md) · [Changelog cross-check](docs/CHANGELOG_CROSSCHECK_2026-11-20.md)
- [Discord Bug Reports](https://discord.com/channels/1567264381929259189/1571654342023581696) · [Suggestions Forum](https://discord.com/channels/1567264381929259189/1569325066553000006)

## Tracking

The native GitHub Project **Azeroth Reborn - Community Tracker** is now created, linked to this repository, and its board has five columns: **Needs Review, Todo, In Progress, Testing, Done**. The current board was initially populated with three open Issues. The single bug report [#1](../../issues/1) is still **unconfirmed**, and should be moved from the default Todo column to Needs Review until evidence is available.

GitHub Projects field and status edits cannot currently be made with the connected GitHub integration. A moderator can drag cards within the board itself. For layout and optional custom fields, see [configuration](docs/PROJECT_SETUP.md).

## On-demand Discord reviews — no bot

The moderator requests an audit whenever desired. ChatGPT reads only Discord messages and attachments that are accessible in that session or provided as an authorized export, checks existing open/closed Issues, identifies duplicates, enriches reports, and creates/updates Issues directly on GitHub. No automatic monitoring, Discord bot or scheduled collection is used. A Discord URL alone is not sufficient access to message history.

### Editorial rules

1. Keep bug reports and suggestions in English, with direct source links when authorized.
2. Separate player claims, observed evidence and provisional priority recommendations.
3. Never fabricate reproduction steps, screenshots, fixes, assignments or developer decisions.
4. Only put confirmed progress into In Progress, Testing or Done.
5. This repo and its project links are public-facing: do not copy private Discord content, player identifiers or screenshots without permission.
6. Add an audit coverage record for each review, including inaccessible channels/threads.
7. Preserve existing Issue history and link duplicate reports to one canonical Issue.

## Initial issues

- [#1 — Cataclysm trinkets in Classic](../../issues/1) — SNX report, unverified.
- [#2 — Finalize board metadata](../../issues/2) — project exists; optional fields and views remain.
- [#3 — Complete historical Discord audit](../../issues/3) — initial partial snapshot done; older history, thread replies and screenshots remain.

**First partial browser audit completed on 2026-11-20:** 14 community Issues (#5–#18) added from visible Discord messages and forum previews. The official 0.7.0–0.7.4 changelogs were subsequently reviewed: #15 was closed as shipped in 0.7.4, and #9 was flagged as probably fixed pending retest. This was **not** a complete historical scan; screenshots and archived topics are still pending review. See the [audit log](docs/AUDIT_LOG.md). The project may be transferred to the official Reborn team with their agreement.

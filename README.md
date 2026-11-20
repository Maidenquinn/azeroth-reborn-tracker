# Azeroth Survivors: Reborn — Community Tracker

Community bug reports and suggestions, organized for the Azeroth Survivors: Reborn moderation/development team.

> **Unofficial community-maintained tracker.** Not an official game roadmap; developers decide what is accepted, scheduled, implemented, or rejected.

## Quick links

- [All issues](../../issues) · [New bug](../../issues/new?template=bug_report.yml) · [New suggestion](../../issues/new?template=feature_request.yml)
- [Project board setup](docs/PROJECT_SETUP.md) · [Discord ingestion](docs/DISCORD_IMPORT.md)
- [Discord bug reports](https://discord.com/channels/1567264381929259189/1571654342023581696)
- [Discord suggestions](https://discord.com/channels/1567264381929259189/1569325066553000006)

## Workflow

| Status | Meaning |
| --- | --- |
| Needs Review | Community report collected; not yet verified or accepted |
| To Do | Staff approved for tracking |
| In Progress | A developer explicitly confirmed work has begun |
| Testing | Fix/change awaiting verification |
| Done | Fix/change verified or explicitly completed |

Track **type** (bug / suggestion), **priority** (critical / high / medium / low), and **decision** (proposed / accepted / needs discussion / rejected / duplicate) separately. A high volume of comments does not prove a report is a bug, and no AI triage is allowed to claim developer decisions.

## Privacy and evidence

This repository is **public**. Do not publish member identities, private-channel messages, private attachments, access tokens, or screenshots without authorization and a review. Link to original Discord reports only when disclosure is allowed; viewers may need Discord permissions. Source links are references, not evidence that the bot has imported the contents.

## Initial seed

The [first issue](../../issues/1) documents SNX's specific example of Cataclysm trinkets appearing in Classic mode. All other bugs/suggestions require verified source material.

## Automation

`tracker/import_discord.py` supports review-first Discord collection. A moderator explicitly reviews draft records before any GitHub Issues are created. See [setup and security notes](docs/DISCORD_IMPORT.md). No bot is running or authorized simply because the code is published.

## Ownership

Maintained initially under Maidenquinn; this tracker may be transferred to the Reborn team with their agreement. This project is not affiliated with or endorsed by the game's developers unless they expressly confirm that.

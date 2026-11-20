# Discord → GitHub: moderated import

This project includes a **local collector and draft generator**. It is not a live, deployed service.

## Prerequisites

- The game/server owner approves a bot being added to the server, and approves which content can be republished to public GitHub.
- A bot with **View Channel**, **Read Message History**, and required forum/thread access to the specified channels. The **Message Content Intent** may need to be enabled in the Discord developer portal and code configuration.
- Python 3.11+ and `pip install -r requirements.txt`.
- `DISCORD_BOT_TOKEN` as an environment variable, **never** committed.
- Only later, for publishing approved drafts: GitHub token with *Issues: write* scoped to this repository, passed as `GITHUB_TOKEN`.

## Local commands

```bash
python -m pip install -r requirements.txt
python tracker/import_discord.py collect --output drafts.json
python tracker/import_discord.py preview --input drafts.json
```

By default, collection is **read-only**, stores draft reports locally and **does not publish to GitHub**. Store `drafts.json` privately, never commit it. The collector captures IDs, channel/thread source URLs, timestamps, author IDs, text, image attachment links, and thread titles. Attachment links are not guaranteed to remain accessible.

The moderator must review each draft, remove personal/private material, enrich reproduction/expected behavior, and decide what can safely be published. Import into public Issues can be implemented after this review workflow and permissions have been agreed with SNX. Do not use user account tokens or self-bots.

## Source identifiers

- Guild: `1567264381929259189`
- Bug channel: `1571654342023581696`
- Suggestions forum: `1569325066553000006`

## Not yet implemented

- Automatic semantic deduplication/classification.
- Image backup/upload to GitHub; only attachment URLs are referenced in *private local drafts*.
- Live incremental monitoring, scheduled runs, or GitHub Project field updates.
- OAuth / bot invite and hosting.

No GitHub Issue is to be automatically created from Discord content before review.

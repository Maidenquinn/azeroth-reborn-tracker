"""Read-only Discord historical collector: do not publish Discord content without approval."""
from __future__ import annotations
import argparse
import asyncio
import json
import os
from pathlib import Path
from datetime import datetime, timezone

import discord

GUILD_ID = 1567264381929259189
BUG_CHANNEL_ID = 1571654342023581696
SUGGESTIONS_FORUM_ID = 1569325066553000006


def record(message: discord.Message, kind: str, thread_name: str | None = None) -> dict:
    return {
        "source_id": str(message.id),
        "kind": kind,
        "thread_name": thread_name,
        "source_url": message.jump_url,
        "channel_id": str(message.channel.id),
        "author_id": str(message.author.id),
        "timestamp": message.created_at.isoformat(),
        "content": message.content,
        "attachments": [
            {"filename": a.filename, "url": a.url, "content_type": a.content_type}
            for a in message.attachments
        ],
    }


async def collect(output: Path) -> None:
    token = os.getenv("DISCORD_BOT_TOKEN")
    if not token:
        raise SystemExit("DISCORD_BOT_TOKEN environment variable is required")
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    reports: list[dict] = []

    @client.event
    async def on_ready() -> None:
        try:
            channel = client.get_channel(BUG_CHANNEL_ID) or await client.fetch_channel(BUG_CHANNEL_ID)
            if not hasattr(channel, "history"):
                raise RuntimeError("Bug channel does not support message history")
            async for msg in channel.history(limit=None, oldest_first=True):
                reports.append(record(msg, "bug"))
            forum = client.get_channel(SUGGESTIONS_FORUM_ID) or await client.fetch_channel(SUGGESTIONS_FORUM_ID)
            if not isinstance(forum, discord.ForumChannel):
                raise RuntimeError("Suggestions channel is not a forum")
            threads = {t.id: t for t in forum.threads}
            async for thread in forum.archived_threads(limit=None):
                threads[thread.id] = thread
            for thread in threads.values():
                async for msg in thread.history(limit=None, oldest_first=True):
                    reports.append(record(msg, "suggestion", thread.name))
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(json.dumps({
                "collected_at": datetime.now(timezone.utc).isoformat(),
                "source_guild": str(GUILD_ID),
                "records": reports,
            }, ensure_ascii=False, indent=2), encoding="utf-8")
            print(f"Stored {len(reports)} draft messages at {output} (local only)")
        finally:
            await client.close()

    await client.start(token)


def preview(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    rows = data.get("records", [])
    for kind in ("bug", "suggestion"):
        filtered = [r for r in rows if r.get("kind") == kind]
        print(f"{kind}: {len(filtered)} messages")
        print(f"  attachments: {sum(len(r.get('attachments', [])) for r in filtered)}")
    print("Preview only. No GitHub content was published.")


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    c = sub.add_parser("collect", help="Fetch accessible historical messages into private local drafts")
    c.add_argument("--output", type=Path, default=Path("drafts.json"))
    v = sub.add_parser("preview", help="Show counts in a local draft file")
    v.add_argument("--input", type=Path, default=Path("drafts.json"))
    args = p.parse_args()
    if args.command == "collect":
        asyncio.run(collect(args.output))
    else:
        preview(args.input)


if __name__ == "__main__":
    main()

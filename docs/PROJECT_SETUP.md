# GitHub Project board configuration

The GitHub connector used to publish this repository does **not** expose creation of GitHub Projects or custom labels. These need a repository owner/maintainer with GitHub Projects permissions.

Suggested project: **Reborn Community Tracker**, using the **Board** layout with a custom single-select **Status** field:

1. Needs Review
2. To Do
3. In Progress
4. Testing
5. Done

Add custom single-select fields **Priority** (Critical, High, Medium, Low) and **Decision** (Proposed, Needs Discussion, Accepted, Rejected, Duplicate). Suggested separate views: All, Bugs, Suggestions, Critical, Recently Updated.

Suggested labels:

- `type: bug`, `type: suggestion`
- `status: needs-review`, `status: to-do`, `status: in-progress`, `status: testing`, `status: done`
- `priority: critical`, `priority: high`, `priority: medium`, `priority: low`
- `decision: needs-discussion`, `decision: accepted`, `decision: rejected`, `decision: duplicate`
- `area: gameplay`, `area: balance`, `area: items`, `area: ui-ux`, `area: performance`

Avoid marking bugs as **Done** purely because a GitHub issue was closed. Require an explicit verification or staff decision.

When the project is created, enable automatic addition of Issues from this repo and sync the `Status` field to the board. Public GitHub Projects may expose issue descriptions or metadata: follow the publication policy below.

## Publication policy

The source Discord community channels are not implicitly public-domain. Obtain SNX/server administrator permission before reading the full history through a bot and get permission before *republishing* screenshots, player identities, and message content to this public repository. Paraphrase and remove personal information; store restricted evidence outside the public repo.

## Current state

- Repository and issue templates: included.
- Example issue from SNX: tracked.
- GitHub Project itself: **not yet created**.
- Discord automatic sync: **not deployed**.

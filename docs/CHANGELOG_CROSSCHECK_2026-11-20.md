# Changelog cross-check — 20 November 2026

## Sources and limits

- [Official Reborn changelog channel](https://discord.com/channels/1567264381929259189/1570187164610732052)
- Browser context included changelog posts for **0.7.0 through 0.7.4**, dated Nov 17–20, 2026.
- **Not a full 10–20 November history audit:** earlier changelog entries and older community messages are not present in the loaded browser context. Changelog claims do not replace in-game verification.

## Directly addressed by release notes

| Issue | Release evidence | Conclusion |
| --- | --- | --- |
| [#15 Racial / passive API](../../issues/15) | 0.7.4: addons can request racial and passive abilities, with name, description and cooldown | **Shipped / issue closed**, subject to API usability feedback |
| [#9 Vashj'ir enemies above water](../../issues/9) | 0.7.3: enemies swim down/up after the player; 0.7.4: underwater spawns and repositioning keep the intended depth | **Probable fix announced; in-game recheck needed** |

## Relevant updates, but *not* proven fixes

| Issue | Related change | Why still open |
| --- | --- | --- |
| [#1 Cata trinkets in Classic](../../issues/1) | 0.7.4 expansion trinket upgrade support | No cross-mode restriction fix stated |
| [#6 Starting spell preview](../../issues/6) | 0.7.4 Hunter starting spell changes for Demolitionist / Great Hunt | Not a general preview/build-switch bug fix |
| [#7 Missing Auto Shot icon](../../issues/7) | 0.7.4 damage meter adds pet attack icons | Different UI surface, not Auto Shot spell icon |
| [#8 Hunter pet damage](../../issues/8) | 0.7.4 damage meter pet icon change | Doesn't demonstrate bonus scaling works |
| [#10 Slow updater and Deepholm loading](../../issues/10) | 0.7.1 launcher fallback/progress, 0.7.4 parallel update mirror checks | Specific reported slow download and 9-minute loading not verified |
| [#12 6 yd melee range](../../issues/12) | 0.7.4 Monk Backswing expands Leg Sweep radius | Not a universal range change; remains balance discussion |

## Other observations

- **AZS_GetLocalTime**: 0.7.4 explicitly announces local time including seconds; a player also acknowledged the fix in the bug channel. Don't open an active bug without evidence of regression.
- **Deep Freeze Echo / Time Fracture**: community exchange attributes lack of Echo to intentional balance constraints; classify as a design discussion, not a confirmed defect.
- **0.7.1 Cataclysm zones not loading in 0.7.0**: changelog explicitly says archive loading was fixed in 0.7.1. This isn't proof that a Nov 20 individual Deepholm slow-load complaint was resolved.
- **0.7.4 Vashj'ir** includes a second update enabling enemies to share the zone's swim speed bonus; still verify any remaining surface-rendering symptoms.

## Review policy

**Fixed in changelog** = developer-announced, not automatically verified live. Direct feature requests fulfilled by a release note can be closed with an explicit version reference, as with #15. Potential regressions or close-but-not-identical fixes should stay open until tested.

Screenshots and exact individual message permalinks have not been comprehensively captured. No private Discord media has been republished.

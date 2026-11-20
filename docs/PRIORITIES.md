# Audit priority tracker — 2026-11-20

Priorities are provisional and describe what to verify first. New community reports require current-build reproduction. Game design and implementation decisions remain with the developers.

| Priority | Issues | Reason |
| --- | --- | --- |
| High | [#22](../../issues/22), [#35](../../issues/35) | Update can fail or leave the prior build running. Long solo runs reportedly become unplayable. Test current builds first. |
| High | [#21](../../issues/21), [#26](../../issues/26), [#20](../../issues/20) | Potentially blocks leaving a co-op run, accessing Endless encounters, or obtaining expected jewelry upgrades. |
| High | [#1](../../issues/1), [#5](../../issues/5), [#8](../../issues/8), [#10](../../issues/10), [#12](../../issues/12) | Existing mode, skill, set, loading and melee reports. Some changelog entries address adjacent behavior, so use the individual verification criteria. |
| Medium | [#6](../../issues/6), [#7](../../issues/7), [#11](../../issues/11), [#19](../../issues/19), [#24](../../issues/24), [#25](../../issues/25), [#28](../../issues/28), [#29](../../issues/29), [#30](../../issues/30), [#32](../../issues/32), [#36](../../issues/36), [#37](../../issues/37), [#38](../../issues/38), [#43](../../issues/43) | Specific reports for targeted testing. #11 identifies Deathbringer’s Will from the attached card. #25 needs separate spell-card and jewelry-card cases. |
| Medium | [#13](../../issues/13), [#14](../../issues/14), [#18](../../issues/18), [#33](../../issues/33), [#34](../../issues/34), [#39](../../issues/39), [#40](../../issues/40), [#41](../../issues/41), [#44](../../issues/44) | Accessibility, interface, API, class or balance proposals for discussion. |
| Low | [#16](../../issues/16), [#17](../../issues/17), [#27](../../issues/27), [#31](../../issues/31), [#42](../../issues/42) | Cosmetics, optional progression or localized presentation. #17 requires survivability analysis before replacing a talent. |
| Published, retest requested | [#9](../../issues/9) | Version 0.7.4 specifically addresses Vashj’ir depth on spawn and reposition. Retest reported behavior on the current build. |
| Published, closed | [#15](../../issues/15), [#23](../../issues/23) | Version 0.7.4 documents addon access to racial/passive information and the Netherwind Blizzard visual correction. |

[GitHub Project](https://github.com/users/Maidenquinn/projects/1/views/1) — verified #5, #6 and #7 in **Needs Review**, and #15 and #23 in **Done**. Remaining cards auto-added to the board may still show the default **Todo** status. In particular, #9 is a candidate for **Testing** and the open High-priority reports above are candidates for **Needs Review**. The card-status view failed during further updates. The [audit log](AUDIT_LOG.md) records the remaining source coverage.

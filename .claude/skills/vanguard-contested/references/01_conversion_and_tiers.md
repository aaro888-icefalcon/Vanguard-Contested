# 01 · TIERS & CONVERSION SPEC
*The contract between the simulation and the game. Every game-facing number traces back to a sim output through this file.*

## The power ladder (12 rungs, colloquial)

Mode bumped: the empowered median is **3× baseline**, reach ~2,000×. One in five humans is empowered; **~41% of them are sub-Spark** (a knack, no more), and only **~3.6% of all humanity** is individually decisive (Breaker and up).

| Rung | Base tier | × baseline | Population | What it means on the ground |
|---|---|---|---|---|
| **Flicker** | Trivial | 1–1.4 | 537M | barely touched; a parlor trick |
| **Spark** | Trivial | 1.4–2 | 124M | a small, real gift |
| **Plus** | Minor | 2–3.2 | 172M | a notch above human; a useful edge |
| **Ringer** | Minor | 3.2–5 | 162M | clearly enhanced; wins any human contest |
| **Bruiser** | Street | 5–8.7 | 184M | wins real fights, kills feral monsters |
| **Heavy** | Street | 8.7–15 | 150M | a serious local threat *(85th-pct reference)* |
| **Breaker** | City | 15–27 | 120M | breaks armor and walls; a one-person problem |
| **Siege** | City | 27–50 | 82M | a walking siege engine |
| **Warlord** | Elite | 50–100 | 51M | breaks military formations |
| **Titan** | Elite | 100–200 | 23M | a regional power |
| **Crown** | Apex | 200–600 | 11M | a living legend |
| **Horror** | Apex | 600–2,000+ | 2M | the human ceiling; a walking catastrophe |

Power *type* matters as much as rung — a Heavy perception-power and a Heavy striker live different lives. After the EMP, biological and self-powers (durability, regeneration, senses, the kinetic suites) are more reliable than anything tech-dependent.

## Sim → game translation table

| Sim quantity | Game term | Mapping |
|---|---|---|
| Power × (rung) | Build budget / PL | **System: M&M 3e** (see `SKILL.md`). Flicker–Spark ≈ PL2–4, Bruiser–Heavy ≈ PL6–8, Breaker–Siege ≈ PL9–11, Warlord–Titan ≈ PL12–14, Crown–Horror ≈ PL15+. **PCs start PL 8 or 9 = Heavy–Breaker.** Warlord+ NPCs operate *above PL caps* as boss/unwinnable threats. |
| Patch status | Region danger band | Redoubt → **Guarded**, Contested → **Embattled**, Overrun → **Hostile-Held / No-Man's-Land** |
| Patch casualty rate | Region lethality number | the sim %; sets baseline encounter deadliness |
| Crosser capability share | Faction **Tier** (1–6) + **Hold** | Empire = Tier 6 Strong; major blocs Tier 4–5; tribal/discordant Tier 2–3 Weak |
| Alignment value | Relationship **track** | −3 war · −2 hostile · −1 friction · 0 neutral · +1 cooperative · +2 allied · +3 sworn |
| Front motion / event | Project **clock** | segment count from the sim's pace (see clocks file) |
| Import-dependence × trade-severance | Resource **scarcity** rating | drives downtime supply, foraging DCs |
| Coherence | Local **law/order** rating | governs whether the empowered are conscripted, free, or warlords |

**Coupling rule:** if the sim is re-run (different sub-profile, EMP recalibration), only the numbers in this table change — the prose canon stays valid. Keep this file as the single conversion point.

## Default PC framing
PCs start **PL 8–9 (Heavy–Breaker)** as ordinary New Yorkers who **manifest at the Pulse on Day Zero**, and play through one in-world year — the corridor's fall, the evacuation west, the redoubt forming (see `SKILL.md` and file 07). A Breaker can dominate a street fight and kill feral monsters, but Warlord+ crossers, monster-lords, and the Empire's champions operate above PL and will end them — which is the deadliness the world is tuned for.

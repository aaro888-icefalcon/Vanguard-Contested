# 15 · POWERED-WORLD GENERATION FRAMEWORK
*A scale-aware toolkit for populating a vast, dense, powered world on the fly — built on top of files 08 (the oracle) and 09 (the generators), and keyed to file 01's ladder. Where 08 answers moment-to-moment questions and 09 builds the world's pieces, **this file answers "who is this person, how strong are they, and how do their powers enter the scene"** — fast, honestly weighted, and without drowning the GM when a lot is going on. Roll with code; honor the lethality lean.*

> **The problem this solves.** One in five people is empowered; a metro holds millions; the corridor is a churn of factions, refugees, war-bands, and free agents. You cannot stat that. This file is the discipline for generating only what the PC can touch, at the right tier, with the right cost — and abstracting the rest into clocks and Tiers so the world feels enormous and alive while you track almost nothing.

---

## 1 · THE DENSITY MODEL — what "1 in 5" actually means on the street
From file 01: 1 in 5 humans manifested; **~41% of the empowered are sub-Spark** (a knack, no more); only **~3.6% of all humanity is Breaker+** (individually decisive). Derived from the ladder's populations (1,618M empowered), the honest distribution of a **truly random manifested person** is:

**RANDOM EMPOWERED TIER (d100) — weighted to canon population**
| d100 | Rung | Band | Feel on the ground |
|---|---|---|---|
| 01–33 | **Flicker** | Trivial | a parlor trick; barely touched |
| 34–41 | **Spark** | Trivial | a small real gift |
| 42–52 | **Plus** | Minor | a useful edge |
| 53–62 | **Ringer** | Minor | wins any human contest |
| 63–74 | **Bruiser** | Street | wins real fights; kills feral |
| 75–83 | **Heavy** | Street | a serious local threat |
| 84–91 | **Breaker** | City | a one-person problem (PC band) |
| 92–96 | **Siege** | City | a walking siege engine (above PC) |
| 97–99 | **Warlord** | Elite | breaks formations (flee) |
| 00 | **Titan+** | Elite–Apex | roll 1–6 Titan · 7–9 Crown · 10 Horror |

**Reading the rarity:** ~38% of the manifested are Bruiser+ (a real fight), but only **~18% are Breaker+** and **~10% are above the PC band (Siege+)**. In raw numbers a **Breaker is roughly 1 in 70 people**, a **Heavy about 1 in 36**, a **Bruiser about 1 in 30** — so on a single dense block expect a handful who win fights, a Heavy as a block-scale event, and a Breaker as a neighborhood event. Warlord+ is a regional event; you should know they exist before you meet them.

**Bias the roll to context — don't use it raw for everything:**
- *The street / a refugee column / a child:* skew **down** (most are Flicker–Ringer). Roll, then cap at Heavy unless something says otherwise.
- *A warlord's retinue / a faction's muscle / a "named" foe:* skew **up** (Bruiser minimum; the lieutenant is Heavy, the boss is Breaker+).
- *Region band gate (file 05):* Guarded encounters cap lower; No-Man's-Land is where Warlord+ legitimately appears. Tune to the band, not the PC's confidence.

---

## 2 · THE ABSTRACTION LADDER — stat only what the PC can touch
Run the world at five zoom levels and **only ever stat the bottom one**:

1. **World** → six clocks (file 04). Rumor only.
2. **Region** → a danger band + lethality number (file 03/10). A weather system, not a cast.
3. **Settlement** → a faction Tier + 1–2 assets + one leader (file 13). Not a headcount.
4. **Site** → a keyed location: band, what it is, what's wrong (file 10/08). 3–5 fixtures.
5. **Scene** → the handful of people present **now**. *This* is where you generate NPCs and supers.

**Crowds and mobs are environment, not individuals.** A panicked crowd, a refugee mass, a faction's foot-soldiers = a **single hazard** with a rating, or a **minion-wave** (file 11): one forced save per round at a DC set by the lethality number, failure = injury + a cost, and it keeps coming until the PC breaks contact or finds a choke. Never roll forty people.

**A faction's strength is its Tier, not its roster.** When the Indenture (file 14) "sends muscle," that's a Tier-3 pressure expressed as 1 statted leader + a wave — not a spreadsheet.

**Spotlight discipline (the rule that keeps "a lot going on" runnable):** **one fully-statted powered foe per scene.** Everyone else is a wave, a Tier, a clock, or an unstatted face. If two Breakers must share a scene, one is the threat and the other is terrain (busy elsewhere, held off, arriving as a clock). This is how the world stays vast while your tracking stays small.

---

## 3 · NPC QUICK-BUILD — a person in one pass
For anyone the PC talks to. Roll or pick; emit one line.

1. **Tier** — §1 table (biased to context). Most are sub-Bruiser and need no stat block.
2. **Role** — file 08 NPC generator (d20).
3. **Want** — file 08 (d12).
4. **Lever** — what moves them (file 08 attitude d8 + hidden-truth d12 give it).
5. **Tell** — one concrete sensory detail that makes them a person (a limp, a dead man's coat, a child's drawing kept folded).

**Emit format:** *Name — [role], [tier]. Wants [X]; moved by [lever]; [tell].* Attach a **file 11 frame only if they may fight.** Add anyone who could recur to the Character List in `vanguard-state.md`.

*Example:* *Pruett — scavenger, Ringer. Wants out before the Tide; moved by a debt to a dead partner; wears the partner's oversized boots, stuffed with rag.* (No stat block until a knife comes out; then: Ringer, unpowered, Equipment: blade.)

---

## 4 · THE SUPERS GENERATOR — a powered NPC with a stat block
When the scene needs a manifested person who matters mechanically. Five rolls, then emit a file 11 frame.

1. **Rung** — §1 table (biased), or set by role. → fixes the PL via file 01 (Bruiser PL6 · Heavy PL8 · Breaker PL9 · Siege+ above-PL boss).
2. **Power** — file 08 power table (d20). Slot its rank at the rung (≈ rung's effect cap).
3. **Intent** — file 08 free-agent intent (d10): protect own · build a fief · prey · hide it · sell it · join a faction · revenge · zealotry · can't control it · quietly decent.
4. **Control** *(d6 — how the power sits in them):* 1–2 **mastered** (reliable, no tell) · 3–4 **costly** (a tell/Exposure every significant use) · 5 **barely held** (fires under stress) · 6 **unreliable** (fails or overfires — a complication and a Hero-Point engine).
5. **Defining complication** *(d10 — the standing trigger, rolled every relevant scene, per SKILL.md):*
   1 **a tell** (signature signature — frost, heat, sound, light — alters the scene, draws trackers)
   2 **a hunger/addiction** the power feeds (pulls them toward overuse / the strongest threat)
   3 **a cost in the body** (each use injures, drains, ages, or sickens them)
   4 **a tech-leash** (power routed through a device at the dark grid's mercy — file 06)
   5 **a dependent** the power can't protect (a person who is leverage and weakness)
   6 **a mark** (a faction/threat hunts the power or its bearer)
   7 **a limit they hide** (a hard ceiling/blind spot they bluff past — exposed at the worst time)
   8 **a collateral problem** (the power hurts bystanders/structures; an Exposure engine)
   9 **a reputation** (people know what they are and react — fear, recruitment, purge)
   10 **a fracture** (the power and the person are at odds — it changes them, or wants something)

**Emit:** the matching file 11 frame at the rung, the signature power at rank, intent as motivation, the complication as a **recurring die** (not flavor) — it fires every relevant scene and is where the NPC's own Hero Points and surprises come from.

### Worked supers *(engine-rolled in the foundation pass — file 08 power + intent)*
1. **The Spotter** — *senses/perception · intent: sell their power.* Heavy (PL 8) recon-for-hire; can't be flanked, sees the ambush — sells the read to the highest bidder. *Complication: a reputation; every faction wants the eyes.*
2. **The Unkillable** — *regeneration · intent: flee/hide it.* Bruiser (PL 6) who knits visibly and **hides it** because it makes them a prize or a heretic. *Complication: a mark — someone wants to find out what they are.*
3. **The Quiet Forager** — *stealth/invisibility · intent: quietly decent.* Plus/Ringer; unseen, just surviving, feeds a block. *No block until cornered; Equipment + Hide.*
4. **The Stress-Hand** — *telekinesis · intent: can't fully control it.* Heavy (PL 8) whose **power fires when frightened or cornered** — Move Object 8 + a panic burst. *Complication (control 5, barely held): the worst moment is when it goes off on its own.* A walking liability and a tragedy.
5. **The Hidden Mercy** — *healing (others) · intent: flee/hide it.* Heavy; a secret healer like Doc (file 12), **hunted for the gift** by everyone who needs it. *Complication: a dependent + a mark.*
6. **The Iron Convert** — *durability/armor · intent: zealotry/cult.* Heavy (PL 8) enforcer for **the Quiet Child** (file 14); near-unhurt by PC-band hits, fanatical, won't break. *Complication: zeal — can't compromise or adapt.*
7. **The Breaker-Hands** — *enhanced strength · intent: can't control it.* Bruiser (PL 6) who **shatters what he holds** — useful and dangerous to everyone near him, including his own people. *Complication: collateral.*
8. **The Live Wire** — *electrical · intent: protect their own.* Bruiser (PL 6) guarding his block — **cruel post-EMP irony**: his gift is half-wasted in a dead-grid world, lethal only up close, and he knows it. *Complication: a tech-leash inverted — the world that would have made him a king is gone.*

---

## 5 · INTRODUCING POWERED INTERACTIONS — the guidelines
The hard part isn't generating powers; it's **bringing them into a scene honestly**, at scale, without softening or chaos.

**Tier-gate, and give the read.** Per file 01/05, never drop Warlord+ on the PC unless death is the intended stake — and when something above the PC's band is present, **telegraph it** (the way it moves, what it did to the last people, a power-sense read) so **flight is a real, informed choice**. A character who stands and fights what they should have fled dies, and that is correct — but they must have been able to *know*.

**Most powered interactions are not fights.** A Heavy is a person with a job — a foreman, an enforcer, a healer, a smuggler. Stat the interaction as a **social contest** (Persuasion, Intimidation, Deception, Insight) as readily as a combat. Power is leverage, labor, fear, and recruitment far more often than it is a brawl. Ask what the powered NPC *wants* before you ask what they can *do*.

**Every significant power use has a tell, and display has a cost.** Post-EMP, biological/self-powers are reliable and tech-powers are at the dark grid's mercy (file 06). When a power fires loud, run the NPC's **complication die** and feed the **Exposure clock** (SKILL.md): witnesses are a clock toward a hunter. This is what makes the world *react* to powers without you tracking the city — power is never free and never unseen.

**Escalation ladder — let the PC choose where to enter, the enemy escalates to win:**
parley → posture/threat → first blow (non-lethal) → lethal. NPCs act to win (SKILL.md): a smart powered foe opens where it's strongest, focuses the wounded, uses cover and numbers, lies, and denies fair rematches. Don't walk a clever enemy down the ladder for the PC's benefit.

**NPC complications fire as dice too.** The standing-trigger rule isn't just for the PC. A recurring powered NPC's complication (the Stress-Hand's misfire, the Live Wire's dead-grid limit, the Iron Convert's zeal) **fires on its relevant scene** — which is where the GM's surprises and the NPC's Hero-Point-equivalent reversals come from.

**Running "a lot going on" without drowning:** show **2–3 perceivable clocks** at a time, the rest as rumor (file 08 · word from the road). Spotlight **one statted power per scene**; render the rest as waves, Tiers, and tells. When the world should feel chaotic, **raise Tension** (file 08) and let the scene-setup interrupt hijack the plan — that *is* the feeling of a dense, powered, collapsing world, and it costs you no extra bookkeeping.

---

## 6 · QUICK LOOP (this file)
Need a person? → §3 quick-build (tier biased to context). → Do their powers matter mechanically? → §4 supers generator (rung → power → intent → control → complication) → emit a file 11 frame. → Bringing powers into the scene? → §5: gate the tier and give the read, decide social vs combat, run the tell + Exposure, escalate to win, fire the complication die. → Keep one statted power in the spotlight; everything else is a clock, a Tier, or a wave. → Record anyone who recurs to `vanguard-state.md`.

---

*Provenance: the random-tier d100 is derived from file 01's ladder populations (1,618M empowered; Bruiser+ ≈38.5%, Breaker+ ≈17.9%, Siege+ ≈10.4%); generators build on files 08/09; frames and caps from file 11; the worked supers were rolled (power + intent) in the foundation pass. This file extends the engine — it does not replace the oracle (08) or the sandbox generators (09).*

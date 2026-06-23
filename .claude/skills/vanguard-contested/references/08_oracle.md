# 08 · THE ORACLE
*An expansive GM-emulator oracle for solo and AI-GM play, built on the Mythic GME framework (tension factor, odds-based yes/no, doubles-triggered events, word-pair meaning tables) with all content native to Vanguard Contested. Original content; pairs with Mythic GME 2e — if you own it, use its Fate Chart/Chaos Factor and treat everything below as setting-specific tables that plug in. Roll everything with code; honor the lethality mandate (weight interpretation toward danger).*

> **In this workspace:** the `mythic-gm` engine owns the yes/no Fate Question, the Scene Test, and the
> Random-Event trigger. The setting tables below (Event Focus, the Meaning tables, and every setting
> oracle) are mirrored as **verified JSON in `bridge/generators/`** and rolled with
> `dice.py table bridge/generators/<name>.json` (routing in `bridge/generators/registry.md`). This file
> remains the human-readable canon and design notes for those tables.

---

## HOW IT WORKS

**Tension (1–9, start at 5)** — the world's hostility and momentum (Mythic's Chaos Factor by another name). It rises when the world is winning — when the PC loses control, a clock advances, a scene spirals — and falls when the PC asserts control and stabilizes a situation. High Tension means more random events and danger reads more likely. *(Using Mythic GME? Use its Chaos Factor directly.)*

**Asking a yes/no.** Frame the question, rate the odds, roll **d100** under the threshold for *yes*.

| Odds | Yes on d100 ≤ (at Tension 5) |
|---|---|
| Certain | 90 |
| Very likely | 75 |
| Likely | 65 |
| 50 / 50 | 50 |
| Unlikely | 35 |
| Very unlikely | 25 |
| Nearly impossible | 10 |

**Tension modifier:** for each point of Tension above 5, **+5** to the threshold (yes more likely); for each point below 5, **−5**. Clamp to 2–99.

**Exceptional results.** If the roll shows **doubles** (11, 22, … 99, 00), the answer is *exceptional* — a yes becomes an emphatic yes with a bonus, a no becomes a hard no with a cost. Read it strongly, and toward danger.

**Random event trigger.** On any **doubles** where the matched digit **≤ Tension** (e.g., 33 at Tension 5 → 3 ≤ 5, fires; 88 → 8 > 5, doesn't), a **Random Event** also occurs alongside the yes/no. Resolve it (below), then continue.

**When else to check for a random event.** At the start of a scene that may have drifted (ask: does the scene begin as expected? — odds by Tension), and any time play stalls and you need the world to move.

---

## RANDOM EVENTS

When an event fires: roll **Event Focus (d100)**, then roll one **Action** word and one **Aspect** word (d100 each) and interpret the pair through the focus, in context, toward consequence.

### Event Focus (d100)
| Roll | Focus | Read it as |
|---|---|---|
| 01–06 | **The war moves** | a front shifts, a clock ticks, territory changes hands |
| 07–13 | **A faction advances** | a present faction pushes its agenda a step |
| 14–18 | **A faction turns on another** | two powers collide; pick or roll which |
| 19–22 | **A new power emerges** | generate a faction (file 04) — a vacuum just filled |
| 23–29 | **Threat closes in** | a hostile force, hunt, or ambush arrives (encounter table) |
| 30–35 | **Monster surge** | feral or sapient; the swarm presses (monster tables) |
| 36–41 | **Crosser contact** | a bloc element appears or makes contact (crosser tables) |
| 42–46 | **The empowered** | a new power manifests, or a free agent acts (empowered tables) |
| 47–53 | **Scarcity bites** | something runs out, breaks, or is taken (scarcity table) |
| 54–60 | **An ally / NPC acts** | a known figure moves toward their goal |
| 61–65 | **An NPC's truth surfaces** | a secret, lie, or real loyalty is exposed |
| 66–69 | **A thread advances** | an open thread lurches forward |
| 70–73 | **A thread is blocked** | an open thread reverses, stalls, or is closed against you |
| 74–79 | **Refugees / civilians** | the human tide — need, panic, opportunity, witness |
| 80–84 | **The dark world** | environment/hazard — grid, weather, structure, terrain fails |
| 85–88 | **Authority acts** | police, Guard, redoubt, or local power asserts itself |
| 89–92 | **Word arrives** | rumor, news, a message, a runner (rumor table) |
| 93–96 | **A turn against you** | betrayal, defection, a price comes due |
| 97–99 | **The PC's world** | something tied to the PC's people, past, or ties intrudes |
| 00 | **The horizon** | a glimpse of the Unmaking, the Empire, or the deep future |

---

## MEANING TABLE — ACTIONS (d100)
| | | | |
|---|---|---|---|
|01 Abandon|26 Decay|51 Hunt|76 Reclaim|
|02 Ambush|27 Deceive|52 Imprison|77 Recruit|
|03 Arm|28 Defend|53 Infect|78 Refuse|
|04 Bargain|29 Delay|54 Inform|79 Release|
|05 Betray|30 Demand|55 Inherit|80 Repair|
|06 Bleed|31 Deny|56 Intercept|81 Resist|
|07 Block|32 Destroy|57 Invade|82 Retreat|
|08 Break|33 Divide|58 Isolate|83 Reveal|
|09 Burn|34 Dominate|59 Judge|84 Sabotage|
|10 Capture|35 Drain|60 Lead|85 Sacrifice|
|11 Carry|36 Drive|61 Leave|86 Salvage|
|12 Collapse|37 Endure|62 Loot|87 Scatter|
|13 Conceal|38 Escalate|63 Lose|88 Seize|
|14 Confront|39 Escape|64 Manifest|89 Shelter|
|15 Connect|40 Exhaust|65 Mourn|90 Starve|
|16 Consume|41 Expose|66 Negotiate|91 Submit|
|17 Control|42 Fail|67 Obstruct|92 Surrender|
|18 Corrupt|43 Fall|68 Offer|93 Survive|
|19 Crack|44 Fight|69 Oppress|94 Threaten|
|20 Crush|45 Flee|70 Overrun|95 Transform|
|21 Dare|46 Fortify|71 Persuade|96 Trap|
|22 Deal|47 Gather|72 Plead|97 Turn|
|23 Decide|48 Govern|73 Plunder|98 Unmake|
|24 Defect|49 Guard|74 Pursue|99 Warn|
|25 Deceive|50 Hoard|75 Push|00 Witness|

## MEANING TABLE — ASPECTS (d100)
| | | | |
|---|---|---|---|
|01 Alliance|26 Duty|51 Iron|76 Ruin|
|02 Ambition|27 Echo|52 Law|77 Sacrifice|
|03 Armor|28 Edge|53 Leader|78 Salvage|
|04 Ash|29 Empire|54 Legacy|79 Scar|
|05 Authority|30 Enemy|55 Light|80 Secret|
|06 Barrier|31 Exile|56 Line|81 Shadow|
|07 Blood|32 Faith|57 Machine|82 Shelter|
|08 Border|33 Family|58 Medicine|83 Siege|
|09 Burden|34 Famine|59 Mercy|84 Signal|
|10 Cargo|35 Fear|60 Message|85 Silence|
|11 Catastrophe|36 Fire|61 Mob|86 Strength|
|12 Child|37 Flesh|62 Monster|87 Stranger|
|13 Choice|38 Fortress|63 Need|88 Supply|
|14 Cold|39 Fuel|64 Network|89 Territory|
|15 Command|40 Future|65 Order|90 Threshold|
|16 Corridor|41 Ghost|66 Outsider|91 Tide|
|17 Corruption|42 Grid|67 Pact|92 Trust|
|18 Crew|43 Grief|68 Power|93 Tyrant|
|19 Crossing|44 Harbor|69 Predator|94 Vengeance|
|20 Crowd|45 Haven|70 Promise|95 Vow|
|21 Dark|46 History|71 Refuge|96 Wall|
|22 Death|47 Home|72 Refugee|97 Water|
|23 Debt|48 Hope|73 Remnant|98 Weapon|
|24 Despair|49 Hunger|74 Rift|99 Wound|
|25 Dread|50 Injury|75 Rival|00 Wreckage|

> *Interpretation example:* Focus **A faction turns on another** + Action **Seize** + Aspect **Fuel** → a faction makes a move to take a rival's fuel depot. Roll which factions (file 04), set a clock, decide whether it touches the PC.

---

## SETTING ORACLES

### Faction Move (d20) — what a faction does on its clock
1 Consolidate territory · 2 Raid a rival · 3 Seize a resource (roll: fuel/food/meds/arms/water) · 4 Recruit (the empowered / refugees / a rival's people) · 5 Fortify · 6 Negotiate or ally · 7 Betray an ally · 8 Demand tribute · 9 Purge internal dissent · 10 Expand a clock toward completion · 11 Hunt a specific person · 12 Spread propaganda/rumor · 13 Open a supply line · 14 Cut a rival's supply · 15 Take hostages · 16 Retreat and regroup · 17 Splinter (generate a new faction) · 18 Make an example (public violence) · 19 Probe the PC's position · 20 A bold stroke — a clock jumps two segments.

### What Shows Up (encounter, by danger band)
**Guarded (d12):** 1 refugees in need · 2 a patrol/militia checkpoint · 3 a scavenger crew · 4 a lone Flicker/Spark in trouble · 5 a faction recruiter · 6 a minor feral intrusion · 7 a supply dispute · 8 an informant with news · 9 a Compact envoy/ally · 10 a sick or injured stranger · 11 a thief · 12 a quiet moment (gift it, then complicate).
**Embattled (d12):** 1 a Reaver/raider probe · 2 a feral pack · 3 a rival empowered (Bruiser–Heavy) · 4 a desperate mob · 5 a collapsing structure/hazard · 6 a checkpoint shakedown · 7 wounded who'll die without help · 8 a sniper/ambusher · 9 a faction war-band passing through · 10 a black-market deal gone wrong · 11 a fleeing column under attack · 12 a crosser scouting element.
**No-Man's-Land (d12):** 1 an ambush · 2 a Warlord-tier threat (flee) · 3 a sapient monster-lord's territory · 4 an Empire/Reaver cohort · 5 a marine feral surge · 6 a corpse-field and what made it · 7 a predatory enclave · 8 a trap/minefield/baited site · 9 a hunted survivor begging help · 10 a rival after the same salvage · 11 a feral horde on the move · 12 something worse than expected (roll twice, combine).

### Crosser Contact
**Bloc element (d12):** 1 Empire vanguard · 2 Reaver war-band · 3 Warrior-Kingdom outriders · 4 Corsair raiders · 5 a Pacific House (split loyalty) · 6 Atlantic Concord observers · 7 Interior Compact envoys · 8 a loyal-anchor patrol · 9 a discordant-bloc fragment · 10 refugees from a bloc · 11 a defector/exile · 12 an unknown rift-arrival.
**Disposition (d10):** 1–2 hostile · 3–4 wary/testing · 5–6 transactional · 7 desperate · 8 curious · 9 friendly minority · 10 actively seeking alliance.
**What they want (d12):** 1 territory · 2 food/water · 3 safe passage · 4 to recruit you · 5 information · 6 a rival dealt with · 7 shelter from the swarm · 8 medicine/aid · 9 to test your strength · 10 to trade · 11 vengeance · 12 to flee something worse (the Unmaking's shadow).

### The Empowered
**Manifested power (d20):** 1 enhanced strength · 2 durability/armor · 3 regeneration · 4 a kinetic/force suite · 5 flight · 6 speed · 7 pyro/thermal · 8 cryo · 9 electrical (cruel post-EMP irony) · 10 telekinesis · 11 senses/perception · 12 stealth/invisibility · 13 emotion/mind influence · 14 healing (others) · 15 matter shaping · 16 summoning/control of feral · 17 toxin/disease · 18 teleport (short) · 19 a body-horror mutation · 20 something unclassified and frightening.
**Free agent's intent (d10):** 1 protect their own · 2 build a fief · 3 prey/extort · 4 flee/hide their nature · 5 sell their power · 6 join a faction · 7 revenge · 8 zealotry/cult · 9 collapse/can't control it · 10 quietly decent, just surviving.

### NPC Generator
**Role (d20):** 1 ex-cop · 2 Guard/soldier · 3 doctor/nurse · 4 mechanic/engineer · 5 criminal/fixer · 6 priest/imam/rabbi · 7 union/worker · 8 refugee parent · 9 child · 10 hoarder/profiteer · 11 militia leader · 12 empowered free agent · 13 crosser · 14 bureaucrat/official · 15 farmer/operator · 16 scavenger · 17 teacher · 18 warlord's lieutenant · 19 healer/herbalist · 20 someone from the PC's old life.
**Wants (d12):** 1 safety for someone · 2 food/meds · 3 power/control · 4 to get west · 5 revenge · 6 information · 7 belonging · 8 to protect a secret · 9 redemption · 10 wealth/leverage · 11 escape · 12 to be left alone.
**Attitude to PC (d8):** 1 hostile · 2 afraid · 3 wary · 4 transactional · 5 curious · 6 needs you · 7 admiring · 8 loyal.
**Hidden truth (d12):** 1 none — honest · 2 lying about who they are · 3 working for a faction · 4 already betrayed you · 5 empowered and hiding it · 6 dying/infected · 7 protecting someone hidden · 8 did something terrible to survive · 9 knows where a resource is · 10 a crosser sympathizer/agent · 11 marked by an enemy · 12 connected to the PC's past.

### Location / Site
**What it is (d20):** 1 hospital · 2 precinct/armory · 3 warehouse/distribution hub · 4 refinery/fuel depot · 5 water plant · 6 power station · 7 subway/tunnel · 8 bridge/crossing · 9 high-rise/tower · 10 church/mosque/synagogue · 11 school/shelter · 12 market/black market · 13 docks/harbor · 14 a holdout enclave · 15 a faction stronghold · 16 a dead corporate campus · 17 a refugee camp · 18 a rift-site · 19 a monster lair · 20 ordinary homes, now a graveyard or a haven.
**What's wrong with it (d20):** 1 occupied by a faction · 2 booby-trapped · 3 feral-infested · 4 flooding/structural collapse · 5 a desperate group inside · 6 contested by two powers · 7 contaminated/diseased · 8 a sapient monster claims it · 9 already stripped · 10 a survivor needs rescue · 11 a corpse-field · 12 fire/no exit · 13 a valuable cache, well-guarded · 14 the dark — no light, no power · 15 freezing/exposure · 16 a rival arrives as you do · 17 a clock is ticking (collapse/raid incoming) · 18 a moral trap (help costs you) · 19 watched/an ambush · 20 nothing wrong — which is itself suspicious.

### Scarcity / Complication (d20)
1 Out of fuel · 2 out of ammunition · 3 out of clean water · 4 out of food · 5 out of medicine · 6 injury worsens/infects · 7 power source dies · 8 vehicle/gear fails · 9 shelter compromised · 10 a resource is stolen · 11 a debt comes due · 12 someone must be left behind · 13 cold/exposure sets in · 14 a witness/heat problem · 15 an ally is wounded · 16 numbers against you · 17 the route is cut · 18 trust breaks · 19 a clock advances against you · 20 two complications at once (roll twice).

### Salvage / What You Find (d20)
1 fuel · 2 ammunition · 3 medicine/first aid · 4 food/water · 5 a working pre-electronic vehicle · 6 a shielded radio/comms · 7 tools/parts · 8 a weapon (roll quality) · 9 winter gear · 10 a map/intel · 11 a generator · 12 currency-that-still-works (fuel, meds, ammo, gold) · 13 a survivor · 14 a body with useful gear · 15 a clue/thread · 16 nothing — picked clean · 17 a trap with the bait · 18 something a faction wants back · 19 a hidden cache (jackpot, but guarded) · 20 something inexplicable (rift-touched/Unmaking-adjacent).

### Word from the Road (rumor, d20)
1 the corridor is falling faster than thought · 2 a redoubt is forming west · 3 a warlord is recruiting the empowered · 4 a safe enclave exists (true? roll) · 5 crossers seen nearby · 6 a monster-lord stirs · 7 a faction seeks a specific person · 8 a supply cache located · 9 a route is now impassable · 10 an ally has fallen · 11 the Concord is watching · 12 a betrayal in a known group · 13 the Guard/redoubt is conscripting · 14 a massacre upriver · 15 a cure/resource for the famine · 16 the Empire's vanguard moves · 17 a holdout needs help · 18 a price on someone's head · 19 the rifts are doing something new · 20 the rumor is bait — a trap.

### Monster Behavior (d12)
1 hunt/stalk · 2 swarm/overwhelm · 3 ambush · 4 territorial display (flee available) · 5 feed (distracted) · 6 migrate through · 7 nest/den nearby · 8 lure prey · 9 flee from something bigger · 10 sapient — it negotiates or toys · 11 wounded/desperate/erratic · 12 something new — it shouldn't do that.

### Twist / Escalation (d20)
1 an ally betrays · 2 the threat was a feint · 3 a worse threat arrives · 4 a clock completes now · 5 reinforcements (theirs) · 6 a hostage/innocent in the line of fire · 7 the ground/structure fails · 8 a hidden power reveals (enemy is higher-tier) · 9 a resource you relied on is gone · 10 a rival faction intervenes · 11 the real objective was elsewhere · 12 a moral cost surfaces · 13 the enemy wants you alive · 14 a face from the past · 15 the swarm arrives, indifferent to both sides · 16 your power falters at the worst moment · 17 a trusted fact was a lie · 18 mercy is offered (with a hook) · 19 the win has a price · 20 raise Tension by 2 and let it spiral.

---

## SCENE SETUP

Begin each scene by stating the **expected scene** — the most likely next situation given where things stand. Then test whether the world lets it happen. Roll **d10**:
- **Greater than Tension** → the scene plays **as expected**.
- **≤ Tension and odd** → **Interrupted.** Set the expected scene aside; a **Random Event** takes over (roll Event Focus + Action + Aspect). The interruption is what actually happens.
- **≤ Tension and even** → **Altered.** The scene happens, but something is wrong — roll Alterations.

The higher the Tension, the more the world hijacks your plans. That is the point.

**Scene Alterations (d12):** 1 someone unexpected is here · 2 someone expected is gone · 3 the place is changed (damaged, occupied, emptied) · 4 it's later/worse than you thought — a clock advanced · 5 a resource you counted on is gone · 6 an enemy got here first · 7 an ally is compromised or turned · 8 the goal has moved · 9 a hazard is present (fire, flood, swarm, cold) · 10 it's a trap · 11 a third party complicates it · 12 the stakes just doubled.

**Opening frame — how the scene hits (d20), to start in the thick of it:** 1 gunfire nearby · 2 a scream · 3 smoke · 4 a crowd surging · 5 sudden silence · 6 someone bleeding out · 7 a stranger in the way · 8 a body · 9 cold cutting through · 10 a child alone · 11 an engine that shouldn't run · 12 a rumor passed mouth to mouth · 13 lights flicker on, then die · 14 a monster's sign · 15 a checkpoint ahead · 16 someone calls your name · 17 a deal offered · 18 the structure groans · 19 a familiar face · 20 the horizon does something wrong.

**After the scene, adjust Tension:** PC ended in control → **−1**; the world dominated, spiraled, or the PC was overwhelmed → **+1** (clamp 1–9). Closing a major thread can also drop it −1.

---

## THREADS & CHARACTERS *(kept in chat — there is no side tracker)*

The `references/` files are read-only canon, so these two lists live in the **live state** —
`campaigns/vanguard/campaign-state.md` (the engine maintains the Threads & Characters Lists there),
shown in the end-of-scene state block and overwritten every scene. They are the campaign's working
memory — carry them forward every session.

- **Thread List** — open goals, mysteries, and dangers, numbered.
- **Character List** — the NPCs in play who might recur, numbered.

**Rolling on a list.** When an Event Focus points to "a thread" or "an NPC," or whenever you want fate to choose which one, roll **d20** against the numbered list:
- A **filled slot** → that thread/character is involved.
- An **empty slot** (a number past the current list) → a **new** one enters; generate it (NPCs via the NPC generator).

This self-weights: a short list mostly spawns new material; a full list mostly revisits the established. (Past 20 entries, roll d100 at ten slots per band, or split into two lists.)

**Upkeep.** Add a thread when a new goal, question, or danger opens; close it when resolved or moot. Add a character when the PC meets someone who could return; retire them when they die or leave for good. Prune so the lists stay live and the d20 keeps biting.

---

## QUICK LOOP
Set the scene (expected) → test d10 vs Tension → **as expected / altered / interrupted** → frame questions → rate odds → roll d100 vs threshold (±Tension) → read yes/no, doubles = exceptional and maybe a Random Event → on event: Focus + Action + Aspect, rolling Thread/Character lists as needed → interpret toward consequence → update the lists and clocks → adjust Tension → next scene. When in doubt, the lethality mandate sets the lean: toward danger, toward cost, toward the world acting on its own terms.

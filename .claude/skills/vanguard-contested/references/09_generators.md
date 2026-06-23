# 09 · SANDBOX GENERATORS
*Prep-time generators in the Godbound sandbox-toolkit style — faction tags, adventure seeds, cults, rift anomalies, relics — with all content native to Vanguard Contested. Original content; pairs with Godbound if you own it. Where file 08 answers moment-to-moment questions in play, this file builds the pieces you drop into the world. Roll with code; honor the lethality mandate.*

> **In this workspace:** the tables here (faction tags, missions, cults, rift sites, relics) are mirrored
> as **verified JSON in `bridge/generators/`** and rolled with `dice.py table bridge/generators/<name>.json`
> (routing in `bridge/generators/registry.md`). This file remains the human-readable canon and design notes.

---

## FACTION TAGS (d20 — take 1–2 per faction)
Each tag gives a faction a defining strength **and** a built-in catch. Bolt onto the faction generator in file 04.

1. **Armed to the Teeth** — seized an armory/cache. Wins fights above its Tier · but it's a prize others come for.
2. **Fuel Barons** — controls a fuel source. Everyone needs them · everyone covets it; raided constantly.
3. **Empowered Core** — led or shielded by Breaker+ powers. Punches above its weight · the powers have their own wills and may walk.
4. **Holdout Fortress** — a defensible strongpoint. Safe and hard to break · fixed in place, can be besieged or bypassed.
5. **Nomadic** — no fixed base. Can't be pinned or starved out · can't hold ground or stockpile.
6. **Zealots** — bound by a creed. Fearless, cohesive, won't break · can't compromise or adapt.
7. **Crosser-Allied** — backed by a crosser sub-faction. Alien capability on tap · divided loyalties, and the bloc has its own aims.
8. **Crosser-Infiltrated** — hidden crosser agents inside. Knows things it shouldn't · already compromised; its secrets aren't its own.
9. **Medical Lifeline** — controls a clinic or the drugs. Indispensable, courted by all · raided, and bled when it's needed elsewhere.
10. **Granary** — controls food: farms, stores, a warehouse. Feeds people, so it rules them · must defend the stores or starve.
11. **Radio Net** — working shielded comms. Coordinates and overhears everything · a priority target the instant it's known.
12. **Press-Gang** — takes people by force. Grows fast, never short of bodies · universally hated, riddled with the unwilling.
13. **Refugee Mass** — huge, mostly unarmed population. Numbers and moral weight · a burden, slow, and desperately vulnerable.
14. **Old Authority** — remnant of pre-Pulse legitimacy (Guard, police, officials). Organized and recognized · rigid, resented, slow to adapt.
15. **Predatory** — lives by raiding. Lean, mobile, dangerous · makes enemies everywhere and can't sustain itself.
16. **Hidden** — location unknown. Safe from direct attack · can't project power or be found when you need them.
17. **Industrialists** — runs a working plant (refinery, water, grid). Strategically vital, courted by the redoubt · slow, immobile, conquerable.
18. **Warlord-Led** — one Breaker+ rules absolutely. Decisive, feared, fast · collapses or fractures if the leader falls.
19. **Doomed** — running out of something vital. Will gamble, will deal, unpredictable · a clock is ticking on them.
20. **Sanctuary-Builders** — genuinely protects people. Legitimacy, recruits, allies · soft, and the obvious prey of predators.

---

## MISSION & ADVENTURE SEEDS
Roll the job, the catch, and the stakes; add a patron if someone sent you.

**The job (d20):** 1 extract a person · 2 secure a resource · 3 escort a group · 4 defend a place · 5 recover an object · 6 scout a zone · 7 sabotage something · 8 broker a deal/truce · 9 hunt a specific threat · 10 deliver a message/cargo · 11 rescue captives · 12 destroy a target · 13 investigate a disappearance · 14 hold a line · 15 evacuate civilians · 16 find the source of a problem · 17 remove a warlord/leader · 18 clear a route · 19 retrieve intel · 20 buy time for someone else.

**The catch (d20):** 1 it's a trap · 2 a rival wants it too · 3 the client is lying · 4 the target outclasses you (above your tier) · 5 a clock is already running · 6 a moral cost is baked in · 7 the prize is anomalous/cursed · 8 the person won't be saved · 9 the route is impassable · 10 a faction war crosses it · 11 the swarm is in the way · 12 a betrayal is seeded · 13 the reward can't actually be paid · 14 innocents are in the line · 15 the truth is worse than the job · 16 the enemy expects you · 17 a monster-lord holds the ground · 18 you're being used as a pawn · 19 it's already too late (pivot) · 20 a second problem lands mid-job.

**The stakes / reward (d12):** 1 fuel · 2 food · 3 medicine · 4 a working vehicle · 5 a safe place · 6 a faction's favor · 7 intel/a map · 8 a relic (this file) · 9 a person who matters · 10 territory · 11 a debt cleared · 12 reputation that opens doors.

**The patron, if any (d12):** 1 the Redoubt Authority · 2 a local militia/enclave · 3 a desperate family · 4 a fixer/criminal · 5 a faction leader · 6 the Interior Compact · 7 a rival empowered · 8 a dying official · 9 a cult/movement · 10 a crosser · 11 an old tie from before the Pulse · 12 no one — you stumble into it.

---

## MOVEMENTS & CULTS (the post-Pulse creeds)
Roll belief, leader, practice, and how it bites the PC.

**Core belief (d12):** 1 the Pulse was divine judgment · 2 the empowered are gods/the chosen · 3 the empowered are abominations to be purged · 4 the crossers are saviors · 5 the crossers are demons · 6 the old world must be restored exactly · 7 the old world must be burned away · 8 the Unmaking is coming and only *we* survive it · 9 submission to the strong is salvation · 10 the rifts are doors to paradise · 11 might is the only law now · 12 a prophet alone knows the way.

**The leader (d10):** 1 a Crown/Titan "prophet" · 2 a charismatic unpowered demagogue · 3 a surviving cleric/imam/rabbi · 4 a crosser · 5 a former official · 6 a warlord with a creed · 7 a "miracle" child · 8 a council of elders · 9 a voice on the radio · 10 leaderless and viral.

**The practice (d10):** 1 tithes and tribute · 2 purges/sacrifice · 3 recruiting the empowered · 4 mass pilgrimage (to a rift or the redoubt) · 5 ritual violence · 6 sharing/hoarding resources as sacrament · 7 marking the faithful · 8 rejecting all technology · 9 militant conversion · 10 rites at rift-sites.

**How it bites the PC (d10):** 1 conscripts/recruits the PC's people · 2 marks someone like the PC for purging · 3 controls a resource the PC needs · 4 blocks a route with pilgrims · 5 ignites a faction war · 6 harbors a real monster or power · 7 spreads a lie that gets people killed · 8 offers a tempting refuge at a price · 9 turns an ally of the PC's · 10 hardens into a true faction (build it in file 04).

---

## RIFT SITES & ANOMALIES (the Unmaking's edge)
The metaplot made local. Roll what it is, what it does, and — rarely — a sign of the Unmaking.

**What it is (d12):** 1 an open rift, still disgorging · 2 a sealed, scarred rift · 3 a deeper EMP dead-zone (even shielded tech fails) · 4 a monster-spawning hotspot · 5 a "wrong" zone (space/physics bent) · 6 a die-back zone — life withers · 7 a time-echo/slow zone · 8 unnatural cold and dark · 9 a fertile/healing anomaly (rare boon) · 10 a crosser-arrival site · 11 a transcendent's claimed domain · 12 a place the swarm refuses to enter — why?

**What it does / the hazard (d10):** 1 drains power and tech · 2 mutates the living · 3 draws monsters for miles · 4 disorients and maddens · 5 plain physical danger (collapse, exposure) · 6 spawns crossers or feral · 7 emits something sensed from far off · 8 shelters something that shouldn't be disturbed · 9 spreads slowly (a growing clock) · 10 offers something valuable for a price.

**Sign of the Unmaking (d8, ominous — use sparingly):** 1 nothing grows here, and won't again · 2 the dead don't rot · 3 a creeping grey edge · 4 survivors speak of "the quiet that eats" · 5 a crosser refugee weeps at the sight of it · 6 the rare working instrument fails in a way it shouldn't · 7 animals have fled the whole region · 8 it is larger than it was.

---

## RELICS & ANOMALOUS OBJECTS
Every relic is a **gift with a price**. Roll the object, its gift, and its catch.

**The object (d12):** 1 a pre-Pulse shielded device that still works · 2 a rift-touched weapon · 3 an empowered's lost focus · 4 a crosser-made object · 5 a cache of meds or fuel (mundane, priceless) · 6 a map or data on hardened media · 7 an oddity that suppresses or boosts powers · 8 a useful monster-part · 9 a transcendent relic · 10 a contained sample of the Unmaking · 11 a piece of crosser tech · 12 an heirloom a faction would kill to reclaim.

**The gift / use (d10):** 1 reliable power and light · 2 a real weapon edge · 3 healing/medicine · 4 comms or hidden knowledge · 5 protection (armor/ward) · 6 mobility (it runs) · 7 leverage over a faction · 8 suppresses or amplifies powers · 9 detects monsters or rifts · 10 pure trade value.

**The catch (d10):** 1 a faction wants it back, badly · 2 it slowly harms the bearer (sickness, mutation, madness) · 3 it's failing or finite (a clock) · 4 it draws monsters · 5 it marks the bearer to something · 6 it works only for the empowered — or only for the unpowered · 7 it's bait in someone's trap · 8 using it carries a moral cost · 9 it's anomalous and unpredictable · 10 no catch — a true find (rare; raise the price elsewhere).

---

## HOW TO USE
- **Prep:** roll a faction's tags, a mission, a cult, an anomaly, or a relic *before* a session to seed the sandbox, then let file 04's clocks carry them.
- **Play:** when file 08's oracle says "a new power emerges," "a thread opens," or "something inexplicable," reach here for the concrete shape of it. Build it, drop it in, and add any lasting result to the Thread/Character lists in `campaigns/vanguard/campaign-state.md`.
- Keep the lethality mandate's lean: gifts come with prices, sanctuaries hide hooks, and the world acts on its own terms.

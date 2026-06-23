# 16 · POWERED ROSTER & RELATIONSHIP ENGINE (Bonds & Nemeses)
*The campaign's spine. A **randomly generated, evolving cast** of fresh manifesters who become the PC's contacts, friends, allies, patrons, lovers, rivals, and nemeses — and who **remember, deepen, sour, ascend, scar, and transform** on rolled triggers, Shadow-of-War style, in both directions. Built on file 15 (the tier weighting and power table); this file turns single NPCs into a persistent web carried in `campaigns/vanguard/campaign-state.md`. Roll everything; honor the lethality lean; never soften a bond or a grudge.*

> **Why this is the spine.** In the powered-conflict campaign the throughline is *who you fight, trust, and lose* — not a place or a plot. The roster is that throughline made mechanical: a living graph the PC reads, manipulates, is targeted by, and inherits across deaths (§Legacy). Disposition is the **output** of this engine, never a label assigned by mood.

---

## 1 · GENERATING A POWERED NPC
When a powered person matters, roll a **relationship card**. Build on file 15's biasing (street skews low; a warlord's champion skews high), then add the relationship fields.

**Roll (code, shown):**
1. **Tier** — file 15 weighted random-tier d100 (or set by role/context).
2. **Power** — file 08 power table (d20), ranked to tier; flesh as an M&M effect (file 11 frame).
3. **Defense profile** — *hard* (d4: 1 Toughness-tank · 2 high all-around · 3 evasive Dodge/Parry · 4 resolute Will) and **neglected save** (d4: 1 Dodge / 2 Parry / 3 Fortitude / 4 Will). The neglected save is the printed gap (§9.3 of the plan / file 11).
4. **Flaw** (d8): 1 Limited · 2 Unreliable · 3 Tiring · 4 Activation · 5 Power-Loss (fails when wet/grounded/bound) · 6 Noticeable (a loud tell) · 7 Side-Effect · 8 Quirk. The flaw is how they're beaten.
5. **Temperament** (d6): 1 ambusher · 2 duelist · 3 glory-hound · 4 loyalist · 5 coward-who-returns · 6 zealot.
6. **Starting relationship state** (d10): 1 nemesis · 2 rival · 3–4 contact · 5 ally · 6 friend · 7 patron · 8 dependent/charge · 9 wildcard (roll regard) · 10 stranger (noted). *Bias by how they were met.*
7. **Regard** (d8): 1 fear · 2 respect · 3 affection · 4 contempt · 5 hatred · 6 wary · 7 curious · 8 love-potential.
8. **Ambition / trajectory** (d6): 1 protector · 2 tyrant · 3 cult-head · 4 recluse · 5 martyr · 6 climber.

Add a **name**, the person they were before the Pulse, a faction tie (none / member / leader — files 13/18), and any **inter-NPC ties** (roll against the existing roster). Record the card to the **Powered Roster** in `campaigns/vanguard/campaign-state.md`.

---

## 2 · THE RELATIONSHIP CARD (the state-block format)
```
[Name] — was: [pre-Pulse life] · TIER (PL) · POWER (rank, descriptor, range)
  Defense: hard [profile] / neglected [save]   Flaw: [the counter]   Temperament: [x]
  State: [contact/friend/ally/patron/dependent/romance/rival/nemesis]   Track: [-3..+3 or fear→love]   Regard: [x]
  Faction & Rank: [tie]   Ambition: [trajectory] ([clock n/n])
  Memory: [defeats, mercies, gifts, wounds, promises, betrayals — terse]
  Ties: [bonds/rivalries with other roster NPCs]
```

---

## 3 · THE RELATIONSHIP STATES (each its own loop)
| State | Gives | Costs | Deepens on | Strains on |
|---|---|---|---|---|
| **Contact** | access, goods, intel — *for a price* | reciprocity, exposure | fair dealings, paid debts | stiffing them, heat |
| **Friend** | backup, refuge, honesty at cost | obligation; you're both a target | shared danger, loyalty shown | neglect, broken word |
| **Ally** | force, coordination (often + faction Rank §18) | shared enemies, split priorities | won fights, kept faith | conflicting loyalties |
| **Patron** | missions, resources, protection, Rank | obedience; they can spend you | service, results | defiance, embarrassment |
| **Dependent/charge** | meaning, leverage, a future asset | constant risk; their death is a wound | protection delivered | failure to protect |
| **Romance** | a true ally and a reason | the sharpest leverage an enemy holds | intimacy, sacrifice | betrayal, absence |
| **Rival** | a measure, a spur | escalation risk | respect earned | humiliation |
| **Nemesis** | — (the hostile loop, §5) | they hunt you | (deepens *their* grudge) | (your defeats feed it) |

---

## 4 · THE SHARED LOOP & THE TRANSITION ENGINE
Every card carries a **track** and a **memory log**. Kept promises, shared danger, gifts, and time **deepen**; betrayal, neglect, conflicting loyalties, and cost **strain**. When a track crosses a threshold, **roll a transition** — relationships move, they don't sit still.

**Transition trigger (d12)** — *what just happened; then move the state and narrate to the locked result:*
1 betrayal → **bond becomes Nemesis** · 2 shared danger survived → deepen · 3 a kept promise → deepen · 4 neglect/abandonment → strain · 5 conflicting loyalties → drift to Rival · 6 a gift/rescue → deepen · 7 an intimacy beat → **Romance** · 8 you defied them → **Patron becomes Rival** · 9 a bigger threat unites you → **Nemesis becomes Ally** · 10 they rose above you → becomes **Patron** · 11 they fell / need you → becomes **Dependent** · 12 a death or departure → **Legacy thread** (§7).

Transitions are **rolled** (weighted by track, regard, temperament, and trajectory), never chosen for drama. The web your enemies most want to engineer is **Friend/Ally/Romance → Nemesis**; the redemption arc you can earn is **Nemesis → Ally**.

---

## 5 · THE NEMESIS ENCOUNTER LOOP (Rival/Nemesis states — all rolled, all remembered, never softened)
- **They beat you, or you flee** → they **ascend**: advance their ambition clock / faction Rank (maybe a tier bump), regard hardens to contempt, and they seek you out to finish it or lord it. If they *kill* this character, they ascend **and persist via Legacy** (§7).
- **You beat them and spare/leave them** → **survive scarred**: a scar, often a new **immunity born of surviving your signature** (lived through your fire → fire-resist; your kinetics → partial Impervious to kinetic), regard turns to vengeance, and they return harder and fixated.
- **You humiliate them** (beaten, not killed, before their people) → **break** (flee, lose rank) or **fixate** (obsessive vendetta) — rolled by temperament.
- **You kill them** → a **vacancy others fight over** (§6); rarely (rolled) they **cheat death**, returning maimed or transformed (often a force-of-nature horror, file 11/§10 of the plan).
- **You aid, spare, or dominate them** → they can be **turned** toward Ally/Contact, with a later **betrayal risk** weighted by regard.

---

## 6 · THE POWER-STRUGGLE MINIGAME (between scenes, rolled on the oracle)
Each in-world interval (or when the PC idles), advance the roster's ambitions whether the PC is present or not.

**Power-struggle event (d10):** 1 challenges a superior · 2 ambushes a rival · 3 ascends on a kill · 4 recruits followers · 5 betrays an ally · 6 makes a move on the PC · 7 consolidates territory · 8 a feud erupts (roll two roster NPCs) · 9 seeks the PC's help · 10 a patron tests the PC's loyalty.

Resolve the outcome on the oracle, shift ranks/states, and rewrite the local board (file 17/18). The PC may **intervene**: tip a struggle, back an ally under challenge, set two rivals against each other, spend a contact, or walk into the ambush an ambition built for them. Killing one can enrage their blood-brother (a fresh vendetta, via ties); exploiting a feud can hand the PC a rival's head for free.

---

## 7 · TRAJECTORIES & THE LEGACY HAND-OFF
**Trajectory clocks.** Each card's ambition (protector / tyrant / cult-head / recluse / martyr / climber) is a small clock that ticks on power-struggle events and on encounters with the PC. Filling it transforms the NPC (a protector becomes a Sanctuary faction-leader; a tyrant becomes a warlord; a cult-head founds a movement, file 14). The PC can speed, stall, or redirect a trajectory.

**Legacy across deaths.** When a character dies (the ~80% expectation), the web **does not reset**. Carry to the next character's opening (the Legacy ledger, plan §9.5): ascended nemeses (named, grown, holding the grudge — sometimes wearing the dead PC's gear or name), a grieving lover (vengeance or collapse), a patron who mourns and replaces you (voiding protection that kept your charges alive), a friend or freed dependent who carries your name. Each is a thread the successor inherits, can pick up, or is hunted by. The roster is the memory the world keeps of your dead.

---

## 8 · MANIFESTATION CADENCE
The world keeps making powered people. Every few in-world days (or on a scene-setup interrupt, file 08), **roll one in**: a new manifester near the PC (§1), placed by context — a survivor in the camp, an enemy in the fight, a name on the road. Most are low-tier (file 15 weighting); a few reshape the board. Add the ones who could recur to the roster; let the rest pass.

---

## 9 · WORKED EXAMPLE (engine-rolled, dice shown)
Three cards rolled live, to show the engine producing story:

- **Ade Kovac** — *Siege [d100 92], pyro/thermal [d20 7].* Hard: resolute (Will); **neglected: Parry** (soft in melee). **Flaw: Power-Loss — fire fails when wet/grounded.** Temperament: ambusher. **State: rival, regard: affection.** Ambition: cult-head. → *A above-PC fire-rook who likes the PC and whom the PC defied (transition [d12 8]: patron → rival). You don't beat Ade head-on (a rook); you beat the fire with water and the duelist with melee — and the affection means this rivalry could still turn. He's building a fire-cult.*
- **Ray Cho** — *Bruiser [d100 64], body-horror mutation [d20 19].* Hard: high all-around; **neglected: Will.** Flaw: Power-Loss. Temperament: glory-hound. **State: contact, regard: wary.** Ambition: protector. → *A peer-ish mutating contact; rattle his Will to break him. Power-struggle [d10 10]: a patron uses Ray to test the PC's loyalty.*
- **Tess Reyes** — *Flicker [d100 26], summon/control feral [d20 16].* Unreliable. Temperament: zealot. **State: contact, regard: respect.** Ambition: martyr. → *Low personal tier but dangerous reach — a zealot who can throw feral at a problem (a bridge between the powered and force-of-nature pillars). A martyr-in-waiting.*

**Sample local board** [Embattled corridor town, coastal-heat +4 → No-Man's-Land threats]: three predation-driven factions — a Hidden armed bloc, a Crosser-Infiltrated industrial remnant, a Nomadic crosser band — the two strongest **clashing over territory** (file 18). Drop the cards onto it and the scene writes itself.

---

*Provenance: tier weighting and power table from file 15/08; the relationship, transition, and power-struggle tables original to this file, rolled live in the build-seed pass (dice shown above). The roster lives in `campaigns/vanguard/campaign-state.md`; the Conflict Director (file 17) reads it each scene; the Faction-War spine (file 18) is where ranks and fronts resolve.*

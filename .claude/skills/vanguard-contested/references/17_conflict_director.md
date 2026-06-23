# 17 · THE CONFLICT DIRECTOR + DUEL / BATTLE / SURVIVAL PLAYBOOKS
*The scene engine for the powered-conflict campaign. Each scene it reads the **roster** (file 16) and the PC's locale, **generates the local board**, picks a **pillar**, and runs the result honestly. It does not replace the oracle (file 08) or the GM creed (SKILL.md) — it points them at powered-vs-powered, faction-vs-faction, and powered-vs-world play. Roll everything; pre-commit stakes; never soften.*

> **The lead is rivalry.** The spine is the roster (file 16): most scenes pull a face you know — a rival, a contact, a lover, a nemesis — into a fight, a deal, or a betrayal. Factions are the arenas; the world is the storm. Weight scene generation accordingly.

---

## 1 · DEADLINESS READS (the knight feel, via the existing gates)
No new model — use file 01's tier gates and file 05's band rule. Before a fight, **read the tier** (file 15 / a power-sense / what they did to the last people) and tell the player enough to choose:
- **Pawn / peer (Pawn–Breaker, PL ≤9):** a real fight — *winnable but lethal.* Peers can dumpster you in numbers, a bad matchup, or when you're hurt.
- **Rook (Siege, PL 10–11):** outclasses you. Winnable only with terrain, allies, surprise, or the **blind-spot** (§3). Never head-on.
- **Queen (Warlord+, PL 12+ / willful monster-lords):** flee.
- **The world (Pillar 3):** **ignores tier entirely** — the swarm, a kaiju-disaster, famine, the Unmaking bury a knight and a Siege alike. Endurance and flight, never a duel.

Telegraph the rook and the queen so flight is an informed choice; then let the dice be honest.

---

## 2 · THE LOCAL-BOARD GENERATOR (wherever the PC is)
There is no fixed map — generate the **local board** when the PC enters a locale, and regenerate when they move. Persistent factions, roster cards, Standing, and clocks carry between locales (file 18).

**Step 1 — effective danger (the coastal-heat formula):**
`effective threat tier = base region band (file 03) + coastal-proximity step + time step`
- *coastal-proximity step* (0–3): deep interior 0 · interior 1 · near-coast 2 · coastal/tidal 3.
- *time step* (0–2): early year 0 · mid (riding the Famine Wave / Reaver Tide clocks) 1 · late or a coastal-surge tick 2.
A higher total means *more* threats on the board and *worse* ones (push the encounter band up). The safe direction is almost always **inland**.

**Step 2 — what's here:** roll **2 + d2 local factions** (file 04 origin/drive + file 09 tags + file 18 strata), set their fronts (clash / truce / one dominant), and **pull roster cards** present (roll d20 vs the roster — file 08 list method; empty slot ⇒ generate one, file 16). Mark the active **front** (who is fighting whom) and the **board's prize** (the resource/ground/person in contention).

**Step 3 — the hook:** state the expected scene; test it on the oracle (file 08 scene setup); let the board and the pillar (below) shape what actually happens.

---

## 3 · PILLAR-WEIGHTED SCENE GENERATION
When a scene needs a spine, roll **d10** (rivalry-led):
- **1–4 · Powered vs Powered** — pull a roster face (file 16): a rival's move, a contact's deal, a friend's plea, a nemesis's ambush, a lover's crisis. The lead.
- **5–7 · Faction vs Faction** — a war beat on the board (file 18): a front shifts, a side recruits/betrays, the PC is asked to tip a battle.
- **8–10 · Powered vs World** — a survival or disaster beat (§6): a scarcity bite, a swarm surge, a kaiju-as-weather, the Unmaking's creep.
Raise the world's share (8–10 → 7–10) when coastal-heat is high or supplies are low; raise the rivalry share near a hot roster grudge. High Tension (file 08) lets the scene-setup interrupt hijack the plan — that *is* the dense, collapsing world.

---

## 4 · THE DUEL PLAYBOOK (powered vs powered — a puzzle, not a stat-check)
Run a powered fight on the card's printed fields (file 16):
1. **Read & pre-commit.** Name the tier and the stakes (death/maiming/capture where the fiction warrants). Give the player the read.
2. **Find the gap.** Attacks target one defense; damage targets Toughness. Hit the **neglected save** (a Toughness-tank folds to a Will or Fortitude effect). A **rook's Impervious** ignores small hits — you need Penetrating, a bigger hit, or a different defense.
3. **Counter the descriptor.** Cold beats fire; water grounds electrical; a Nullify/Immunity by descriptor shuts a power off (Ade Kovac's fire **fails when wet** — file 16).
4. **Use geometry (the knight's L).** Close fighters die to kiting; ranged blasters to cover and closing; sustained powers to broken concentration; ambushers to being seen first.
5. **Exploit the flaw.** Unreliable, Tiring, Activation, Power-Loss, Noticeable — each is a window. Force the condition that switches them off.
6. **The Self-thread fires.** Pushing your own power hard runs your defining complication as a die (§7) and feeds the Exposure clock — winning can cost you.
7. **Fair vs flee.** Peer = fight; rook = only with an edge; queen = run. A fight you should have fled is a death scene, and that is correct.
Resolve in M&M RAW (file 11 frames), rolled and shown; apply degrees exactly; read incapacitation per the lethality mod, then run the **encounter loop** (file 16 §5) — ascend / scar / humiliate / kill / turn.

---

## 5 · SET-PIECE BATTLE RESOLUTION (powered + troops + monsters on one field, fast)
When the fight is a *battle*, don't roll every soldier. Abstract:
- **Sides have Strength** = troops (file 11 minion waves) + powered assets (roster cards) + any monster (asset or disaster, §10 of the plan).
- **Run a Battle Clock** (e.g., 4–6): each round = the **PC's personal fight** (a duel or a hold-the-line, §4) **plus a battle-tide roll** (oracle, weighted by relative Strength and by what the PC just did). PC wins on their front ⇒ tide ticks their way; losses tick the enemy's.
- **Swing it by targeting the spine:** kill or break the enemy's **powered/command** card and the enemy Strength drops a step (the warlord-led tag, file 09); take the prize and the front collapses.
- **Cost is real:** casualties among the PC's side hit the roster (allies can die ⇒ Legacy, file 16 §7) and the Supply track. A battle the PC "wins" can still cost a friend, a charge, or a limb.
- Resolve the clock to victory, rout, stalemate, or a fighting withdrawal; update fronts and Standing (file 18).

---

## 6 · THE POWERED-vs-WORLD ENGINE (Pillar 3 — the unfightable side)
The world is the third antagonist and it ignores tier. Run it as **hazards, waves, and clocks**, not duels (file 11 force-of-nature frames).

- **Scarcity bites.** Each in-world day draw down the Supply track (SKILL.md); when a category empties, run the RAW deprivation. Foraging/scavenging are rolls against the locale's effective lethality (§2), not free refills.
- **Disasters & the world-breaking (d10, when a Pillar-3 scene fires):** 1 a feral/marine **swarm surge** (a wave, file 11) · 2 a **kaiju-as-weather** crossing the route (a moving deadline; evade/evacuate) · 3 the **grid/structure fails** (dark, cold, collapse) · 4 a **famine-wave bite** (the ration line breaks) · 5 a **cold snap / exposure** clock · 6 the **Unmaking's creep** widens (a die-back zone grows — file 14) · 7 a **flood/fire/terrain** hazard cuts the route · 8 a **transformed-powered horror** (someone lost to the change) stalks the camp · 9 a **rift event** disgorges (file 14) · 10 **two at once** (roll twice, combine).
- **Survival-horror beats.** The uncanny ones (the quiet that eats, the dead that don't rot, a horror wearing a familiar face) are run for dread: limited information, dwindling resources, the thing you can't fight — flight, denial, and cost, not victory.
- **The answer is endurance and direction:** ration, shelter, flee inland (away from coastal heat, §2), and pay the price of the ground the world takes.

---

## 7 · THE POWERED-vs-SELF THREAD (the second axis of every scene)
- **The complication die.** Significant power use runs the PC's (and a roster NPC's) defining complication as a roll every relevant scene (SKILL.md), feeding the Exposure clock.
- **Control / corruption.** Pushing power past its safe envelope (overcharging, taking the rush, using the forbidden trick) calls a control check; failure advances a **personal trajectory** toward what you're becoming (protector → tyrant, etc., file 16 §7) and can leave a mark.
- **Winning can cost.** A duel won by going too far is still a loss on this axis. Track it; let it change who the PC is over the year.

---

## 8 · QUICK LOOP
Enter a locale → **generate the local board** (§2: coastal-heat danger + factions + roster faces + front/prize) → set the expected scene, test on the oracle → **roll the pillar** (§3) → run it: **duel** (§4) / **battle** (§5) / **survival-disaster** (§6), with the **Self-thread** (§7) live → apply the roster **encounter loop & transitions** (file 16) → between scenes, run a **power-struggle** (file 16 §6) and tick clocks/fronts (file 18) → adjust Tension → write everything to `campaigns/vanguard/campaign-state.md`.

---

*Provenance: deadliness from file 01/05; local-board + coastal-heat from the revision plan §5/§8b (sample rolled in the build-seed pass); pillar weights, battle clock, and the disaster table original to this file; duels run on file 16's card fields and file 11's frames. The Director is the conductor — the roster (16), the bestiary (11), and the war spine (18) are the instruments.*

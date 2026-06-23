# World Subsystems — Vanguard Contested   (hook: world-tick; fired by `tick.py <bridge> <scene#>` at bookkeeping)
# tick.py reads ONLY the table rows below (name · cadence · advance-by) and reports which are DUE.
# cadence must read "every scene" | "every N scenes" | "on trigger: …". The engine then advances each
# by rolling its named generator table honestly (dice.py table) and/or ticking its clock; record to state.

| subsystem | cadence | advance by |
|-----------|---------|-----------|
| Supply track | every scene | draw down food/water/medicine/fuel/warmth by the day's rolled amount; injuries & cold-treatment cost extra medicine; foraging = a roll vs the region lethality number, not a refill; at 0 apply RAW deprivation (fatigue/dehydration/exposure). A scene where no resource moved is INVALID — regenerate it. |
| Jeopardy Counter | every scene | if the scene had no injury, no lost resource, and no death/maiming/capture-stakes roll → +1. At 2, the NEXT scene must open with lethal stakes or a hard scarcity bite. At 3, log a GM error, +1 Tension, and don't send a scene lacking a present above-tier threat or a forced attrition draw. Resets to 0 only on a scene that imposes injury, loss, or a death-stakes roll. |
| Exposure clock | on trigger: each unresolved witness / collateral / loud power-use | add a segment (run the PC's/NPC's defining-complication tell — `generators/supers_defining_complication`). When full, it discharges (oracle-rolled) into a hunt, a betrayal, or a faction that now knows the PC's nature and moves on it. |
| Faction moves | on trigger: each in-world week, and any scene the PC burns a day without advancing a goal | roll `generators/faction_move` for an acting faction + a Move Toward/Away a Thread; advance that faction's relationship track and clock; prune dead factions, grow new ones (`generators/faction_tags`, ref 04). |
| World clocks (six) | on trigger: each in-world week or on player action that warrants | advance the live values from state: Empire Consolidates (8) · Famine Wave (6) · Concord Swing (6, two-way) · Reaver Tide (4) · Redoubt Recovery (8) · Unmaking Horizon (12). Show only perceivable clocks; the Concord Swing & Reaver Tide are the most player-responsive (ref 04). |
| Powered Roster | every 5 scenes | a new manifester arrives: roll `generators/empowered_tier` + `empowered_power` + `empowered_intent` (+ `supers_control`, `supers_defining_complication` if they may matter mechanically); add to the Characters List / roster; run relationship transitions on rolled triggers (ref 16). |
| War Fronts | on trigger: each in-world week (powered-conflict mode) | advance the active War-Front clock (ref 18); per-faction Standing (−3…+3) spreads by network, never global; resolve Rank consequences inside a joined faction. |

## Notes (not read by tick.py)
- **Powered-Conflict Directive is the default mode.** Suspend the Roster / War-Fronts rows if the player asks
  for the original survival-sim emphasis; the rest still binds.
- The Supply track and Jeopardy Counter are the anti-drift spine — they fire **every** scene. If both are
  inert, the scene is soft (see `interpretation.md` self-audit / the engine SELF-AUDIT gate).
- "advance by" rows that name a `generators/` table are rolled with
  `python3 ../../mythic-gm/scripts/dice.py table generators/<name>.json` and recorded to `campaign-state.md`.
- Full clock ranges, triggers, and faction detail live in `references/04_factions_and_clocks.md`,
  `references/16_roster_relationship_engine.md`, `references/17_conflict_director.md`,
  `references/18_faction_war_spine.md`.

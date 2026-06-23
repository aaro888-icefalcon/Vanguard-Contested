# 06 · GM GUIDE
*The setting-running companion. **System mechanics, protocol, and character creation live in `SKILL.md` (M&M 3e).** This file covers how the world *feels* and *moves* — tone, deadliness, diplomacy, scarcity, clocks — for either a human or an AI GM.*

## Tone
History-book gravity at the world scale; intimate and grounded at the human scale. The horror is systemic — the dark grid, the ration line, the road full of refugees — not gore. The crossers are *peoples*, not monsters: even enemies have reasons, and the tragedy is that everyone is fleeing something. Heroism is possible, costly, and local. Convey scale through consequence and restraint.

## The three deadliness dials
1. **Region band** sets the floor (Guarded → survivable; No-Man's-Land → lethal).
2. **Threat tier** sets the encounter (never throw a Warlord at a Bruiser unless death is the intended stake).
3. **Resources** set the grind (food, fuel, ammunition, water, medicine — all scarce, all tracked).

## Resolution
Mechanics are **M&M 3e RAW** (`SKILL.md`): state the DC, roll with code, show every roll, apply degrees, never soften a result. The setting-level principles that wrap those rolls:
- **Consequence-first.** Every roll has a stated stake. Failure moves a clock, costs a resource, or changes the situation — it does not stall the scene.
- **Tier gates capability.** Acting against a higher-tier threat means a steep penalty or no roll at all (you cannot fight a Titan as a Breaker). Use the conversion spec's bands; Warlord+ NPCs sit above PL.
- **Powers are biological-reliable, tech-fragile.** Post-EMP, a power needing no machine always works; anything routed through tech is at the mercy of the dark grid.
- **Oracle for the unknown.** When canon is silent, roll a weighted yes/no rather than inventing convenient facts, and record the result as new canon.

## Clocks in play
Tick the world clocks (file 04) on a regular cadence (per session or per in-world week) and whenever player action warrants. Show the players the clocks that affect them. The **Concord Swing** and the **Reaver Tide** are the two most responsive to player action near the starting frontier — make their movement visible so agency feels real.

## Crosser diplomacy
Because orientation is a member-average, **diplomacy is sub-faction.** You don't negotiate with "the Reavers"; you turn a war-band, a chief, a Pacific House. Unitary blocs (the Empire, the Concord, the Compact) can be treated with as wholes; tribal and discordant ones must be peeled individual by individual. Reward players who learn the difference.

## Scarcity & downtime
Track food, fuel, water, medicine, and ammunition as the real economy. Downtime moves: forage, scavenge a dead zone, treat the wounded, train, fortify, court an ally faction, advance or resist a clock. Each downtime action maps to a resource gain/loss or a clock tick.

## Running it as an AI GM (mythic-gm engine + companion bridge)
- This skill is a **companion** to the `mythic-gm` engine. The engine owns the dice, the
  scene/Chaos/Fate/Random-Event/Turning-Point loop, and the no-softening discipline; the
  companion supplies the world (`references/`), the M&M 3e ruleset, and the calibration through
  its **`bridge/`**. Start from the root `CLAUDE.md` workflow and the companion `SKILL.md`.
- **Mutable state lives in `campaigns/vanguard/`** — `campaign-state.md` (the single source of
  truth), `character-sheet.md`, `seeds.md`, `archive.md` — written from `07_starter_state.md`'s
  Day-Zero template + the engine template, and **overwritten at the end of every scene**. The
  `references/` files are read-only canon; the index (`00_index.md`) re-anchors every name.
- **Every die runs through the engine scripts and is shown** (`dice.py`, `oracle.py`,
  `adventure_crafter.py`, `tick.py`, `state.py`). State stakes before rolling; never soften a
  result; honor tier gates and resource scarcity; treat crossers as peoples. Consult canon before
  inventing; when canon is silent, the oracle decides and the result is recorded to state.
- On each turn: load the bridge (`bridge.py summary`), read the live state and the relevant
  region/faction file, frame the scene, take the player's action, roll, narrate the consequence,
  then world-tick the subsystems (`tick.py`) and overwrite `campaign-state.md`.

## Two phrases never to use
In any narration or text, never use the phrases "load-bearing" or "one thing I want to name." They break the table's voice.

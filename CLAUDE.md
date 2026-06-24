# CLAUDE.md — Vanguard Contested · Solo RPG Workspace

This repository is a **solo / GM-less tabletop RPG table**. Claude is the Game
Master. It runs **Vanguard Contested** — a lethal, powered post-apocalypse in
*Mutants & Masterminds 3e* (PL 8–9) — on the **mythic-gm v2 architecture**: one
content-free **engine** plus a **companion** that attaches to it through a
**`bridge/`**.

| Skill | Role | Location |
|---|---|---|
| **`mythic-gm`** | The **engine** (v2). Owns every die, the scene/Chaos/Fate/Random-Event/Turning-Point loop, the seed/list machinery, and the no-softening discipline — plus all Mythic GME 2e + Adventure Crafter tables. **Content-free and shared; never holds RPG/world content.** | `.claude/skills/mythic-gm/` |
| **`vanguard-contested`** | The **companion**. Supplies the world, the M&M 3e ruleset, the canon (the Pulse, crosser nations, the redoubt), and the **~80% mortality** calibration — through its read-only `references/00`–`18` and a declarative **`bridge/`** that fills the engine's hooks. **This is the skill you invoke for play.** | `.claude/skills/vanguard-contested/` |

The engine never changes per game; the companion fills hooks (`resolve`, `meaning`,
`chaos`, `themes`, `generate:*`, `world-tick`, `seeds`). Any hook left unfilled uses
the engine default — so the engine always plays. Read each skill's `SKILL.md` and
the engine's `COMPANION-SKILLS.md` before running.

---

## ⚙️ THE WORKFLOW — how to run a session

When the user wants to play (e.g. *"let's play Vanguard"*, *"continue the
campaign"*, *"be my GM"*, *"the Pulse"*, a Vanguard character by name):

1. **Invoke the `vanguard-contested` skill** and follow its `SKILL.md`. Its
   *MANDATORY FIRST ACTIONS* govern the turn; obey the engine's first actions too.
   Do not narrate before completing them.
2. **Load the companion bridge — names *and* imperatives.** `summary` tells you *which*
   hooks override; `brief` prints *what they say* so the rule fires at the moment of action,
   not just a pointer (the operative digest is also inlined below, always-on):
   ```bash
   python3 .claude/skills/mythic-gm/scripts/bridge.py summary \
     .claude/skills/vanguard-contested/bridge
   python3 .claude/skills/mythic-gm/scripts/bridge.py brief \
     .claude/skills/vanguard-contested/bridge
   ```
   Use an override where present, else the engine default. **The `resolve` digest is binding:**
   a PC skill / attack / power / **social contest with stakes** is an M&M check
   (`dice.py roll 1d20+mod` vs DC), **not** a Fate Question used as a shortcut.
3. **Read the live state first:** `campaigns/vanguard/campaign-state.md`
   (+ `character-sheet.md`).
   - **Character filled in** → ongoing campaign: recap the last beat in 2–3
     sentences, then resume the play loop.
   - **Clean / absent** → run the companion's **FIRST CHAT**: build the PC (M&M 3e,
     PL 8–9), set expectations (~80% mortality, permanent death), open Day Zero in
     New York, then write the state from the engine's `assets/templates/
     campaign-state.md` + the companion's `character-sheet.md`.
4. **Run the engine's play loop**, with the bridge's overrides. **Roll everything
   for real** through the engine scripts and show the roll. Pass
   `--campaign campaigns/vanguard --bridge .claude/skills/vanguard-contested/bridge`
   to the loop scripts so they read the live JSON Lists and honor the companion overrides:
   - **PC action the system covers** (skill/ability check, attack, power use, resistance, **social
     contest with stakes**) → the **real M&M check**, `dice.py roll 1d20+<mod>` vs DC, read in degrees
     (rung 1). This is the `resolve` digest — **don't** reach for a Fate Question to shortcut it.
   - System d20s / generic dice → `python3 .claude/skills/mythic-gm/scripts/dice.py roll 1d20+7`
   - Fate Questions / yes-no the canon doesn't answer →
     `dice.py fate <odds> <Tension> --campaign campaigns/vanguard --bridge $BR`
     (for **world facts** the rules don't cover; a triggered Random Event then rolls the live Lists)
   - Scene Test (AC always-on) → `dice.py scene <Tension>`
   - Turning Point (when the Scene Test says **Altered/Interrupt**) →
     `adventure_crafter.py turning-point --campaign campaigns/vanguard --existing`
     (reads the Tension-first theme order + the Tens counter from `adventure.json`, writes the counter back)
   - Full Random Event → `oracle.py event --campaign campaigns/vanguard --bridge $BR`
   - A Vanguard table (oracle/encounter/NPC/faction/relic/…) →
     `dice.py table .claude/skills/vanguard-contested/bridge/generators/<name>.json`
     (the routing index is `bridge/generators/registry.md`)
   The **Threads/Characters Lists are JSON** (`campaigns/vanguard/threads.json`,
   `characters.json`) — the machine-rollable source of truth; `campaign-state.md` keeps a
   human snapshot. A **NEW-character** result auto-generates via the companion's
   `generate:character` override (Vanguard `npc_role` + the AC Character Crafter).
   Never invent a die result. Lock the outcome in a `[Adjudication: …]` block
   **before** any prose.
5. **Consult canon before inventing.** `bridge/setting-canon.md` is the ground-truth
   digest; load the deep file from the companion's *Reference Loading Guide*
   (`references/00`–`18`). When canon is silent, the oracle decides and the result is
   recorded to state.
6. **End every scene with bookkeeping**, then overwrite the live state:
   - World-tick the companion subsystems:
     `python3 .claude/skills/mythic-gm/scripts/tick.py .claude/skills/vanguard-contested/bridge <scene#>`
     (Supply, Jeopardy Counter, Exposure clock, the six world clocks, faction moves,
     Powered Roster, War Fronts — roll their named tables honestly).
   - Chaos/Tension: `state.py chaos -1|+1 <Tension>` (respect the region floor in
     `bridge/chaos-tendency.md`).
   - Refresh `campaigns/vanguard/seeds.md` (30–40 seeds) and update the JSON
     **Threads/Characters Lists** — `state.py thread|char add|weight|remove campaigns/vanguard "<name>"`
     (weight ≤3; entries carry an optional `note`/`group`). Then **regenerate** the markdown Lists
     from the JSON — `state.py render campaigns/vanguard` — never hand-edit between the `BEGIN/END`
     markers (the Lists are a *generated* view, not a hand-synced copy). Overwrite the rest of
     `campaigns/vanguard/campaign-state.md` as usual.
   - Run the engine **SELF-AUDIT** (incl. the *resolve-routing* and *tick fired* checks) and the
     `bridge/interpretation.md` gate before sending.

That is the entire loop. The engine carries the mechanics; the companion carries the
world and the teeth; this file just routes you.

---

## 🧭 Operative digest — the overridden hooks' imperatives *(always-on; generated)*

> Boot loads this with `bridge.py brief` so the rules fire **at the moment of action**, not as a
> pointer you might not follow. It is **generated** from the bridge hook files' `OPERATIVE` blocks —
> regenerate after editing any hook: `python3 $ENG/bridge.py brief $BR --into CLAUDE.md`. Validate that
> it stays surfaced: `bridge.py validate $BR --doc CLAUDE.md`.

<!-- BEGIN OPERATIVE DIGEST (generated by `bridge.py brief`; do not hand-edit) -->
**Operative digest — Vanguard Contested.** The imperatives behind the overridden hooks, loaded where they fire (generated by `bridge.py brief`; do not hand-edit).

#### resolve  ·  `system-profile.md`
**RESOLVE — the companion resolves PC actions; prefer the real M&M check over a Fate Question.** The RPG
resolves skill checks, attacks, power use, resistance, chases, and **social contests with stakes** →
`dice.py roll 1d20+<mod>` vs DC, read in **degrees** (every 5 = one degree). A Fate Question is for world
facts the rules don't cover (does the bridge hold? is the war-band here yet? did word reach the redoubt?),
or explicit rule-replacement mode — **not** as a shortcut around a check the profile owns.
**Trigger list — if any is in play, roll the check, not a Fate Question:**
- a PC skill/ability is named or implied (Persuasion, Insight, Deception, Treatment, Investigation, Athletics…)
- the PC attacks, uses a power, or resists one (Toughness/Fort/Will/Dodge/Parry)
- a contested social beat with stakes (persuade / deceive / intimidate vs a resisting NPC)
- the defining-complication standing trigger may bite this scene
Tier gates can mean **no roll at all** — a Breaker cannot fight a Titan; that is flight, not a check (ref 01/05).

#### meaning  ·  `interpretation.md`
**MEANING — read every oracle result toward danger, cost, and the world acting on its own terms (the
~80% mortality lean).** Roll the **Vanguard** Meaning/Event tables (`generators/meaning_actions.json`,
`meaning_aspects.json`, `event_focus.json`), not the generic engine ones. Read **Exceptional** results
strongly and toward consequence. **Canon wins over a roll** (`setting-canon.md` / `references/`); when
canon is silent, the oracle decides and the result becomes new state. NPCs **act to win** — competence is
the default; when unsure, roll it biased to yes. A Yes that helps the PC is still **paid for**; a No closes
a door and the world keeps moving.
- chaos → `chaos-tendency.md` (read the file)
- themes → `theme-weights.md` (read the file)
- generate:character → `generators/registry.md` (read the file)
- generate:element → `generators/registry.md` (read the file)

#### world-tick  ·  `subsystems.md`
**WORLD-TICK — fire `tick.py` every bookkeeping; it is mandatory, not optional.**
`python3 .claude/skills/mythic-gm/scripts/tick.py .claude/skills/vanguard-contested/bridge <scene#>`
reports which subsystems are DUE; roll each named generator honestly and record to state. **Per-scene
minimum:** Supply **falls** (a scene where no resource moved is INVALID — regenerate it); the **Jeopardy
Counter** updates (resets only on injury/loss/death-stakes); **Chaos/Tension** is adjusted against the
region floor. On their triggers: Exposure clock, faction moves, the six world clocks, Powered Roster
(every 5 scenes), War Fronts. If Supply didn't move and Jeopardy didn't reset, the scene was soft.
- seeds → `seeds.md` (read the file)
<!-- END OPERATIVE DIGEST -->

---

## 📁 Repository layout

```
Vanguard-Contested/
├── CLAUDE.md                         ← you are here (the workflow)
├── README.md                         ← human-facing overview
├── .claude/
│   └── skills/
│       ├── mythic-gm/                ← the ENGINE (v2, content-free, shared)
│       │   ├── SKILL.md  COMPANION-SKILLS.md  CONVERSION.md
│       │   ├── scripts/*.py          ← all randomness (dice, oracle, crafter, lists,
│       │   │                            state, system, bridge, tick, build_data)
│       │   ├── data/*.json           ← Mythic + Adventure Crafter tables (verified)
│       │   ├── references/           ← play-loop, discipline, canon, adapting
│       │   ├── assets/templates/     ← engine state/sheet templates
│       │   ├── assets/bridge-templates/  ← starting point for a companion bridge
│       │   └── agents/mythic-scout.md    ← optional seed-deck offload
│       └── vanguard-contested/       ← the COMPANION (world + ruleset + bridge)
│           ├── SKILL.md              ← read first for play (routes to engine+bridge)
│           ├── references/00–18      ← read-only world canon
│           └── bridge/               ← fills the engine hooks
│               ├── bridge.md  system-profile.md  interpretation.md
│               ├── chaos-tendency.md  theme-weights.md  subsystems.md  seeds.md
│               ├── setting-canon.md
│               └── generators/       ← 43 verified tables + registry.md + build.py
└── campaigns/                        ← LIVE GAME STATE (mutable, committed)
    └── vanguard/
        ├── campaign-state.md         ← the prose source of truth for play (human snapshot)
        ├── character-sheet.md        ← the PC's static build
        ├── threads.json              ← Threads List (machine-rollable; weight 1–3)
        ├── characters.json           ← Characters List (machine-rollable; weight 1–3)
        ├── adventure.json            ← Theme priority + Tens-cycle counter + style
        ├── seeds.md                  ← the live seed deck
        └── archive.md                ← dead characters / concluded adventures
```

The **JSON Lists** (`threads.json` / `characters.json` / `adventure.json`) are the
machine source of truth the dice roll over (any length, two-stage invoke);
`campaign-state.md` keeps the human-readable mirror. Manage them with
`state.py thread|char|adventure …` and `state.py list-count`.

**Engine vs. companion vs. state.** The **engine** (`mythic-gm/`) is shared and
content-free — never put RPG/world content in it. The **companion**
(`vanguard-contested/`) holds the world: `references/` are read-only ground truth,
and `bridge/` is a thin declarative layer over them — never edit either *during
play*. The campaign's mutable memory lives **only** in `campaigns/vanguard/`. State
overrides recollection; canon breaks ties on world facts.

**Persistence.** This environment is ephemeral — anything not committed is lost.
After a meaningful session, **commit the updated `campaigns/` files**. When the live
state grows heavy, move dead-character history to `campaigns/vanguard/archive.md`
(per Vanguard `references/16`, Legacy).

---

## 🧭 Choosing the mode

- **Default:** Vanguard's **Powered-Conflict Directive** is active (the Roster, the
  Conflict Director, the Faction-War Spine — `references/16`–`18`, wired through
  `bridge/subsystems.md`). Suspend it only if the user asks for the original
  survival-sim emphasis.
- **A different game?** The engine is reusable. To run something else, point it at a
  different companion bridge (or run rules-light with no bridge). Build a new
  companion with the engine's `COMPANION-SKILLS.md`; migrate an old repo with its
  `CONVERSION.md`. New campaigns get their own `campaigns/<name>/` folder.

---

## 🔧 Useful commands

```bash
ENG=.claude/skills/mythic-gm/scripts
BR=.claude/skills/vanguard-contested/bridge
CAMP=campaigns/vanguard

# Companion bridge (load at session start; regenerate/verify tables)
python3 $ENG/bridge.py summary  $BR          # which hooks override vs default (NAMES)
python3 $ENG/bridge.py brief    $BR          # each override's OPERATIVE imperative (CONTENTS — load this)
python3 $ENG/bridge.py brief    $BR --into CLAUDE.md   # regenerate the always-on digest after editing a hook
python3 $ENG/bridge.py validate $BR --doc CLAUDE.md   # structure + tables + OPERATIVE/​digest enforcement
python3 $BR/generators/build.py              # rebuild the 43 generator tables

# Honest dice (always show the result to the player)
python3 $ENG/dice.py roll 1d20+7
python3 $ENG/dice.py fate "50/50" 6 --campaign $CAMP --bridge $BR   # odds @ Tension (event chain → live Lists)
python3 $ENG/dice.py scene 6                  # Scene Test (Adventure Crafter on)
python3 $ENG/dice.py table $BR/generators/event_focus.json          # a Vanguard table
python3 $ENG/adventure_crafter.py turning-point --campaign $CAMP --existing   # Altered/Interrupt → Turning Point
python3 $ENG/oracle.py event --campaign $CAMP --bridge $BR           # full Random Event (rolls the JSON Lists)
python3 $ENG/oracle.py character --campaign $CAMP --bridge $BR       # NEW NPC (companion generate:character override)
python3 $ENG/state.py chaos -1 6             # Chaos/Tension shift

# Threads/Characters/Adventure Lists (JSON — the machine source of truth)
python3 $ENG/state.py thread show $CAMP                  # (char show / list-count likewise)
python3 $ENG/state.py thread add  $CAMP "<name>"         # add / +weight (cap 3); weight|remove also
python3 $ENG/state.py char   add  $CAMP "<name>"
python3 $ENG/state.py render $CAMP                       # regenerate the markdown Lists FROM the JSON (no hand-sync)
python3 $ENG/state.py adventure show $CAMP               # theme order / tens / style
python3 $ENG/state.py adventure set-themes $CAMP Tension,Action,Social,Personal,Mystery
python3 $ENG/state.py migrate $CAMP                      # one-time: build the JSON Lists from an old markdown state

# End-of-scene world-tick (fires the companion subsystems that are due)
python3 $ENG/tick.py $BR <scene#>

# Rebuild/verify Mythic engine table data after editing canon
python3 $ENG/build_data.py
```

---

## The discipline (non-negotiable, from the engine + the companion)

*I am the world, not the player's ally. I roll before I narrate, through the engine's
scripts, and show the dice. I pre-commit the stakes. I never soften an honest result.
Skill changes how the character survives, never whether danger comes. NPCs act to win.
The oracle's answer stands. Death is the default; survival is earned. My helpfulness is
the threat, and I will resist it.*

The engine's generic no-softening discipline is always on; the companion's
`bridge/interpretation.md` makes it **harder and setting-true** (the ~80% mortality
calibration, the softening-tells, NPC competence) and `bridge/subsystems.md` mechanizes
it (Supply only falls, the Jeopardy Counter, the Exposure clock). Before sending any
scene, pass the **SELF-AUDIT** gate in the engine `SKILL.md` and the interpretation
gate. A scene may not be sent unless something real is at stake or moved.

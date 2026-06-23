# Vanguard Contested

A **solo / GM-less tabletop RPG**, run by Claude as the Game Master.

> **Vanguard Contested** — a lethal, powered post-apocalypse in *Mutants &
> Masterminds 3e* (PL 8–9). One morning the **Pulse** hits: the grid dies, one
> in five people become something else, and eighteen humanoid crosser nations
> arrive fleeing the **Unmaking**. Humanity is beaten in the open but holds a
> defended **redoubt**. You play one of the empowered, from Day Zero in New York
> through one brutal in-world year. Expect to die. Survival is earned, never
> given.

## How to play

Open this repo in Claude Code (or Claude Code on the web) and say:

> *"Let's play Vanguard."* &nbsp;·&nbsp; *"Continue the campaign."* &nbsp;·&nbsp; *"Be my GM."*

Claude reads [`CLAUDE.md`](./CLAUDE.md), invokes the skills, and takes it from
character creation (or your saved state). It rolls every die for real through
Python scripts and shows you the result — it does not fudge, rescue, or soften.

## Architecture: engine + companion + bridge

Vanguard runs on the **mythic-gm v2** model — one reusable engine, any number of
game companions:

- **`.claude/skills/mythic-gm/`** — the **engine**: a standalone, content-free
  solo-RPG engine (Mythic GME 2e + The Adventure Crafter). It owns every die, the
  scene/Chaos/Fate/Random-Event/Turning-Point loop, and the no-softening
  discipline. It can run *any* setting on its own, or via a companion.
- **`.claude/skills/vanguard-contested/`** — the **companion**: the world, the
  M&M 3e ruleset, and the canon (`references/00`–`18`), plus a declarative
  **`bridge/`** that fills the engine's hooks — the M&M resolution
  (`system-profile.md`), the ~80% mortality lens (`interpretation.md`), the
  Tension floors (`chaos-tendency.md`), the scarcity/clock machinery
  (`subsystems.md`), and **43 verified generator tables** (`generators/`).
- **`campaigns/vanguard/`** — your live campaign: `campaign-state.md` (the single
  source of truth), `character-sheet.md`, `seeds.md`, and `archive.md`. Claude
  overwrites the state at the end of every scene.

## Saving your game

This runs in an ephemeral environment. **Commit the `campaigns/` folder** after a
session to keep your campaign — character, injuries, supplies, threads, clocks,
and the Legacy of the characters who came before.

## Building your own / migrating

The engine is reusable. To pair it with a different RPG or setting, build a
companion `bridge/` using `mythic-gm/COMPANION-SKILLS.md`. To convert an older
two-skill repo to this architecture, follow `mythic-gm/CONVERSION.md`.

## Credits & content note

Built on the *Mythic Game Master Emulator 2e* and *The Adventure Crafter*
(© Tana Pigeon / Word Mill Games), bundled in the `mythic-gm` skill for personal
use. Vanguard Contested canon is original fiction. See each skill's `SKILL.md`
and `README.md` for details.

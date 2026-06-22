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

## What's in here

- **`.claude/skills/vanguard-contested/`** — the world, the M&M 3e ruleset, the
  canon, and the GM operating manual (`SKILL.md`).
- **`.claude/skills/mythic-gm/`** — a standalone, reusable honest-dice solo-RPG
  engine (Mythic GME 2e + The Adventure Crafter) that powers the randomness and
  can run *any* other setting on its own.
- **`campaigns/vanguard/vanguard-state.md`** — your live campaign. This is the
  single source of truth; Claude overwrites it at the end of every scene.
- **`CLAUDE.md`** — the workflow that ties it all together. Start there.

## Saving your game

This runs in an ephemeral environment. **Commit the `campaigns/` folder** after a
session to keep your campaign — character, injuries, supplies, threads, clocks,
and the Legacy of the characters who came before.

## Credits & content note

Built on the *Mythic Game Master Emulator 2e* and *The Adventure Crafter*
(© Tana Pigeon / Word Mill Games), bundled in the `mythic-gm` skill for personal
use. Vanguard Contested canon is original fiction. See each skill's `SKILL.md`
and `README.md` for details.

# System Profile — Mutants & Masterminds 3e (PL 8–9)   (hook: resolve)

RAW per the M&M 3e SRD, no house mechanics, plus three **gritty modifications** (below).
The engine routes task resolution and combat here; everything the profile doesn't cover
defers to a Fate Question (`system.py route`).

- **Dice convention:** d20 + modifier vs a DC. Express any roll as `dice.py roll 1d20+<mod>`.
- **Core resolution:** roll d20 + bonus ≥ DC. Margins read in **degrees** (every 5 over/under = one degree).
- **Degrees of success?:** **YES** — degrees are load-bearing (combat conditions, skill outcomes). In
  Fate-Question rule-mode, map Exceptional Yes/No to an extra degree of success/failure.
- **Power level / build:** **PL 8 (120 pp)** or **PL 9 (135 pp)**, set at creation = **Heavy–Breaker**
  (ref 01). Caps: Attack + Effect ≤ 2×PL; Dodge + Toughness ≤ 2×PL; Parry + Toughness ≤ 2×PL; skills ≤ PL+10.
  Two complications minimum; the **defining complication is a standing trigger** (rolled every relevant scene).
- **Abilities (8):** STR STA AGL DEX FGT INT AWE PRE.
- **Defenses:** Dodge, Parry, Fortitude, Will, **Toughness**. Resistance checks per RAW.
- **Health / damage:** no HP. A **Toughness** resistance check (DC 15 + damage rank) on every hit;
  failure steps the condition track **bruised → dazed → staggered → incapacitated**; bruise penalties
  are cumulative and tracked. Afflictions/other effects resolve vs their listed defense.
- **Combat:** initiative d20 + AGL/bonus; attack roll vs **Dodge/Parry (DC = 10 + active defense)**; on a hit
  the target makes the Toughness check above. Conditions stack per RAW.
- **Defeat / death — lethality is LIVE (gritty mod 2):** an **incapacitated** result resolves *in the fiction*
  as **death, maiming, or capture** (harsh default). Killing attacks and falls use RAW lethal damage.
  **Death is permanent**; rebuild the next PC into the same canon year (ref 01, PL 8–9).
- **Hero points:** earned **only** when a complication actively costs the player — never as mercy, rescue,
  or a suggested out. Standard RAW uses (re-roll, edit, recover, instant counter). **No retcons** (gritty mod 3):
  hero points may not rewrite established facts.
- **NPC stat units (on-the-fly NPC Statistics):** express NPCs in **PL-by-tier** (ref 01: Bruiser≈PL6, Heavy≈PL8,
  Breaker≈PL9, Siege+ above-PL boss) → attack/effect bonus, active defenses, Toughness, one signature power at rank.
  A faction's strength is its **Tier**, not a roster (ref 15). Stat **one** powered foe per scene; the rest are
  waves/Tiers/clocks (ref 15 spotlight discipline). Use the engine's NPC Statistics read (Yes = as expected;
  ExcYes +25%; No −25%; ExcNo −50%) to size an unplanned NPC fast.
- **Routing default:** the RPG resolves **combat, skill checks, power use, resistance, chases, social contests
  with stakes**. Defer to **Fate Questions** for world questions canon doesn't answer (does the bridge still
  stand? is the war-band here yet? did word reach the redoubt?). Tier gates can mean **no roll** — you cannot
  fight a Titan as a Breaker (ref 01/05).
- **Subsystems as Fate Questions:** off-screen faction outcomes, rumor truth, weather/grid failures, whether a
  complication's standing trigger bites this scene (or roll its generator). Powers are **biological-reliable,
  tech-fragile** post-EMP — tech-routed effects roll against the dark grid (build flaws / Fate Question).

> Caps audit at creation; degrees read exactly; never lower a DC or re-read a roll because the PC is in
> trouble. See `interpretation.md` for *how hard* to set the world, and `references/01_conversion_and_tiers.md`
> for the tier→PL ladder.

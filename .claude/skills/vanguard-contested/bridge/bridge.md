# Bridge manifest — Vanguard Contested

Vanguard Contested is a **companion** to the mythic-gm engine: a lethal, powered
post-apocalypse run in **Mutants & Masterminds 3e (PL 8–9)**. It supplies the RPG
(`system-profile.md`), the world (`setting-canon.md` + the read-only `references/00`–`18`),
the setting's hardcore GM lens and **~80% mortality** calibration (`interpretation.md`),
the Tension/Chaos floors (`chaos-tendency.md`), grimdark theme bias (`theme-weights.md`),
the scarcity / Jeopardy / clock / roster machinery (`subsystems.md`), the seed sources
(`seeds.md`), and **43 verified generator tables** (`generators/`).

The engine still owns every die, the scene/Chaos/Fate/Random-Event/Turning-Point loop,
and the no-softening discipline. The companion only fills hooks; anything unfilled uses
the engine default. Regenerate the tables with `python3 generators/build.py`; verify the
whole bridge with `python3 ../../mythic-gm/scripts/bridge.py validate .`.

```json
{
  "companion": "Vanguard Contested",
  "engine": "mythic-gm>=2",
  "overrides": ["resolve","meaning","chaos","themes","generate:character","generate:element","world-tick","seeds"],
  "files": {
    "system_profile": "system-profile.md",
    "interpretation": "interpretation.md",
    "chaos": "chaos-tendency.md",
    "themes": "theme-weights.md",
    "generators": "generators/registry.md",
    "subsystems": "subsystems.md",
    "seeds": "seeds.md",
    "canon": "setting-canon.md"
  }
}
```

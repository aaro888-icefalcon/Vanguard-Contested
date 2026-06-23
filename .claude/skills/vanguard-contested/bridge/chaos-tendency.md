# Chaos Tendency — Vanguard Contested   (hook: chaos)
# Vanguard's "Tension" IS the engine's Chaos Factor by another name (ref 08).
# Run it high and by rule: high Tension = more Random Events and a danger-leaned oracle.
- start: 5
- volatility: normal        # ±1 each scene, but asymmetric (see note): hostility accrues faster than it buys down
- floor: "Guarded >= 4 · Embattled >= 5 · No-Man's-Land >= 6"   # never below the current region band's floor
- flavor: standard          # full chaos chart; Random Events on; the world hijacks plans

# Adjust by rule (ref 08), clamped to the region floor..9:
#   +1 when the world dominates a scene, a hostile clock ticks, the PC burns a day without advancing a goal,
#      or the Jeopardy Counter trips (subsystems.md).
#   -1 ONLY when the PC ends a scene in clear control or closes a major thread — never by default.
# The asymmetry (it rises easily, falls rarely) is what a losing year feels like. Engine bookkeeping
# (state.py chaos +1/-1) still applies; this file just sets the floor and the lean.

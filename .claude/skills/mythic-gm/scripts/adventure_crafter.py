#!/usr/bin/env python3
"""
adventure_crafter.py — generate Adventure Crafter content for the Mythic loop.
Honest dice here; Plot Point *text* is read from the bundled canon (the full
themed Plot Point Table lives in references/canon/The-Adventure-Crafter.md).

Commands:
  turning-point [--plotlines N] [--characters M] [--points K] [--existing]
        Generate a Turning Point: roll the Plotline, then K (2-5) Plot Points.
        --existing  = this Turning Point advances an existing Plotline (Plot Point 1
                      may be a Conclusion on 1-8).
  theme                Roll one Plot Point Theme slot (1d10 → priority)
"""
import json, os, random, sys

DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
def load(name): return json.load(open(os.path.join(DATA, name), encoding="utf-8"))
def d(n): return random.randint(1, n)
def lookup(entries, r):
    for e in entries:
        if e["min"] <= r <= e["max"]: return e["value"]

THEME_TBL = load("adventure_crafter/plot_point_theme.json")
THEMES = load("adventure_crafter/themes.json")["themes"]

def roll_plotline(n_plotlines):
    """1d100 on the Plotlines List (n entries). New/Choose results per Adventure Crafter."""
    if n_plotlines <= 0:
        return "NEW PLOTLINE (list empty → automatic)"
    r = d(100)
    # Faithful-enough: filled slots map proportionally across 1-100; tail = New / Choose Most Logical
    # Adventure Crafter lists are 25 lines; use slot logic.
    slot = d(25)
    if slot <= n_plotlines:
        return f"existing Plotline at slot {slot} (read from Plotlines List) [1d25={slot}]"
    elif slot <= n_plotlines + (25 - n_plotlines) // 2:
        return f"NEW PLOTLINE [1d25={slot}, blank]"
    else:
        return f"CHOOSE MOST LOGICAL PLOTLINE [1d25={slot}, blank]"

def theme_slot():
    r = d(10); return r, lookup(THEME_TBL["entries"], r)

def gen_turning_point(n_pl, n_ch, k, existing):
    print("════════ ADVENTURE CRAFTER — TURNING POINT ════════")
    print("Plotline:", roll_plotline(n_pl))
    print(f"(Theme priority order assumed set for this adventure: {', '.join(THEMES)} — adjust to your priority.)")
    k = max(2, min(5, k))
    print(f"\nRolling {k} Plot Points (3d10 each: theme die + 1d100):")
    nones = 0
    for i in range(1, k + 1):
        tr, prio = theme_slot()       # which priority theme
        pp = d(100)                   # the plot point under that theme column
        # First Plot Point of an existing-Plotline advancement can be a Conclusion (1-8)
        if i == 1 and existing and pp <= 8:
            print(f"  Plot Point {i}: theme die 1d10={tr} ({prio}); 1d100={pp} → ** CONCLUSION ** "
                  f"(this Turning Point ends the Plotline)")
            continue
        # 'None' results exist on the table; we flag the roll and let canon lookup decide
        print(f"  Plot Point {i}: theme die 1d10={tr} ({prio}); 1d100={pp} → read Plot Point {pp} "
              f"under the {prio} theme column in canon (may be 'None').")
    print("\n↳ Invoke Characters where a Plot Point requires (oracle.py list characters <filled>).")
    print("↳ Add Invoked Threads/Characters to the Lists NOW (during generation), weighted up to 3.")
    print("[src ac.plot_point_table via references/canon/The-Adventure-Crafter.md]")

def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h","--help"): print(__doc__); return
    def opt(f, dv): return type(dv)(a[a.index(f)+1]) if f in a else dv
    if a[0] == "theme":
        r, p = theme_slot(); print(f"🎭 Plot Point Theme: 1d10={r} → {p}")
    elif a[0] == "turning-point":
        gen_turning_point(opt("--plotlines",0), opt("--characters",0),
                          opt("--points",5), "--existing" in a)
    else:
        sys.exit(f"Unknown command '{a[0]}'. See --help.")

if __name__ == "__main__":
    main()

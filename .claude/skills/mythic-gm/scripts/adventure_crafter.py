#!/usr/bin/env python3
"""
adventure_crafter.py — Adventure Crafter generation for the Mythic loop. Honest
dice here; Plot Point *titles* are read from bundled canon (the full themed Plot
Point Table). Mechanical structure (Conclusion / None / Meta) is hard-coded.

Commands:
  themes [--style action|horror|mystery|intrigue|drama|balanced]
        Roll the adventure's 5 Theme priorities (1st..5th), weighted by RPG style.
  theme [--style ...]                Roll a single Theme (style-weighted)
  turning-point [--plotlines N] [--characters M] [--points K] [--existing]
        Generate a Turning Point: roll the Plotline, then K (2-5) Plot Points,
        applying the hard-coded structure and invoking Characters as needed.
"""
import json, os, random, sys

DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
def load(name): return json.load(open(os.path.join(DATA, name), encoding="utf-8"))
def d(n): return random.randint(1, n)
def lookup(entries, r):
    for e in entries:
        if e["min"] <= r <= e["max"]: return e["value"]

THEME_TBL = load("adventure_crafter/plot_point_theme.json")
THEMES_DEF = load("adventure_crafter/themes.json")
STRUCT = load("adventure_crafter/plot_point_structure.json")["universal"]

def weighted_theme_order(style):
    w = dict(THEMES_DEF["style_weights"].get(style, THEMES_DEF["style_weights"]["balanced"]))
    order = []
    pool = list(w.items())
    while pool:
        total = sum(x[1] for x in pool); r = random.uniform(0, total); acc = 0
        for i, (t, wt) in enumerate(pool):
            acc += wt
            if r <= acc:
                order.append(t); pool.pop(i); break
    return order

def cmd_themes(style):
    order = weighted_theme_order(style)
    print(f"🎭 ADVENTURE THEMES (style: {style}) — priority order:")
    for i, t in enumerate(order, 1):
        print(f"   {i}. {t}")
    print("   [src ac.themes; style-weighted]   Record these as this adventure's Theme priorities.")

def cmd_theme(style):
    order = weighted_theme_order(style); print(f"🎭 Theme (style {style}): {order[0]}")

def roll_plotline(n):
    if n <= 0: return "NEW PLOTLINE (Plotlines List empty → automatic)"
    r = d(25)  # crafter mode: full 25-line list
    if r <= n: return f"existing Plotline at slot {r} (1d25={r}) — read it off the Plotlines List"
    # blank line → New / Choose Most Logical (Adventure Crafter result)
    return f"BLANK (1d25={r} > {n}) → NEW PLOTLINE or CHOOSE MOST LOGICAL PLOTLINE"

def theme_slot():
    r = d(10); return r, lookup(THEME_TBL["entries"], r)

PRIORITY_IDX = {"First Priority":0,"Second Priority":1,"Third Priority":2,
                "Fourth Priority (cycle to Fifth)":3}
def plot_point(theme, existing, first):
    """Roll 1d100 on the hard-coded per-theme Plot Point table; honor structure."""
    t = load(f"adventure_crafter/plot_points_{theme.lower()}.json")
    pp = d(100); val = lookup(t["entries"], pp)
    if pp <= 8 and not (first and existing):
        # Conclusion only triggers on the first Plot Point of an existing-Plotline advancement
        val = "None (Conclusion only applies to Plot Point 1 of an existing Plotline)"
    return pp, val

def gen_turning_point(n_pl, n_ch, k, existing, order):
    print("════════ ADVENTURE CRAFTER — TURNING POINT ════════")
    print(f"Theme priority: {', '.join(order)}")
    print("Plotline:", roll_plotline(n_pl))
    k = max(2, min(5, k))
    print(f"\nRolling {k} Plot Points (3d10: Theme die → priority → theme; 1d100 on that theme's table):")
    for i in range(1, k + 1):
        tr, prio = theme_slot()
        idx = PRIORITY_IDX.get(prio, 3)
        if prio.startswith("Fourth"):  # 10 cycles Fourth→Fifth across the turning point
            idx = 3 if i % 2 else 4
        theme = order[idx % len(order)]
        pp, val = plot_point(theme, existing, first=(i == 1))
        print(f"  Plot Point {i}: theme 1d10={tr} ({prio} → {theme}); 1d100={pp} → {val}")
    print("\n↳ Invoke Characters where a Plot Point requires:  python3 scripts/oracle.py list "
          f"{n_ch} --new   (a New result → python3 scripts/oracle.py character)")
    print("↳ Add Invoked Threads/Characters to the Lists NOW (during generation), weighted ≤3.")
    print("[src ac.plot_points.<theme> — fully hard-coded]")

def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h","--help"): print(__doc__); return
    def opt(f, dv): return type(dv)(a[a.index(f)+1]) if f in a else dv
    style = opt("--style", "balanced")
    if a[0] == "themes": cmd_themes(style)
    elif a[0] == "theme": cmd_theme(style)
    elif a[0] == "turning-point":
        order = (a[a.index("--themes")+1].split(",") if "--themes" in a else THEMES_DEF["themes"])
        gen_turning_point(opt("--plotlines", 0), opt("--characters", 0), opt("--points", 5),
                          "--existing" in a, [t.strip().capitalize() for t in order])
    else: sys.exit(f"Unknown command '{a[0]}'. See --help.")

if __name__ == "__main__":
    main()

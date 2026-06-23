#!/usr/bin/env python3
"""
oracle.py — Mythic event/meaning oracle. ALL rolls honest, shown, and cited.
The full Random Event chain (Focus → List invoke → Meaning) is hard-coded here.

Commands:
  event [--threads N] [--characters M] [--crafter]
        FULL Random Event: roll Event Focus → (auto-roll the right List if the focus
        invokes one) → roll a Meaning pair → print the assembled prompt to interpret.
        --crafter routes an Interrupt to an Adventure Crafter Turning Point instead.
  event-focus                 Just the Event Focus roll (1d100)
  meaning <table>             One Meaning Table (1d100): actions_1|actions_2|descriptors_1|descriptors_2
  pair actions|descriptors    Both columns → a word pair (the usual oracle)
  elements "<Table Name>"     Honest 1d100 for an Elements table; reads the row from JSON if
                              hard-coded, else from bundled canon (one indexed lookup)
  list <filled> [--new]       Weighted List invoke (1d25 over the 25-line List). Blank line →
                              Choose Most Logical (or, with --new, Add New Thread/Character)
  character [--threads N] [--characters M]
                              Adventure Crafter Character Crafter: Special Trait + Identity + Descriptors
  answer <table> <yes|no|exc_yes|exc_no|random_event>
"""
import glob, json, os, random, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
def load(name): return json.load(open(os.path.join(DATA, name), encoding="utf-8"))
def has(name): return os.path.exists(os.path.join(DATA, name))
def d(n): return random.randint(1, n)
def lookup(entries, r):
    for e in entries:
        if e["min"] <= r <= e["max"]: return e["value"]

# ---- Event Focus → how to resolve (the combined-use routing, hard-coded) ----
# list: 'characters' | 'threads' | None ; new: generate a new Character ; note: extra step
FOCUS_ROUTING = {
    "Remote Event":        {"list": None,         "note": "an event elsewhere; PC not directly involved yet"},
    "Ambiguous Event":     {"list": None,         "note": "neither clearly good nor bad — an opening to explore"},
    "New NPC":             {"list": None, "new": True, "note": "introduce/generate a new Character (Character Crafter)"},
    "NPC Action":          {"list": "characters", "note": "the invoked Character takes an action"},
    "NPC Negative":        {"list": "characters", "note": "something negative happens to/around the invoked Character"},
    "NPC Positive":        {"list": "characters", "note": "something positive happens to/around the invoked Character"},
    "Move Toward A Thread":{"list": "threads",    "note": "progress toward the invoked Thread"},
    "Move Away From A Thread":{"list": "threads", "note": "a setback on the invoked Thread"},
    "Close A Thread":      {"list": "threads",    "note": "the invoked Thread concludes (Plotline Conclusion)"},
    "PC Negative":         {"list": None,         "note": "something negative happens to the PC"},
    "PC Positive":         {"list": None,         "note": "something positive happens to the PC"},
    "Current Context":     {"list": None,         "note": "about the current situation"},
}

def roll_list(filled, allow_new=False, mode="mythic"):
    """Invoke on the 25-line List. Weighted naturally (repeats occupy more slots).
    mode 'mythic' (Random Events): die scales to fullness → fewer blanks.
    mode 'crafter' (Plot-Point invoke): always 1d25 → blanks (New/Choose) more likely.
    Returns (text, is_blank)."""
    filled = int(filled)
    if filled <= 0:
        return ("List empty → use Current Context (no roll)", True)
    sides = 25 if mode == "crafter" else (10 if filled <= 10 else 20 if filled <= 20 else 25)
    r = d(sides)
    if r <= filled:
        return (f"slot {r} (1d{sides}={r}) → read that entry off the List", False)
    opt = "Choose Most Logical, or Add a New element" if allow_new else "Choose Most Logical, or roll again"
    return (f"BLANK line (1d{sides}={r} > {filled} filled) → {opt}", True)

def cmd_event_focus(_print=True):
    t = load("mythic/event_focus.json"); r = d(100); v = lookup(t["entries"], r)
    if _print: print(f"🎯 EVENT FOCUS  1d100={r} → {v}   [src mythic.event_focus]")
    return v, r

def cmd_pair(which, _print=True):
    cols = {"actions": ("actions_1","actions_2"), "descriptors": ("descriptors_1","descriptors_2")}[which]
    out = []
    for c in cols:
        t = load(f"mythic/meaning_{c}.json"); r = d(100); out.append((lookup(t["entries"], r), r))
    if _print:
        print(f"📖 MEANING PAIR ({which}): " + "  ·  ".join(f"{w} (d100={r})" for w, r in out))
    return out

def cmd_event(threads=0, characters=0, crafter=False):
    print("⚡ RANDOM EVENT")
    focus, fr = cmd_event_focus()
    route = FOCUS_ROUTING.get(focus, {"list": None, "note": ""})
    print(f"   Focus: {focus} — {route['note']}")
    if crafter:
        print("   (Crafter mode: an Interrupt is built as a Turning Point — run "
              "adventure_crafter.py turning-point instead of a plain event.)")
    if route.get("new"):
        print("   → generate a new Character:  python3 scripts/oracle.py character "
              f"--threads {threads} --characters {characters}")
    elif route["list"] == "characters":
        text, blank = roll_list(characters, allow_new=True)
        print(f"   Characters List invoke → {text}")
    elif route["list"] == "threads":
        text, blank = roll_list(threads, allow_new=True)
        print(f"   Threads List invoke → {text}")
    pair = cmd_pair("actions")
    print(f"   Meaning (actions): {pair[0][0]}  ·  {pair[1][0]}")
    print("   → interpret Focus + invoked element + word pair into the Event. "
          "Add any new Thread/Character to the Lists (weight ≤3).")

def cmd_meaning(table):
    t = load(f"mythic/meaning_{table}.json"); r = d(100)
    print(f"📖 {t['title']}  1d100={r} → {lookup(t['entries'], r)}   [src {t['id']}]")

def cmd_elements(name):
    slug = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")
    p = f"mythic/elements/{slug}.json"
    if not has(p):
        avail = sorted(os.path.basename(x)[:-5] for x in glob.glob(os.path.join(DATA, "mythic/elements/*.json"))
                       if not x.endswith("_index.json"))
        sys.exit(f"No Elements table '{name}'. Available: {', '.join(avail)}")
    t = load(p); r = d(100)
    print(f"📖 Elements — {name}: 1d100={r} → {lookup(t['entries'], r)}   [src {t['id']}]")

def cmd_list(filled, allow_new=False):
    text, _ = roll_list(filled, allow_new)
    print(f"📃 LIST invoke → {text}")

def cmd_character(threads=0, characters=0):
    print("🧬 CHARACTER CRAFTER (Adventure Crafter)")
    st = load("adventure_crafter/character_special_trait.json"); r = d(100)
    print(f"   Special Trait: 1d100={r} → {lookup(st['entries'], r)}   [src ac.character_special_trait]")
    # Identity & Descriptors — hard-coded Mythic Element tables
    for label, slug in [("Identity","character_identity"),("Descriptors","character_descriptors")]:
        t = load(f"mythic/elements/{slug}.json"); rr = d(100)
        print(f"   {label}: 1d100={rr} → {lookup(t['entries'], rr)}   [src {t['id']}]")
    print("   → name the Character, add to the Characters List (weight ≤3).")

def cmd_answer(table, key):
    t = load(f"mythic/{table}.json"); v = t.get("answers", {}).get(key)
    if v is None: sys.exit(f"No answer '{key}' in {table}: keys {list(t.get('answers',{}))}")
    print(f"📐 {t['title']} [{key}]: {v}   [src {t['id']}]")

def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h","--help"): print(__doc__); return
    def opt(f, dv=0): return int(a[a.index(f)+1]) if f in a else dv
    c = a[0]
    try:
        if c == "event": cmd_event(opt("--threads"), opt("--characters"), "--crafter" in a)
        elif c == "event-focus": cmd_event_focus()
        elif c == "meaning": cmd_meaning(a[1])
        elif c == "pair": cmd_pair(a[1])
        elif c == "elements": cmd_elements(a[1])
        elif c == "list": cmd_list(a[1], "--new" in a)
        elif c == "character": cmd_character(opt("--threads"), opt("--characters"))
        elif c == "answer": cmd_answer(a[1], a[2])
        else: sys.exit(f"Unknown command '{c}'. See --help.")
    except IndexError:
        sys.exit("Missing argument. See --help.")

if __name__ == "__main__":
    main()

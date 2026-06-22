#!/usr/bin/env python3
"""
oracle.py — Mythic event/meaning oracle. All rolls honest and cited.

Commands:
  event-focus                 Roll the Random Event Focus Table (1d100)
  meaning <table>             Roll one Meaning Table (1d100): actions_1|actions_2|
                              descriptors_1|descriptors_2
  pair actions|descriptors    Roll BOTH columns → a word pair (the usual oracle)
  elements "<Table Name>"     Honest 1d100 for an Elements table not in JSON; prints
                              the index to read from the bundled canon (45 Elements tables)
  list <filled> [slots]       Weighted List roll (Threads/Characters). filled = entries
                              present; returns the slot rolled (blank = New/Choose)
  answer <table> <yes|no|exc_yes|exc_no|random_event>   Look up an answer-keyed table
"""
import json, os, random, sys

DATA = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data")
def load(name): return json.load(open(os.path.join(DATA, name), encoding="utf-8"))
def d(n): return random.randint(1, n)

def lookup(entries, roll):
    for e in entries:
        if e["min"] <= roll <= e["max"]: return e["value"]
    return None

def cmd_event_focus():
    t = load("mythic/event_focus.json"); r = d(100); v = lookup(t["entries"], r)
    print(f"🎯 EVENT FOCUS  1d100 = {r} → {v}   [src mythic.event_focus]")
    hints = {"NPC Action":"roll on the Characters List","Move Toward A Thread":"roll on the Threads List",
             "Move Away From A Thread":"roll on the Threads List","Close A Thread":"roll on the Threads List",
             "NPC Negative":"roll on the Characters List","NPC Positive":"roll on the Characters List",
             "New NPC":"introduce/generate a new Character"}
    if v in hints: print(f"   ↳ then {hints[v]}, then roll a Meaning pair to interpret.")
    else: print("   ↳ then roll a Meaning pair (oracle.py pair actions) to interpret.")

def cmd_meaning(table):
    t = load(f"mythic/meaning_{table}.json"); r = d(100); v = lookup(t["entries"], r)
    print(f"📖 {t['title']}  1d100 = {r} → {v}   [src {t['id']}]")

def cmd_pair(which):
    cols = {"actions":("actions_1","actions_2"), "descriptors":("descriptors_1","descriptors_2")}[which]
    words = []
    for c in cols:
        t = load(f"mythic/meaning_{c}.json"); r = d(100); v = lookup(t["entries"], r); words.append((r, v))
    print(f"📖 MEANING PAIR ({which}): " + "  ·  ".join(f"{w} (d100={r})" for r, w in words))
    print(f"   → interpret the pair in context.   [src mythic.meaning.{which}]")

def cmd_elements(name):
    r = d(100)
    print(f"📖 ELEMENTS — {name}: honest 1d100 = {r}")
    print(f"   ↳ read entry {r} from the '{name}' Elements Meaning Table in "
          f"references/canon/Mythic-GME.md (one indexed lookup; dice already rolled).")

def cmd_list(filled, slots=25):
    """Mythic weighted list: lists hold up to `slots` lines. Roll to pick a line;
    lines beyond `filled` are blank (→ Choose, or New for an Adventure-Crafter invoke)."""
    filled = int(filled)
    if filled <= 0:
        print("📃 LIST is empty → use Current Context as the focus (no roll)."); return
    # Mythic 2e: roll across the filled portion proportionally (simple, faithful enough)
    r = d(slots)
    if r <= filled:
        print(f"📃 LIST roll 1d{slots} = {r} → slot {r} (an existing entry; read it off the List).")
    else:
        print(f"📃 LIST roll 1d{slots} = {r} → BLANK line. Option: Choose an existing entry, "
              f"or (Adventure-Crafter invoke) Add a New Thread/Character.")

def cmd_answer(table, key):
    t = load(f"mythic/{table}.json")
    v = t.get("answers", {}).get(key)
    if v is None: sys.exit(f"No answer '{key}' in {table}. Keys: {list(t.get('answers',{}))}")
    print(f"📐 {t['title']} [{key}]: {v}   [src {t['id']}]")

def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h","--help"): print(__doc__); return
    try:
        c = a[0]
        if c == "event-focus": cmd_event_focus()
        elif c == "meaning": cmd_meaning(a[1])
        elif c == "pair": cmd_pair(a[1])
        elif c == "elements": cmd_elements(a[1])
        elif c == "list": cmd_list(a[1], int(a[2]) if len(a) > 2 else 25)
        elif c == "answer": cmd_answer(a[1], a[2])
        else: sys.exit(f"Unknown command '{c}'. See --help.")
    except IndexError:
        sys.exit("Missing argument. See --help.")

if __name__ == "__main__":
    main()

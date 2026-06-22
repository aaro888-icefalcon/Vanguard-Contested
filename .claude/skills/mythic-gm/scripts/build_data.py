#!/usr/bin/env python3
"""
build_data.py — derive verified, machine-rollable JSON tables from the bundled
canon Markdown (references/canon/*.md). Single source of truth = the Markdown;
this emits data/**/*.json + manifest.json and runs a verification gate.

Run:  python3 scripts/build_data.py
"""
import json, os, re, sys, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CANON = os.path.join(ROOT, "references", "canon")
DATA = os.path.join(ROOT, "data")
MYTHIC = open(os.path.join(CANON, "Mythic-GME.md"), encoding="utf-8").read()
AC = open(os.path.join(CANON, "The-Adventure-Crafter.md"), encoding="utf-8").read()

errors, warnings, built = [], [], []
def err(m): errors.append(m)
def warn(m): warnings.append(m)
def sha(s): return "sha256:" + hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]

def write(relpath, obj):
    p = os.path.join(DATA, relpath)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(obj, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    built.append(relpath)

def lines_of(text): return text.split("\n")

# ---------------------------------------------------------------- Fate Chart
ODDS = ["Certain","Nearly Certain","Very Likely","Likely","50/50",
        "Unlikely","Very Unlikely","Nearly Impossible","Impossible"]
def parse_fate_chart():
    L = lines_of(MYTHIC)
    # find the FATE CHART code block (the one followed by Certain ... CHAOS FACTOR)
    grid = {}
    for i, ln in enumerate(L):
        if ln.strip() == "FATE CHART" and i+1 < len(L) and L[i+1].strip().startswith("Certain"):
            for label in ODDS:
                row = next((r for r in L[i:i+14] if r.strip().startswith(label+" ")
                            and re.search(r"\d", r)), None)
                if not row:
                    err(f"fate_chart: missing row {label}"); continue
                toks = row.strip()[len(label):].split()
                vals = [0 if t.upper()=="X" else int(t) for t in toks]
                if len(vals) != 27:
                    err(f"fate_chart: row {label} had {len(vals)} values (want 27)"); continue
                cells = []
                for c in range(9):
                    a,b,cc = vals[c*3:c*3+3]
                    # a=ExcYes ceil, b=Yes ceil, cc=ExcNo floor (0 sentinel -> none)
                    cells.append({"exc_yes_max": a, "yes_max": b,
                                  "exc_no_min": cc if cc else 101})
                grid[label] = cells
            break
    if len(grid) == 9:
        write("mythic/fate_chart.json", {
            "id":"mythic.fate_chart","title":"Fate Chart","type":"grid_fate_chart",
            "dice":"1d100","source":"references/canon/Mythic-GME.md#fate-chart",
            "odds":ODDS,"chaos_factor":list(range(1,10)),"grid":grid,
            "answer_rule":"r<=exc_yes_max:Exceptional Yes; r<=yes_max:Yes; r>=exc_no_min:Exceptional No; else No",
            "checksum":sha(str(grid))})
    return grid

# ------------------------------------------------ generic code-block range table
def parse_range_block(text, title, dice):
    """Parse a code block of 'lo-hi  Result' or 'lo  Result' lines."""
    L = lines_of(text)
    for i, ln in enumerate(L):
        if ln.strip() == title:
            entries = []
            for r in L[i+1:i+40]:
                if r.strip() in ("```","") or r.strip().startswith("1d") or "RESULT" in r.upper():
                    if entries and (r.strip()=="```"): break
                    continue
                m = re.match(r"^\s*(\d+)\s*[-–]\s*(\d+)\s+(.+?)\s*$", r) or \
                    re.match(r"^\s*(\d+)\s+([A-Za-z].+?)\s*$", r)
                if not m:
                    if entries: break
                    continue
                if m.lastindex == 3:
                    entries.append({"min":int(m.group(1)),"max":int(m.group(2)),"value":m.group(3).strip()})
                else:
                    entries.append({"min":int(m.group(1)),"max":int(m.group(1)),"value":m.group(2).strip()})
            return entries
    return None

def build_event_focus():
    e = parse_range_block(MYTHIC, "RANDOM EVENT FOCUS TABLE", "1d100")
    if not e: err("event_focus: not parsed"); return
    cov = sum(x["max"]-x["min"]+1 for x in e)
    if cov != 100: err(f"event_focus: coverage {cov}/100")
    write("mythic/event_focus.json", {"id":"mythic.event_focus","title":"Random Event Focus Table",
        "type":"list_d100","dice":"1d100","source":"references/canon/Mythic-GME.md#random-event-focus-table",
        "entries":e,"checksum":sha(str(e))})

def build_scene_adjustment():
    e = parse_range_block(MYTHIC, "SCENE ADJUSTMENT TABLE", "1d10")
    if not e: err("scene_adjustment: not parsed"); return
    cov = sum(x["max"]-x["min"]+1 for x in e)
    if cov != 10: err(f"scene_adjustment: coverage {cov}/10")
    write("mythic/scene_adjustment.json", {"id":"mythic.scene_adjustment","title":"Scene Adjustment Table",
        "type":"list_d10","dice":"1d10","source":"references/canon/Mythic-GME.md#scene-adjustment-table",
        "entries":e,"checksum":sha(str(e))})

# ------------------------------------------------------- Meaning tables (pipe)
def parse_meaning(name, start_line, source_anchor):
    """Collect **N:** word pairs from pipe rows after a header line index until 100 found."""
    L = lines_of(MYTHIC)
    pairs = {}
    for r in L[start_line: start_line+30]:
        if "|" not in r:
            if pairs: break
            continue
        flat = r.replace("|", " ")
        for m in re.finditer(r"\*\*(\d+):\*\*\s*([A-Za-z][A-Za-z /'\-]*)", flat):
            n = int(m.group(1)); w = m.group(2).strip()
            if 1 <= n <= 100 and w: pairs.setdefault(n, w)
    if len(pairs) != 100:
        warn(f"meaning {name}: parsed {len(pairs)}/100 entries")
    entries = [{"min":n,"max":n,"value":pairs[n]} for n in sorted(pairs)]
    write(f"mythic/meaning_{name}.json", {"id":f"mythic.meaning.{name}","title":f"Meaning Tables — {name}",
        "type":"list_d100","dice":"1d100","source":f"references/canon/Mythic-GME.md#{source_anchor}",
        "entries":entries,"complete":len(pairs)==100,"checksum":sha(str(entries))})
    return len(pairs)

# header line numbers (0-indexed) confirmed from canon
MEANING_BLOCKS = {"actions_1":1458,"actions_2":1478,"descriptors_1":1504,"descriptors_2":1525}

# ----------------------------------------- small hand-verified structured tables
def build_static():
    # Fate Check (2d10 + modifiers)
    write("mythic/fate_check.json", {"id":"mythic.fate_check","title":"Fate Check (2d10)",
        "type":"modifier_lookup","dice":"2d10","source":"references/canon/Mythic-GME.md#the-fate-check",
        "odds_mod":{"Certain":5,"Nearly Certain":4,"Very Likely":2,"Likely":1,"50/50":0,
                    "Unlikely":-1,"Very Unlikely":-2,"Nearly Impossible":-4,"Impossible":-5},
        "cf_mod":{"9":5,"8":4,"7":2,"6":1,"5":0,"4":-1,"3":-2,"2":-4,"1":-5},
        "answers":[{"min":18,"max":20,"value":"Exceptional Yes"},
                   {"min":11,"max":17,"value":"Yes"},
                   {"min":5,"max":10,"value":"No"},
                   {"min":2,"max":4,"value":"Exceptional No"}],
        "answer_rule":"sum 2d10 + odds_mod + cf_mod; >=18:Exceptional Yes; >=11:Yes; 5-10:No(<=10); 2-4:Exceptional No"})
    # answer-keyed tables
    write("mythic/npc_behavior.json", {"id":"mythic.npc_behavior","title":"NPC Behavior Table",
        "type":"answer_keyed","source":"references/canon/Mythic-GME.md#npc-behavior-table",
        "answers":{"yes":"The NPC does what you expect, or continues their ongoing action.",
            "no":"The NPC does the next most expected behavior. If unsure, roll a Meaning Table.",
            "exc_yes":"The NPC does the expected/ongoing action with greater intensity.",
            "exc_no":"The NPC does the opposite of what you expected, or the next-expected behavior intensified. If unsure, roll a Meaning Table and intensify.",
            "random_event":"Roll a Meaning Table for an additional action from the NPC."}})
    write("mythic/npc_statistics.json", {"id":"mythic.npc_statistics","title":"NPC Statistics Table",
        "type":"answer_keyed","source":"references/canon/Mythic-GME.md#npc-statistics-table",
        "answers":{"yes":"The value is what you expect.","exc_yes":"About 25% higher than expected.",
            "no":"About 25% lower than expected.","exc_no":"About 50% lower than expected.",
            "random_event":"Generate a Random Event as a special condition tied to this statistic."}})
    write("mythic/discovery_fate_question.json", {"id":"mythic.discovery_fate_question",
        "title":"Discovery Fate Question","type":"answer_keyed",
        "source":"references/canon/Mythic-GME.md#discovery-fate-question",
        "answers":{"yes":"Roll on the Thread Discovery Check Table.","no":"Nothing useful is found.",
            "exc_yes":"Roll twice on the Thread Discovery Check Table, combining results.",
            "exc_no":"Nothing found; you cannot make another Discovery Check for the rest of this Scene."}})
    # Scene Test (mode-aware) is logic, but store the canonical mapping for transparency
    write("mythic/scene_test.json", {"id":"mythic.scene_test","title":"Testing the Expected Scene",
        "type":"logic","dice":"1d10","source":"references/canon/Mythic-GME.md#testing-the-expected-scene",
        "rule":{"over_cf":"Expected Scene","within_cf_odd":"Altered Scene","within_cf_even":"Interrupt Scene"}})
    # Adventure Crafter — Plot Point Theme Table (1d10 -> priority slot)
    write("adventure_crafter/plot_point_theme.json", {"id":"ac.plot_point_theme",
        "title":"Plot Point Theme Table","type":"list_d10","dice":"1d10",
        "source":"references/canon/The-Adventure-Crafter.md#plot-point-theme-table",
        "entries":[{"min":1,"max":4,"value":"First Priority"},{"min":5,"max":7,"value":"Second Priority"},
                   {"min":8,"max":9,"value":"Third Priority"},{"min":10,"max":10,"value":"Fourth Priority (then cycle to Fifth)"}]})
    write("adventure_crafter/themes.json", {"id":"ac.themes","title":"Adventure Crafter Themes",
        "type":"reference","source":"references/canon/The-Adventure-Crafter.md#themes",
        "themes":["Action","Tension","Mystery","Social","Personal"],
        "theme_translation":{"Action":"Action","Horror":"Tension","Mystery":"Mystery",
                             "Social":"Social","Personal":"Personal","Tension":"Tension"}})

# ---------------------------------------------------------------- verification
def verify(fate, mcounts):
    # spot checks
    try:
        if fate["50/50"][4] != {"exc_yes_max":10,"yes_max":50,"exc_no_min":91}:
            err(f"SPOT fate 50/50@CF5 = {fate['50/50'][4]} (want 10/50/91)")
    except Exception as e: err(f"SPOT fate_chart: {e}")
    # event focus spot
    try:
        ef = json.load(open(os.path.join(DATA,"mythic/event_focus.json")))
        hit = next((x for x in ef["entries"] if x["min"]==21), None)
        if not hit or "NPC Action" not in hit["value"]: err(f"SPOT event_focus 21-: {hit}")
    except Exception as e: err(f"SPOT event_focus: {e}")
    # meaning spot
    try:
        a1 = json.load(open(os.path.join(DATA,"mythic/meaning_actions_1.json")))
        if a1["entries"][0]["value"] != "Abandon": err(f"SPOT actions_1 #1 = {a1['entries'][0]}")
    except Exception as e: err(f"SPOT actions_1: {e}")

def main():
    fate = parse_fate_chart()
    build_event_focus(); build_scene_adjustment(); build_static()
    mcounts = {}
    for name, ln in MEANING_BLOCKS.items():
        mcounts[name] = parse_meaning(name, ln, name.replace("_","-"))
    # manifest
    manifest = {"tables_built": sorted(built),
                "meaning_entry_counts": mcounts,
                "canon": {"mythic": sha(MYTHIC), "adventure_crafter": sha(AC)},
                "note": "Long-tail Elements & full Plot Point tables fall back to bundled canon via oracle.py --from-canon."}
    json.dump(manifest, open(os.path.join(DATA,"manifest.json"),"w"), indent=1)
    verify(fate, mcounts)
    print(f"BUILT {len(built)} tables:")
    for b in built: print("  -", b)
    print("meaning counts:", mcounts)
    if warnings:
        print("\nWARNINGS:"); [print("  !", w) for w in warnings]
    if errors:
        print("\nERRORS:"); [print("  X", e) for e in errors]
        sys.exit(1)
    print("\nVERIFICATION PASSED ✓")

if __name__ == "__main__":
    main()

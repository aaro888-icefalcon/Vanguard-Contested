#!/usr/bin/env python3
"""
bridge.py — discover / validate / summarize a companion bridge.

A bridge is a folder with a bridge.md manifest (containing a fenced ```json block)
that declares which engine hooks the companion overrides and where its files are.
The engine reads the manifest at load and uses an override where present, else the
Mythic/AC default.

Commands:
  summary <bridge_dir>     Print overrides-vs-defaults for the 9 hooks
  validate <bridge_dir>    Check the manifest + that declared files exist; roll-test tables
  manifest <bridge_dir>    Print the parsed JSON manifest
"""
import json, os, re, sys, glob

HOOKS = ["resolve","generate:character","generate:element","meaning","chaos",
         "themes","world-tick","seeds","adventure-ingest"]

def read_manifest(bdir):
    p = os.path.join(bdir, "bridge.md")
    if not os.path.exists(p): sys.exit(f"No bridge.md in {bdir}")
    txt = open(p, encoding="utf-8").read()
    m = re.search(r"```json\s*(\{.*?\})\s*```", txt, re.DOTALL)
    if not m: sys.exit("bridge.md has no ```json manifest block")
    try: return json.loads(m.group(1))
    except Exception as e: sys.exit(f"manifest JSON error: {e}")

def cmd_summary(bdir):
    man = read_manifest(bdir); ov = set(man.get("overrides", []))
    print(f"Companion: {man.get('companion','?')}   engine: {man.get('engine','?')}")
    for h in HOOKS:
        hit = h in ov or any(o.startswith("generate:") for o in ov) if h.startswith("generate:") else h in ov
        print(f"  {'OVERRIDE' if h in ov else 'default ':8}  {h}")

def cmd_validate(bdir):
    man = read_manifest(bdir); problems = []
    for key, rel in man.get("files", {}).items():
        if not os.path.exists(os.path.join(bdir, rel)):
            problems.append(f"missing file '{rel}' (declared as {key})")
    for h in man.get("overrides", []):
        if h not in HOOKS and not h.startswith("generate:"):
            problems.append(f"unknown hook '{h}'")
    # roll-test any generator tables
    tested = 0
    for f in glob.glob(os.path.join(bdir, "generators", "*.json")):
        try:
            t = json.load(open(f))
            if t.get("type","").startswith("list_"):
                cov = sum(e["max"]-e["min"]+1 for e in t["entries"])
                need = 100 if t["type"]=="list_d100" else 10
                if cov != need: problems.append(f"{os.path.basename(f)}: coverage {cov}/{need}")
                tested += 1
        except Exception as e:
            problems.append(f"{os.path.basename(f)}: {e}")
    if problems:
        print("INVALID:"); [print("  X", p) for p in problems]; sys.exit(1)
    print(f"Bridge valid ✓  ({len(man.get('overrides',[]))} overrides, {tested} generator tables roll-tested)")

def cmd_manifest(bdir):
    print(json.dumps(read_manifest(bdir), indent=2))

def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h","--help"): print(__doc__); return
    if len(a) < 2: sys.exit("Need a bridge directory.")
    {"summary":cmd_summary,"validate":cmd_validate,"manifest":cmd_manifest}.get(
        a[0], lambda d: sys.exit(f"Unknown command '{a[0]}'"))(a[1])

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
state.py — campaign-state.md helpers. The state file is human-readable Markdown
and IS the source of truth; Claude edits it directly. These helpers enforce the
few rules that must be mechanical.

Commands:
  init <campaign_dir>          Copy the state template into a campaign folder
  chaos <+1|-1> <current>      Apply a clamped Chaos Factor change (1..9)
  validate <statefile>         Check the required sections are present
"""
import os, re, sys, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE = os.path.join(ROOT, "assets", "templates", "campaign-state.md")
REQUIRED = ["Chaos Factor", "Threads List", "Characters List", "Adventure Source",
            "Discipline", "Scene"]

def cmd_init(dirpath):
    os.makedirs(dirpath, exist_ok=True)
    dst = os.path.join(dirpath, "campaign-state.md")
    if os.path.exists(dst): sys.exit(f"{dst} already exists — refusing to overwrite.")
    shutil.copy(TEMPLATE, dst); print(f"Initialised {dst}")

def cmd_chaos(delta, current):
    cur = int(current); dv = int(delta)
    new = max(1, min(9, cur + dv))
    note = "" if new != cur else "  (clamped — no change)"
    print(f"Chaos Factor {cur} {dv:+d} → {new}{note}")

def cmd_validate(path):
    txt = open(path, encoding="utf-8").read()
    missing = [s for s in REQUIRED if s.lower() not in txt.lower()]
    cf = re.search(r"Chaos Factor[^0-9]*([1-9])", txt)
    if cf and not (1 <= int(cf.group(1)) <= 9): missing.append("Chaos Factor in range 1-9")
    if missing:
        print("INVALID — missing/!ok:", ", ".join(missing)); sys.exit(1)
    print("State valid ✓  (Chaos Factor = %s)" % (cf.group(1) if cf else "?"))

def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h","--help"): print(__doc__); return
    c = a[0]
    if c == "init": cmd_init(a[1])
    elif c == "chaos": cmd_chaos(a[1], a[2])
    elif c == "validate": cmd_validate(a[1])
    else: sys.exit(f"Unknown command '{c}'. See --help.")

if __name__ == "__main__":
    main()

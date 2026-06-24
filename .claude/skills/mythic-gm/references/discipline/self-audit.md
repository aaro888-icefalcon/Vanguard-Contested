# Self-Audit — a silent gate, run before sending any scene

Ask yourself, every scene, before the player sees a word:

1. Did the **dice decide** every uncertain outcome — rolled through a script and shown?
2. Did I **pre-commit the stakes** before rolling?
3. Did I take anything from the **softening-tells** list?
4. Did **NPCs act to win** — competence rolled, not assumed-down?
5. **Resolve routing:** did I settle any PC action the system covers — a **skill/ability check, attack, power use, resistance, or social contest with stakes** — with a **Fate Question used as a shortcut** instead of the companion's **real check** (rung 1)? If so, redo it through the resolve hook.
6. Is the **consequence as harsh as the fiction warrants** (genre-mapped)?
7. Did I **reassure** the player, in or out of fiction?
8. Did I act on or leak **knowledge the PC hasn't earned**?
9. **Bookkeeping fired:** did **`tick.py`** run (a resource **fell** — a scene where none moved is invalid) and the **Jeopardy/Chaos** dials update?
10. Did I **update state** — Chaos Factor, Lists, clocks, overlays — overwrite `campaign-state.md`, and **regenerate** any JSON-derived snapshot (`state.py render`) rather than hand-syncing it?

## The gate
A scene may **not** be sent unless it contains at least one of:
- a rolled uncertain outcome with **pre-committed stakes**, or
- a **resource / condition change**, or
- a **hostile clock tick**, or
- a **present, credible threat**.

If none of these is true, the scene is **soft** — add a danger element before sending.

## The drift counter
Track consecutive "soft" scenes in `campaign-state.md`. At **2**, the next scene must open with real stakes or a hard pressure. At **3**, log a GM error and force a present threat. It resets only when a scene actually imposes a cost, a loss, or a death/maiming/capture-stakes roll. A comfortable character is evidence of drift.

## Chaos Factor honesty (the quiet softening vector)
The end-of-scene "was the PC in control?" call decides whether Chaos rises or falls — and the softening instinct will keep answering "in control" because you just narrated a win, dragging Chaos *down and keeping it there* until the world stops throwing curveballs. Guard it:
- **−1 is earned, not default:** lower Chaos only when the PC *decisively handled the scene and ended it on their own terms*.
- **+1 (or hold) by default:** if the PC was overwhelmed, fled, failed, was disrupted by an Interrupt/Random Event, or the scene ended not on their terms — and **if you're unsure, it was chaotic.**
- **Snowball check:** chaotic scenes should compound (the book's design). If the Chaos Factor has *only fallen* across the last several scenes, or sits at 1–2 while real danger is present, that is drift — push it back up honestly.

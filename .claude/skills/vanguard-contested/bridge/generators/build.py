#!/usr/bin/env python3
"""
build.py — generate Vanguard Contested's companion generator tables as verified
list_d100 JSON for the mythic-gm engine.

The engine's dice.py table / bridge.py validate only understand list_d100 (1d100,
coverage must sum to 100) and list_d10 (1d10, sum 10). Vanguard's source tables
(refs 08/09/15) are native d8/d10/d12/d20/d100. This script re-scales every table
to a list_d100 with a contiguous partition of 1..100 via the largest-remainder
method, so uniform dN tables come out as near-uniform d100 weights (exact when
N divides 100, e.g. d20 -> 5 each). Weighted/explicit tables keep their canon ranges.

Run:  python3 build.py        (writes *.json next to this file)
Verify: python3 ../../../mythic-gm/scripts/bridge.py validate ..
Roll:  python3 ../../../mythic-gm/scripts/dice.py table <this-dir>/<name>.json
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

# ── helpers ──────────────────────────────────────────────────────────────────
def partition_100(weights):
    """Largest-remainder allocation of 100 across len(weights) buckets."""
    W = sum(weights)
    raw = [100 * w / W for w in weights]
    base = [int(x) for x in raw]
    deficit = 100 - sum(base)
    rema = sorted(range(len(weights)), key=lambda i: (-(raw[i] - base[i]), i))
    for i in rema[:deficit]:
        base[i] += 1
    return base

def entries_from_values(values, weights=None):
    weights = weights or [1] * len(values)
    sizes = partition_100(weights)
    out, lo = [], 1
    for v, s in zip(values, sizes):
        out.append({"min": lo, "max": lo + s - 1, "value": v})
        lo += s
    assert out[-1]["max"] == 100, "coverage != 100"
    return out

def write_table(name, title, entries):
    t = {"id": f"vanguard.{name}", "title": title, "type": "list_d100",
         "dice": "1d100", "entries": entries}
    with open(os.path.join(HERE, f"{name}.json"), "w", encoding="utf-8") as f:
        json.dump(t, f, ensure_ascii=False, indent=1)
    cov = sum(e["max"] - e["min"] + 1 for e in entries)
    assert cov == 100, f"{name}: coverage {cov}"
    return name

# ── UNIFORM dN tables (equal weight per entry; re-scaled to d100) ─────────────
UNIFORM = {
 # ref 08 — setting oracles
 "faction_move": ("Faction Move (what a faction does on its clock)", [
   "Consolidate territory","Raid a rival","Seize a resource (roll fuel/food/meds/arms/water)",
   "Recruit (the empowered / refugees / a rival's people)","Fortify","Negotiate or ally",
   "Betray an ally","Demand tribute","Purge internal dissent","Expand a clock toward completion",
   "Hunt a specific person","Spread propaganda/rumor","Open a supply line","Cut a rival's supply",
   "Take hostages","Retreat and regroup","Splinter (generate a new faction)",
   "Make an example (public violence)","Probe the PC's position","A bold stroke — a clock jumps two segments"]),
 "encounter_guarded": ("What Shows Up — Guarded band", [
   "refugees in need","a patrol/militia checkpoint","a scavenger crew","a lone Flicker/Spark in trouble",
   "a faction recruiter","a minor feral intrusion","a supply dispute","an informant with news",
   "a Compact envoy/ally","a sick or injured stranger","a thief","a quiet moment (gift it, then complicate)"]),
 "encounter_embattled": ("What Shows Up — Embattled band", [
   "a Reaver/raider probe","a feral pack","a rival empowered (Bruiser–Heavy)","a desperate mob",
   "a collapsing structure/hazard","a checkpoint shakedown","wounded who'll die without help",
   "a sniper/ambusher","a faction war-band passing through","a black-market deal gone wrong",
   "a fleeing column under attack","a crosser scouting element"]),
 "encounter_nomansland": ("What Shows Up — No-Man's-Land band", [
   "an ambush","a Warlord-tier threat (flee)","a sapient monster-lord's territory","an Empire/Reaver cohort",
   "a marine feral surge","a corpse-field and what made it","a predatory enclave","a trap/minefield/baited site",
   "a hunted survivor begging help","a rival after the same salvage","a feral horde on the move",
   "something worse than expected (roll twice, combine)"]),
 "crosser_bloc": ("Crosser Contact — bloc element", [
   "Empire vanguard","Reaver war-band","Warrior-Kingdom outriders","Corsair raiders",
   "a Pacific House (split loyalty)","Atlantic Concord observers","Interior Compact envoys",
   "a loyal-anchor patrol","a discordant-bloc fragment","refugees from a bloc","a defector/exile",
   "an unknown rift-arrival"]),
 "crosser_wants": ("Crosser Contact — what they want", [
   "territory","food/water","safe passage","to recruit you","information","a rival dealt with",
   "shelter from the swarm","medicine/aid","to test your strength","to trade","vengeance",
   "to flee something worse (the Unmaking's shadow)"]),
 "empowered_power": ("Manifested Power", [
   "enhanced strength","durability/armor","regeneration","a kinetic/force suite","flight","speed",
   "pyro/thermal","cryo","electrical (cruel post-EMP irony)","telekinesis","senses/perception",
   "stealth/invisibility","emotion/mind influence","healing (others)","matter shaping",
   "summoning/control of feral","toxin/disease","teleport (short)","a body-horror mutation",
   "something unclassified and frightening"]),
 "empowered_intent": ("Free Agent's Intent", [
   "protect their own","build a fief","prey/extort","flee/hide their nature","sell their power",
   "join a faction","revenge","zealotry/cult","collapse/can't control it","quietly decent, just surviving"]),
 "npc_role": ("NPC — role", [
   "ex-cop","Guard/soldier","doctor/nurse","mechanic/engineer","criminal/fixer","priest/imam/rabbi",
   "union/worker","refugee parent","child","hoarder/profiteer","militia leader","empowered free agent",
   "crosser","bureaucrat/official","farmer/operator","scavenger","teacher","warlord's lieutenant",
   "healer/herbalist","someone from the PC's old life"]),
 "npc_wants": ("NPC — wants", [
   "safety for someone","food/meds","power/control","to get west","revenge","information","belonging",
   "to protect a secret","redemption","wealth/leverage","escape","to be left alone"]),
 "npc_attitude": ("NPC — attitude to PC", [
   "hostile","afraid","wary","transactional","curious","needs you","admiring","loyal"]),
 "npc_hidden_truth": ("NPC — hidden truth", [
   "none — honest","lying about who they are","working for a faction","already betrayed you",
   "empowered and hiding it","dying/infected","protecting someone hidden",
   "did something terrible to survive","knows where a resource is","a crosser sympathizer/agent",
   "marked by an enemy","connected to the PC's past"]),
 "location_what": ("Location / Site — what it is", [
   "hospital","precinct/armory","warehouse/distribution hub","refinery/fuel depot","water plant",
   "power station","subway/tunnel","bridge/crossing","high-rise/tower","church/mosque/synagogue",
   "school/shelter","market/black market","docks/harbor","a holdout enclave","a faction stronghold",
   "a dead corporate campus","a refugee camp","a rift-site","a monster lair",
   "ordinary homes, now a graveyard or a haven"]),
 "location_wrong": ("Location / Site — what's wrong with it", [
   "occupied by a faction","booby-trapped","feral-infested","flooding/structural collapse",
   "a desperate group inside","contested by two powers","contaminated/diseased","a sapient monster claims it",
   "already stripped","a survivor needs rescue","a corpse-field","fire/no exit","a valuable cache, well-guarded",
   "the dark — no light, no power","freezing/exposure","a rival arrives as you do",
   "a clock is ticking (collapse/raid incoming)","a moral trap (help costs you)","watched/an ambush",
   "nothing wrong — which is itself suspicious"]),
 "scarcity_complication": ("Scarcity / Complication", [
   "Out of fuel","out of ammunition","out of clean water","out of food","out of medicine",
   "injury worsens/infects","power source dies","vehicle/gear fails","shelter compromised",
   "a resource is stolen","a debt comes due","someone must be left behind","cold/exposure sets in",
   "a witness/heat problem","an ally is wounded","numbers against you","the route is cut","trust breaks",
   "a clock advances against you","two complications at once (roll twice)"]),
 "salvage": ("Salvage / What You Find", [
   "fuel","ammunition","medicine/first aid","food/water","a working pre-electronic vehicle",
   "a shielded radio/comms","tools/parts","a weapon (roll quality)","winter gear","a map/intel","a generator",
   "currency-that-still-works (fuel, meds, ammo, gold)","a survivor","a body with useful gear","a clue/thread",
   "nothing — picked clean","a trap with the bait","something a faction wants back",
   "a hidden cache (jackpot, but guarded)","something inexplicable (rift-touched/Unmaking-adjacent)"]),
 "rumor": ("Word from the Road (rumor)", [
   "the corridor is falling faster than thought","a redoubt is forming west",
   "a warlord is recruiting the empowered","a safe enclave exists (true? roll)","crossers seen nearby",
   "a monster-lord stirs","a faction seeks a specific person","a supply cache located","a route is now impassable",
   "an ally has fallen","the Concord is watching","a betrayal in a known group","the Guard/redoubt is conscripting",
   "a massacre upriver","a cure/resource for the famine","the Empire's vanguard moves","a holdout needs help",
   "a price on someone's head","the rifts are doing something new","the rumor is bait — a trap"]),
 "monster_behavior": ("Monster Behavior", [
   "hunt/stalk","swarm/overwhelm","ambush","territorial display (flee available)","feed (distracted)",
   "migrate through","nest/den nearby","lure prey","flee from something bigger",
   "sapient — it negotiates or toys","wounded/desperate/erratic","something new — it shouldn't do that"]),
 "twist_escalation": ("Twist / Escalation", [
   "an ally betrays","the threat was a feint","a worse threat arrives","a clock completes now",
   "reinforcements (theirs)","a hostage/innocent in the line of fire","the ground/structure fails",
   "a hidden power reveals (enemy is higher-tier)","a resource you relied on is gone","a rival faction intervenes",
   "the real objective was elsewhere","a moral cost surfaces","the enemy wants you alive","a face from the past",
   "the swarm arrives, indifferent to both sides","your power falters at the worst moment","a trusted fact was a lie",
   "mercy is offered (with a hook)","the win has a price","raise Tension by 2 and let it spiral"]),
 "scene_alteration": ("Scene Alteration (Altered scene)", [
   "someone unexpected is here","someone expected is gone","the place is changed (damaged, occupied, emptied)",
   "it's later/worse than you thought — a clock advanced","a resource you counted on is gone","an enemy got here first",
   "an ally is compromised or turned","the goal has moved","a hazard is present (fire, flood, swarm, cold)",
   "it's a trap","a third party complicates it","the stakes just doubled"]),
 "opening_frame": ("Opening Frame (start in the thick of it)", [
   "gunfire nearby","a scream","smoke","a crowd surging","sudden silence","someone bleeding out",
   "a stranger in the way","a body","cold cutting through","a child alone","an engine that shouldn't run",
   "a rumor passed mouth to mouth","lights flicker on, then die","a monster's sign","a checkpoint ahead",
   "someone calls your name","a deal offered","the structure groans","a familiar face","the horizon does something wrong"]),
 # ref 09 — sandbox generators
 "faction_tags": ("Faction Tag (strength + catch; take 1–2)", [
   "Armed to the Teeth — wins fights above Tier · but a prize others come for",
   "Fuel Barons — everyone needs them · everyone covets it; raided constantly",
   "Empowered Core — punches above its weight · the powers have their own wills and may walk",
   "Holdout Fortress — safe, hard to break · fixed in place, can be besieged or bypassed",
   "Nomadic — can't be pinned or starved · can't hold ground or stockpile",
   "Zealots — fearless, cohesive, won't break · can't compromise or adapt",
   "Crosser-Allied — alien capability on tap · divided loyalties; the bloc has its own aims",
   "Crosser-Infiltrated — knows things it shouldn't · already compromised",
   "Medical Lifeline — indispensable, courted by all · raided, and bled when needed elsewhere",
   "Granary — feeds people, so it rules them · must defend the stores or starve",
   "Radio Net — coordinates and overhears · a priority target the instant it's known",
   "Press-Gang — grows fast, never short of bodies · universally hated, riddled with the unwilling",
   "Refugee Mass — numbers and moral weight · a burden, slow, desperately vulnerable",
   "Old Authority — organized and recognized · rigid, resented, slow to adapt",
   "Predatory — lean, mobile, dangerous · makes enemies everywhere, can't sustain itself",
   "Hidden — safe from direct attack · can't project power or be found when needed",
   "Industrialists — strategically vital, courted by the redoubt · slow, immobile, conquerable",
   "Warlord-Led — decisive, feared, fast · collapses or fractures if the leader falls",
   "Doomed — will gamble, will deal, unpredictable · a clock is ticking on them",
   "Sanctuary-Builders — legitimacy, recruits, allies · soft, the obvious prey of predators"]),
 "mission_job": ("Mission — the job", [
   "extract a person","secure a resource","escort a group","defend a place","recover an object","scout a zone",
   "sabotage something","broker a deal/truce","hunt a specific threat","deliver a message/cargo","rescue captives",
   "destroy a target","investigate a disappearance","hold a line","evacuate civilians","find the source of a problem",
   "remove a warlord/leader","clear a route","retrieve intel","buy time for someone else"]),
 "mission_catch": ("Mission — the catch", [
   "it's a trap","a rival wants it too","the client is lying","the target outclasses you (above your tier)",
   "a clock is already running","a moral cost is baked in","the prize is anomalous/cursed","the person won't be saved",
   "the route is impassable","a faction war crosses it","the swarm is in the way","a betrayal is seeded",
   "the reward can't actually be paid","innocents are in the line","the truth is worse than the job",
   "the enemy expects you","a monster-lord holds the ground","you're being used as a pawn",
   "it's already too late (pivot)","a second problem lands mid-job"]),
 "mission_stakes": ("Mission — the stakes / reward", [
   "fuel","food","medicine","a working vehicle","a safe place","a faction's favor","intel/a map",
   "a relic","a person who matters","territory","a debt cleared","reputation that opens doors"]),
 "mission_patron": ("Mission — the patron, if any", [
   "the Redoubt Authority","a local militia/enclave","a desperate family","a fixer/criminal","a faction leader",
   "the Interior Compact","a rival empowered","a dying official","a cult/movement","a crosser",
   "an old tie from before the Pulse","no one — you stumble into it"]),
 "cult_belief": ("Cult — core belief", [
   "the Pulse was divine judgment","the empowered are gods/the chosen","the empowered are abominations to be purged",
   "the crossers are saviors","the crossers are demons","the old world must be restored exactly",
   "the old world must be burned away","the Unmaking is coming and only *we* survive it",
   "submission to the strong is salvation","the rifts are doors to paradise","might is the only law now",
   "a prophet alone knows the way"]),
 "cult_leader": ("Cult — the leader", [
   "a Crown/Titan \"prophet\"","a charismatic unpowered demagogue","a surviving cleric/imam/rabbi","a crosser",
   "a former official","a warlord with a creed","a \"miracle\" child","a council of elders","a voice on the radio",
   "leaderless and viral"]),
 "cult_practice": ("Cult — the practice", [
   "tithes and tribute","purges/sacrifice","recruiting the empowered","mass pilgrimage (to a rift or the redoubt)",
   "ritual violence","sharing/hoarding resources as sacrament","marking the faithful","rejecting all technology",
   "militant conversion","rites at rift-sites"]),
 "cult_bite": ("Cult — how it bites the PC", [
   "conscripts/recruits the PC's people","marks someone like the PC for purging","controls a resource the PC needs",
   "blocks a route with pilgrims","ignites a faction war","harbors a real monster or power",
   "spreads a lie that gets people killed","offers a tempting refuge at a price","turns an ally of the PC's",
   "hardens into a true faction (build it in ref 04)"]),
 "rift_what": ("Rift Site — what it is", [
   "an open rift, still disgorging","a sealed, scarred rift","a deeper EMP dead-zone (even shielded tech fails)",
   "a monster-spawning hotspot","a \"wrong\" zone (space/physics bent)","a die-back zone — life withers",
   "a time-echo/slow zone","unnatural cold and dark","a fertile/healing anomaly (rare boon)",
   "a crosser-arrival site","a transcendent's claimed domain","a place the swarm refuses to enter — why?"]),
 "rift_hazard": ("Rift Site — what it does / the hazard", [
   "drains power and tech","mutates the living","draws monsters for miles","disorients and maddens",
   "plain physical danger (collapse, exposure)","spawns crossers or feral","emits something sensed from far off",
   "shelters something that shouldn't be disturbed","spreads slowly (a growing clock)",
   "offers something valuable for a price"]),
 "rift_unmaking_sign": ("Sign of the Unmaking (ominous — use sparingly)", [
   "nothing grows here, and won't again","the dead don't rot","a creeping grey edge",
   "survivors speak of \"the quiet that eats\"","a crosser refugee weeps at the sight of it",
   "the rare working instrument fails in a way it shouldn't","animals have fled the whole region",
   "it is larger than it was"]),
 "relic_object": ("Relic — the object", [
   "a pre-Pulse shielded device that still works","a rift-touched weapon","an empowered's lost focus",
   "a crosser-made object","a cache of meds or fuel (mundane, priceless)","a map or data on hardened media",
   "an oddity that suppresses or boosts powers","a useful monster-part","a transcendent relic",
   "a contained sample of the Unmaking","a piece of crosser tech","an heirloom a faction would kill to reclaim"]),
 "relic_gift": ("Relic — the gift / use", [
   "reliable power and light","a real weapon edge","healing/medicine","comms or hidden knowledge",
   "protection (armor/ward)","mobility (it runs)","leverage over a faction","suppresses or amplifies powers",
   "detects monsters or rifts","pure trade value"]),
 "relic_catch": ("Relic — the catch", [
   "a faction wants it back, badly","it slowly harms the bearer (sickness, mutation, madness)",
   "it's failing or finite (a clock)","it draws monsters","it marks the bearer to something",
   "it works only for the empowered — or only for the unpowered","it's bait in someone's trap",
   "using it carries a moral cost","it's anomalous and unpredictable",
   "no catch — a true find (rare; raise the price elsewhere)"]),
 # ref 15 — supers generator
 "supers_defining_complication": ("Supers — defining complication (the standing trigger die)", [
   "a tell (signature frost/heat/sound/light — alters the scene, draws trackers)",
   "a hunger/addiction the power feeds (pulls toward overuse / the strongest threat)",
   "a cost in the body (each use injures, drains, ages, sickens)",
   "a tech-leash (power routed through a device at the dark grid's mercy)",
   "a dependent the power can't protect (leverage and weakness)",
   "a mark (a faction/threat hunts the power or its bearer)",
   "a limit they hide (a hard ceiling/blind spot bluffed past — exposed at the worst time)",
   "a collateral problem (the power hurts bystanders/structures; an Exposure engine)",
   "a reputation (people know what they are — fear, recruitment, purge)",
   "a fracture (the power and the person are at odds — it changes them, or wants something)"]),
}

# ── WEIGHTED tables (canon merged ranges) ────────────────────────────────────
WEIGHTED = {
 "crosser_disposition": ("Crosser Contact — disposition", [
   ("hostile", 2), ("wary/testing", 2), ("transactional", 2), ("desperate", 1),
   ("curious", 1), ("friendly minority", 1), ("actively seeking alliance", 1)]),
 "supers_control": ("Supers — how the power sits in them", [
   ("mastered (reliable, no tell)", 2), ("costly (a tell/Exposure every significant use)", 2),
   ("barely held (fires under stress)", 1), ("unreliable (fails or overfires — a Hero-Point engine)", 1)]),
}

# ── EXPLICIT d100 tables (native d100 ranges kept verbatim) ───────────────────
EXPLICIT = {
 "event_focus": ("Random Event Focus (Vanguard)", [
   (1,6,"The war moves — a front shifts, a clock ticks, territory changes hands"),
   (7,13,"A faction advances — a present faction pushes its agenda a step"),
   (14,18,"A faction turns on another — two powers collide (roll which)"),
   (19,22,"A new power emerges — generate a faction (ref 04); a vacuum just filled"),
   (23,29,"Threat closes in — a hostile force, hunt, or ambush arrives (encounter table)"),
   (30,35,"Monster surge — feral or sapient; the swarm presses (monster tables)"),
   (36,41,"Crosser contact — a bloc element appears or makes contact (crosser tables)"),
   (42,46,"The empowered — a new power manifests, or a free agent acts (empowered tables)"),
   (47,53,"Scarcity bites — something runs out, breaks, or is taken (scarcity table)"),
   (54,60,"An ally / NPC acts — a known figure moves toward their goal"),
   (61,65,"An NPC's truth surfaces — a secret, lie, or real loyalty is exposed"),
   (66,69,"A thread advances — an open thread lurches forward"),
   (70,73,"A thread is blocked — an open thread reverses, stalls, or is closed against you"),
   (74,79,"Refugees / civilians — the human tide: need, panic, opportunity, witness"),
   (80,84,"The dark world — environment/hazard: grid, weather, structure, terrain fails"),
   (85,88,"Authority acts — police, Guard, redoubt, or local power asserts itself"),
   (89,92,"Word arrives — rumor, news, a message, a runner (rumor table)"),
   (93,96,"A turn against you — betrayal, defection, a price comes due"),
   (97,99,"The PC's world — something tied to the PC's people, past, or ties intrudes"),
   (100,100,"The horizon — a glimpse of the Unmaking, the Empire, or the deep future")]),
 "empowered_tier": ("Random Empowered Tier (weighted to canon population)", [
   (1,33,"Flicker (Trivial) — a parlor trick; barely touched"),
   (34,41,"Spark (Trivial) — a small real gift"),
   (42,52,"Plus (Minor) — a useful edge"),
   (53,62,"Ringer (Minor) — wins any human contest"),
   (63,74,"Bruiser (Street) — wins real fights; kills feral"),
   (75,83,"Heavy (Street) — a serious local threat"),
   (84,91,"Breaker (City) — a one-person problem (PC band)"),
   (92,96,"Siege (City) — a walking siege engine (above PC)"),
   (97,99,"Warlord (Elite) — breaks formations (flee)"),
   (100,100,"Titan+ (Elite–Apex) — roll 1–6 Titan · 7–9 Crown · 10 Horror")]),
}

# ── Vanguard-native Meaning Tables (d100, one word each) ──────────────────────
MEANING_ACTIONS = ["Abandon","Ambush","Arm","Bargain","Betray","Bleed","Block","Break","Burn","Capture",
 "Carry","Collapse","Conceal","Confront","Connect","Consume","Control","Corrupt","Crack","Crush","Dare",
 "Deal","Decide","Defect","Deceive","Decay","Deceive","Defend","Delay","Demand","Deny","Destroy","Divide",
 "Dominate","Drain","Drive","Endure","Escalate","Escape","Exhaust","Expose","Fail","Fall","Fight","Flee",
 "Fortify","Gather","Govern","Guard","Hoard","Hunt","Imprison","Infect","Inform","Inherit","Intercept",
 "Invade","Isolate","Judge","Lead","Leave","Loot","Lose","Manifest","Mourn","Negotiate","Obstruct","Offer",
 "Oppress","Overrun","Persuade","Plead","Plunder","Pursue","Push","Reclaim","Recruit","Refuse","Release",
 "Repair","Resist","Retreat","Reveal","Sabotage","Sacrifice","Salvage","Scatter","Seize","Shelter","Starve",
 "Submit","Surrender","Survive","Threaten","Transform","Trap","Turn","Unmake","Warn","Witness"]
MEANING_ASPECTS = ["Alliance","Ambition","Armor","Ash","Authority","Barrier","Blood","Border","Burden","Cargo",
 "Catastrophe","Child","Choice","Cold","Command","Corridor","Corruption","Crew","Crossing","Crowd","Dark",
 "Death","Debt","Despair","Dread","Duty","Echo","Edge","Empire","Enemy","Exile","Faith","Family","Famine",
 "Fear","Fire","Flesh","Fortress","Fuel","Future","Ghost","Grid","Grief","Harbor","Haven","History","Home",
 "Hope","Hunger","Injury","Iron","Law","Leader","Legacy","Light","Line","Machine","Medicine","Mercy","Message",
 "Mob","Monster","Need","Network","Order","Outsider","Pact","Power","Predator","Promise","Refuge","Refugee",
 "Remnant","Rift","Rival","Ruin","Sacrifice","Salvage","Scar","Secret","Shadow","Shelter","Siege","Signal","Silence",
 "Strength","Stranger","Supply","Territory","Threshold","Tide","Trust","Tyrant","Vengeance","Vow","Wall",
 "Water","Weapon","Wound","Wreckage"]

# ── build all ────────────────────────────────────────────────────────────────
def main():
    written = []
    for name, (title, values) in UNIFORM.items():
        written.append(write_table(name, title, entries_from_values(values)))
    for name, (title, pairs) in WEIGHTED.items():
        vals = [v for v, _ in pairs]; wts = [w for _, w in pairs]
        written.append(write_table(name, title, entries_from_values(vals, wts)))
    for name, (title, rngs) in EXPLICIT.items():
        ents = [{"min": a, "max": b, "value": v} for a, b, v in rngs]
        assert sum(e["max"]-e["min"]+1 for e in ents) == 100, f"{name} explicit != 100"
        written.append(write_table(name, title, ents))
    for name, words in (("meaning_actions", MEANING_ACTIONS), ("meaning_aspects", MEANING_ASPECTS)):
        assert len(words) == 100, f"{name} has {len(words)} words"
        ents = [{"min": i+1, "max": i+1, "value": w} for i, w in enumerate(words)]
        written.append(write_table(name, f"Meaning Table — {name.split('_')[1].title()} (Vanguard)", ents))
    print(f"BUILT {len(written)} generator tables:")
    for n in sorted(written):
        print(f"   vanguard.{n}.json")

if __name__ == "__main__":
    main()

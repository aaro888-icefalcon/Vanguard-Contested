# Generator Index — Vanguard Contested   (hooks: generate:* ; oracle overrides)
# need | when it's called | table(s) | mode (replace | conjunction | default)
# Tables are verified list_d100 JSON in this folder (built by build.py), rolled with:
#   python3 ../../mythic-gm/scripts/dice.py table generators/<name>.json
# "Anything not listed -> Mythic/AC default." Vanguard adds/replaces specifically; the engine still owns
# the Fate Question, Scene Test, Chaos math, Random-Event trigger, Turning Points, and the discipline.

| need | when called | table(s) | mode |
|------|-------------|----------|------|
| new NPC (generic) | any new Character invoked | AC Character Crafter (`oracle.py character`) + npc_role + npc_wants + npc_attitude + npc_hidden_truth | conjunction |
| new NPC (powered) | a manifester who may matter mechanically (ref 15 supers) | empowered_tier + empowered_power + empowered_intent + supers_control + supers_defining_complication | replace |
| how strong is this person | sizing any empowered NPC | empowered_tier (biased to context: street→down, retinue/named→up) | replace |
| location / site | a scene needs a place | location_what + location_wrong | replace |
| new faction | a power vacuum / crosser split / clock completes (ref 04) | faction_tags (1–2) + faction_move | conjunction |
| what a faction does | a faction acts on its clock (world-tick) | faction_move | replace |
| encounter | "what shows up," by region band | encounter_guarded / encounter_embattled / encounter_nomansland | replace |
| crosser contact | a bloc element appears | crosser_bloc + crosser_disposition + crosser_wants | replace |
| mission / job | seeding or framing an objective | mission_job + mission_catch + mission_stakes + mission_patron | replace |
| cult / movement | a post-Pulse creed enters | cult_belief + cult_leader + cult_practice + cult_bite | replace |
| rift / anomaly | a rift-site or the Unmaking's edge | rift_what + rift_hazard + rift_unmaking_sign (sparingly) | replace |
| relic / object | an anomalous object (gift with a price) | relic_object + relic_gift + relic_catch | replace |
| scarcity bite | a resource runs out / breaks / is taken | scarcity_complication | replace |
| salvage | what you find scavenging | salvage | replace |
| rumor / word | news from the road | rumor | replace |
| monster behavior | a feral/sapient threat acts | monster_behavior | replace |
| twist / escalation | a scene needs to turn harder | twist_escalation | replace |
| scene alteration | the Scene Test says Altered (engine) | scene_alteration | conjunction |
| opening frame | start a scene in the thick of it | opening_frame | default |
| Random Event Focus | a Random Event fires (engine doubles ≤ CF) | event_focus | replace |
| Meaning — Action | reading any Meaning result | meaning_actions | replace |
| Meaning — Aspect | reading any Meaning result | meaning_aspects | replace |
| generic inspiration | Discover Meaning, no specific need | Mythic Elements (engine default) | default |

# Notes:
# - "replace" tables are Vanguard-native; roll them instead of the engine's generic equivalent.
# - "conjunction" layers a Vanguard table on top of the AC/Mythic core (e.g. Character Crafter + npc_role).
# - event_focus / meaning_actions / meaning_aspects are the setting's flavored oracle: when the engine fires
#   a Random Event or asks for Meaning, roll these (the engine still owns *when* it fires).
# - Bias the empowered_tier roll to context and the region band (ref 15 §1); never use it raw for everything.

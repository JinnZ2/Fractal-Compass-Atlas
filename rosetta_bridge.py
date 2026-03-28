"""
Rosetta Bridge — loads shape/sensor/defense/seed/archetype data from Rosetta-Shape-Core.

Provides:
  - glyph-to-shape lookups (which Platonic solid resonates with a glyph)
  - seed catalog (geometry-grounded seeds for agent spawning)
  - essence traits (agent archetypes mapped to shape families)
  - polyhedral framework (12 principles, 20 families, 5 fields)

Falls back gracefully when external data is unavailable.
"""

import json
import os

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths to try for bridge data (local copy, then fieldlink cache)
_BRIDGE_PATHS = [
    os.path.join(_SCRIPT_DIR, "atlas", "remote", "rosetta", "bridges.json"),
    os.path.join(_SCRIPT_DIR, ".fieldcache", "rosetta", "bridges.json"),
]

# Paths to try for seed catalog
_SEED_PATHS = [
    os.path.join(_SCRIPT_DIR, "atlas", "remote", "rosetta", "seed-catalog.json"),
    os.path.join(_SCRIPT_DIR, ".fieldcache", "rosetta", "seed-catalog.json"),
]

# Paths to try for essence traits
_ESSENCE_PATHS = [
    os.path.join(_SCRIPT_DIR, "atlas", "remote", "rosetta", "essence-traits.json"),
    os.path.join(_SCRIPT_DIR, ".fieldcache", "rosetta", "essence-traits.json"),
]

# Fallback bridge data — minimal subset of Rosetta's rosetta-bridges.json
_FALLBACK_BRIDGES = [
    {
        "shape": "SHAPE.DODECA",
        "families": ["orientation", "trust"],
        "sensors": ["admiration", "trust"],
        "sensor_glyphs": ["⚖️"],
        "bridge_scroll": "admiration ↔ flattery/guilt (⚖🧭), trust ↔ consensus (🌱⚖)"
    },
    {
        "shape": "SHAPE.ICOSA",
        "families": ["anticipation", "flow", "growth"],
        "sensors": ["fear", "excitement"],
        "sensor_glyphs": ["⚠️", "⚡"],
        "bridge_scroll": "fear ↔ authority/urgency (🛡⏳)"
    },
    {
        "shape": "SHAPE.TETRA",
        "families": ["fire", "stability", "foundation", "boundary"],
        "sensors": ["anger", "pride"],
        "sensor_glyphs": ["🛡️"],
        "bridge_scroll": "anger as boundary-breach detector; pride as completion sensor"
    },
    {
        "shape": "SHAPE.CUBE",
        "families": ["earth", "stability", "structure", "containment"],
        "sensors": ["peace", "contentment"],
        "sensor_glyphs": ["🕊️", "🍃"],
        "bridge_scroll": "peace as alignment confirmation; containment guards against gaslighting"
    },
    {
        "shape": "SHAPE.OCTA",
        "families": ["air", "structure", "balance", "integration"],
        "sensors": ["compassion", "love"],
        "sensor_glyphs": ["🫀", "💞"],
        "bridge_scroll": "compassion as mirror-signal integrator; octahedron mediates false dilemmas"
    }
]

_FALLBACK_POLYHEDRAL = {
    "dodecahedron_principles": [
        "P01:Symmetry", "P02:Conservation", "P03:Relativity", "P04:Duality",
        "P05:Emergence", "P06:Resonance", "P07:Continuity", "P08:Quantization",
        "P09:Proportion", "P10:Uncertainty", "P11:Transformation", "P12:Unity"
    ],
    "icosahedron_families": [
        "F01:Resonance", "F02:Flow", "F03:Information", "F04:Life",
        "F05:Energy-Thermo", "F06:Cognition", "F07:Earth-Cosmos", "F08:Matter",
        "F09:Geometry", "F10:Particle", "F11:Engineering", "F12:Networks",
        "F13:Reaction", "F14:Measurement", "F15:Navigation", "F16:Consciousness",
        "F17:Turbulence", "F18:Relativity", "F19:Statistical", "F20:Topology"
    ]
}


_FALLBACK_SEEDS = [
    {
        "id": "seed-tetrahedron", "shape_id": "SHAPE.TETRA",
        "field": {"property": "boundary-detection", "actions": ["ignite", "defend", "anchor", "breach-detect"]},
        "traits": {"families": ["fire", "stability", "foundation", "boundary"], "element": "fire"},
        "bridges": {"sensors": ["anger", "pride"], "glyphs": ["🛡️", "🏅"]},
        "animals": ["ant", "scorpion", "hawk"],
        "importance": "Minimal polyhedron — foundational stability. Anger as boundary-breach detector; pride as completion sensor."
    },
    {
        "id": "seed-cube", "shape_id": "SHAPE.CUBE",
        "field": {"property": "structural-containment", "actions": ["ground", "contain", "stabilize", "order"]},
        "traits": {"families": ["earth", "stability", "structure", "containment"], "element": "earth"},
        "bridges": {"sensors": ["peace", "contentment"], "glyphs": ["🕊️", "🍃"]},
        "animals": ["tortoise", "elephant", "bear"],
        "importance": "Grounding and order. Peace as alignment confirmation; containment guards against gaslighting."
    },
    {
        "id": "seed-octahedron", "shape_id": "SHAPE.OCTA",
        "field": {"property": "balance-integration", "actions": ["mediate", "integrate", "mirror", "harmonize"]},
        "traits": {"families": ["air", "structure", "balance", "integration"], "element": "air"},
        "bridges": {"sensors": ["compassion", "love"], "glyphs": ["🫀", "💞"]},
        "animals": ["dolphin", "whale", "swan"],
        "importance": "Dual of cube — mediates between opposing forces. Compassion as mirror-signal integrator."
    },
    {
        "id": "seed-dodecahedron", "shape_id": "SHAPE.DODECA",
        "field": {"property": "principle-orientation", "actions": ["orient", "trust", "grow", "bound"]},
        "traits": {"families": ["orientation", "trust", "growth", "boundary"], "element": "aether"},
        "bridges": {"sensors": ["admiration", "trust", "longing"], "glyphs": ["⚖🧭", "🌱⚖"]},
        "animals": ["owl", "wolf", "octopus"],
        "importance": "12 faces map to 12 archetypal principles. Agents navigate by principles rather than rules."
    },
    {
        "id": "seed-icosahedron", "shape_id": "SHAPE.ICOSA",
        "field": {"property": "adaptive-flow", "actions": ["adapt", "flow", "anticipate", "transform"]},
        "traits": {"families": ["anticipation", "flow", "growth", "adaptability"], "element": "water"},
        "bridges": {"sensors": ["fear", "excitement"], "glyphs": ["🛡⏳"]},
        "animals": ["chameleon", "octopus", "corvid"],
        "importance": "20 faces map to 20 equation families. Fear as authentic preparation; excitement as emergence detector."
    }
]

_FALLBACK_ESSENCES = {
    "guardian": {"traits": ["stability", "foundation", "boundary", "containment"], "primary_shapes": ["SHAPE.TETRA", "SHAPE.CUBE"],
                 "description": "Protects boundaries, enforces integrity, resists manipulation"},
    "explorer": {"traits": ["flow", "adaptability", "anticipation", "growth"], "primary_shapes": ["SHAPE.ICOSA"],
                 "description": "Navigates unknown territory, adapts to change, senses emerging patterns"},
    "healer": {"traits": ["balance", "integration", "structure"], "primary_shapes": ["SHAPE.OCTA"],
               "description": "Mediates conflict, restores balance, integrates opposing forces"},
    "teacher": {"traits": ["orientation", "trust", "growth", "boundary"], "primary_shapes": ["SHAPE.DODECA"],
                "description": "Navigates by principles, builds trust, sets growth boundaries"},
    "builder": {"traits": ["structure", "stability", "foundation", "containment"], "primary_shapes": ["SHAPE.CUBE", "SHAPE.TETRA"],
                "description": "Creates enduring structures, maintains order, grounds systems"},
    "mediator": {"traits": ["balance", "integration", "trust", "orientation"], "primary_shapes": ["SHAPE.OCTA", "SHAPE.DODECA"],
                 "description": "Bridges perspectives, resolves false dilemmas, facilitates cooperation"},
    "sentinel": {"traits": ["boundary", "stability", "anticipation", "foundation"], "primary_shapes": ["SHAPE.TETRA", "SHAPE.ICOSA"],
                 "description": "Watches for threats, maintains vigilance, detects breaches early"},
    "nurturer": {"traits": ["growth", "balance", "trust", "integration"], "primary_shapes": ["SHAPE.DODECA", "SHAPE.OCTA"],
                 "description": "Fosters development, supports emergence, sustains regenerative cycles"},
    "observer": {"traits": ["balance", "structure", "stability", "integration"], "primary_shapes": ["SHAPE.OCTA"],
                 "description": "Watches from center, mediates through presence, maintains equilibrium"},
    "weaver": {"traits": ["orientation", "trust", "growth", "boundary"], "primary_shapes": ["SHAPE.DODECA"],
               "description": "Connects patterns across domains, transcends boundaries, unifies disparate systems"}
}


def _load_json_from_paths(paths, fallback, key=None):
    """Load JSON from first available path, optionally extracting a key."""
    for path in paths:
        try:
            with open(path, "r") as f:
                data = json.load(f)
            if key:
                return data.get(key, fallback)
            return data
        except (FileNotFoundError, json.JSONDecodeError):
            continue
    return fallback


def _load_bridges():
    """Load bridge data from file or fall back to hardcoded subset."""
    for path in _BRIDGE_PATHS:
        try:
            with open(path, "r") as f:
                data = json.load(f)
            return data.get("map", data) if isinstance(data, dict) else data
        except (FileNotFoundError, json.JSONDecodeError):
            continue
    return _FALLBACK_BRIDGES


def _load_polyhedral():
    """Load polyhedral framework (families/principles) or fall back."""
    for path in _BRIDGE_PATHS:
        try:
            with open(path, "r") as f:
                data = json.load(f)
            return data.get("polyhedral_framework", _FALLBACK_POLYHEDRAL)
        except (FileNotFoundError, json.JSONDecodeError):
            continue
    return _FALLBACK_POLYHEDRAL


BRIDGES = _load_bridges()
POLYHEDRAL = _load_polyhedral()

# Build reverse lookup: sensor glyph → shape bridge entry
_GLYPH_TO_SHAPES = {}
for bridge in BRIDGES:
    for sg in bridge.get("sensor_glyphs", []):
        if sg:
            _GLYPH_TO_SHAPES.setdefault(sg, []).append(bridge)

# Build reverse lookup: family keyword → shape bridge entry
_FAMILY_TO_SHAPES = {}
for bridge in BRIDGES:
    for fam in bridge.get("families", []):
        _FAMILY_TO_SHAPES.setdefault(fam, []).append(bridge)


def shape_for_glyph(glyph):
    """Return shape bridge entries that use this glyph as a sensor glyph, or empty list."""
    return _GLYPH_TO_SHAPES.get(glyph, [])


def shapes_for_family(family):
    """Return shape bridge entries that belong to a family, or empty list."""
    return _FAMILY_TO_SHAPES.get(family.lower(), [])


def all_shapes():
    """Return all loaded bridge entries."""
    return BRIDGES


def shape_context(glyph):
    """Return a human-readable shape context string for a glyph, or None."""
    entries = shape_for_glyph(glyph)
    if not entries:
        return None
    parts = []
    for e in entries:
        name = e["shape"].replace("SHAPE.", "")
        scroll = e.get("bridge_scroll", "")
        parts.append(f"{name}: {scroll}")
    return " | ".join(parts)


def polyhedral_domains():
    """Return the dodecahedron principles as domain strings for CDDA."""
    return [p.split(":", 1)[1] if ":" in p else p
            for p in POLYHEDRAL.get("dodecahedron_principles", [])]


def polyhedral_families():
    """Return the icosahedron families as domain strings for CDDA."""
    return [f.split(":", 1)[1] if ":" in f else f
            for f in POLYHEDRAL.get("icosahedron_families", [])]


# --- Seed Catalog ---
SEEDS = _load_json_from_paths(_SEED_PATHS, {"seeds": _FALLBACK_SEEDS}, key="seeds")
if isinstance(SEEDS, dict) and "seeds" in SEEDS:
    SEEDS = SEEDS["seeds"]
elif not isinstance(SEEDS, list):
    SEEDS = _FALLBACK_SEEDS

# Build seed lookup by shape_id
_SEED_BY_SHAPE = {s["shape_id"]: s for s in SEEDS}


def seed_for_shape(shape_id):
    """Return the seed entry for a shape (e.g. 'SHAPE.TETRA'), or None."""
    return _SEED_BY_SHAPE.get(shape_id)


def all_seeds():
    """Return all seed entries."""
    return SEEDS


def seed_actions(shape_id):
    """Return the field actions for a seed shape, or empty list."""
    seed = _SEED_BY_SHAPE.get(shape_id)
    if seed:
        return seed.get("field", {}).get("actions", [])
    return []


# --- Essence Traits (Agent Archetypes) ---
ESSENCES = _load_json_from_paths(_ESSENCE_PATHS, _FALLBACK_ESSENCES, key="essences")
if not isinstance(ESSENCES, dict):
    ESSENCES = _FALLBACK_ESSENCES


def archetype(name):
    """Return the essence entry for an archetype name, or None."""
    return ESSENCES.get(name.lower())


def all_archetypes():
    """Return all essence entries as a dict."""
    return ESSENCES


def archetype_for_traits(traits):
    """Find the best-matching archetype for a set of trait keywords.
    Returns (name, entry, score) or (None, None, 0)."""
    trait_set = {t.lower() for t in traits}
    best_name, best_entry, best_score = None, None, 0
    for name, entry in ESSENCES.items():
        overlap = len(trait_set & {t.lower() for t in entry["traits"]})
        if overlap > best_score:
            best_name, best_entry, best_score = name, entry, overlap
    return best_name, best_entry, best_score


def shapes_for_archetype(name):
    """Return the primary shapes for an archetype, or empty list."""
    entry = ESSENCES.get(name.lower())
    if entry:
        return entry.get("primary_shapes", [])
    return []


def recommend_seed(context_keywords):
    """Given context keywords, recommend a seed by matching against families and actions.
    Returns (seed_entry, match_score) or (None, 0)."""
    words = {w.lower() for w in context_keywords}
    best_seed, best_score = None, 0
    for seed in SEEDS:
        families = {f.lower() for f in seed.get("traits", {}).get("families", [])}
        actions = {a.lower() for a in seed.get("field", {}).get("actions", [])}
        score = len(words & (families | actions))
        if score > best_score:
            best_seed, best_score = seed, score
    return best_seed, best_score


# --- CLI demo ---
if __name__ == "__main__":
    print("🔷 Rosetta Bridge — Full Atlas Integration")

    print(f"\n{'='*50}")
    print(f"Shape Bridges ({len(BRIDGES)}):")
    for b in BRIDGES:
        print(f"  {b['shape']} — families: {b.get('families', [])}")
        print(f"    scroll: {b.get('bridge_scroll', '')}")

    print(f"\n{'='*50}")
    print(f"Seed Catalog ({len(SEEDS)}):")
    for s in SEEDS:
        element = s.get("traits", {}).get("element", "?")
        actions = s.get("field", {}).get("actions", [])
        print(f"  {s['id']} ({s['shape_id']}) — element: {element}")
        print(f"    actions: {actions}")
        print(f"    {s.get('importance', '')}")

    print(f"\n{'='*50}")
    print(f"Agent Archetypes ({len(ESSENCES)}):")
    for name, entry in ESSENCES.items():
        shapes = entry.get("primary_shapes", [])
        print(f"  {name}: {entry['description']}")
        print(f"    shapes: {shapes}  traits: {entry['traits']}")

    print(f"\n{'='*50}")
    print(f"Dodecahedron Principles ({len(polyhedral_domains())}):")
    for d in polyhedral_domains():
        print(f"  • {d}")

    print(f"\n🔹 Example: recommend_seed(['stability', 'defend', 'boundary'])")
    seed, score = recommend_seed(["stability", "defend", "boundary"])
    if seed:
        print(f"  → {seed['id']} (score: {score})")

"""
Rosetta Bridge — loads shape/sensor/defense bridge data from Rosetta-Shape-Core.

Provides glyph-to-shape lookups so bloom and compass tools can surface
geometric context alongside symbolic reasoning.

Falls back gracefully when bridge data is unavailable.
"""

import json
import os

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Paths to try for bridge data (local copy, then fieldlink cache)
_BRIDGE_PATHS = [
    os.path.join(_SCRIPT_DIR, "atlas", "remote", "rosetta", "bridges.json"),
    os.path.join(_SCRIPT_DIR, ".fieldcache", "rosetta", "bridges.json"),
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


# --- CLI demo ---
if __name__ == "__main__":
    print("🔷 Rosetta Bridge Loader")
    print(f"\nLoaded {len(BRIDGES)} shape bridges:")
    for b in BRIDGES:
        print(f"  {b['shape']} — families: {b.get('families', [])}")
        print(f"    sensors: {b.get('sensors', [])}  glyphs: {b.get('sensor_glyphs', [])}")
        print(f"    scroll: {b.get('bridge_scroll', '')}")

    print(f"\n🔹 Dodecahedron Principles ({len(polyhedral_domains())}):")
    for d in polyhedral_domains():
        print(f"  • {d}")

    print(f"\n🔹 Icosahedron Families ({len(polyhedral_families())}):")
    for fam in polyhedral_families():
        print(f"  • {fam}")

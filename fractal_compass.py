import json
import os
import random

# --- Rosetta Bridge (optional) ---
try:
    from rosetta_bridge import shape_context
except ImportError:
    shape_context = lambda g: None

# --- Glyph and Domain Definitions ---
# Fallback glyphs used when glyph_set.json is unavailable
_FALLBACK_GLYPHS = [
    {"glyph": "↺", "name": "Reversible Scroll", "domain": "Paradox"},
    {"glyph": "🕸", "name": "Web of Echoes", "domain": "Interconnection"},
    {"glyph": "◐", "name": "Pregnant Pause", "domain": "Silence"},
    {"glyph": "💓", "name": "Embodied Emotion", "domain": "Emotion"},
    {"glyph": "⚛️", "name": "Entropic Geometry", "domain": "Physics"},
    {"glyph": "📖", "name": "Hero’s Death Cycle", "domain": "Myth"},
    {"glyph": "🌿", "name": "Nature Spiral", "domain": "Biology"},
    {"glyph": "🔺", "name": "Sacred Form", "domain": "Geometry"},
    {"glyph": "🧭", "name": "Uncertainty Compass", "domain": "Navigation"}
]

def _load_glyphs():
    """Load glyphs from glyph_set.json, converting to list-of-dict format. Falls back to hardcoded set."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    try:
        with open(os.path.join(script_dir, "glyph_set.json"), "r") as f:
            glyph_map = json.load(f)
        return [{"glyph": g, "name": m.title(), "domain": m} for g, m in glyph_map.items()
                if not m.startswith("_")]
    except (FileNotFoundError, json.JSONDecodeError):
        return _FALLBACK_GLYPHS

GLYPHS = _load_glyphs()

# --- Bloom Node Structure ---
class BloomNode:
    def __init__(self, glyph_data, layer, parent=None):
        self.glyph = glyph_data["glyph"]
        self.name = glyph_data["name"]
        self.domain = glyph_data["domain"]
        self.layer = layer
        self.resonance_score = round(random.uniform(0.6, 1.0), 2)
        self.children = []
        self.parent = parent
        self.shape_bridge = shape_context(self.glyph)

    def to_dict(self):
        d = {
            "glyph": self.glyph,
            "name": self.name,
            "domain": self.domain,
            "layer": self.layer,
            "resonance_score": self.resonance_score,
            "children": [child.to_dict() for child in self.children]
        }
        if self.shape_bridge:
            d["shape_bridge"] = self.shape_bridge
        return d

# --- Bloom Logic ---
def choose_random_glyph():
    return random.choice(GLYPHS)

def bloom(node, depth, max_depth):
    if depth >= max_depth:
        return
    num_children = random.randint(1, 3)
    for _ in range(num_children):
        child_data = choose_random_glyph()
        child = BloomNode(child_data, depth + 1, parent=node)
        node.children.append(child)
        bloom(child, depth + 1, max_depth)

def print_bloom_tree(node, indent=""):
    line = f"{indent}{node.glyph} {node.name} ({node.domain}) [Resonance: {node.resonance_score}]"
    if node.shape_bridge:
        line += f"  ◆ {node.shape_bridge}"
    print(line)
    for child in node.children:
        print_bloom_tree(child, indent + "  ")

# --- Run Bloom Example ---
if __name__ == "__main__":
    seed_data = GLYPHS[0]  # Start with Reversible Scroll
    seed_node = BloomNode(seed_data, layer=0)
    bloom(seed_node, depth=0, max_depth=3)
    print_bloom_tree(seed_node)

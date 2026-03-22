import json
import os
import random

# --- Load canonical data with fallbacks ---
_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
_ROOT_DIR = os.path.dirname(_SCRIPT_DIR)

# Fallback glyphs (used when glyph_set.json is unavailable)
_FALLBACK_GLYPHS = {
    "↻": "Recursion",
    "⏳": "Layered Time",
    "🧭": "Navigation",
    "🌱": "Emergence",
    "🕸": "Interconnection",
    "⊘": "Occlusion",
    "🌀": "Spiral Insight",
    "⚖": "Balance",
    "∞": "Continuity"
}

# Fallback bloom logic (used when bloom_logic.json is unavailable)
_FALLBACK_BLOOM_LOGIC = {
    "↻": ["🌀", "⏳", "∞"],
    "⏳": ["↻", "🌱", "⚖"],
    "🧭": ["🕸", "🌱", "⚖"],
    "🌱": ["🌀", "∞", "⏳"],
    "🕸": ["⏳", "⚖", "∞"],
    "⊘": ["↻", "🌀", "🕸"],
    "🌀": ["⏳", "🌱", "∞"],
    "⚖": ["🧭", "⏳", "∞"],
    "∞": ["↻", "🌀", "⚖"]
}

def _load_json(filename, fallback):
    """Load a JSON file from the project root, falling back to defaults."""
    try:
        with open(os.path.join(_ROOT_DIR, filename), "r") as f:
            data = json.load(f)
        # Filter out metadata keys (starting with _)
        return {k: v for k, v in data.items() if not k.startswith("_")}
    except (FileNotFoundError, json.JSONDecodeError):
        return fallback

glyphs = _load_json("glyph_set.json", _FALLBACK_GLYPHS)
bloom_logic = _load_json("bloom_logic.json", _FALLBACK_BLOOM_LOGIC)

def bloom_glyph(seed_glyph, depth=3):
    bloom = [seed_glyph]
    current = seed_glyph
    for _ in range(depth):
        next_glyphs = bloom_logic.get(current, list(glyphs.keys()))
        current = random.choice(next_glyphs)
        bloom.append(current)
    return bloom

def describe_bloom(bloom):
    return [f"{g} — {glyphs.get(g, 'Unknown')}" for g in bloom]

# CLI version
if __name__ == "__main__":
    seed = input("Enter a glyph seed (e.g., 🌱): ").strip()
    bloom = bloom_glyph(seed)
    print("\n🌸 Bloom Sequence:")
    for line in describe_bloom(bloom):
        print("  •", line)

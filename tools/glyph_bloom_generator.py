import random

# Core glyphs with symbolic functions
glyphs = {
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

# Bloom logic — how glyphs relate symbolically
bloom_logic = {
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

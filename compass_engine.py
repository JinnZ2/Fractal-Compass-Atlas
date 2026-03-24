import json
import random

# --- Rosetta Bridge (optional) ---
try:
    from rosetta_bridge import shape_context, all_shapes
    _HAS_ROSETTA = True
except ImportError:
    shape_context = lambda g: None
    all_shapes = lambda: []
    _HAS_ROSETTA = False

# Load glyphs if needed
try:
    with open("glyph_set.json", "r") as f:
        GLYPHS = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    GLYPHS = {
        "🌱": "growth",
        "↻": "recursion",
        "⚖️": "balance",
        "🧭": "navigation",
        "⏳": "time shift",
        "🕸️": "interconnection",
        "∞": "continuity"
    }

def symbolic_bloom(seed):
    print(f"\n🔮 Blooming seed: '{seed}'")

    # Step 1: Glyph suggestions (with shape bridges when available)
    suggested = random.sample(list(GLYPHS.items()), 3)
    print("\n🌐 Suggested Glyphs:")
    for g, m in suggested:
        ctx = shape_context(g)
        if ctx:
            print(f"  {g} — {m}  ◆ {ctx}")
        else:
            print(f"  {g} — {m}")

    # Show Rosetta shape context if available
    if _HAS_ROSETTA:
        shapes = all_shapes()
        if shapes:
            bridge = random.choice(shapes)
            print(f"\n🔷 Shape Resonance: {bridge['shape']}")
            print(f"   Families: {', '.join(bridge.get('families', []))}")
            print(f"   Sensors: {', '.join(bridge.get('sensors', []))}")
            print(f"   Scroll: {bridge.get('bridge_scroll', '')}")

    # Step 2: Inversion
    inverse = input("\n🔁 Invert the seed meaning (optional): ").strip()

    # Step 3: Cross-domain scan (manual, enriched with Rosetta families)
    domains = "biology, physics, emotion, ethics, or systems"
    if _HAS_ROSETTA and bridge:
        families = bridge.get("families", [])
        if families:
            domains += f" — or through {', '.join(families)}"
    print(f"\n📚 Consider: How does this idea appear in {domains}?")
    insights = input("🧠 Cross-domain insight (enter brief notes): ").strip()

    # Step 4: Fractal Principle
    principle = input("💡 Final emergent principle (1-sentence distilled truth): ").strip()

    print("\n✅ Your Fractal Principle:")
    print(f"🌱 {principle}\n")

    # Save output for logging
    save = input("💾 Save to log? (y/n): ").lower()
    if save == "y":
        with open("fractal_principles.md", "a") as f:
            f.write(f"""
---

## 🌱 New Principle from Seed: {seed}

**Glyphs:** {' '.join([g for g, _ in suggested])}  
**Inversion:** {inverse}  
**Cross-Domain Insight:** {insights}  
**Fractal Principle:** {principle}

""")
        print("📁 Appended to fractal_principles.md")

if __name__ == "__main__":
    print("🌌 Fractal Compass Engine (CLI Mode)")
    seed = input("🔹 Enter symbolic seed or question: ")
    symbolic_bloom(seed)

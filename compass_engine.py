import json
import random

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

    # Step 1: Glyph suggestions
    suggested = random.sample(list(GLYPHS.items()), 3)
    print("\n🌐 Suggested Glyphs:")
    for g, m in suggested:
        print(f"  {g} — {m}")

    # Step 2: Inversion
    inverse = input("\n🔁 Invert the seed meaning (optional): ").strip()

    # Step 3: Cross-domain scan (manual)
    print("\n📚 Consider: How does this idea appear in biology, physics, emotion, ethics, or systems?")
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

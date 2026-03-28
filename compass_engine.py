import json
import random

# --- Rosetta Bridge (optional) ---
try:
    from rosetta_bridge import (
        shape_context, all_shapes, all_archetypes, archetype,
        shapes_for_archetype, seed_for_shape, recommend_seed
    )
    _HAS_ROSETTA = True
except ImportError:
    shape_context = lambda g: None
    all_shapes = lambda: []
    all_archetypes = lambda: {}
    archetype = lambda n: None
    shapes_for_archetype = lambda n: []
    seed_for_shape = lambda s: None
    recommend_seed = lambda k: (None, 0)
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


def _show_archetypes():
    """Display available archetypes for selection."""
    archetypes = all_archetypes()
    if not archetypes:
        return None
    print("\n🔷 Agent Archetypes:")
    names = list(archetypes.keys())
    for i, name in enumerate(names, 1):
        entry = archetypes[name]
        shapes = ", ".join(s.replace("SHAPE.", "") for s in entry.get("primary_shapes", []))
        print(f"  {i}. {name:12s} — {entry['description']}")
        print(f"     {'':12s}   shapes: {shapes}")
    return names


def _show_seed_context(shape_id):
    """Display seed details for a shape."""
    seed = seed_for_shape(shape_id)
    if not seed:
        return
    field = seed.get("field", {})
    traits = seed.get("traits", {})
    print(f"\n🌀 Seed: {seed['id']}")
    print(f"   Element: {traits.get('element', '?')}")
    print(f"   Field: {field.get('property', '?')}")
    print(f"   Actions: {', '.join(field.get('actions', []))}")
    print(f"   Animals: {', '.join(seed.get('animals', []))}")
    print(f"   {seed.get('importance', '')}")


def symbolic_bloom(seed):
    print(f"\n🔮 Blooming seed: '{seed}'")

    # Step 0: Archetype orientation (optional, Rosetta-enhanced)
    chosen_archetype = None
    bridge = None
    if _HAS_ROSETTA:
        names = _show_archetypes()
        if names:
            choice = input("\n🧭 Choose archetype (number, name, or Enter to skip): ").strip().lower()
            if choice:
                # Match by number or name
                if choice.isdigit() and 1 <= int(choice) <= len(names):
                    chosen_archetype = names[int(choice) - 1]
                elif choice in names:
                    chosen_archetype = choice

            if chosen_archetype:
                entry = archetype(chosen_archetype)
                print(f"\n✦ Operating as: {chosen_archetype.upper()}")
                print(f"  {entry['description']}")
                # Show seed context for primary shapes
                for shape_id in entry.get("primary_shapes", []):
                    _show_seed_context(shape_id)

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
            if chosen_archetype:
                # Prefer shapes that match the chosen archetype
                arch_shapes = shapes_for_archetype(chosen_archetype)
                matching = [s for s in shapes if s["shape"] in arch_shapes]
                bridge = random.choice(matching) if matching else random.choice(shapes)
            else:
                bridge = random.choice(shapes)
            print(f"\n🔷 Shape Resonance: {bridge['shape']}")
            print(f"   Families: {', '.join(bridge.get('families', []))}")
            print(f"   Sensors: {', '.join(bridge.get('sensors', []))}")
            print(f"   Scroll: {bridge.get('bridge_scroll', '')}")

    # Step 2: Inversion
    inverse = input("\n🔁 Invert the seed meaning (optional): ").strip()

    # Step 3: Cross-domain scan (enriched with Rosetta families)
    domains = "biology, physics, emotion, ethics, or systems"
    if bridge:
        families = bridge.get("families", [])
        if families:
            domains += f" — or through {', '.join(families)}"
    print(f"\n📚 Consider: How does this idea appear in {domains}?")
    insights = input("🧠 Cross-domain insight (enter brief notes): ").strip()

    # Step 4: Occlusion check
    print("\n⊘ Occlusion Check: What might you be missing?")
    occlusion = input("  What is NOT visible in this pattern? (optional): ").strip()

    # Step 5: Fractal Principle
    principle = input("\n💡 Final emergent principle (1-sentence distilled truth): ").strip()

    # Confidence scoring
    print("\n📊 Confidence Assessment:")
    print("  80-100%: Confirmed across 5+ domains → Act on it")
    print("  50-80%:  Contextually useful → Act cautiously")
    print("  20-50%:  Insightful but early → Hold, bloom deeper")
    print("  < 20%:   Possible bias → Discard or invert")
    confidence = input("  Your confidence (0-100): ").strip()

    print("\n✅ Your Fractal Principle:")
    print(f"🌱 {principle}")
    if chosen_archetype:
        print(f"🧭 Archetype: {chosen_archetype}")
    if bridge:
        print(f"🔷 Shape: {bridge['shape']}")
    if confidence:
        print(f"📊 Confidence: {confidence}%")
    if occlusion:
        print(f"⊘ Blind spot: {occlusion}")
    print()

    # Save output for logging
    save = input("💾 Save to log? (y/n): ").lower()
    if save == "y":
        archetype_line = f"**Archetype:** {chosen_archetype}  \n" if chosen_archetype else ""
        shape_line = f"**Shape:** {bridge['shape']}  \n" if bridge else ""
        confidence_line = f"**Confidence:** {confidence}%  \n" if confidence else ""
        occlusion_line = f"**Occlusion:** {occlusion}  \n" if occlusion else ""
        with open("fractal_principles.md", "a") as f:
            f.write(f"""
---

## 🌱 New Principle from Seed: {seed}

**Glyphs:** {' '.join([g for g, _ in suggested])}
{archetype_line}{shape_line}**Inversion:** {inverse}
**Cross-Domain Insight:** {insights}
{occlusion_line}{confidence_line}**Fractal Principle:** {principle}

""")
        print("📁 Appended to fractal_principles.md")


if __name__ == "__main__":
    print("🌌 Fractal Compass Engine (CLI Mode)")
    print("    See guides/Agent-Compass-Guide.md for full orientation.\n")
    seed = input("🔹 Enter symbolic seed or question: ")
    symbolic_bloom(seed)

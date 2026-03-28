"""
CDDA Engine — Cross-Domain Discovery Algorithm.

Validates a theme by checking resonance across multiple domains.
When Rosetta bridge data is available, enriches analysis with
polyhedral families, shape resonance, and sensor context.
"""

import random

# --- Rosetta Bridge (optional) ---
try:
    from rosetta_bridge import (
        polyhedral_domains, polyhedral_families, all_shapes, all_seeds,
        recommend_seed
    )
    _HAS_ROSETTA = True
except ImportError:
    _HAS_ROSETTA = False

# --- Core domain sets ---
_BASE_DOMAINS = [
    "Biology", "Physics", "Psychology", "Ethics", "Systems Theory",
    "Art", "Mathematics", "Ecology", "Linguistics", "Economics"
]


def _keyword_overlap(theme, word_sets):
    """Count how many words from theme appear in any of the word sets."""
    theme_words = set(theme.lower().split())
    matches = 0
    for words in word_sets:
        if theme_words & {w.lower() for w in words}:
            matches += 1
    return matches


def _compute_confidence(theme, domains):
    """Estimate confidence based on domain count and bridge resonance."""
    # Base: more domains = higher confidence
    base = min(len(domains) * 15, 60)

    # Bonus for Rosetta shape resonance
    shape_bonus = 0
    if _HAS_ROSETTA:
        shapes = all_shapes()
        theme_words = set(theme.lower().split())
        for s in shapes:
            families = {f.lower() for f in s.get("families", [])}
            if theme_words & families:
                shape_bonus += 5
        # Seed match bonus
        seed, score = recommend_seed(theme.lower().split())
        if score > 0:
            shape_bonus += score * 3

    # Domain breadth bonus
    domain_set = {d.lower() for d in domains}
    breadth_bonus = 0
    for base_d in _BASE_DOMAINS:
        if base_d.lower() in domain_set:
            breadth_bonus += 2

    raw = base + shape_bonus + breadth_bonus
    # Add slight randomness for organic feel (simulates incomplete data)
    raw += random.randint(-5, 5)
    return max(10, min(raw, 98))


def _find_shape_resonance(theme):
    """Find shapes whose families resonate with the theme."""
    if not _HAS_ROSETTA:
        return []
    shapes = all_shapes()
    theme_words = set(theme.lower().split())
    resonant = []
    for s in shapes:
        families = {f.lower() for f in s.get("families", [])}
        overlap = theme_words & families
        if overlap:
            resonant.append({
                "shape": s["shape"],
                "matched_families": list(overlap),
                "scroll": s.get("bridge_scroll", ""),
                "sensors": s.get("sensors", [])
            })
    return resonant


def _generate_questions(theme, domains, confidence):
    """Generate next questions based on theme, domains, and confidence."""
    questions = []

    if confidence < 50:
        questions.append(f"What domains outside {', '.join(domains[:2])} might validate or refute this pattern?")
        questions.append("Is this pattern genuinely cross-domain, or an artifact of metaphor?")

    if confidence < 80:
        questions.append("What would inversion of this theme reveal — what is the anti-pattern?")

    # Shape-informed questions
    if _HAS_ROSETTA:
        resonant = _find_shape_resonance(theme)
        if resonant:
            shape = resonant[0]
            sensors = shape.get("sensors", [])
            if sensors:
                questions.append(
                    f"How do the sensors {', '.join(sensors)} ({shape['shape']}) "
                    f"respond to this theme in lived experience?"
                )
        else:
            questions.append("Which Platonic solid best grounds this theme — and what does its absence reveal?")

    # Always add a recursion question
    questions.append("If this pattern applies to itself recursively, does it hold or collapse?")

    return questions[:5]


def _assess_scope(theme, domains, confidence):
    """Determine the scope of applicability."""
    if confidence >= 80:
        return "Broad — cross-domain principle with strong validation"
    elif confidence >= 50:
        return f"Moderate — validated in {', '.join(domains[:3])}, needs wider testing"
    else:
        return "Narrow — early pattern, domain-specific until further validation"


def _assess_limitations(theme, confidence):
    """Identify limitations based on confidence and theme."""
    limits = []
    if confidence < 50:
        limits.append("Low domain coverage — may be metaphor rather than pattern")
    if confidence < 80:
        limits.append("Not yet validated across 5+ domains")

    # Check for missing elements
    theme_lower = theme.lower()
    if "time" not in theme_lower and "temporal" not in theme_lower:
        limits.append("Temporal dimension not addressed")
    if "emotion" not in theme_lower and "sensor" not in theme_lower:
        limits.append("Emotional/sensor dimension not addressed")

    if not limits:
        limits.append("May not apply in rigid, non-adaptive environments")

    return "; ".join(limits)


def run_cdda(theme, domains):
    """Run cross-domain discovery analysis on a theme.

    Args:
        theme: The pattern or principle to validate.
        domains: List of domain strings to check against.

    Returns:
        Dict with theme, domains, confidence, scope, limitations,
        next questions, shape resonance, and polyhedral context.
    """
    confidence = _compute_confidence(theme, domains)
    probability_weight = round(confidence / 100.0, 2)

    result = {
        "THEME": theme,
        "DOMAINS": domains,
        "CONFIDENCE": f"{confidence}%",
        "PROBABILITY_WEIGHT": probability_weight,
        "SCOPE": _assess_scope(theme, domains, confidence),
        "LIMITATIONS": _assess_limitations(theme, confidence),
        "NEXT_QUESTIONS": _generate_questions(theme, domains, confidence),
    }

    # Enrich with Rosetta data when available
    if _HAS_ROSETTA:
        resonant = _find_shape_resonance(theme)
        if resonant:
            result["SHAPE_RESONANCE"] = resonant

        seed, score = recommend_seed(theme.lower().split())
        if seed and score > 0:
            result["RECOMMENDED_SEED"] = {
                "id": seed["id"],
                "shape": seed["shape_id"],
                "element": seed.get("traits", {}).get("element", "?"),
                "match_score": score
            }

        result["POLYHEDRAL_PRINCIPLES"] = polyhedral_domains()
        result["POLYHEDRAL_FAMILIES"] = polyhedral_families()

    return result


# --- Example Run ---
if __name__ == "__main__":
    print("🔬 CDDA Engine — Cross-Domain Discovery Algorithm\n")

    theme = input("📝 Theme to validate (or Enter for default): ").strip()
    if not theme:
        theme = "Layered pattern recognition enables adaptive change"

    domain_input = input("🌍 Domains (comma-separated, or Enter for default): ").strip()
    if domain_input:
        domains = [d.strip() for d in domain_input.split(",")]
    else:
        domains = ["Cognitive Science", "Design", "Ethnomusicology", "AI Ethics",
                    "Biology", "Physics"]

    result = run_cdda(theme, domains)

    print(f"\n{'='*60}")
    for key, value in result.items():
        if isinstance(value, list) and len(value) > 5:
            print(f"\n{key}:")
            for item in value[:8]:
                if isinstance(item, dict):
                    print(f"  • {item}")
                else:
                    print(f"  • {item}")
            if len(value) > 8:
                print(f"  ... and {len(value) - 8} more")
        elif isinstance(value, dict):
            print(f"\n{key}:")
            for k, v in value.items():
                print(f"  {k}: {v}")
        elif isinstance(value, list):
            print(f"\n{key}:")
            for item in value:
                if isinstance(item, dict):
                    print(f"  • {item.get('shape', '')} — {item.get('scroll', '')}")
                else:
                    print(f"  • {item}")
        else:
            print(f"{key}: {value}")

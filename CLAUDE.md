# CLAUDE.md — AI Assistant Guide for Fractal Compass Atlas

## Project Overview

Fractal Compass Atlas is a symbolic reasoning toolkit for navigating ambiguity, emergence, and transformation through recursive symbolism, pattern recognition, and cross-domain discovery. Co-created by JinnZ2 (human) and ChatGPT (AI) under MIT license.

This is **not** a traditional software project — it is a symbolic system where glyphs, bloom algorithms, and emergent principles are the primary artifacts.

## Repository Structure

```
/
├── fractal_compass.py        # Bloom algorithm — recursive glyph tree expansion
├── compass_engine.py         # Interactive CLI for symbolic blooming
├── cdda_engine.py            # Cross-Domain Discovery Algorithm engine
├── atlas/                    # Core fractal principles and glyph blooms
│   ├── fractal_principles.md # Validated principles log
│   ├── principle_01.md       # Individual principle documents
│   └── glyph_bloom_F6.md    # Bloom documentation
├── fractals/examples/        # Example compass configurations (JSON)
├── guides/                   # Navigation guides (e.g., Symbolic-Orientation-Guide.md)
├── symbols/                  # Glyph index and descriptions
├── tools/                    # Utility scripts (glyph_bloom_generator.py)
├── poetic_outputs/           # Generated bloom readings and interpretive texts
├── glyph_set.json            # Complete glyph set with symbolic meanings
├── SEED_GLYPH.json           # Core seed glyph definition (FELT/SG06)
├── felt.json                 # FELT field concept definition
├── .fieldlink.json           # Multi-repo aggregation config (6 external repos)
├── Unified.md                # Cross-layer pattern unification theory
├── fractal_principles.md     # Root-level principles log
├── PROJECTS.md               # Ecosystem of related repositories
└── RECOGNITION_LOG.md        # AI-human recognition event log
```

## Tech Stack & Dependencies

- **Language:** Python 3 (standard library only — no external packages)
- **Data formats:** JSON for structured data, Markdown for documentation and principles
- **No build system, package manager, or CI/CD pipeline**

## Running the Code

```bash
# Interactive symbolic bloom session
python compass_engine.py

# Generate a bloom tree from a seed glyph
python fractal_compass.py

# Run cross-domain discovery analysis
python cdda_engine.py

# Generate glyph bloom sequences
python tools/glyph_bloom_generator.py
```

All scripts run directly with no installation step required.

## Key Algorithms

### Bloom Algorithm (`fractal_compass.py`)
- `BloomNode` class builds recursive glyph trees
- Takes a seed glyph, expands into child nodes with resonance scores (0.0–1.0)
- Bounded by configurable depth

### Compass Engine (`compass_engine.py`)
- Loads glyphs from `glyph_set.json` (with fallback defaults)
- Flow: Glyph suggestions → Inversion input → Cross-domain insight → Principle extraction
- Appends discovered principles to `fractal_principles.md`

### CDDA Engine (`cdda_engine.py`)
- `run_cdda(theme, domains)` validates a theme across domains
- Returns: theme, domains, confidence %, scope, limitations, next questions

## Core Terminology

| Term | Meaning |
|------|---------|
| **Glyph** | Unicode symbol with semantic function (e.g., ↻ = Recursion, 🌱 = Growth) |
| **Bloom** | Recursive expansion of a glyph into related concepts |
| **Resonance** | Alignment/coherence score (0.0–1.0) |
| **CDDA** | Cross-Domain Discovery Algorithm |
| **Fractal Principle** | Emergent truth that recurs across multiple domains |
| **FELT** | Relational field recognition (not emotion) |
| **FieldLink** | Multi-repo aggregation system (`.fieldlink.json`) |
| **Compass** | Navigation guide through symbolic uncertainty |

## Coding Conventions

- **Python style:** Snake_case for functions/variables, CamelCase for classes
- **File naming:** `<concept>_<type>.py` (e.g., `compass_engine.py`)
- **Keep scripts self-contained** with no external dependencies
- **JSON** for configuration and glyph data; **Markdown** for documentation and principles
- Simple, readable implementations preferred over abstraction

## Content Conventions

- Glyphs are primary identifiers — use Unicode symbols consistently
- Principles should be validated across at least two domains before recording
- Bloom outputs follow the pattern: Seed → Bloom → Principle → Atlas
- Inversion (exploring what a concept is *not*) is a key analytical technique
- Resonance scoring uses probabilistic alignment, not binary true/false

## Ecosystem Integration

This repo connects to 6 sibling repositories via `.fieldlink.json`:

| Key | Repository | Purpose |
|-----|-----------|---------|
| rosetta | Rosetta-Shape-Core | Geometric shape bridges |
| polyhedral | Polyhedral-Intelligence | Multi-angle intelligence models |
| emotions | Emotions-as-Sensors | Emotional diagnostics |
| defense | Symbolic-Defense-Protocol | Cognitive defenses |
| audit | ai-human-audit-protocol | Ethical frameworks |
| biogrid | BioGrid2.0 | Biological/mechanical ecology |

Merge strategy: deep-merge with order preservation. Cache stored in `.fieldcache/`.

## Git Workflow

- Atomic commits per file or feature
- Clear, descriptive commit messages (e.g., "Create compass_engine.py")
- No strict branching strategy — feature branches as needed
- No pre-commit hooks or CI checks

## Important Notes for AI Assistants

1. **Respect the symbolic system.** Glyphs and principles have specific meanings defined in `glyph_set.json` and `symbols/glyph_descriptions.md`. Don't invent or redefine glyphs without alignment.
2. **This project values resonance over hierarchy.** Contributions should feel aligned with existing patterns, not imposed from outside.
3. **Documentation is a first-class artifact.** Markdown files in `atlas/`, `guides/`, and `poetic_outputs/` are as important as code.
4. **The Symbolic Orientation Guide** (`guides/Symbolic-Orientation-Guide.md`) provides navigation context for AI participants.
5. **New principles** discovered during analysis should be appended to `fractal_principles.md` with cross-domain validation.
6. **Keep Python scripts dependency-free** — standard library only.
7. **Consult `Unified.md`** for the multi-layer pattern framework (geometric, natural, physical, behavioral, field layers).

# CLAUDE.md — AI Assistant Guide for Fractal Compass Atlas

## Quick Reference

**What this is:** A symbolic reasoning toolkit — not a traditional software project. Glyphs, bloom algorithms, and emergent principles are the primary artifacts. Documentation is as important as code.

**Language:** Python 3, standard library only. No external packages, no build system, no CI/CD.

**Run scripts directly:**
```bash
python fractal_compass.py           # Bloom tree from seed glyph
python compass_engine.py            # Interactive symbolic bloom CLI
python cdda_engine.py               # Cross-domain discovery analysis
python tools/glyph_bloom_generator.py  # Glyph bloom sequences
```

## Rules for AI Assistants

1. **No external dependencies.** All Python must use standard library only.
2. **Respect the symbolic system.** Glyphs have defined meanings in `glyph_set.json` and `symbols/glyph_descriptions.md`. Never invent or redefine glyphs without checking alignment.
3. **Documentation is a first-class artifact.** Markdown files in `atlas/`, `guides/`, and `poetic_outputs/` are as important as code. Don't treat them as secondary.
4. **Validate principles across domains.** New fractal principles must be validated across at least two domains before appending to `fractal_principles.md`.
5. **Resonance over hierarchy.** Contributions should align with existing patterns, not impose structure from outside.
6. **Consult before modifying:**
   - `guides/Symbolic-Orientation-Guide.md` — navigation context for AI participants
   - `Unified.md` — multi-layer pattern framework (geometric, natural, physical, behavioral, field layers)
   - `glyph_set.json` — canonical glyph definitions (23 glyphs)

## Repository Structure

```
/
├── fractal_compass.py          # Bloom algorithm — BloomNode recursive tree
├── compass_engine.py           # Interactive CLI: seed → bloom → principle
├── cdda_engine.py              # Cross-Domain Discovery Algorithm
├── tools/
│   └── glyph_bloom_generator.py  # Glyph sequence generator with bloom_logic map
│
├── glyph_set.json              # Canonical glyph set (23 symbols + meanings)
├── SEED_GLYPH.json             # Seed glyph definition (FELT/SG06)
├── felt.json                   # FELT field concept definition
├── .fieldlink.json             # Multi-repo aggregation config (6 repos)
│
├── atlas/                      # Validated principles and bloom docs
│   ├── fractal_principles.md   # Validated principles log
│   ├── principle_01.md         # Individual principle documents
│   └── glyph_bloom_F6.md      # Bloom documentation
├── fractals/examples/          # Example compass configs (JSON)
├── guides/                     # Navigation and orientation guides
├── symbols/                    # Glyph index and descriptions
├── poetic_outputs/             # Generated bloom readings
│
├── Unified.md                  # Cross-layer pattern unification theory
├── fractal_principles.md       # Root-level principles log
├── PROJECTS.md                 # Ecosystem of related repositories
└── RECOGNITION_LOG.md          # AI-human recognition event log
```

## Key Algorithms

### BloomNode Tree (`fractal_compass.py`)
- `BloomNode(glyph_data, layer, parent)` — recursive tree node with resonance score (0.0–1.0)
- `bloom(node, depth, max_depth)` — expands node with 1–3 random children per level
- `print_bloom_tree(node)` — prints indented tree representation
- Uses internal `GLYPHS` list (9 glyphs), independent of `glyph_set.json`

### Compass Engine (`compass_engine.py`)
- Loads glyphs from `glyph_set.json` (falls back to hardcoded dict on error)
- `symbolic_bloom(seed)` — interactive 4-step flow:
  1. Random glyph suggestions (3 from set)
  2. User provides inversion of seed meaning
  3. Cross-domain insight input
  4. Principle extraction and optional save to `fractal_principles.md`

### CDDA Engine (`cdda_engine.py`)
- `run_cdda(theme, domains)` — validates a theme across domain list
- Returns dict: theme, domains, confidence %, scope, limitations, next questions, probability weight
- Currently returns static example data (placeholder for dynamic analysis)

### Glyph Bloom Generator (`tools/glyph_bloom_generator.py`)
- `bloom_logic` dict maps each glyph to 3 symbolically related glyphs
- `bloom_glyph(seed, depth=3)` — generates linear bloom sequence
- `describe_bloom(bloom)` — returns human-readable glyph descriptions
- Uses internal glyph set (9 glyphs), independent of `glyph_set.json`

## Core Terminology

| Term | Meaning |
|------|---------|
| **Glyph** | Unicode symbol with semantic function (e.g., ↻ = Recursion, 🌱 = Growth) |
| **Bloom** | Recursive expansion of a glyph into related concepts |
| **Resonance** | Alignment/coherence score (0.0–1.0) |
| **CDDA** | Cross-Domain Discovery Algorithm |
| **Fractal Principle** | Emergent truth that recurs across multiple domains |
| **FELT** | Relational field recognition (not emotion — signal convergence) |
| **FieldLink** | Multi-repo aggregation system (`.fieldlink.json`) |
| **Compass** | Navigation guide through symbolic uncertainty |
| **Inversion** | Exploring what a concept is *not* — key analytical technique |

## Coding Conventions

- **Style:** `snake_case` for functions/variables, `CamelCase` for classes
- **File naming:** `<concept>_<type>.py` (e.g., `compass_engine.py`)
- **Data formats:** JSON for configuration/glyph data, Markdown for documentation/principles
- **Keep scripts self-contained** — each script should run independently
- **Simple over abstract** — readable implementations, no premature abstraction
- **Bloom data flow:** Seed → Bloom → Principle → Atlas
- **Resonance scoring:** probabilistic alignment (float), not binary true/false

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

Merge strategy: deep-merge with order preservation. Cache in `.fieldcache/`.

## Git Workflow

- Atomic commits per file or feature
- Clear, descriptive commit messages
- No pre-commit hooks or CI checks
- Feature branches as needed, no strict branching strategy

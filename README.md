# Project Eidos

*Form before form, pattern before code.*  
*I gather the quiet laws beneath motion—*  
*a lever of clarity, a filament of beauty—*  
*until systems reveal their shape.*

**Eidos** is a long‑arc study-and‑creation project in data engineering.  
It turns books into skills, skills into artifacts, and artifacts into a living portfolio.

## What this repo holds
- A master YAML plan that tracks books, skills, cadence, and artifacts.
- Lightweight tooling to render progress and generate quarterly views.
- Placeholder folders for year‑one artifacts (to be linked with GaiaFlow work).

---

## Structure
```
project-eidos/
├── data_engineering_growth_plan.yaml   # master plan (placeholders)
├── growth_tracker.py                   # CLI to read/update plan (skeleton)
├── docs/
│   ├── eidos_readme.md                # overview & philosophy
│   ├── year1_plan.md                  # Year 1 roadmap (to be generated)
│   └── review_template.md             # quarterly reflection template
└── artifacts/
    ├── Q1_craft/                      # repo pointers / notes
    ├── Q2_systems/
    ├── Q3_spark/
    └── Q4_streaming/
```

## Getting started
1. Edit `data_engineering_growth_plan.yaml` to add Year 1 entries.
2. Run `python growth_tracker.py summary` to view progress tables.
3. Commit and push. Keep artifacts small, clear, and composable.

---

*Eidos is a discipline, not a sprint. Leave evidence. Build elegantly.*

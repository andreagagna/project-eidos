# Project Eidos

*Form before form, pattern before code.*  
*I gather the quiet laws beneath motion—*  
*a lever of clarity, a filament of beauty—*  
*until systems reveal their shape.*

**Eidos** is a place to practice designing data systems and keep evidence of the decisions behind them. The current focus is to choose data models, reason about partial failures, and defend an architecture when its requirements change.

## Start with a decision

1. Pick a problem from the [practice roadmap](docs/roadmap.md) or from a project you already work on. Write down your choice and the assumption it depends on.
2. Test the assumption with a few records, a counterexample, or a design review. Keep the work in the project where it belongs.
3. Use the [weekly review](docs/review_template.md) to record what you learned. When you have something worth revisiting, append one entry under `evidence` in the [plan](data_engineering_growth_plan.yaml).

Each entry has a `skill`, a sentence under `demonstrates`, and a `link`. Use a path from this repository's root for local work, or a permalink to a decision, PR, or experiment in another project. Two examples are the [Week 1 reflection on data quality](artifacts/Q1_craft/pragmatic_reflections_01.md) and [cinema-monitor’s decision to parse structured seat data](https://github.com/andreagagna/cinema-monitor/blob/e891c7371b58bb91ba9cb1d176a3b168a129b517/docs/decisions.md#1-switch-from-screenshots-to-svg-parsing).

## Run the tracker

Use Python 3.10 or newer with `venv` and `pip` available. If Debian or Ubuntu reports that `ensurepip` is unavailable, install the venv package for the system Python with `sudo apt install python3-venv`. From the repository root on macOS or Linux, run

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python growth_tracker.py summary
python growth_tracker.py list-books
```

On Windows PowerShell, create the environment with `py -3 -m venv .venv` and activate it with `.\.venv\Scripts\Activate.ps1`, then run the same three `python` commands.

`summary` shows linked evidence first, then artifact and reading counts. To record a finished book, set its `status.completed` to the finish date (`YYYY-MM-DD`) in the plan. The tracker calculates reading progress as completed books divided by listed books. A reflection can count as evidence even while the book is in progress.

Run the regression tests with `python -m unittest discover -s tests`. The [project overview](docs/eidos_readme.md) explains the learning philosophy, and the [original Year 1 plan](docs/year1_plan.md) preserves the reading sequence and proposed portfolio projects.

---

*Eidos is a discipline, not a sprint. Leave evidence. Build elegantly.*

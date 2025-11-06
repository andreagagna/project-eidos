#!/usr/bin/env python3
import argparse
import sys
import yaml
import pathlib

PLAN_PATH = pathlib.Path(__file__).parent / "data_engineering_growth_plan.yaml"


def load_plan():
    if not PLAN_PATH.exists():
        print("Plan file not found:", PLAN_PATH)
        sys.exit(1)
    with open(PLAN_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def cmd_summary():
    plan = load_plan()
    metrics = plan.get("metrics", {})
    books = plan.get("books", [])
    artifacts = plan.get("artifacts", [])
    print("\nEidos — Plan Summary")
    print("-" * 40)
    print(f"Books (total): {metrics.get('total_books', len(books))}")
    print(f"Books completed: {metrics.get('books_completed', 0)}")
    print(f"Average OPI: {metrics.get('avg_opi', 0.0)}")
    print(f"Artifacts: {metrics.get('total_artifacts', len(artifacts))}")
    print(f"Progress (%): {metrics.get('progress_pct', 0)}")
    print("\nPillars:")
    for p in plan.get("pillars", []):
        print(f"  - {p.get('id')}: {p.get('name')}")


def cmd_list_books():
    plan = load_plan()
    books = plan.get("books", [])
    if not books:
        print("No books yet. Edit data_engineering_growth_plan.yaml to add entries.")
        return
    print("\nBooks")
    print("-" * 40)
    for b in books:
        print(
            f"{b.get('id', '?')}: {b.get('title', '?')} — pillar {b.get('pillar', '?')} (OPI {b.get('opi', '?')})"
        )


def main():
    parser = argparse.ArgumentParser(description="Eidos Growth Tracker")
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("summary")
    sub.add_parser("list-books")
    args = parser.parse_args()
    if args.cmd == "summary":
        cmd_summary()
    elif args.cmd == "list-books":
        cmd_list_books()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

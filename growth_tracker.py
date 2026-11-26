#!/usr/bin/env python3
import argparse
from datetime import date
from pathlib import Path
from statistics import mean

import yaml

PLAN_PATH = Path(__file__).resolve().with_name("data_engineering_growth_plan.yaml")


def load_plan():
    with PLAN_PATH.open(encoding="utf-8") as source:
        plan = yaml.safe_load(source)
    if not isinstance(plan, dict):
        raise ValueError("expected a YAML mapping at the top level")
    for section in ("books", "artifacts", "pillars", "evidence"):
        records = plan.get(section, [])
        if not isinstance(records, list) or not all(
            isinstance(record, dict) for record in records
        ):
            raise ValueError(f"{section} must be a list of records")
    for item in plan.get("evidence", []):
        for field in ("skill", "demonstrates", "link"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                raise ValueError(f"each evidence entry needs a {field} value")
    return plan


def book_is_complete(book):
    status = book.get("status")
    if status is None:
        return False
    book_id = book.get("id", "?")
    if not isinstance(status, dict):
        raise ValueError(f"{book_id}: status must contain started or completed dates")
    completed = status.get("completed")
    if completed is None:
        return False
    message = f"{book_id}: completed must be a date (YYYY-MM-DD) or null"
    # PyYAML returns a date for an unquoted ISO date and a string for a quoted one.
    value = str(completed)
    try:
        parsed = date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(message) from error
    if parsed.isoformat() != value:
        raise ValueError(message)
    return True


def cmd_summary():
    plan = load_plan()
    books = plan.get("books", [])
    artifacts = plan.get("artifacts", [])
    completed = sum(book_is_complete(book) for book in books)
    progress = 100 * completed / len(books) if books else 0
    scores = [book["opi"] for book in books if book.get("opi") is not None]
    if any(type(score) not in (int, float) for score in scores):
        raise ValueError("book OPI must be a number or null")
    planned = sum(artifact.get("status") == "planned" for artifact in artifacts)
    print("\nEidos — Plan Summary")
    print("-" * 40)
    print("Learning evidence:")
    evidence = plan.get("evidence", [])
    if not evidence:
        print("  No evidence linked yet.")
    for item in evidence:
        print(f"  - {item['skill']}: {item['demonstrates']}\n    {item['link']}")
    print(f"\nArtifacts: {len(artifacts)} ({planned} planned)")
    print(f"Books (total): {len(books)}")
    print(f"Books completed: {completed}")
    print(f"Reading progress (%): {progress:.1f}")
    print(f"Average OPI: {mean(scores):.2f}" if scores else "Average OPI: n/a")
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
    sub.add_parser(
        "summary", help="show learning evidence, artifacts, and reading progress"
    )
    sub.add_parser("list-books", help="list the reading resources in the plan")
    args = parser.parse_args()
    try:
        if args.cmd == "summary":
            cmd_summary()
        elif args.cmd == "list-books":
            cmd_list_books()
        else:
            parser.print_help()
    except (OSError, ValueError, yaml.YAMLError) as error:
        parser.exit(1, f"{PLAN_PATH}: {error}\n")


if __name__ == "__main__":
    main()

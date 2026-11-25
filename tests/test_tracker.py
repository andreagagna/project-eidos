import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


class TrackerTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        script = Path(__file__).resolve().parents[1] / "growth_tracker.py"
        self.script = shutil.copy(script, self.root)
        self.plan = self.root / "data_engineering_growth_plan.yaml"

    def run_cli(self, command):
        return subprocess.run(
            [sys.executable, self.script, command], capture_output=True, text=True
        )

    def test_editing_a_book_updates_progress_even_with_legacy_metrics(self):
        books = [{"id": "A", "opi": 4}, {"id": "B", "opi": 5, "status": None}]
        plan = {
            "books": books,
            "metrics": {
                "total_books": 9,
                "books_completed": 0,
                "progress_pct": 0,
                "avg_opi": 0,
                "total_artifacts": 0,
            },
            "artifacts": [{"status": "planned"}, {"status": "completed"}],
        }
        self.plan.write_text(yaml.safe_dump(plan), encoding="utf-8")
        result = self.run_cli("summary")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Books completed: 0", result.stdout)

        books[0]["status"] = {"completed": "2026-11-25"}
        self.plan.write_text(yaml.safe_dump(plan), encoding="utf-8")
        result = self.run_cli("summary")
        self.assertEqual(result.returncode, 0, result.stderr)
        for line in (
            "Books (total): 2",
            "Books completed: 1",
            "Reading progress (%): 50.0",
            "Average OPI: 4.50",
            "Artifacts: 2 (1 planned)",
        ):
            self.assertIn(line, result.stdout.splitlines())

    def test_evidence_is_visible_without_books_or_artifacts(self):
        evidence = {
            "skill": "Recovery",
            "demonstrates": "Replays a batch.",
            "link": "replay.sql",
        }
        self.plan.write_text(yaml.safe_dump({"evidence": [evidence]}), encoding="utf-8")
        result = self.run_cli("summary")
        self.assertEqual(result.returncode, 0, result.stderr)
        for text in (*evidence.values(), "Reading progress (%): 0.0", "Artifacts: 0"):
            self.assertIn(text, result.stdout)
        result = self.run_cli("list-books")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("No books yet.", result.stdout)

    def test_unquoted_completion_date_and_unfinished_book(self):
        self.plan.write_text(
            "books:\n"
            "  - {id: A, title: Storage, status: {completed: 2026-11-25}}\n"
            "  - {id: B, title: Streams, status: {started: 2026-11-25, completed: null}}\n",
            encoding="utf-8",
        )
        result = self.run_cli("summary")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Books completed: 1", result.stdout)
        self.assertIn("Average OPI: n/a", result.stdout)
        result = self.run_cli("list-books")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("A: Storage", result.stdout)
        self.assertIn("B: Streams", result.stdout)

    def test_invalid_plans_report_the_file_and_exit_nonzero(self):
        for content in (
            "",
            "books: [",
            "books: DE01",
            "books: [{status: {completed: later}}]",
            "books: [{status: {completed: 20261125}}]",
            "evidence: [{skill: Recovery, demonstrates: Replays a batch.}]",
        ):
            with self.subTest(content=content):
                self.plan.write_text(content, encoding="utf-8")
                result = self.run_cli("summary")
                self.assertNotEqual(result.returncode, 0)
                self.assertIn(str(self.plan), result.stderr)
                self.assertNotIn("Traceback", result.stderr)

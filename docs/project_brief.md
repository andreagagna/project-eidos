# Project Eidos and its hands-on companion

Eidos is a self-paced data engineering project for 2026–2028. Its aim is to develop the judgment to design a data system, explain why it behaves as it does, and revise a choice when the evidence changes. Eidos keeps the learning roadmap and a record of what the learner can demonstrate. A companion repository would provide regular practice writing, debugging, and testing the code behind those decisions.

## Scope and roadmap

The four pillars are **Foundations & Craft**, **Data Systems & Infrastructure**, **Streaming & Scalability**, and **Intelligence & Lifecycle Integration**. Year 1 develops the first three through four ordered stages. Each stage has a checkpoint tied to work the learner can inspect. Reading, implementation, and review can take place in different weeks. [Year 1 roadmap](year1_plan.md)

| Year 1 stage | Reading resources | Planned work and checkpoint |
| --- | --- | --- |
| Craft & Flow | *The Pragmatic Programmer* and *Accelerate* | **A01 — Engineering Ethos & CI Metrics.** Document a change that improved maintainability. Trace one change through delivery and choose a useful CI/CD measure. |
| Systems & Warehousing | *Fundamentals of Data Engineering* and *The Data Warehouse Toolkit* | **A02 — GaiaFlow Core Dataflow.** Map the path from source to consumer. Demonstrate which questions a dimensional model can answer and explain the grain of its fact table. |
| Distributed Processing | *Designing Data-Intensive Applications* and *Spark: The Definitive Guide* | **A03 — Spark & Kafka Integration Demo, batch component.** Build a Spark pipeline and use a replay test to check its recovery behavior. |
| Streaming Integration | *Kafka: The Definitive Guide*, with *Streaming Systems* as an optional follow-up | **A03, streaming component.** Extend the pipeline with Kafka ingestion, an Exasol sink, and an orchestration DAG. Defend the design against a freshness target and record how it recovers from interruption. |

The YAML plan records books, checkpoints, planned artifacts, and links to learning evidence. A small Python CLI reads it with PyYAML. Its `summary` command shows evidence and reading progress, and `list-books` lists the reading resources. For implementation details, pair the readings with the documentation for the runtime in use. [Growth plan](../data_engineering_growth_plan.yaml) · [Tracker](../growth_tracker.py) · [Apache Spark documentation](https://spark.apache.org/documentation/)

## Learning method

1. **Choose a question.** Start with the current reading or a decision from a project. Write down the assumption behind your choice and what you expect to observe.
2. **Test the choice.** Use a small implementation, query, measurement, or design review. Compare the result with your prediction and explain a discrepancy or trade-off.
3. **Keep the evidence where the work lives.** When a result demonstrates a skill, add its link and a one-sentence claim to Eidos. Use the short review to capture what you decided, what tested it, and what would change your mind. [Review template](review_template.md)
4. **Leave a place to resume.** End a session with the next page, question, or command. Return to the stage checkpoint when you have evidence for its question.

## What the hands-on companion needs

The proposed companion is a separate practice repository for short, runnable problems. Eidos supplies the sequence and larger portfolio goals. The companion should also be useful when a single technique needs practice between stages.

| Practice area | Skills to exercise |
| --- | --- |
| Python | Write and test transformations, parse inputs, handle errors, and debug unexpected behavior. |
| SQL | Reason about grain and cardinality, write joins and window queries, and use query plans to investigate performance. |
| PySpark | Work with DataFrames, inspect execution plans, and test how partitioning and replay affect results. |

For the first version, organize problems by skill and document how to run them locally. Python and SQL problems should run on their own. PySpark problems should specify how to start a local Spark session.

Give each problem a clear prompt, small reproducible inputs, expected behavior, and a command that checks the learner’s solution. A learner should be able to attempt a problem and get useful feedback in one short session. Keeping the inputs and checks with the solution makes it easy to resume after a break.

Keep solutions, tests, and observations in the companion. When a result supports a Year 1 checkpoint or changes a design decision, link that specific file or commit from the Eidos plan and say what it demonstrates. Routine drills can stay entirely in the companion.

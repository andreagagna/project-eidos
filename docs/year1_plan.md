# Year 1 Roadmap — Eidos

Year 1 moves from the craft of changing software to the design of a streaming pipeline. Follow the four stages in order, at your own pace. A reading session, a small experiment, and a portfolio project can happen on different weeks.

**A place to resume.** The [Week 1 reflection](../artifacts/Q1_craft/pragmatic_reflections_01.md#action-pledge--week-2) ends with a concrete idea for the next session. Find one piece of duplicated work, then refactor or document it. A before-and-after example and a sentence about why the change helped are enough to pick up the thread of *The Pragmatic Programmer*.

## 1. Craft & Flow

Read *The Pragmatic Programmer*, then *Accelerate*. Use the first to develop your Engineering Ethos note from changes you have actually made. With the second, trace one change from commit to deployment. Where did it spend the most time waiting?

**A01 — Engineering Ethos & CI Metrics.** Start the CI/CD mini-dashboard with the measure that would help you decide what to improve in that delivery process.

## 2. Systems & Warehousing

Read *Fundamentals of Data Engineering* and *The Data Warehouse Toolkit*. Follow one record from source to consumer, then write down what one row of your fact table represents. To test the model, try two orders and a correction that arrives the next day. For GaiaFlow, use two sensor readings and a revised measurement. Can your model answer both “what did we report yesterday?” and “what do we know now?”

**A02 — GaiaFlow Core Dataflow.** Keep the dataflow sketch and a small dimensional model with example rows and a query. To explore database internals, compare the query plan before and after adding an index, then measure the cost of inserting rows.

## 3. Distributed Processing

Read *Designing Data-Intensive Applications* and *Spark: The Definitive Guide*. Carry the same records into a small Spark ETL pipeline. Predict the totals if a worker writes its result and stops before recording its checkpoint. Replay the input, compare the totals, and explain how the pipeline handles a repeated delivery. Use the [Spark documentation](https://spark.apache.org/documentation/) for the version you run.

**A03 — Spark & Kafka Integration Demo, batch component.** Keep the runnable Spark pipeline, a replay test, and an architecture note about the recovery choice. These become the starting point for streaming.

## 4. Streaming Integration

Read *Kafka: The Definitive Guide*, with *Streaming Systems* as an optional follow-up. Give the pipeline a concrete freshness requirement. Would a scheduled batch meet it? What cost and recovery responsibilities would continuous ingestion add?

**A03 — streaming component.** Build the Kafka → Exasol demo and its orchestration DAG. Keep a run log showing how it recovers from an interruption. To close Year 1, try the design on an unfamiliar dataset and record which assumption you had to revise.

## Keeping your place

At the end of a session, leave the next page, question, or command in the note you already use. After a gap, start there. When an experiment changes your thinking, the [short review](review_template.md) gives you three prompts. Link the result in the [YAML plan](../data_engineering_growth_plan.yaml) if you want to find it again.

The Q1–Q4 artifact folders follow these four stages. The [original calendar](https://github.com/andreagagna/project-eidos/blob/65aca161a5e46bad654cb62bda9d5eec67eaa3c5/docs/year1_plan.md) records the dates and six-hour weekly estimate used in the first draft.

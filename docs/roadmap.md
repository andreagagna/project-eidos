# Architecture practice through May 2027

The aim for this cycle is to design a small data system, explain what can go wrong, and defend a choice when a requirement changes. Pick a question that fits the time available that week. An existing project, a local SQL database, or a handful of PySpark records can provide the evidence.

| Capability | Question to investigate | Evidence to keep |
| --- | --- | --- |
| Database internals | Which index helps this query, and what does it cost on writes? | Query plans and measurements for the same dataset with and without the index. |
| Data modelling | What does one row represent when an order can be corrected after purchase? | Two candidate models and an example query that gives a different answer under each. |
| Distributed systems | If a worker retries after writing its output, can it count the same order twice? | A replayable failure case, the expected totals, and the assumption that makes recovery safe. |
| Architecture and judgment | Under a stated freshness target and budget, when would batch or incremental processing be appropriate? | A decision record with two alternatives, the costs of each, and a condition that would change the choice. |

## First exercise

Start with a daily customer-total table. Write the expected result for two orders, one repeated delivery, and a correction that arrives the following day. Decide how to identify a correction. Compare rebuilding the affected day's totals with updating them incrementally. Save the first design before testing it.

Run both approaches against those records. Then ask a reviewer what happens if a worker stops after publishing totals and before recording its checkpoint. Record which totals you observed and whether the design needs to change. A short SQL script and a paragraph explaining the decision are enough.

## Reading and review

Choose a chapter when a question calls for it. Kimball is useful for deciding the grain of a table. *Designing Data-Intensive Applications* provides background on storage, replication, and failure. For Spark exercises, pair the book with the [Apache Spark documentation](https://spark.apache.org/documentation/) for the runtime you use. The [original Year 1 plan](year1_plan.md) lists the full reading sequence.

Try a ten-minute [weekly review](review_template.md) after a meaningful decision. At the end of the cycle, take an unfamiliar design problem, save a first attempt, and invite a challenge. Compare it with the first exercise. Which requirements did you uncover on your own? Which failure did you anticipate? What evidence changed your choice?

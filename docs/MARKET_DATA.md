# Market data used for the mechanical-role seed update

The seed update adds five entry-level mechanical and manufacturing roles using
aggregated evidence from the datasets supplied locally in October 2026.

| Source | Used for |
| --- | --- |
| `indian-job-market-dataset-2025.xlsx` | Role titles, skills, experience ranges, and disclosed salary bands across broad Indian job categories. |
| `job_market_india.csv` | Fresher mechanical, production, quality, and trainee job examples and salary signals. |
| `indian_tech_jobs_2026.csv` | Validation that the normalised schema can represent the supplied 2026 job-listing structure. It is not used to estimate mechanical entry-level salary because its matching records are primarily experienced or technology-adjacent. |
| `Indian_Fresher_Salary_Skills_2025.csv` | Entry-level skill and salary schema validation. It contains no mechanical-role records, so it is not used to estimate mechanical roles. |

The broad job-market workbook contains matching rows for Mechanical Design
Engineer, Production Engineer, Quality Engineer, Maintenance Engineer, and
Mechanical Engineer. For rows with up to one year minimum experience and a
disclosed salary, midpoint medians were approximately 2.9, 2.4, 2.5, 3.2, and
2.9 LPA respectively. The seed values are rounded, explainable estimates, not
live salary guarantees.

Raw source files remain outside the repository because they are user-supplied
downloads and include large datasets. The decision system consumes only the
normalised role records generated into `data/seed/seed_roles.csv`.

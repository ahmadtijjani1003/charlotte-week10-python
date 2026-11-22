# Week 10 Class 2 Homework — Completed

## Project contents

- `homework_pandas.py` — solution for Part B, using six invented well-day readings.
- `ANSWERS_Part_A_and_C.md` — written responses for Part A and the 150–200 word interpretation for Part C.
- `pandas_production_lab.py` — the previously supplied/completed class practical script.
- `data/daily_production.csv` — the actual daily production CSV supplied for the class practical.
- `data/production_enriched.csv` — enriched output from the class practical, when provided.
- `outputs/` — folder for any homework run output (the script prints its results to the terminal).

## Run the homework script

Install Pandas if it is not already installed:

```bash
python -m pip install pandas
```

Run:

```bash
python homework_pandas.py
```

The script prints the DataFrame, shape, dtypes, producing observations, total liquid, and missing oil count.

## Units and data notes

Oil, water and total liquid are measured in barrels per day (bpd). The six rows in `homework_pandas.py` are invented sample readings because Part B explicitly asks for invented well-day readings. The supplied `daily_production.csv` is included separately as the real class dataset and is not substituted for the six invented homework rows.

## Part D — GitHub evidence

From the repository root, create/switch to the Class 2 branch and commit the homework files:

```bash
git switch -c feature/class-02-pandas
git add homework_pandas.py ANSWERS_Part_A_and_C.md README.md data/ pandas_production_lab.py
git commit -m "Complete Week 10 Class 2 Pandas homework"
git push -u origin feature/class-02-pandas
```

Open a Pull Request from `feature/class-02-pandas` into `main`. Include a short summary of the script, the input/sample data, and the test evidence. Do not commit virtual environments, credentials, or unnecessary generated files.

# Week 10 Class 2 — Pandas Production Lab

## What the program does
The Python program reads `daily_production.csv` with Pandas and parses `date`
as timestamps. It reports the data shape and quality counts, selects rows with
`status == "PRODUCING"`, and creates an enriched copy of the original data.

The enriched file keeps all seven original columns and adds exactly two:
- `total_liquid_bpd` = `oil_bpd + water_bpd` (barrels per day).
- `pressure_kpa` = `pressure_psi * 6.8947572932` (kilopascals).

## How to run
Install Pandas if needed:

```bash
python -m pip install pandas
```

Run from this folder:

```bash
python pandas_production_lab.py
```

Input: `daily_production.csv`  
Output: `outputs/production_enriched.csv`

## Results from the supplied class dataset
- DataFrame shape: 16 rows and 7 columns.
- Missing oil readings: 1.
- Missing pressure readings: 1.
- Unique wells: 4.
- PRODUCING observations: 14.
- Other status observations: 2.

## Operational observation
The dataset contains 14 PRODUCING observations out of 16.
One oil reading is missing for WELL-12 on 2026-11-02, while one pressure
reading is missing for WELL-12 on 2026-11-03. The missing oil value occurs on
a PRODUCING observation, so its total liquid calculation remains missing too.
These gaps should be checked before using the readings for operational
comparisons or decisions.

## Why missing values must not be set to zero
A missing measurement means no value was recorded; it does not prove the
measurement was zero. Replacing a missing oil reading with zero could falsely
report no oil production and distort totals. The program preserves missing
values as NaN, including in derived calculations when an input is missing.

# Week 10 Class 3 — Production Surveillance Lab

## Files
- `production_surveillance_lab_solve.py` — completed Python analysis.
- `production_surveillance.csv` — input data supplied for the lab. Keep this file in the same folder as the Python script.
- `requirements.txt` — Python package requirements.
- `.gitignore` — excludes the virtual environment, environment file, Python cache, and generated output folder.

## Setup
Open a terminal in this folder and create a virtual environment:

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

Install the required package:

```bash
python -m pip install -r requirements.txt
```

## Run the analysis

```bash
python production_surveillance_lab_solve.py
```

The script reads `production_surveillance.csv` from the same folder and creates an `outputs` folder containing:

- `valid_active_records.csv`
- `well_summary.csv`
- `field_summary.csv`

## Filtering and calculation rules
- Keep only rows whose status is `ACTIVE`.
- Oil and water readings must both be present and nonnegative.
- Missing oil or water readings are not replaced with zero.
- Oil, water, and pressure readings are converted to numeric values; invalid values become missing.
- A missing pressure reading alone does not remove a record.
- `liquid_bbl` is calculated as oil plus water.
- `water_cut_pct` is calculated as water divided by liquid, multiplied by 100.
- If liquid production is zero, water cut is left missing to avoid division by zero.
- Well summaries are grouped by field and well.
- Field summaries count unique wells and total oil, water, and liquid production.
- The top well is selected by total valid ACTIVE oil production; ties are sorted alphabetically by well ID.

## Results for the supplied CSV
- Valid ACTIVE records: 20
- Top oil-producing well: `WELL-B1` — 1,122 bbl
- North field: 2 wells; 1,669 bbl oil; 622 bbl water; 2,291 bbl liquid.
- South field: 2 wells; 1,661 bbl oil; 768 bbl water; 2,429 bbl liquid.

## Git reminder
The class guide specifies the branch:

```bash
git switch -c feature/class-03-aggregation
```

Commit the Python source, input CSV, `requirements.txt`, `.gitignore`, and README. Do not commit `.venv`, `.env`, or the generated `outputs` folder.

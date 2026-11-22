# Production Surveillance Report

## 1. Scope

This report analyses the supplied synthetic `production_surveillance.csv` using Pandas. The source contains **24 observations**, covering **4 wells** across **2 fields**.

Observation dates: **2026-10-01 to 2026-10-06**.

## 2. Data preparation and filtering

- Converted `oil_bbl`, `water_bbl`, and `pressure_psi` to numeric values; invalid values become missing.
- Retained only rows with status `ACTIVE`.
- Required both oil and water readings to be present and nonnegative.
- Did not replace missing production readings with zero.
- Calculated `liquid_bbl = oil_bbl + water_bbl`.
- Calculated `water_cut_pct = water_bbl / liquid_bbl × 100`; when liquid is zero, water cut is left missing.

**20 records were retained** and **4 were excluded**.

### Excluded observations

| record_id   | well_id   | status   | exclusion_reason      |
|:------------|:----------|:---------|:----------------------|
| R002        | WELL-A1   | ACTIVE   | Missing water reading |
| R010        | WELL-A2   | SHUT_IN  | Not ACTIVE            |
| R015        | WELL-B1   | ACTIVE   | Missing oil reading   |
| R023        | WELL-B2   | SHUT_IN  | Not ACTIVE            |

## 3. Well-level surveillance

| field   | well_id   |   records |   oil_total_bbl |   water_total_bbl |   liquid_total_bbl |   avg_pressure_psi |   avg_water_cut_pct |
|:--------|:----------|----------:|----------------:|------------------:|-------------------:|-------------------:|--------------------:|
| North   | WELL-A1   |         5 |             926 |               263 |               1189 |             2495.6 |               22.1  |
| North   | WELL-A2   |         5 |             743 |               359 |               1102 |             2340.8 |               32.58 |
| South   | WELL-B1   |         5 |            1122 |               186 |               1308 |             2823.2 |               14.19 |
| South   | WELL-B2   |         5 |             539 |               582 |               1121 |             2158.4 |               51.96 |

## 4. Field-level surveillance

| field   |   wells |   records |   oil_total_bbl |   water_total_bbl |   liquid_total_bbl |   avg_pressure_psi |
|:--------|--------:|----------:|----------------:|------------------:|-------------------:|-------------------:|
| North   |       2 |        10 |            1669 |               622 |               2291 |             2418.2 |
| South   |       2 |        10 |            1661 |               768 |               2429 |             2490.8 |

## 5. Key findings

- **Top oil-producing well:** WELL-B1, with **1,122 bbl** of valid ACTIVE oil production.
- **North field:** 1,669 bbl oil, 622 bbl water, 2,291 bbl liquid.
- **South field:** 1,661 bbl oil, 768 bbl water, 2,429 bbl liquid.
- South has slightly lower total oil than North, but higher total water and total liquid production.
- WELL-B2 has the highest average per-record water cut among the four wells, indicating a higher water share in its produced liquid during the retained observations.

## 6. Interpretation and limitations

These are synthetic, short-period observations (six dates per well). The report describes the supplied records only; it should not be treated as a forecast or a long-term reservoir performance assessment. Missing oil or water readings were excluded from production totals rather than imputed. Average water cut is calculated as the mean of each retained record's water-cut percentage.

## 7. Output files

- `valid_active_records.csv` — retained observations with calculated liquid and water cut.
- `well_summary.csv` — grouped metrics by field and well.
- `field_summary.csv` — grouped metrics by field.
- `excluded_records.csv` — excluded rows and the reason for exclusion.
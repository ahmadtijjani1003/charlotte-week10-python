"""Charlotte Project Week 10 Class 1 — Completed NumPy sensor lab.

Uses csv.DictReader and NumPy only (no pandas).
Blank numeric cells are converted to np.nan.
"""

from pathlib import Path
import csv
import numpy as np

DATA_FILE = Path(__file__).with_name("multiwell_sensor_readings.csv")
COLUMNS = ("pressure_psi", "temperature_f", "vibration_mm_s", "flow_bpd")


def load_numeric_sensor_matrix(csv_path=DATA_FILE):
    """Return (sample_ids, well_ids, numeric 2D ndarray); blanks -> np.nan."""
    sample_ids = []
    well_ids = []
    numeric_rows = []

    with open(csv_path, mode="r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            sample_ids.append(row["sample_id"])
            well_ids.append(row["well_id"])

            values = []
            for column in COLUMNS:
                value = row[column].strip()
                if value == "":
                    values.append(np.nan)
                else:
                    values.append(float(value))

            numeric_rows.append(values)

    matrix = np.array(numeric_rows, dtype=float)
    return sample_ids, well_ids, matrix


def convert_units(matrix):
    """Return new matrix: pressure kPa, temperature C, vibration, flow."""
    pressure_kpa = matrix[:, 0] * 6.8947572932
    temperature_c = (matrix[:, 1] - 32) * 5 / 9
    vibration = matrix[:, 2]
    flow = matrix[:, 3]

    processed_matrix = np.column_stack(
        (pressure_kpa, temperature_c, vibration, flow)
    )
    return processed_matrix


def analyze_sensor_matrix(sample_ids, well_ids, matrix):
    """Return thresholds, missing counts and numeric summaries."""
    pressure = matrix[:, 0]
    vibration = matrix[:, 2]
    flow = matrix[:, 3]
    well_ids_array = np.array(well_ids)

    # Part C: Boolean masks. Missing values are excluded explicitly.
    high_pressure_mask = (~np.isnan(pressure)) & (pressure > 3500)
    high_vibration_mask = (~np.isnan(vibration)) & (vibration > 6.0)

    high_pressure_sample_ids = np.array(sample_ids)[high_pressure_mask].tolist()

    # Part D: summaries ignore missing readings.
    pressure_average = np.nanmean(pressure)
    pressure_maximum = np.nanmax(pressure)
    flow_average = np.nanmean(flow)

    pressure_average_by_well = {}
    for well in np.unique(well_ids_array):
        well_mask = well_ids_array == well
        pressure_average_by_well[well] = np.nanmean(pressure[well_mask])

    return {
        "high_pressure_count": int(np.count_nonzero(high_pressure_mask)),
        "high_pressure_sample_ids": high_pressure_sample_ids,
        "high_vibration_count": int(np.count_nonzero(high_vibration_mask)),
        "missing_pressure_count": int(np.count_nonzero(np.isnan(pressure))),
        "missing_flow_count": int(np.count_nonzero(np.isnan(flow))),
        "average_pressure_psi": pressure_average,
        "maximum_pressure_psi": pressure_maximum,
        "average_flow_bpd": flow_average,
        "average_pressure_by_well_psi": pressure_average_by_well,
    }


def main():
    sample_ids, well_ids, matrix = load_numeric_sensor_matrix()

    # Part A: Load and inspect.
    print("PART A — LOAD AND INSPECT")
    print("shape:", matrix.shape)
    print("ndim:", matrix.ndim)
    print("dtype:", matrix.dtype)
    print("total elements:", matrix.size)
    print("first three rows:")
    print(matrix[:3])
    print("pressure column (psi):")
    print(matrix[:, 0])

    # Part B: Vectorized unit conversions.
    print("\nPART B — VECTORIZE")
    processed_matrix = convert_units(matrix)
    print("processed columns: [pressure_kpa, temperature_c, vibration_mm_s, flow_bpd]")
    print(np.round(processed_matrix, 2))

    # Parts C and D: Filter, assess and aggregate.
    report = analyze_sensor_matrix(sample_ids, well_ids, matrix)

    print("\nPART C — FILTER AND ASSESS")
    print("high-pressure count (> 3500 psi):", report["high_pressure_count"])
    print("high-pressure sample IDs:", report["high_pressure_sample_ids"])
    print("high-vibration count (> 6.0 mm/s):", report["high_vibration_count"])
    print("missing pressure entries:", report["missing_pressure_count"])
    print("missing flow entries:", report["missing_flow_count"])

    print("\nPART D — AGGREGATE")
    print(f"average pressure: {report['average_pressure_psi']:.2f} psi")
    print(f"maximum pressure: {report['maximum_pressure_psi']:.2f} psi")
    print(f"average flow: {report['average_flow_bpd']:.2f} bpd")
    print("average pressure by well:")
    for well, average in report["average_pressure_by_well_psi"].items():
        print(f"  {well}: {average:.2f} psi")

    # Part E is completed in README.md, requirements.txt and .gitignore.
    print("\nPART E — DOCUMENT AND SUBMIT")
    print("See README.md for setup, units, missing-value policy and interpretation.")


if __name__ == "__main__":
    main()

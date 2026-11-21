"""Week 10 Class 1 — NumPy in Drilling Analytics homework."""
from pathlib import Path
import csv
import numpy as np

DATA_FILE = Path(__file__).with_name("data") / "multiwell_sensor_readings.csv"
NUMERIC_COLUMNS = ("pressure_psi", "temperature_f", "vibration_mm_s", "flow_bpd")


def load_sensor_data(csv_path=DATA_FILE):
    sample_ids, well_ids, numeric_rows = [], [], []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            sample_ids.append(row["sample_id"])
            well_ids.append(row["well_id"])
            values = []
            for column in NUMERIC_COLUMNS:
                value = row[column].strip()
                values.append(np.nan if value == "" else float(value))
            numeric_rows.append(values)
    return sample_ids, well_ids, np.array(numeric_rows, dtype=float)


def main():
    sample_ids, well_ids, matrix = load_sensor_data()
    pressure = matrix[:, 0]
    vibration = matrix[:, 2]
    flow = matrix[:, 3]

    # Q5: both conditions must be true for a sample to be selected.
    combined_mask = (flow > 400) & (vibration > 6.0)
    print("Flow > 400 bpd AND vibration > 6.0 mm/s:")
    print(np.array(sample_ids)[combined_mask].tolist())

    # Q6: calculate each well's pressure range, ignoring NaN.
    well_array = np.array(well_ids)
    pressure_ranges = {}
    print("\nPressure range by well (psi):")
    for well in np.unique(well_array):
        well_mask = well_array == well
        values = pressure[well_mask]
        pressure_range = np.nanmax(values) - np.nanmin(values)
        pressure_ranges[well] = pressure_range
        print(f"{well}: {pressure_range:.2f}")

    widest = max(pressure_ranges, key=pressure_ranges.get)
    narrowest = min(pressure_ranges, key=pressure_ranges.get)
    print(
        f"Observation: {widest} has the widest pressure range "
        f"({pressure_ranges[widest]:.2f} psi), while {narrowest} "
        f"has the narrowest ({pressure_ranges[narrowest]:.2f} psi)."
    )

    # Q7: dividing by 3500 psi preserves missing values as NaN.
    ratios = pressure / 3500.0
    print("\nPressure ratios (pressure_psi / 3500):")
    print(np.round(ratios, 3))
    above_one = ratios > 1
    print("\nRatios above 1:")
    for sample_id, ratio in zip(np.array(sample_ids)[above_one], ratios[above_one]):
        print(f"{sample_id}: {ratio:.3f}")


if __name__ == "__main__":
    main()

"""Week 10 Class 2 Homework — Pandas well-day readings.

Run:
    python homework_pandas.py

Units:
    oil_bpd, water_bpd and total_liquid_bpd are barrels per day (bpd).
The six records below are invented practice readings, as required by Part B.
"""
import pandas as pd


def build_homework_dataframe() -> pd.DataFrame:
    """Build a DataFrame containing six invented well-day readings."""
    readings = [
        {"well_id": "WELL-01", "date": "2026-11-01", "status": "PRODUCING",
         "oil_bpd": 1250.0, "water_bpd": 350.0},
        {"well_id": "WELL-02", "date": "2026-11-01", "status": "PRODUCING",
         "oil_bpd": 980.0, "water_bpd": 420.0},
        {"well_id": "WELL-03", "date": "2026-11-01", "status": "SHUT-IN",
         "oil_bpd": 0.0, "water_bpd": 0.0},
        {"well_id": "WELL-01", "date": "2026-11-02", "status": "PRODUCING",
         "oil_bpd": None, "water_bpd": 375.0},
        {"well_id": "WELL-04", "date": "2026-11-02", "status": "PRODUCING",
         "oil_bpd": 1430.0, "water_bpd": 510.0},
        {"well_id": "WELL-02", "date": "2026-11-02", "status": "PRODUCING",
         "oil_bpd": 1025.0, "water_bpd": 390.0},
    ]
    df = pd.DataFrame(readings)
    df["date"] = pd.to_datetime(df["date"])
    return df


def main() -> None:
    df = build_homework_dataframe()

    print("FULL DATAFRAME")
    print(df)
    print("\nDataFrame shape:", df.shape)
    print("\nColumn data types:")
    print(df.dtypes)

    producing = df.loc[df["status"] == "PRODUCING"].copy()
    print("\nPRODUCING READINGS")
    print(producing)

    # Work on a separate copy. NaN is preserved if oil_bpd is missing.
    producing["total_liquid_bpd"] = (
        producing["oil_bpd"] + producing["water_bpd"]
    )
    print("\nPRODUCING READINGS WITH TOTAL LIQUID (bpd)")
    print(producing)

    missing_oil_count = int(df["oil_bpd"].isna().sum())
    print("\nMissing oil reading count:", missing_oil_count)


if __name__ == "__main__":
    main()

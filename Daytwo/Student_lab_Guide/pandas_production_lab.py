"""Week 10 Class 2 — Pandas production table profiling and enrichment."""
from pathlib import Path
import pandas as pd

INPUT_FILE = Path(__file__).with_name("daily_production.csv")
OUTPUT_FILE = Path(__file__).parent / "outputs" / "production_enriched.csv"


def load_production(path: Path = INPUT_FILE) -> pd.DataFrame:
    """Load the CSV and parse date values as timestamps."""
    return pd.read_csv(path, parse_dates=["date"])


def enrich_production(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy with total liquid and converted pressure columns."""
    enriched = df.copy()
    enriched["total_liquid_bpd"] = enriched["oil_bpd"] + enriched["water_bpd"]
    enriched["pressure_kpa"] = enriched["pressure_psi"] * 6.8947572932
    return enriched


def select_producing(df: pd.DataFrame) -> pd.DataFrame:
    """Select PRODUCING observations without changing the input."""
    return df.loc[df["status"] == "PRODUCING"].copy()


def data_quality_counts(df: pd.DataFrame) -> dict:
    """Count missing oil and pressure readings and the unique wells."""
    return {
        "missing_oil_readings": int(df["oil_bpd"].isna().sum()),
        "missing_pressure_readings": int(df["pressure_psi"].isna().sum()),
        "unique_wells": int(df["well_id"].nunique()),
    }


def main() -> None:
    """Run the production profiling and export the enriched CSV."""
    df = load_production()
    quality = data_quality_counts(df)
    producing = select_producing(df)
    enriched = enrich_production(df)

    print("Data shape:", df.shape)
    print("Data quality counts:")
    for item, count in quality.items():
        print(f"  {item}: {count}")
    print("Producing observations:", len(producing))

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    enriched.to_csv(OUTPUT_FILE, index=False)
    print("Enriched CSV saved to:", OUTPUT_FILE)


if __name__ == "__main__":
    main()

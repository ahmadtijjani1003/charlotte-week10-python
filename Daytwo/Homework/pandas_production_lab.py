
from pathlib import Path
import pandas as pd

INPUT_FILE = Path(__file__).with_name("daily_production.csv")
OUTPUT_FILE = Path(__file__).parent / "outputs" / "production_enriched.csv"


def load_production(path: Path = INPUT_FILE) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"])
    return df


def enrich_production(df: pd.DataFrame) -> pd.DataFrame:
    enriched = df.copy()
    enriched["total_liquid_bpd"] = (
        enriched["oil_bpd"] + enriched["water_bpd"]
    )
    enriched["pressure_kpa"] = (
        enriched["pressure_psi"] * 6.8947572932
    )
    return enriched


def select_producing(df: pd.DataFrame) -> pd.DataFrame:
    return df.loc[df["status"] == "PRODUCING"].copy()


def data_quality_counts(df: pd.DataFrame) -> dict:
    return {
        "missing_oil_readings": int(df["oil_bpd"].isna().sum()),
        "missing_pressure_readings": int(df["pressure_psi"].isna().sum()),
        "unique_wells": int(df["well_id"].nunique())
    }


def main() -> None:
    df = load_production()

    quality = data_quality_counts(df)
    producing = select_producing(df)
    enriched = enrich_production(df)

    print("Data shape:", df.shape)
    print("Data quality counts:", quality)
    print("Producing observations:", len(producing))

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    enriched.to_csv(OUTPUT_FILE, index=False)

    print("Saved successfully:", OUTPUT_FILE)


if __name__ == "__main__":
    main()

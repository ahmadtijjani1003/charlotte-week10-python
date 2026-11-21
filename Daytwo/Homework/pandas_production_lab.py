"""Week 10 Class 2 — student starter. Fill TODOs. Do not submit notebook solutions."""
from pathlib import Path
import pandas as pd

INPUT_FILE = Path(__file__).with_name("daily_production.csv")
OUTPUT_FILE = Path(__file__).parent / "outputs" / "production_enriched.csv"

def load_production(path: Path = INPUT_FILE) -> pd.DataFrame:
    """Read input CSV and return a DataFrame with `date` parsed as dates."""
    # TODO: use pd.read_csv(..., parse_dates=[...])
    raise NotImplementedError

def enrich_production(df: pd.DataFrame) -> pd.DataFrame:
    """Return an independent copy with total_liquid_bpd and pressure_kpa columns."""
    # TODO: never replace missing readings with zero
    raise NotImplementedError

def select_producing(df: pd.DataFrame) -> pd.DataFrame:
    """Return rows whose status is PRODUCING; do not mutate input."""
    raise NotImplementedError

def data_quality_counts(df: pd.DataFrame) -> dict:
    """Return missing counts for oil_bpd and pressure_psi, and unique well count."""
    raise NotImplementedError

def main() -> None:
    """Load, enrich, inspect summary and export enriched CSV."""
    # TODO: print shape, missing counts, producing count; create outputs folder
    raise NotImplementedError

if __name__ == "__main__":
    main()

"""Week 10 Class 3 lab — production surveillance analysis."""
from pathlib import Path
import pandas as pd

REQUIRED = ["record_id", "date", "field", "well_id", "status", "oil_bbl", "water_bbl", "pressure_psi"]

def load_and_validate(path: str | Path) -> pd.DataFrame:
    df = pd.read_csv(path)
    missing = [c for c in REQUIRED if c not in df.columns]
    if missing:
        raise ValueError(f"CSV is missing required columns: {missing}")
    for c in ["oil_bbl", "water_bbl", "pressure_psi"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df

def active_valid_records(df: pd.DataFrame) -> pd.DataFrame:
    mask = (
        df["status"].eq("ACTIVE")
        & df["oil_bbl"].notna()
        & df["water_bbl"].notna()
        & df["oil_bbl"].ge(0)
        & df["water_bbl"].ge(0)
    )
    return df.loc[mask].copy()

def enrich_production(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result["liquid_bbl"] = result["oil_bbl"] + result["water_bbl"]
    result["water_cut_pct"] = (
        result["water_bbl"].div(result["liquid_bbl"]).mul(100)
        .where(result["liquid_bbl"].ne(0), pd.NA)
    )
    return result

def well_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby(["field", "well_id"], as_index=False)
        .agg(
            records=("record_id", "count"),
            oil_total_bbl=("oil_bbl", "sum"),
            water_total_bbl=("water_bbl", "sum"),
            liquid_total_bbl=("liquid_bbl", "sum"),
            avg_pressure_psi=("pressure_psi", "mean"),
            avg_water_cut_pct=("water_cut_pct", "mean"),
        )
        .sort_values(["field", "well_id"], kind="stable")
        .reset_index(drop=True)
    )
    return summary[["field", "well_id", "records", "oil_total_bbl",
                    "water_total_bbl", "liquid_total_bbl",
                    "avg_pressure_psi", "avg_water_cut_pct"]]

def field_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby("field", as_index=False)
        .agg(
            wells=("well_id", "nunique"),
            oil_total_bbl=("oil_bbl", "sum"),
            water_total_bbl=("water_bbl", "sum"),
            liquid_total_bbl=("liquid_bbl", "sum"),
        )
        .sort_values("field", kind="stable")
        .reset_index(drop=True)
    )
    return summary[["field", "wells", "oil_total_bbl",
                    "water_total_bbl", "liquid_total_bbl"]]

def top_well(df: pd.DataFrame) -> str:
    if df.empty:
        raise ValueError("Cannot determine the top well: there are no valid ACTIVE records.")
    totals = (
        df.groupby("well_id", as_index=False)["oil_bbl"].sum()
        .sort_values(["oil_bbl", "well_id"], ascending=[False, True], kind="stable")
    )
    return str(totals.iloc[0]["well_id"])

def main() -> None:
    source = Path(__file__).with_name("production_surveillance.csv")
    output = Path(__file__).with_name("outputs")
    output.mkdir(exist_ok=True)
    raw = load_and_validate(source)
    clean = enrich_production(active_valid_records(raw))
    clean.to_csv(output / "valid_active_records.csv", index=False)
    well_summary(clean).to_csv(output / "well_summary.csv", index=False)
    field_summary(clean).to_csv(output / "field_summary.csv", index=False)
    print(f"Valid ACTIVE rows: {len(clean)}; top oil well: {top_well(clean)}")

if __name__ == "__main__":
    main()

from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_RAW_PATH = PROJECT_ROOT / "data" / "raw" / "Telco-Customer-Churn.csv"


def load_raw_churn_data(path: Path = DEFAULT_RAW_PATH) -> pd.DataFrame:
    """
    Load the raw Telco churn CSV without any cleaning.
    """
    return pd.read_csv(path)


def load_and_clean_churn_data(path: Path = DEFAULT_RAW_PATH) -> pd.DataFrame:
    """
    Load the Telco churn data and apply basic cleaning.
    This should match what you were already doing in your notebooks.
    """
    df = pd.read_csv(path)

    # Drop customerID (not useful for modeling)
    if "customerID" in df.columns:
        df = df.drop(columns=["customerID"])

    # Convert TotalCharges to numeric and drop invalid rows
    if "TotalCharges" in df.columns:
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
        df = df.dropna(subset=["TotalCharges"])

    # Remove entries with tenure == 0
    if "tenure" in df.columns:
        df = df[df["tenure"] != 0].copy()

    # Encode Churn as 0/1
    if "Churn" in df.columns:
        df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    return df

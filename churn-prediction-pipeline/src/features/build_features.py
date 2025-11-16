# src/features/build_features.py
import pandas as pd


def add_churn_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add additional, more informative features for churn prediction.
    """
    df = df.copy()

    # 1) Number of services used (the more services, the more "locked in")
    service_cols = [
        "PhoneService",
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
    ]
    existing = [c for c in service_cols if c in df.columns]
    if existing:
        df["num_services"] = (df[existing] == "Yes").sum(axis=1)

    # 2) Tenure buckets (people early in their contract churn more)
    if "tenure" in df.columns:
        df["tenure_bucket"] = pd.cut(
            df["tenure"],
            bins=[0, 12, 24, 48, 72, float("inf")],
            labels=["0-1y", "1-2y", "2-4y", "4-6y", "6y+"],
            right=True,
        )

    # 3) Charges per tenure (rough "average monthly spend over lifetime")
    if {"TotalCharges", "tenure"} <= set(df.columns):
        df["charges_per_month_lifetime"] = df["TotalCharges"] / df["tenure"].replace(0, 1)

    # 4) Flags for common patterns
    if "InternetService" in df.columns:
        df["has_fiber_optic"] = (df["InternetService"] == "Fiber optic").astype(int)

    if "PaymentMethod" in df.columns:
        df["is_electronic_check"] = (df["PaymentMethod"] == "Electronic check").astype(int)

    if "PaperlessBilling" in df.columns:
        df["is_paperless"] = (df["PaperlessBilling"] == "Yes").astype(int)

    return df

import os
import pandas as pd


def ingest_data(
    source_path: str = "data/source/input.csv",
    output_path: str = "data/raw/data.csv",
) -> None:
    """
    Ingest data from an external source (API dump / S3 sync / shared folder).
    """

    if not os.path.exists(source_path):
        raise FileNotFoundError(f"Source file not found: {source_path}")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    df = pd.read_csv(source_path)

    # Minimal validation
    if df.empty:
        raise ValueError("Ingested data is empty")

    df.to_csv(output_path, index=False)
    print(f"Data ingested from {source_path} → {output_path}")


if __name__ == "__main__":
    ingest_data()

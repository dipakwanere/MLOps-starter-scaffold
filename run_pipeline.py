# run_pipeline.py
import os

# Import the functions defined in your src directory
from src.preprocessing import process_data
from src.train import train_model

# from src.ingestion import evaluate_model  # Assume this function exists


def main():
    # Define input/output paths
    RAW_DATA = "data/raw_data.csv"
    PROCESSED_DATA = "data/processed_data.csv"
    MODEL_PATH = "models/my_model.pkl"
    # METRICS_PATH = "reports/metrics.json"

    # Ensure directories exist (simple example)
    os.makedirs("data", exist_ok=True)
    os.makedirs("models", exist_ok=True)
    os.makedirs("reports", exist_ok=True)
    # Assume a raw_data.csv file is already in data/

    print("--- Starting ML Pipeline ---")

    # Step 1: Process Data
    process_data(RAW_DATA, PROCESSED_DATA)

    # Step 2: Train Model
    train_model(PROCESSED_DATA, MODEL_PATH)

    # Step 3: Evaluate Model
    # evaluate_model(MODEL_PATH, PROCESSED_DATA, METRICS_PATH)

    print("--- Pipeline Finished Successfully ---")


if __name__ == "__main__":
    main()

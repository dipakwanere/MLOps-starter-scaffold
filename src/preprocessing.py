# src/processing.py
import pandas as pd


def process_data(input_path, output_path):
    print(f"Processing data from {input_path}...")
    # ... logic to clean data, handle NaNs, etc. ...
    processed_data = pd.DataFrame({"feature": [1, 2, 3], "target": [0, 1, 0]})
    processed_data.to_csv(output_path, index=False)
    print("Data processed and saved.")

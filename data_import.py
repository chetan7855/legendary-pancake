import pandas as pd

def load_data(filepath):
    """Loads a CSV file into a DataFrame."""
    try:
        data = pd.read_csv(filepath)
        print(f"Data loaded successfully from {filepath}.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

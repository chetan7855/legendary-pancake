def inspect_data(data):
    """Prints a summary of the dataset."""
    print(f"Shape of data: {data.shape}")
    print(f"Columns: {data.columns.tolist()}")
    print(f"Missing values:\n{data.isnull().sum()}")
    print(f"Data types:\n{data.dtypes}")
    print(f"First few rows:\n{data.head()}")

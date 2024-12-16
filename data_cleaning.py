def clean_data(data):
    """Handles missing values and corrects data types."""
    # Fill missing numerical values with the median
    for col in data.select_dtypes(include=['float64', 'int64']):
        data[col] = data[col].fillna(data[col].median())

    # Fill missing categorical values with mode
    for col in data.select_dtypes(include=['object']):
        data[col] = data[col].fillna(data[col].mode()[0])

    print("Data cleaning completed.")
    return data

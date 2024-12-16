def merge_data(app_data, prev_data, key='SK_ID_CURR'):
    """Merges application and previous application data on a key."""
    merged_data = app_data.merge(prev_data, on=key, how='inner')
    print(f"Data merged. Shape: {merged_data.shape}")
    return merged_data

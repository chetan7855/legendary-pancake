from data_import import load_data
from data_inspection import inspect_data
from data_cleaning import clean_data
from univariate_analysis import plot_categorical, plot_numerical
from bivariate_analysis import plot_correlation
from data_merge import merge_data
import os

# Step 1: Create 'outputs' directory if it does not exist
os.makedirs('outputs', exist_ok=True)

# Step 2: Load datasets
application_data = load_data('data/application.csv')
previous_data = load_data('data/previous_application.csv')

# Step 3: Inspect datasets
print("\nInspecting Application Data:")
inspect_data(application_data)
print("\nInspecting Previous Application Data:")
inspect_data(previous_data)

# Step 4: Clean datasets
print("\nCleaning Application Data:")
application_data = clean_data(application_data)
print("\nCleaning Previous Application Data:")
previous_data = clean_data(previous_data)

# Step 5: Univariate Analysis
print("\nPerforming Univariate Analysis:")
plot_categorical(application_data, 'CODE_GENDER')  # Correct column name for gender
application_data['AGE_YEARS'] = application_data['DAYS_BIRTH'] / -365  # Convert age to years
plot_numerical(application_data, 'AGE_YEARS')  # Use the derived age in years

# Step 6: Bivariate Analysis
print("\nPerforming Bivariate Analysis:")
plot_correlation(application_data)

# Step 7: Merge datasets
print("\nMerging Application and Previous Application Data:")
merged_data = merge_data(application_data, previous_data)

# Step 8: Save cleaned and merged datasets
print("\nSaving Cleaned and Merged Data:")
application_data.to_csv('outputs/cleaned_application.csv', index=False)
previous_data.to_csv('outputs/cleaned_previous_application.csv', index=False)
merged_data.to_csv('outputs/merged_data.csv', index=False)

print("\nEDA Process Completed Successfully!")

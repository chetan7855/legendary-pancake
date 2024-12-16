# Credit EDA Project

This project performs Exploratory Data Analysis (EDA) on credit application data to identify patterns and insights that can help in decision-making for loan approvals. The analysis ensures that reliable applicants are not rejected and potential defaulters are identified, reducing financial risks for the company.

---

## **Project Structure**

```
legendary-pancake/
├── data/                     # Contains the input datasets
│   ├── application.csv
│   ├── previous_application.csv
├── outputs/                  # Contains the processed and merged datasets
│   ├── cleaned_application.csv
│   ├── cleaned_previous_application.csv
│   ├── merged_data.csv
├── scripts/                  # Contains all Python scripts
│   ├── main.py               # Main script to execute the project
│   ├── data_import.py        # Script for importing datasets
│   ├── data_inspection.py    # Script for inspecting datasets
│   ├── data_cleaning.py      # Script for handling missing values
│   ├── univariate_analysis.py # Script for univariate visualizations
│   ├── bivariate_analysis.py  # Script for bivariate analysis
│   ├── data_merge.py         # Script for merging datasets
├── README.md                 # Project overview and instructions
```

---

## **Features Implemented**

1. **Data Import**:
   - Loads application and previous application datasets.

2. **Data Inspection**:
   - Displays structure, missing values, and data types.

3. **Data Cleaning**:
   - Handles missing values for numerical and categorical columns.
   - Converts `DAYS_BIRTH` to `AGE_YEARS` for better interpretability.

4. **Univariate Analysis**:
   - Generates visualizations for categorical and numerical variables.

5. **Bivariate Analysis**:
   - Displays correlation heatmaps for numerical variables.

6. **Data Merging**:
   - Merges application and previous application datasets on `SK_ID_CURR`.

7. **Data Saving**:
   - Saves cleaned and merged datasets to the `outputs/` directory.

---

## **Getting Started**

### **Prerequisites**

- Python 3.8+
- Install required libraries:
  ```bash
  pip install pandas numpy matplotlib seaborn
  ```

### **Running the Project**

1. Clone the repository:
   ```bash
   git clone https://github.com/chetan7855/legendary-pancake.git
   ```

2. Navigate to the project folder:
   ```bash
   cd legendary-pancake
   ```

3. Place the datasets (`application.csv` and `previous_application.csv`) in the `data/` folder.

4. Run the main script:
   ```bash
   python scripts/main.py
   ```

---

## **Outputs**

- **Cleaned Datasets**:
  - `cleaned_application.csv`: Processed application data.
  - `cleaned_previous_application.csv`: Processed previous application data.
- **Merged Dataset**:
  - `merged_data.csv`: Combined dataset for further analysis.

---

## **License**

This project is licensed under the MIT License. See `LICENSE` for details.

---

## **Contributing**

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

---

## **Contact**

If you have any questions or issues, please contact [Chetan](https://github.com/chetan7855).


import pandas as pd
import re

# Load dataset
df = pd.read_excel(r'E:/Qurratulain/FHP-performance-testing-mobile-apps/dataset/Test Cases for all Applications.xlsx', engine='openpyxl') 

# Print the first few rows to check the data
print("Initial Data:\n", df.head())

# Function to extract numeric values from strings
def extract_numeric(val):
    if isinstance(val, str):
        # Use regex to extract numeric values from strings
        numeric_val = re.findall(r'\d+', val)
        if numeric_val:
            return float(numeric_val[0])  # Return the first numeric value found
        else:
            return None
    return val  # Return the value if it's already numeric

# Apply extraction to all columns
df_cleaned = df.applymap(extract_numeric)

# Drop rows with NaN (non-numeric) values
df_cleaned = df_cleaned.dropna()

# Print the cleaned data to verify that numeric data remains
print("\nCleaned Data:\n", df_cleaned.head())

# Function to calculate quartiles for the dataset
def calculate_quartiles(data):
    quartiles = {}
    for column in data.columns:
        if pd.api.types.is_numeric_dtype(data[column]):
            Q1 = data[column].quantile(0.25)
            Q2 = data[column].quantile(0.5)  # Median
            Q3 = data[column].quantile(0.75)
            quartiles[column] = {
                'Q1': Q1,
                'Median (Q2)': Q2,
                'Q3': Q3
            }
    return quartiles

# Calculate quartiles for the cleaned dataset
quartile_results = calculate_quartiles(df_cleaned)

# Display the results
for column, quartiles in quartile_results.items():
    print(f"{column}:")
    print(f"  Q1: {quartiles['Q1']}")
    print(f"  Median (Q2): {quartiles['Median (Q2)']}")
    print(f"  Q3: {quartiles['Q3']}")

# Convert the quartile results to a DataFrame
quartiles_df = pd.DataFrame.from_dict(quartile_results, orient='index')

# Save the quartiles to a CSV file
quartiles_df.to_csv(r'E:/Qurratulain/FHP-performance-testing-mobile-apps/quartiles_output_cleaned.csv')

# Print confirmation message
print("Quartiles have been saved to 'quartiles_output_cleaned.csv'")

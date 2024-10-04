import pandas as pd

# Load your dataset (adjust the path to your dataset)
df = pd.read_csv(r'E:/Qurratulain/FHP-performance-testing-mobile-apps/dataset.csv')  # Adjust file path

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

# Calculate quartiles for your dataset
quartile_results = calculate_quartiles(df)

# Display the results
for column, quartiles in quartile_results.items():
    print(f"{column}:")
    print(f"  Q1: {quartiles['Q1']}")
    print(f"  Median (Q2): {quartiles['Median (Q2)']}")
    print(f"  Q3: {quartiles['Q3']}")

# Convert the quartile results to a DataFrame
quartiles_df = pd.DataFrame.from_dict(quartile_results, orient='index')

# Save the quartiles to a CSV file
quartiles_df.to_csv(r'E:/Qurratulain/FHP-performance-testing-mobile-apps/quartiles_output.csv')

# Print confirmation message
print("Quartiles have been saved to 'quartiles_output.csv'")

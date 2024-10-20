import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Fuzzy Triangular Numbers based on linguistic terms
linguistic_to_tfn = {
    'Absolutely Important (AI)': (7, 9, 9),
    'Strongly Important (SI)': (5, 7, 9),
    'Fairly Important (FI)': (3, 5, 7),
    'Weakly Important (WI)': (1, 3, 5),
    'Equally Important (EI)': (1, 1, 1)
}

# Convert linguistic terms to fuzzy triangular numbers
def convert_linguistic_to_fuzzy(linguistic_weights):
    return [linguistic_to_tfn[term] for term in linguistic_weights]

# Fuzzy AHP Process
def run_fahp_process(file_path, custom_criteria, linguistic_weights):
    # Step 1: Load the data
    df = pd.read_excel(file_path)
    df.columns = custom_criteria

    # Step 2: Convert linguistic weights to fuzzy numbers
    fuzzy_values = convert_linguistic_to_fuzzy(linguistic_weights)

    # Step 3: Fuzzy calculations (synthetic extent, etc.)
    fuzzy_synthetic_extents = calculate_fuzzy_synthetic_extent(df.values, fuzzy_values)
    priority_weights = calculate_priority_weights(fuzzy_synthetic_extents, df.columns)

    # Save results to CSV and generate visualization
    results_path = f"{file_path.split('.')[0]}_results.csv"
    graph_path = f"{file_path.split('.')[0]}_results.png"
    save_results_to_csv_and_visualize(priority_weights, results_path, graph_path)

    return priority_weights, results_path, graph_path

# Synthetic extent calculation
def calculate_fuzzy_synthetic_extent(data, fuzzy_values):
    synthetic_extents = []
    for row in data:
        synthetic_extents.append(sum(fuzzy_values))
    return synthetic_extents

# Priority weight calculation based on fuzzy synthetic extent
def calculate_priority_weights(synthetic_extents, criteria):
    priority_weights = {criterion: 0 for criterion in criteria}
    for i, extent in enumerate(synthetic_extents):
        priority_weights[criteria[i]] = extent  # Simplified for demo purposes
    total_weight = sum(priority_weights.values())
    for criterion in priority_weights:
        priority_weights[criterion] /= total_weight
    return priority_weights

# Save results to CSV and visualize
def save_results_to_csv_and_visualize(data, results_path, graph_path):
    df = pd.DataFrame(list(data.items()), columns=['Criterion', 'Weight'])
    df.to_csv(results_path, index=False)

    # Visualization
    plt.figure(figsize=(10, 6))
    plt.bar(df['Criterion'], df['Weight'], color='skyblue')
    plt.xlabel('Criteria')
    plt.ylabel('Weight')
    plt.title('FAHP Criteria Weights')
    plt.savefig(graph_path)
    plt.close()

    print(f"Results saved to {results_path} and visualization saved to {graph_path}")

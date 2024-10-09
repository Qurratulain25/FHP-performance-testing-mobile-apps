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

# Step 2: Calculate Fuzzy Synthetic Extent for pairwise comparisons
def calculate_fuzzy_synthetic_extent(comparisons):
    l_sum, m_sum, u_sum = 0, 0, 0
    for (l, m, u) in comparisons:
        l_sum += l
        m_sum += m
        u_sum += u
    return (l_sum, m_sum, u_sum)

# Step 3: Degree of Possibility
def calculate_degree_of_possibility(S_i, S_j):
    l_i, m_i, u_i = S_i
    l_j, m_j, u_j = S_j
    if m_i >= m_j:
        return 1
    elif u_i <= l_j:
        return 0
    else:
        return (l_j - u_i) / ((m_i - u_j) - (l_j - l_i))

# Step 4: Priority Weights Calculation
def calculate_priority_weights(possibilities, criteria):
    priority_weights = {criterion: 0 for criterion in criteria}
    for (c1, c2), possibility in possibilities.items():
        priority_weights[c1] += possibility
    total_weight = sum(priority_weights.values())
    for criterion in priority_weights:
        priority_weights[criterion] /= total_weight
    return priority_weights

# Step 5: Save results to CSV
def save_results_to_csv_and_visualize(data, file_path, app_name):
    # Convert the dictionary into a DataFrame
    df = pd.DataFrame(list(data.items()), columns=['Criterion', 'Weight'])
    
    # Save the DataFrame to a CSV file
    df.to_csv(file_path, index=False)
    print(f"Results saved to {file_path}")
    
    # Visualization: Bar chart of the criteria weights
    plt.figure(figsize=(10, 6))
    plt.bar(df['Criterion'], df['Weight'], color='navy')  # Set color to navy blue
    plt.xlabel('Criteria')
    plt.ylabel('Weights')
    plt.title(f'FAHP Criteria Weights for {app_name}')  # Title includes the application name
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Save the plot as an image (optional) and display it
    image_file_path = file_path.replace('.csv', '.png')
    plt.savefig(image_file_path)  # Save as a PNG image
    plt.show()  # Display the plot
    
    print(f"Visualization saved to {image_file_path}")
import pandas as pd
from fahp_utils import calculate_fuzzy_synthetic_extent, calculate_priority_weights, save_results_to_csv_and_visualize


def run_fahp_for_github():
    # Step 1: Load dataset
    df = pd.read_excel('E:/Qurratulain/FHP-performance-testing-mobile-apps/dataset/GITHUB_combined.xlsx')

    # Step 2: Define the criteria and pairwise comparisons
    criteria = ['Elapsed Time', 'Throughput', 'Load/Network', 'Latency']

    # Pairwise comparisons based on linguistic judgments for GitHub
    pairwise_comparisons = {
        'Elapsed Time': [(5, 7, 9), (3, 5, 7), (3, 5, 7)],  # Comparisons with other criteria
        'Throughput': [(1, 3, 5), (3, 5, 7)],               # Comparisons with Load/Network, Latency
        'Load/Network': [(1, 1, 1)]                        # Comparisons with Latency
    }

    # Step 3: Calculate fuzzy synthetic extent for each criterion
    fuzzy_synthetic_extents = {criterion: calculate_fuzzy_synthetic_extent(comparisons) for criterion, comparisons in pairwise_comparisons.items()}

    # Step 4: Calculate priority weights (dummy values for possibilities)
    possibilities = {
        ('Elapsed Time', 'Throughput'): 0.85,
        ('Elapsed Time', 'Load/Network'): 0.9,
        ('Elapsed Time', 'Latency'): 0.9,
        ('Throughput', 'Load/Network'): 0.8,
        ('Throughput', 'Latency'): 0.85,
        ('Load/Network', 'Latency'): 0.7
    }
    
    priority_weights = calculate_priority_weights(possibilities, criteria)

    # Step 5: Save the results
    save_results_to_csv_and_visualize(priority_weights, 'results/github_fahp_results.csv','GitHub')

# Call the function
if __name__ == "__main__":
    run_fahp_for_github()

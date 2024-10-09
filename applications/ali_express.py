import pandas as pd
from fahp_utils import calculate_fuzzy_synthetic_extent, calculate_priority_weights, save_results_to_csv

def run_fahp_for_aliexpres():
    # Step 1: Load dataset
    df = pd.read_excel('dataset/ALI_EXPRESS_combined.xlsx')

    # Step 2: Define the criteria and pairwise comparisons
    criteria = ['Elapsed Time', 'Throughput', 'Load/Network', 'Latency']
    
    # Pairwise comparisons based on linguistic judgments for ALI EXPRESS
    pairwise_comparisons = {
        'Elapsed Time': [(5, 7, 9), (3, 5, 7), (3, 5, 7)],  # Comparisons with other criteria
        'Throughput': [(1, 3, 5), (3, 5, 7)],               # Comparisons with Load/Network, Latency
        'Load/Network': [(1, 3, 5)]                        # Comparisons with Latency
    }

    # Step 3: Calculate fuzzy synthetic extent for each criterion
    fuzzy_synthetic_extents = {criterion: calculate_fuzzy_synthetic_extent(comparisons) for criterion, comparisons in pairwise_comparisons.items()}

    # Step 4: Calculate priority weights (dummy values for possibilities)
    possibilities = {
        ('Elapsed Time', 'Throughput'): 0.8,
        ('Elapsed Time', 'Load/Network'): 0.9,
        ('Elapsed Time', 'Latency'): 1.0,
        ('Throughput', 'Load/Network'): 0.7,
        ('Throughput', 'Latency'): 0.8,
        ('Load/Network', 'Latency'): 0.6
    }
    
    priority_weights = calculate_priority_weights(possibilities, criteria)

    # Step 5: Save the results
    save_results_to_csv(priority_weights, 'results/ali_express_fahp_results.csv')

# Call the function
if __name__ == "__main__":
    run_fahp_for_aliexpres()

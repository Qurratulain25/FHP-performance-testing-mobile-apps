# fuzzy_ahp.py
#libraries used 
import numpy as np
import pandas as pd
# Step 1: Define the hierarchy for Fuzzy AHP

# Goal: Select the test cases that impact performance testing
goal = "Select test cases impacting performance testing of mobile applications"

# Criteria
criteria = ["Elapsed Time", "Throughput", "Load/Network", "Latency"]

# Alternatives: Test cases for Airbnb (as provided in the dataset)
alternatives = ["TC1", "TC2", "TC3", "TC4", "TC5", "TC6", "TC7", "TC8", "TC9", "TC10"]

# Display the hierarchy
def display_hierarchy():
    print(f"Goal: {goal}")
    print(f"Criteria: {criteria}")
    print(f"Alternatives: {alternatives}")

if __name__ == "__main__":
    display_hierarchy()

#Step 2: Pair wise Comparison

# Fuzzy Triangular Numbers (l, m, u) for pairwise comparisons
# These are provided based on linguistic judgments for the Airbnb application.

fuzzy_pairwise_comparisons = {
    "Elapsed Time": [(4, 5, 6), (6, 7, 8), (2, 3, 4), (5, 6, 7)],  # Elapsed Time for all criteria
    "Throughput": [(5, 6, 7), (2, 3, 4), (4, 5, 6), (6, 7, 8)],    # Throughput
    "Load/Network": [(2, 3, 4), (4, 5, 6), (6, 7, 8), (2, 3, 4)],   # Load/Network
    "Latency": [(5, 6, 7), (4, 5, 6), (2, 3, 4), (13, 14, 15)]     # Latency
}

# Display the fuzzy pairwise comparison matrix for each criterion
def display_fuzzy_comparisons():
    for criterion, comparisons in fuzzy_pairwise_comparisons.items():
        print(f"Fuzzy comparisons for {criterion}: {comparisons}")

if __name__ == "__main__":
    display_hierarchy()  # Step 1: Display the hierarchy
    display_fuzzy_comparisons()  # Step 2: Display the pairwise comparisons
# Step 3: Calculate Fuzzy Synthetic Extent
# This function calculates the fuzzy synthetic extent for each criterion

def calculate_fuzzy_synthetic_extent(comparisons):
    # Initialize variables to hold the sum of fuzzy comparisons
    l_sum, m_sum, u_sum = 0, 0, 0
    
    # Sum up the fuzzy triangular numbers
    for (l, m, u) in comparisons:
        l_sum += l
        m_sum += m
        u_sum += u

    # Return the sum of the fuzzy numbers
    return (l_sum, m_sum, u_sum)

# Calculate fuzzy synthetic extents for each criterion
def calculate_synthetic_extents():
    synthetic_extents = {}
    
    # Iterate over each criterion and calculate the synthetic extent
    for criterion, comparisons in fuzzy_pairwise_comparisons.items():
        synthetic_extents[criterion] = calculate_fuzzy_synthetic_extent(comparisons)
    
    return synthetic_extents

if __name__ == "__main__":
    display_hierarchy()  # Step 1: Display the hierarchy
    display_fuzzy_comparisons()  # Step 2: Display the pairwise comparisons

    # Step 3: Calculate and display fuzzy synthetic extents
    fuzzy_synthetic_extents = calculate_synthetic_extents()
    print("\nFuzzy Synthetic Extents:")
    for criterion, extent in fuzzy_synthetic_extents.items():
        print(f"{criterion}: {extent}")
# Step 4: Calculate the possible degree between fuzzy synthetic extents

def calculate_degree_of_possibility(S_i, S_j):
    l_i, m_i, u_i = S_i
    l_j, m_j, u_j = S_j
    
    # Case 1: If the middle value of S_i is greater or equal to the middle value of S_j
    if m_i >= m_j:
        return 1
    # Case 2: If the upper value of S_i is less than the lower value of S_j
    elif u_i <= l_j:
        return 0
    # Case 3: Calculate the degree of possibility using the given formula
    else:
        return (l_j - u_i) / ((m_i - u_j) - (l_j - l_i))

# Calculate the degree of possibility between all criteria
def calculate_possibilities(extents):
    possibilities = {}
    criteria = list(extents.keys())
    
    for i in range(len(criteria)):
        for j in range(i+1, len(criteria)):
            S_i = extents[criteria[i]]
            S_j = extents[criteria[j]]
            possibility = calculate_degree_of_possibility(S_i, S_j)
            possibilities[(criteria[i], criteria[j])] = possibility
    
    return possibilities

if __name__ == "__main__":
    display_hierarchy()  # Step 1: Display the hierarchy
    display_fuzzy_comparisons()  # Step 2: Display the pairwise comparisons

    # Step 3: Calculate fuzzy synthetic extents
    fuzzy_synthetic_extents = calculate_synthetic_extents()
    print("\nFuzzy Synthetic Extents:")
    for criterion, extent in fuzzy_synthetic_extents.items():
        print(f"{criterion}: {extent}")
    
    # Step 4: Calculate and display the possible degrees
    possibilities = calculate_possibilities(fuzzy_synthetic_extents)
    print("\nDegree of Possibilities between Criteria:")
    for (criterion1, criterion2), possibility in possibilities.items():
                print(f"V({criterion1} >= {criterion2}): {possibility}")
# Step 5: Calculate the Priority Weights

# Calculate the priority weights based on the degree of possibilities
def calculate_priority_weights(possibilities, criteria):
    priority_weights = {}
    for criterion in criteria:
        # Sum the possibilities where the criterion is greater or equal to others
        weight = 0
        for (c1, c2), possibility in possibilities.items():
            if c1 == criterion:
                weight += possibility
        priority_weights[criterion] = weight
    
    # Normalize the weights so they sum to 1
    total_weight = sum(priority_weights.values())
    for criterion in priority_weights:
        priority_weights[criterion] /= total_weight
    
    return priority_weights

if __name__ == "__main__":
    display_hierarchy()  # Step 1: Display the hierarchy
    display_fuzzy_comparisons()  # Step 2: Display the pairwise comparisons

    # Step 3: Calculate fuzzy synthetic extents
    fuzzy_synthetic_extents = calculate_synthetic_extents()
    print("\nFuzzy Synthetic Extents:")
    for criterion, extent in fuzzy_synthetic_extents.items():
        print(f"{criterion}: {extent}")
    
    # Step 4: Calculate and display the possible degrees
    possibilities = calculate_possibilities(fuzzy_synthetic_extents)
    print("\nDegree of Possibilities between Criteria:")
    for (criterion1, criterion2), possibility in possibilities.items():
        print(f"V({criterion1} >= {criterion2}): {possibility}")
    
    # Step 5: Calculate and display the priority weights
    priority_weights = calculate_priority_weights(possibilities, criteria)
    print("\nPriority Weights for Each Criterion:")
    for criterion, weight in priority_weights.items():
        print(f"{criterion}: {weight}")
# Save the fuzzy synthetic extents to a CSV file
def save_synthetic_extents_to_csv(synthetic_extents, file_path):
    synthetic_df = pd.DataFrame.from_dict(synthetic_extents, orient='index', columns=["L", "M", "U"])
    synthetic_df.to_csv(file_path)
    print(f"Fuzzy synthetic extents have been saved to {file_path}")

# Save the priority weights to a CSV file
def save_priority_weights_to_csv(priority_weights, file_path):
    weights_df = pd.DataFrame(list(priority_weights.items()), columns=["Criterion", "Weight"])
    weights_df.to_csv(file_path, index=False)
    print(f"Priority weights have been saved to {file_path}")

if __name__ == "__main__":
    # Perform the Fuzzy AHP steps
    display_hierarchy()
    display_fuzzy_comparisons()
    
    fuzzy_synthetic_extents = calculate_synthetic_extents()
    possibilities = calculate_possibilities(fuzzy_synthetic_extents)
    priority_weights = calculate_priority_weights(possibilities, criteria)
    
    # Save the fuzzy synthetic extents to CSV
    save_synthetic_extents_to_csv(fuzzy_synthetic_extents, r'E:/Qurratulain/FHP-performance-testing-mobile-apps/fuzzy_synthetic_extents.csv')
    
    # Save the priority weights to CSV
    save_priority_weights_to_csv(priority_weights, r'E:/Qurratulain/FHP-performance-testing-mobile-apps/fuzzy_priority_weights.csv')
# Step 6: Calculate weighted scores and rank the test cases based on the fuzzy AHP results

# Assuming test_case_scores is available and corresponds to the test case scores for each criterion
# For example purposes, we'll use simulated scores here:
test_case_scores = {
    "Elapsed Time": [17, 18, 19, 20, 21, 22, 23, 24, 25, 26],
    "Throughput": [17, 16, 15, 14, 13, 12, 11, 10, 9, 8],
    "Load/Network": [14, 13, 12, 11, 10, 9, 8, 7, 6, 5],
    "Latency": [24, 23, 22, 21, 20, 19, 18, 17, 16, 15]
}

# Function to calculate weighted scores for each test case
def calculate_weighted_scores(test_cases, test_case_scores, priority_weights):
    total_scores = {tc: 0 for tc in test_cases}  # Initialize total scores for each test case
    
    # Loop through each criterion and its corresponding scores for test cases
    for criterion, scores in test_case_scores.items():
        weight = priority_weights.get(criterion, 0)
        # Add the weighted score to the total score for each test case
        for i, score in enumerate(scores):
            total_scores[test_cases[i]] += weight * score
    
    return total_scores

# Calculate the weighted scores for each test case
weighted_scores = calculate_weighted_scores(alternatives, test_case_scores, priority_weights)

# Sort test cases by their total scores in descending order (higher score = higher priority)
ranked_test_cases = sorted(weighted_scores.items(), key=lambda x: x[1], reverse=True)

# Display the ranked test cases
print("\nRanked Test Cases based on Weighted Scores:")
for rank, (test_case, score) in enumerate(ranked_test_cases, start=1):
    print(f"Rank {rank}: {test_case} with score {score}")

# Save ranked test cases to CSV
ranked_df = pd.DataFrame(ranked_test_cases, columns=["Test Case", "Weighted Score"])
ranked_df.to_csv(r'E:/Qurratulain/FHP-performance-testing-mobile-apps/ranked_test_cases.csv', index=False)

print("Ranked test cases have been saved to 'ranked_test_cases.csv'")


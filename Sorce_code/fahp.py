# fuzzy_ahp.py
#libraries used 
import numpy as np
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



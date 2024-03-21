# Define the dynamic programming approach to solve the knapsack problem as given in the example.
def knapsack_dp(values, weights, max_weight):
    n = len(values)
    # Initialize the DP table
    dp = [[0 for j in range(max_weight + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, max_weight + 1):
            if weights[i-1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])
    return dp[n][max_weight], dp

# Define the function to determine the items included in the knapsack
def determine_items(dp, weights, values, max_weight):
    n = len(values)
    i, w = n, max_weight
    items = []
    
    while i > 0 and w >= 0:
        if dp[i][w] != dp[i-1][w]:
            items.append(i)
            w -= weights[i-1]
            i -= 1
        else:
            i -= 1
    
    items.reverse()
    return items

# Read the input file BAG.INP and extract the values and weights
with open('BAG.INP', 'r') as f:
    n, W = map(int, f.readline().split())
    values = []
    weights = []
    for _ in range(n):
        weight, value = map(int, f.readline().split())
        weights.append(weight)
        values.append(value)

# Compute the knapsack solution
max_value_dp, dp_table = knapsack_dp(values, weights, W)
items = determine_items(dp_table, weights, values, W)

# Generate the output string for BAG.OUT
output_str = f"{max_value_dp}\n" + " ".join(str(item) for item in items) + " 1"

# Write the output to BAG.OUT file
output_file_path = 'BAG.OUT'
with open(output_file_path, 'w') as f:
    f.write(output_str)


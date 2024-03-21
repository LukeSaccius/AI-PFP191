# Since we are to read from a file, let's assume that the content of BAG.INP is provided as a string for this environment.
# We will then simulate file reading and writing process.

bag_inp_content = """5 11
3 3
4 4
5 4
9 10
4 4"""

# Writing the BAG.INP content to a file
with open('BAG.INP', 'w') as file:
    file.write(bag_inp_content)

# Now we define the function to read the input file and solve the knapsack problem
def read_from_file(file_path):
    with open(file_path, 'r') as file:
        N, W = map(int, file.readline().split())
        items = [tuple(map(int, line.split())) for line in file]
    return N, W, items

# Define the knapsack solver function
def knapsack_solver(N, W, items):
    # Create a DP table to store the maximum value that can be attained with given weight
    dp = [[0 for x in range(W + 1)] for x in range(N + 1)]
    
    # Build table in bottom up manner
    for i in range(N + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif items[i-1][0] <= w:
                dp[i][w] = max(items[i-1][1] + dp[i-1][w-items[i-1][0]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    # Store the result of the knapsack
    result = dp[N][W]

    # Determine which items to take
    w = W
    taken_items = []
    for i in range(N, 0, -1):
        if result <= 0:
            break
        if result == dp[i-1][w]:
            continue
        else:
            taken_items.append(i)
            result -= items[i-1][1]
            w -= items[i-1][0]

    return dp[N][W], taken_items[::-1]

# Define the function to write the solution to the output file
def write_to_file(file_path, max_value, taken_items):
    with open(file_path, 'w') as file:
        file.write(f"{max_value}\n")
        for item in taken_items:
            file.write(f"{item}\n")

# Read the problem from the file
N, W, items = read_from_file('BAG.INP')

# Solve the knapsack problem
max_value, taken_items = knapsack_solver(N, W, items)

# Write the solution to the output file
write_to_file('BAG.OUT', max_value, taken_items)

# The BAG.OUT content for verification purposes
with open('BAG.OUT', 'r') as file:
    output_content = file.read()

output_content

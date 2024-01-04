# Get the name of the file from the user and open it for reading
filename = input('Enter file name: ')
file_handle = open(filename, 'r')

# Create an empty dictionary to store word frequencies
word_counts = {}

# Iterate over each line in the file
for line in file_handle:
    # Split the line into words
    words = line.split()
    # Count the occurrences of each word
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

# Initialize variables to find the most common word
highest_count = None
most_common_word = None

# Iterate over the dictionary to find the most common word
for word, count in word_counts.items():
    # If highest_count is None or current word count is higher, update the variables
    if highest_count is None or count > highest_count:
        most_common_word = word
        highest_count = count

# Print the most common word and its frequency
print(most_common_word, highest_count)


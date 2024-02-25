# Function to count and display the total number of words in a text file
def count_total_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()
        print(f"Total words are {len(words)}")

# Function to display words less than 4 characters from a text file
def display_short_words(file_path):
    short_words = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            short_words.extend(word for word in line.split() if len(word) < 4)
    print(' '.join(short_words))

# Assuming 'story.txt' is in the same directory as this script
file_path = r"E:\Learn\FPT\Python\Github\AI-PFP191\Lab 4\lab4b\Q2\story.txt"

# Perform task 1: Count total words
print("Task 1: Counting total words.")
count_total_words(file_path)

# Perform task 2: Display short words
print("\nTask 2: Displaying short words.")
display_short_words(file_path)

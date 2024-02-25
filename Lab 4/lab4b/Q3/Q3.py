# Function to count uppercase characters in a text file
def count_uppercase(file_path):
    uppercase_count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            uppercase_count += sum(1 for char in line if char.isupper())
    return uppercase_count

# Function to count the words "this" and "these" in a text file
def count_specific_words(file_path):
    words_count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            words_count += words.count("this") + words.count("these")
    return words_count

# Assuming 'article.txt' is the file we need to check
article_file_path = r"E:\Learn\FPT\Python\Github\AI-PFP191\Lab 4\lab4b\Q3\article.txt"

# Perform task 1: Count uppercase characters
uppercase_count = count_uppercase(article_file_path)
print(f"Number of uppercase characters: {uppercase_count}")

# Perform task 2: Count "this" and "these"
specific_words_count = count_specific_words(article_file_path)
print(f"Total occurrences of 'this' and 'these': {specific_words_count}")

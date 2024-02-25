# Function to display file content with hash between each character
def hash_display(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        hashed_content = '#'.join(content)  # Insert a hash between each character
        print(hashed_content)

# Function to replace 'J' with 'I' in file content
def JTOI(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        corrected_content = content.replace('J', 'I')  # Replace 'J' with 'I'
        print(corrected_content)

# Assuming the files 'matter.txt' and 'WORDS.TXT' are in the same directory as this script
matter_file_path = r"E:\Learn\FPT\Python\Github\AI-PFP191\Lab 4\lab4b\Q4\matter.txt"
words_file_path = r"E:\Learn\FPT\Python\Github\AI-PFP191\Lab 4\lab4b\Q4\WORDS.txt"

# Perform task 1: Hash display
print("Displaying content of 'matter.txt' with hashes:")
hash_display(matter_file_path)

# Perform task 2: Replace 'J' with 'I'
print("\nDisplaying corrected content of 'WORDS.TXT':")
JTOI(words_file_path)

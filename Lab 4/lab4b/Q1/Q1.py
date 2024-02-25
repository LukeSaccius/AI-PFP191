import os

# Function to read and display file content
def read_and_display(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            print(line.strip())

# Function to count lines not starting with 'T'
def count_lines_not_starting_with_t(file_path):
    count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if not line.startswith('T'):
                count += 1
    return count

# Full path to the poem file
poem_file_path = r"E:\Learn\FPT\Python\Github\AI-PFP191\Lab 4\lab4b\Q1\poem.txt"
# Full path to the story file
story_file_path = r"E:\Learn\FPT\Python\Github\AI-PFP191\Lab 4\lab4b\Q1\story.txt"
# If the files exist, perform the tasks
if os.path.exists(poem_file_path):
    read_and_display(poem_file_path)
else:
    print("The file 'poem.txt' does not exist at the specified path.")

if os.path.exists(story_file_path):
    non_t_lines = count_lines_not_starting_with_t(story_file_path)
    print(f"\nNumber of lines not starting with 'T'= {non_t_lines}")
else:
    print("The file 'story.txt' does not exist at the specified path.")

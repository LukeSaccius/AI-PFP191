path = r"E:\Hoc Tập\FPT\Python\New folder\AI-PFP191\Lab 4\lab4b\Q1"

# For reading and displaying the poem.txt
with open(f"{path}\poem.txt", "r") as file:
    for line in file:
        print(line.strip())

# For counting lines not starting with 'T' in story.txt
with open(f"{path}\story.txt", "r") as file:
    count = sum(1 for line in file if not line.startswith('T'))
    print(f"Number of lines not starting with T: {count}")

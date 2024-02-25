# Task 1: Write to a new file
def write_to_new_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Task 2: Write to an existing file (this will overwrite the file if it exists)
def write_to_existing_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# Task 3: Write a list of lines to a file
def write_list_to_file(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)

# Perform the tasks
write_to_new_file('newfile.txt', 'This is new content\n')
write_to_existing_file('existingfile.txt', 'This is overwritten content\n')
write_list_to_file('listfile.txt', ['Name: Emma\n', 'Address: 221 Baker Street\n', 'City: London\n'])

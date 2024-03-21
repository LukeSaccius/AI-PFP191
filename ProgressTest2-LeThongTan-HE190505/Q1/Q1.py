def replace_char(s, char_to_replace, replacement_char):
    """
    Replaces all occurrences of char_to_replace with replacement_char in s.

    Parameters:
    s (str): The string to process.
    char_to_replace (str): The character in s to replace.
    replacement_char (str): The character to replace with.

    Returns:
    str: The resulting string after replacement.
    """
    return s.replace(char_to_replace, replacement_char)

def main():
    # Prompting for combined input
    combined_input = input("Enter the string, character to replace, and replacement character, separated by commas: ")
    parts = combined_input.split(', ')  # This splits the input into parts based on spaces
    
    # Validating the input
    if len(parts) != 3 or len(parts[1]) != 1 or len(parts[2]) != 1:
        print("Invalid input. Please enter the data in the format: string char_to_replace replacement_char")
        return
    
    # Unpacking the parts
    user_string, char_to_replace, replacement_char = parts
    
    # Calling the replace_char function and printing the result
    result_string = replace_char(user_string, char_to_replace, replacement_char)
    print("Result:", result_string)

# Running the program
if __name__ == "__main__":
    main()

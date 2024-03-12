# Writing a Python program to count the frequency of each letter in a given string

# Assuming the input is "hello, world\n" as given in the example
input_text = "hello, world\n"

# Removing any characters that are not letters and converting to lowercase
cleaned_text = ''.join(filter(str.isalpha, input_text)).lower()

# Counting the frequency of each letter
frequency = {}
for letter in cleaned_text:
    if letter in frequency:
        frequency[letter] += 1
    else:
        frequency[letter] = 1

# Sorting the dictionary for display
sorted_frequency = dict(sorted(frequency.items()))

# Displaying the frequency of each letter
for letter, count in sorted_frequency.items():
    print(f"The letter '{letter}' appears {count} time(s).")

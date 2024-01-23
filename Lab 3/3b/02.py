def string_to_hexadecimal(string):
    try:
        return int(string, 16)
    except ValueError:
        return "Error: String contains non-hexadecimal digits."

if __name__ == "__main__":
    hex_string = input("Enter a string to convert from hexadecimal to base-10: ")
    result = string_to_hexadecimal(hex_string)
    print(f"The base-10 value is: {result}" if isinstance(result, int) else result)

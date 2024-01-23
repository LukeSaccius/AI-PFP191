def is_anagram(str1, str2):
    normalize = lambda s: sorted(s.lower().replace(" ", ""))
    return normalize(str1) == normalize(str2)

if __name__ == "__main__":
    string1 = input("Enter the first string to check for an anagram: ")
    string2 = input("Enter the second string to check for an anagram: ")
    print("The strings are anagrams." if is_anagram(string1, string2) else "The strings are not anagrams.")

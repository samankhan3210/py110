def get_substrings(text):
    n = len(text)
    substrings = []
    for start in range(0, n - 1):
        for end in range(start+1 , n):
            substrings.append(text[start:end+1])

    return substrings

def is_palidrome(input_string):
    if input_string == input_string[::-1]:
        return True
    
    else:
        return False


def is_substring_palindrome(text):
    palindrome_strings = []
    substrings = get_substrings(text)
    for sub in substrings:
        if is_palidrome(sub):
            palindrome_strings.append(sub)

    print(palindrome_strings)
    return palindrome_strings

def main():
    text = ""
    is_substring_palindrome("abcddcbA")   # ["bcddcb", "cddc", "dd"]
    is_substring_palindrome("palindrome") # []
    is_substring_palindrome("")           # []
    is_substring_palindrome("repaper")    # ['repaper', 'epape', 'pap']
    is_substring_palindrome("supercalifragilisticexpialidocious") # ["ili"]

if __name__ == "__main__":
    main() 
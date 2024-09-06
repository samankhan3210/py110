''' Given a list of strings, return a new list where the strings are sorted based on the highest 
number of adjacent consonants a string contains. If two strings contain the same highest 
number of adjacent consonants, they should retain their original order in relation to each other. 
Consonants are considered adjacent if they are next to each other in the same word or if there is 
a space between two consonants in adjacent words. (If no. of adj const is 1 then it's not counted and considered zero.)
'''

def sort_by_max_adjacent_consonants(string_list):
    string_list.sort(key = max_adjacent_consonants, reverse = True)
    return string_list

def max_adjacent_consonants(text):
    text = text.replace(" ", "").lower()
    vowels = "aeiou"
    max_const_count = 0
    current_const_count = 0

    for char in text:
        if char in vowels:
            current_const_count = 0

        else:
            current_const_count += 1
        
        if current_const_count > max_const_count and current_const_count > 1:
            max_const_count = current_const_count

    return max_const_count

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_max_adjacent_consonants(my_list))
# Expected: ['dddaa', 'ccaa', 'aa', 'baa']
# Actual:   ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_max_adjacent_consonants(my_list))
# Expected: ['salt pan', 'can can', 'batman', 'toucan']
# Actual:   ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_max_adjacent_consonants(my_list))
# Expected: ['bar', 'car', 'far', 'jar']
# Actual:   ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_max_adjacent_consonants(my_list))
# Expected: ['month', 'day', 'week', 'year']
# Actual:   ['day', 'week', 'month', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_max_adjacent_consonants(my_list))
# Expected: ['xxxx', 'xxxb', 'xxxa']
# Actual:   ['xxxa', 'xxxx', 'xxxb']


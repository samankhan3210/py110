''' Question 1 : Compute and display the total age of the family's male members. 
Try working out the answer two ways: first with an ordinary loop, then with a comprehension. 
The result should be 444.
'''

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

ages = [munsters[key]['age'] for key in munsters if munsters[key]['gender'] == 'male']
print(sum(ages) ==  444)

''' Question 2 : Given the following data structure, return a new list with the same structure, 
but with the values in each sublist ordered in ascending order. Use a comprehension if you can. 
The string values should be sorted as strings, while the numeric values should be sorted as numbers.'''

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]
sorted_list = [sorted(sub_lst) for sub_lst in lst]
print(sorted_list == [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']])

''' Question 3 : Given the following data structure, return a new list with the same structure, 
but with the values in each sublist ordered in ascending order as strings (that is, the numbers 
should be treated as strings). Use a comprehension if you can. '''

sorted_lst_str = [sorted(sub_lst, key = str) for sub_lst in lst]
print(sorted_lst_str == [['a', 'b', 'c'], [-3, 11, 2], ['black', 'blue', 'green']])

''' Question 4 : Given the following data structure, write some code that defines a dictionary where the key 
is the first item in each sublist, and the value is the second.
'''
lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

expected_output = {
    'a': 1,
    'b': 'two',
    'sea': {'c': 3},
    'D': ['a', 'b', 'c']
}

dictionary = {sub[0] : sub[1] for sub in lst}
print(dictionary == expected_output)

''' Question 5 : Given the following data structure, sort the list so that the sub-lists are ordered 
based on the sum of the odd numbers that they contain. You shouldn't mutate the original list.'''

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]
expected_output = [[1, 8, 3], [1, 6, 7], [1, 5, 3]]

def sum_odd_num(num_list):
    odd_nums = [num for num in num_list if num % 2 != 0]
    return sum(odd_nums)

sorted_odd_lst = sorted(lst, key = sum_odd_num)
print(sorted_odd_lst == expected_output)

''' Question 6 : Given the following data structure, return a new list identical in structure to the original 
but, with each number incremented by 1. Do not modify the original data structure. Use a comprehension.'''

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]
expected_output = [{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]
incremented_list = [{key: value + 1 for key, value in dictionary.items()}
                            for dictionary in lst]
print(incremented_list == expected_output)

''' Question 7 : Given the following data structure return a new list identical in structure to the original, 
but containing only the numbers that are multiples of 3.'''

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]
expected_output = [[], [3, 12], [9], [15, 18]]
multiple_of_3 = [[value for value in item if value % 3 == 0] for item in lst]
print(multiple_of_3 == expected_output)

''' Question 8 : Given the following data structure, write some code to return a list that contains the colors 
of the fruits and the sizes of the vegetables. The sizes should be uppercase, and the colors should be capitalized.'''
dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def transform_item(item):
    if item['type'] == 'fruit':
        return [color.capitalize() for color in item['colors']]
    else:
        return item['size'].upper()
    
expected_output = [["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]
colors_and_sizes = [transform_item(item) for item in dict1.values()]
print(colors_and_sizes == expected_output)

''' Question 9 : This problem may prove challenging. Given the following data structure, 
write some code to return a list that contains only the dictionaries where all the numbers are even.'''
lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]
expected_output = [{'e': [8], 'f': [6, 10]}]

def is_even(dicts):
    flag = True
    for value in dicts.values():
        if not all([num % 2 == 0 for num in value]):
            return False

    return True

even_dict_lst = [dicts for dicts in lst if is_even(dicts)]
print(even_dict_lst == expected_output)

''' Question 10 : A UUID (Universally Unique Identifier) is a type of identifier often used to uniquely identify items, even when some of those items were created on a different server or by a different application. That is, without any synchronization, two or more computer systems can create new items and label them with a UUID with no significant risk of stepping on each other's toes. It accomplishes this feat through massive randomization. The number of possible UUID values is approximately 3.4 X 10E38, which is a huge number. The chance of a conflict, a "collision", is vanishingly small with such a large number of possible values.

Each UUID consists of 32 hexadecimal characters (the digits 0-9 and the letters a-f) represented as a string. The value is typically broken into 5 sections in an 8-4-4-4-12 pattern, e.g., 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'.

Note that our description of UUIDs is a simplified description of how UUIDs are formed. There are several UUID versions, each with some non-random characteristics in some of the bits. These different versions can play a part in certain applications.

Write a function that takes no arguments and returns a string that contains a UUID.'''

import random

def generate_uuid():
    hex_chars = '0123456789abcdef'
    sections = [8, 4, 4, 4, 12]
    uuid = []

    for section in sections:
        chars = [random.choice(hex_chars) for _ in range(section)]
        uuid.append(''.join(chars))

    return '-'.join(uuid)

# Outputs shown below are samples - you output will vary
print(generate_uuid())  
print(generate_uuid())  
print(generate_uuid())  

''' Question 11 : The following dictionary has list values that contains strings. 
Write some code to create a list of every vowel (a, e, i, o, u) that appears in the contained strings, 
then print it.'''

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

list_of_vowels = [char for values in dict1.values()
                  for word in values
                  for char in word if char.lower() in 'aeiou']

print(list_of_vowels)
expected_output = ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
print(list_of_vowels == expected_output)
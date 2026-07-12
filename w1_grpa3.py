"""
Odd one out explanation:
This program checks a list of mixed data types and finds which data type appears only once.

It counts how many integers, floats, strings, and booleans are in the list and then
returns the type whose count is exactly 1.
"""


def odd_one(L):
    # Count how many times each data type appears.
    type_counts = {'int': 0, 'float': 0, 'str': 0, 'bool': 0}

    for item in L:
        if type(item) == int:
            type_counts['int'] += 1
        elif type(item) == float:
            type_counts['float'] += 1
        elif type(item) == str:
            type_counts['str'] += 1
        elif type(item) == bool:
            type_counts['bool'] += 1

    # Return the data type that appeared exactly once.
    for data_type, count in type_counts.items():
        if count == 1:
            return data_type
        
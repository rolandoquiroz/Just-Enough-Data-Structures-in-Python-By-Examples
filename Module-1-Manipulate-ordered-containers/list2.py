#!/usr/bin/python3
"""
append & extend

append() - Takes a single item and adds it to the end of the list.
The item can be numbers, strings, another list, tuple, etc.
"""
char_list = ['u', 'v', 'w']
char_list.append('x')
print(char_list)

char_list.append(['y', 'z'])  # append a list to char_list
print(char_list)

"""
extend() - Adds the specified iterable to the end of the current list.
Extends the list by adding all items of the list to an end.
"""
char_list = ['a', 'b', 'c']
print(char_list)
char_list.extend(['d', 'e', 'f'])
print(char_list)
char_list.extend('g')
print(char_list)
char_list.insert(len(char_list), 'h')
print(char_list)

#!/usr/bin/python3
# a function that finds all multiples of 2 in a list.
def divisible_by_2(my_list=[]):
    new_list = []
    if my_list:
        for num in my_list:
            new_list.append(False if num % 2 else True)
        return new_list

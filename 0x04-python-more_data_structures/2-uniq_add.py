#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    adds all unique integers in a
    list (only once for each integer).
    """

    if my_list is None:
        my_list = []

    new_list = []
    sum = 0

    for x in my_list:
        if x not in new_list:
            sum += x
            new_list.append(x)

    return sum

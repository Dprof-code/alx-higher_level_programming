#!/usr/bin/python3

def max_integer(my_list=[]):
    """
        max_integer - finds the biggest integer of a list.
    """

    largest = -1

    if len(my_list) < 1:
        return None
    else:
        for num in my_list:
            if num > largest:
                largest = num

    return largest

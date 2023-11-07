#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
         function that adds 2 tuples.

        Prototype: def add_tuple(tuple_a=(), tuple_b=()):
        Returns a tuple with 2 integers:
            The first element should be the addition of the 
            first element of each argument
            The second element should be the addition of the 
            second element of each argument
        You are not allowed to import any module
        You can assume that the two tuples will only contain integers
        If a tuple is smaller than 2, use the value 0 for each missing integer
        If a tuple is bigger than 2, use only the first 2 integers
    """
    set_a = [num for num in tuple_a]
    set_b = [num for num in tuple_b]

    while len(set_a) < 2 or len(set_b) < 2:
        if len(set_a) < 2:
            set_a.append(0)
        elif len(set_b) < 2:
            set_b.append(0)

    i = 0
    while (i < 1):
        first_elem = set_a[i] + set_b[i]
        i += 1
        second_elem = set_a[i] + set_b[i]

    new_tuple = (first_elem, second_elem)
    return new_tuple

#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    safe_print_list_integers - prints the first x elements of a list and only integers.
    """

    i = 0
    num_of_elem = 0
    while x > 0:
        try:
            if not isinstance(my_list[i], int):
                pass
                # raise ValueError("Element at index {} is not an integer".format(i))
            else:
                print("{:d}".format(my_list[i]), end="")
                num_of_elem += 1
            x -= 1
            i += 1
        except IndexError:
            break

    print()
    return num_of_elem

#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    """
    safe_print_list - prints x elements of a list.
    """

    try:
        i = 0
        if x <= 0:
            return 0
        while x > 0:
            print(f"{my_list[i]}", end="")
            x -= 1
            i += 1
    except IndexError as exec:
        pass

    finally:
        print()

    return i

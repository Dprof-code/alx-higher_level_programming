#!/usr/bin/python3

def safe_print_integer(value):
    """
    safe_print_integer - prints an integer.
    """

    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False

#!/usr/bin/python3

def safe_print_division(a, b):
    """
    safe_print_division - divides 2 integers and prints the result.
    """

    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if result:
            print("Inside result: {:.1f}".format(result))
        else:
            print("Inside result: {}".format(result))
    return result

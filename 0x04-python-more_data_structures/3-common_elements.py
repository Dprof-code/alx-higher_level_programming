#!/usr/bin/python3

def common_elements(set_1, set_2):
    """
    common_elements - returns a set of
    common elements in two sets.
    """

    common = list(set_1 & set_2)

    return common

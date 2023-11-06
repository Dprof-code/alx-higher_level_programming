#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for set_of_int in matrix:
        i = 0
        while i < len(set_of_int):
            print("{:d}".format(set_of_int[i]), end=" ")
            i += 1
        print()

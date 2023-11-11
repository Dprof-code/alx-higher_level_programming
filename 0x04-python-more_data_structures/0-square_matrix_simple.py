#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    square_matrix_simple - computes the square value of all integers of a matrix.
    """

    square = list(map(lambda n : n * n, matrix))

    return (square)

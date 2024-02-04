#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = []
    for item in matrix:
        copy.append(list(map((lambda x: x ** 2), item)))
    return copy

#!/usr/bin/python3
def square_matrix_simple(matrix):
    new_matrix = matrix[:]
    for i in new_matrix:
        for k in range(len(i)):
            i[k] **= 2
    return new_matrix

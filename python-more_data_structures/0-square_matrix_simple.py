#!/usr/bin/python3
def square_matrix_simple(matrix):
    new_matrix = []
    for j in matrix:
        new_matrix += [j]
    for i in new_matrix:
        for k in range(len(i)):
            new_matrix[new_matrix.index(i)][k] **= 2
    return new_matrix

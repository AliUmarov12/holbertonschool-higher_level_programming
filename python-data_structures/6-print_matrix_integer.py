#!/usr/bin/python3
def print_matrix_integer(matrix):
    for i in matrix:
        for k in i:
            if (i.index(k) + 1) % 3 == 0:
                if not ((matrix.index(i) + 1) == len(matrix) and (i.index(k) + 1) == len(i)):
                    print("{:d}".format(k), '\n')
                else:
                    print("{:d}".format(k))
            else:
                print("{:d}".format(k), end=' ')

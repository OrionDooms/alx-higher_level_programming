#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = [[i**2 for i in row] for row in matrix]
    for row in mat:
        return ("{}".format(mat))

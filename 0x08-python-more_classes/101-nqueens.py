#!/usr/bin/python3
"""Nqueens print the solutions in a specific order.
"""
import sys


def nqueens(N):
    """Nqueens print the solutions in a specific order.

    args:
        N (int): the argument that create a Matrix.
    """
    num = int(N)
    """if type(num) != int:
        print("N must be a number\n")
        sys.exit(1)"""
    if num < 4:
        print("N must be at least 4\n")
        sys.exit(1)
    else:
        result = []
        matrix = [[i * num + j + 1 for j in range(num)] for i in range(num)]

        for num in matrix:
            print(num)


if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print("Usage: nqueens N")
        sys.exit(1)
    argument = sys.argv[1]
    nqueens(argument)

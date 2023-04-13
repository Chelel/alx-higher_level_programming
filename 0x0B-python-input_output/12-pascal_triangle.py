#!/usr/bin/python3
"""12-pascal_triangle.py"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""

    triangle = []
    if n <= 0:
        return triangle
    for row in range(n):
        row1 = []
        triangle.append(row1)
        row1.append(1)
        for col in range(1, row):
            row1.append(triangle[row - 1][col - 1] + triangle[row - 1][col])
        if row > 0:
            row1.append(1)
    return triangle

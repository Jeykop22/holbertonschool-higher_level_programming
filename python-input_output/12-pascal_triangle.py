#!/usr/bin/python3
"""
    Function that returns a list of lists of integers
    representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
        Function that returns a list of lists of integers
        representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1] * (i + 1) for i in range(n)]

    for i in range(2, n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

    return triangle

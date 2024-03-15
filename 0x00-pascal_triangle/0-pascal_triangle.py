#!/usr/bin/python3
""" pascal triangle implementation """

def pascal_triangle(n):
    """ pascal function """

    if n <= 0:
        return []

    triangle = [[1], [1, 1]]
    for i in range(2, n):
        triangle.append([1])
        for j in range(i-1):
            triangle[i].append(sum(triangle[i-1][j:j+2]))
        triangle[i].append(1)
    return triangle[:n]


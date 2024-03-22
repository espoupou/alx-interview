#!/usr/bin/python3
"""Minimum Operations"""


def primeFactorization(x):
    """Returns prime factorization elements of x"""
    k = 2
    primes = list()
    while (k <= x):
        if x % k == 0:
            primes.append(k)
            x /= k
        else:
            k += 1
    return primes


def minOperations(n):
    """Calculates the fewest number of operations needed
        to result in exactly n H characters in the file"""
    min = 0
    factors = [x for x in primeFactorization(n)]
    occurences = {item: factors.count(item) for item in factors}
    for k, v in occurences.items():
        min += k * v
    return min

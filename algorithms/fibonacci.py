"""
For education puposes

Demonstration of the fibonacci sequence
"""

__author__ = "alunkeit"
__description__ = "Fibonacci sequence"


def fibonacci(n: int) -> []:
    """
    Implementation of the fibonacci sequence
    """
    fb_numbers = [0, 1]
    for x in range(2, n):
        fb_numbers.append(fb_numbers[-1] + fb_numbers[-2])
    return fb_numbers


if __name__ == "__main__":
    print(fibonacci(10))
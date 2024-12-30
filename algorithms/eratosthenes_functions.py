"""
For education purposes.

This script demonstrates the prime sieve algorithm using functions in Python.
The strategy is quite simple: it is known for sure that 2 is a prime number.
The algorithm tests all elements in the array if they are a multiple of 2 using
the modulo (mod) operation and marks all found elements with -1. Then the next
values that is not equal to -1 is selected and all multiples are sorted out.
In the end all values not equal -1 are prime numbers.

The function declarations used in this example do not return any values. Instead
they operate on variables that are accessible from within the module
"""

__author__ = "alunkeit"
__description__ = "prime sieve of eratosthenes using function declarations"

"""
imports a module that provides basic logging facilities
"""
import logging

"""
sets the log level to INFO level
"""
logging.basicConfig(level=logging.INFO)

"""
numbers is an array that is globaly visible in the implementation unit (module). This array is filled with initial values and used to search for prime numbers.
"""
numbers = []

"""
the result is an array and contains only the prime numbers without any -1 values
"""
result = []

"""
initialize the array the algorithm is working on
"""
def initialize(upper_bound: int):
    logging.info('------------------')
    logging.info(f"initializing array up to {upper_bound}")
    logging.info('------------------')

    for x in range(upper_bound):
        numbers.append(x)


"""
This functions sieves out the primes in the array
"""
def sieve():
    logging.info('------------------')
    logging.info(f"size of search base is {len(numbers)}")
    logging.info('------------------')

    for x in range(2, len(numbers)):
        if numbers[x] == -1:
            continue

        for y in range(x + 1, len(numbers)):
            if numbers[y] % x == 0:
                logging.info(f"not a prime number: {numbers[y]}")
                numbers[y] = -1


"""
wipes out the -1 values from the array
"""
def clean_numbers():
    logging.info('cleaning numbers array')
    for x in range(2, len(numbers)):
        if numbers[x] != -1:
            result.append(numbers[x])

"""
Executes the algorithm
"""
if __name__ == '__main__':
    logging.info('starting program')

    initialize(100)
    sieve()
    clean_numbers()
    print(numbers)
    print(result)

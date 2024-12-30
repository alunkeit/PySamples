"""
for education purposes

Used for executing the OOP prime sieve implementation.
"""
import os
from algorithms import PrimeSieve

print(os.path.dirname(os.path.realpath(__file__)))

sieve = PrimeSieve(100)
sieve.sieve()
print((sieve.get_result()))
sieve.clear()

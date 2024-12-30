"""
for education purposes

This script demontrates the prime siee of erasthostenes in an object oriented style.
"""

__author__ = "alunkeit"
__description__ = "OOP style of prime number sieve"

import logging
"""
Set the global logger configuration
"""
logging.basicConfig(level=logging.INFO)

"""
The class definition starts here. instance variables are declared in the class constructor (def __init__), class variables in the class body. As Python has no mechanisms for declaring variables as public or private, it is the convention to declare variables with a leading underscore if they shoud be treated like a private variable
"""

class PrimeSieve():
	
	"""
	The constructor does the necessary initializations. _numbers and _result shall be treated as private instance variables.
	"""
	def __init__(self, upper_bound: int):
		self._numbers = []
		self._result = []
		
		for x in range(upper_bound):
			self._numbers.append(x)

	"""
	Clear internal values
	"""
	def clear(self):
		self._numbers.clear()
		self._result.clear()

	"""
	Perform sieve algorithm
	"""
	def sieve(self):
		logging.info('------------------')
		logging.info(f"size of search base is {len(self._numbers)}")
		logging.info('------------------')
	
		for x in range(2, len(self._numbers)):
			if self._numbers[x] == -1:
				continue
			
			for y in range(x + 1, len(self._numbers)):
				if self._numbers[y] % x == 0:
					logging.info(f"not a prime number: {self._numbers[y]}")
					self._numbers[y] = -1
		
		"""
		integrates the clean up code here and fills the result array 
		"""
		for x in range(2, len(self._numbers)):
			if self._numbers[x] != -1:
				self._result.append(self._numbers[x])

		
	def get_result(self) -> []:
		return self._result
		
	

if __name__ == '__main__':
	sieve = PrimeSieve(100)
	sieve.sieve()
	print((sieve.get_result()))
	sieve.clear()
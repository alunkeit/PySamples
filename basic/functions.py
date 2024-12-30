"""
for education purposes

Demonstration of basic concepts of functions in Python. This sample is not a complete demonstration,
it shows some of the basic programming concepts when using functions in Python.
"""

__author__ = "alunkeit"
__description__ = "some basic concepts of functions in Python"


"""
The minimum syntax for a function consists of:
	+ the keyowrd def to start a function definition
	+ the name of the function
	+ round brackets
	+ a ':' sign to signal that the head of the function has been declared
	
Be aware: a function does always return a value. Concepts like 'void' are unknown to Python. 
If no explicit return value has been declared, the function returns None
"""
def basic_function_no_arguments():
	print("hello from function with no arguments")
	

"""
Arguments are declared in the round brackets. In minimum the argument has name and the type of the argument is implicitly discovered. A more explicit notation starting with Python 3 are type hints. The function definition below in a more explicit way would be

def basic_function_one_argument(x : int):
"""	
def basic_function_one_argument(x):
	print(f"hello from a function with an argument of variable type, x = {x}")
	print(f"the type of the argument is {type(x)}")
	print(f"the memory position of the argument is {id(x)}")
	
	
"""
A function definition supports default arguments. In case that not all paramters of the function are explicitely initialized, the default value will be used.
"""
def basic_function_default_arguments(x = 10, y = 20):
	print(f"function with default argument: x={x} and y={y}")

"""
Functions do also support the use of a variable number of arguments, even with mixed types
"""
def basic_function_variable_arguments(*args):
	for a in args:
		print(f"argument = {a}")
		if type(a) is int:
			print('argument is an integer')
			
"""
Functions support argument dictioaries, typically named as kwargs (key word arguments). This technique is used to work with variable argument and well defined argument names
"""
def basic_function_named_arguments(**kwargs):
	for k, v in kwargs.items():
		print(f"variable argument with key={k} and value={v}")	
		
		
"""
This function returns a value, the type of the return value is given by type hinting
"""
def basic_function_returning_a_value() -> int:
	return 10

"""
A function may return more than one value. In this case a tuple is returned.
"""	
def function_with_two_return_values() -> int:
	return 10,11,12

	
if __name__ == '__main__':
	basic_function_no_arguments()
	basic_function_one_argument(10)
	basic_function_one_argument("hello world")
	basic_function_default_arguments()
	basic_function_default_arguments(15)
	basic_function_default_arguments(y="hello world")
	basic_function_variable_arguments(10,11,12,13,14,'h','e','l','l','o')
	basic_function_named_arguments(a=10, b=15, c=36, d="Hello world")
	print(f"return value is {basic_function_returning_a_value()}")
	print(f"return values (multiple values) {function_with_two_return_values()}")
	values = function_with_two_return_values();
	print(f"type={type(values)}")
	# a function can be stored in a variable, this concept is similar to function pointers in C/C++
	fun = basic_function_no_arguments
	fun()

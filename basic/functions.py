"""
Licensed under the Educational Community License,  Version 2.0 (the “License”); you may not
use this file except in compliance with the License.

You may obtain a copy of the License at http://www.osedu.org/licenses/ECL-2.0 Unless required
by applicable law or agreed to in writing, software distributed under the License is distributed
on an “AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.

Demonstration of basic concepts of functions in Python. This sample is not a complete demonstration,
it shows some of the basic programming concepts when using functions in Python.
"""

__author__ = "alunkeit"
__description__ = "some basic concepts of functions in Python"


def basic_function_no_arguments():
    """
	The minimum syntax for a function consists of:
		+ the keyword def to start a function definition
		+ the name of the function
		+ round brackets
		+ a ':' sign to signal that the head of the function has been declared

	Be aware: a function does always return a value. Concepts like 'void' are unknown to Python.
	If no explicit return value has been declared, the function returns None
	"""
    print("hello from function with no arguments")
    """
    Returning one or more values is optional
    """
    return 23


def basic_function_one_argument(x):
    """
	Arguments are declared in the round brackets. In minimum the argument has name and the type of the
	argument is implicitly discovered. A more explicit notation starting with Python 3 are type hints.
	The function definition below in a more explicit way would be

	def basic_function_one_argument(x : int):
	"""
    print(f"hello from a function with an argument of variable type, x = {x}")
    print(f"the type of the argument is {type(x)}")
    print(f"the memory position of the argument is {id(x)}")


def basic_function_default_arguments(x=10, y=20):
    """
	A function definition supports default arguments. In case that not all parameters of the
	function are explicitly initialized, the default value will be used.
	"""
    print(f"function with default argument: x={x} and y={y}")


def basic_function_variable_arguments(*args):
    """
	Functions do also support the use of a variable number of arguments, even with mixed types
	"""
    for a in args:
        print(f"argument = {a}")
        if type(a) is int:
            print('argument is an integer')


def basic_function_named_arguments(**kwargs):
    """
	Functions support argument dictionaries, typically named as kwargs (key word arguments).
	This technique is used to work with variable argument and well defined argument names
	"""
    for k, v in kwargs.items():
        print(f"variable argument with key={k} and value={v}")


def basic_function_returning_a_value() -> int:
    """
	This function returns a value, the type of the return value is given by type hinting
	"""
    return 10


def function_with_two_return_values() -> []:
    """
	A function may return more than one value. In this case a tuple is returned.
	"""
    return 10, 11, 12


def function_with_explicit_arguments(x: int, y: float, z: str):
    print(f"type of x = {type(x)}")
    print(f"type of y = {type(y)}")
    print(f"type of z = {type(z)}")

    k = x / 3
    return k


if __name__ == '__main__':
    basic_function_no_arguments()
    basic_function_one_argument(10)
    basic_function_one_argument("hello world")
    basic_function_default_arguments()
    basic_function_default_arguments(15)
    basic_function_default_arguments(y=23)
    basic_function_variable_arguments(10, 11, 12, 13, 14, 'h', 'e', 'l', 'l', 'o')
    basic_function_named_arguments(a=10, b=15, c=36, d="Hello world")
    print(f"return value is {basic_function_returning_a_value()}")
    print(f"return values (multiple values) {function_with_two_return_values()}")
    values = function_with_two_return_values()
    print(f"type={type(values)}")
    # a function can be stored in a variable, this concept is similar to function pointers in C/C++
    fun = basic_function_no_arguments
    fun()
    r = function_with_explicit_arguments(5, 5.0, 'hello')
    print(f"return : {r}")

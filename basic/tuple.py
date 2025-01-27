"""
Licensed under the Educational Community License,  Version 2.0 (the “License”); you may not
use this file except in compliance with the License.

You may obtain a copy of the License at http://www.osedu.org/licenses/ECL-2.0 Unless required
by applicable law or agreed to in writing, software distributed under the License is distributed
on an “AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.

This implementation file shows some basic operations on tuples.
"""


def my_tuple_returning_function() -> ():
    """
    This function returns a tuple of values
    :return: a tuple consisting of 1,2,3
    """
    return (1, 2, 3)


def select_address(name: str) -> ():
    """
    Demonstrates how to use tuples when returning values from functions
    :param name:
    :return:
    """
    if name == "my address":
        return ("Python Road", "110", "14325", "Pythonia")
    return None


# a tuple is a collection of items. Tuples in Python are immutable
t1 = (1, 2, 3)
print(t1)
print(type(t1))

t2 = (1, "yellow", 27.0, 'c')
print(t2)
print(type(t2))

# tuples are iterable.
for e in t1:
    print(f"Element in tuple t1: {e}")

# the number of elements in the tuple
print(f"number of elements in tuple t1: {len(t1)}")

# merging two tuples is possible using the '+' operator
t3 = t1 + t2
print(t3)

# accessing single elements is done using an array operator
print(f"the first element is address 0 -> {t3[0]}")

for c in range(len(t3)):
    print(f"Element in tuple t3[{c}]: {t3[c]}")

# tuple packing. the following sample shows a valid initialisation of a tuple
t5 = 1, 2, 3
print(t5)

# slicing is also supported. This sample shows how to obtain the first 2 values
t6 = t5[:2]

# unpacking the values. The values are stored separately in the variables
x1, x2, x3 = t5
print(x1, x2, x3)

street, number, zip, location = select_address("my address")
print(f"street = {street}, number = {number}, zip = {zip}, location = {location}")

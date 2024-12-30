"""
For education purposes

This implementation file shows some basic operations on lists.
"""

__author__ = "alunkeit"
__description__ = "Demonstration of some concepts of lists in Python"

"""
A helper function that prints some information of the list 
"""


def print_list_properties(l: list):
    print("----")
    print(f"number of elements in list = {len(l)}")
    print(f"Elements in list = {l}")


# create a list. a list may contain items of different types
# initializing a list is typically done by square brackets
list1 = []
print(f"type of list1 = {type(list1)}")

# calling list() explicitly is also an option, preferred is the use of square brackets
list2 = list()
print(f"type of list2 = {type(list2)}")

# use list.append to insert new elements at the end of a list
for x in range(1, 10):
    list1.append(x)

print_list_properties(list1)

# removes an element from the list. in case of our example, 3 is removed from the list
list1.remove(3)
print_list_properties(list1)

# a new item is inserted into the list at a certain position
list1.insert(2, 3)
print_list_properties(list1)

# fill a second list
for x in range(11, 20):
    list2.append(x)
print_list_properties(list2)

# insert all elements of list2 into list1 (merge all elements into list1)
list1.extend(list2)
print_list_properties(list1)

# reverse the items in list1
list1.reverse()
print_list_properties(list1)

# pop removes an item at a certain position. In this example the 6th item os removed from the list
list1.pop(5)
print_list_properties(list1)

# lists can be manipulated using comprehensions. This sample doubles all items in the list.
list3 = [e * 2 for e in list1]
print_list_properties(list3)
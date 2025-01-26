"""
Licensed under the Educational Community License,  Version 2.0 (the “License”); you may not
use this file except in compliance with the License.

You may obtain a copy of the License at http://www.osedu.org/licenses/ECL-2.0 Unless required
by applicable law or agreed to in writing, software distributed under the License is distributed
on an “AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.

This implementation file shows some compare operations
"""

def print_info(i, name: str):
    print(f"Type of {name} = {type(i)}")
    print(f"The memory address of {name} is {id(i)}")


i = 5
print_info(i, name="i")

x = 5.0
print_info(i, name="x")

y = 5
print_info(i, name="y")

k = True
print_info(i, name="k")
print_info(True, name="built in True")

if i == x:
    print("i == x is True")
else:
    print("i == x is False")

if i is x:
    print("i is x is True")
else:
    print("i is x is False")

if i is y:
    print("i is y is True")
else:
    print("i is y is not True")
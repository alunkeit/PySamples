"""
Licensed under the Educational Community License,  Version 2.0 (the “License”); you may not
use this file except in compliance with the License.

You may obtain a copy of the License at http://www.osedu.org/licenses/ECL-2.0 Unless required
by applicable law or agreed to in writing, software distributed under the License is distributed
on an “AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.

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
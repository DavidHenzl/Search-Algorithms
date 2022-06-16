"""Test file for search algoithms"""

import random
import search_algorithms as sa

a = [1, 3, 12, 13, 14, 20, 35, 48, 55, 56,
     66, 71, 72, 73, 75, 82, 87, 91, 95, 99]
# num = random.choice(a)
num = 100

print(f"num = {num}")
# print(f"correct index: {a.index(num)}")
print(f"linear: {sa.linear_search(a, num)}")
print(f"binary recursion: {sa.binary_search_recursion(a, 0, len(a) - 1, num)}")
print(f"binary iteration: {sa.binary_search_iteration(a, num)}")
print(f"jump search: {sa.jump_search(a, num)}")
print(f"fibonacci search: {sa.fibonacci_search(a, num)}")
print(f"exponential search: {sa.exponential_search(a, num)}")
print(
    f"interpolation search: {sa.interpolation_search(a, 0, len(a) - 1, num)}")

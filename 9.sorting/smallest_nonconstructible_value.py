"""
	Write a program which takes an array of positive integers and returns
	the smallest number which is not to the sum of a subset of elements 
	to the array.
"""
from typing import List

"""
	Suppose that a subset of the input array can produce a sum of V but
	not V + 1. If the next value, u, is <= V + 1, we'll be able to
	produce the sum of V + u but not V + u + 1. If the next value is
	greater than V + 1, then V + 1 cannot be constructible by the 
	input array
"""

# O(nlog) + O(n) in time and O(1) in space
def get_smallest_nonconstructible_value(A: List[int]) -> int:
	max_constructible_value = 0
	sorted_A = sorted(A)
	for a in sorted_A:
		if a > max_constructible_value + 1:
			break
		else:
			max_constructible_value += a
	return max_constructible_value + 1
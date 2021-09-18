"""
	Given an integer array, move all elements that are 0 to the left while maintaining
	the order of other elements in the array. The array has to be modified in-place.
"""
from typing import List

# O(n**2) in time
def brute_force(A: List) -> List:
	low = 0
	for i, a in enumerate(A):
		if a == 0:
			j = i - 1
			while j >= low:
				A[j + 1] = A[j]
				j -= 1
			A[low] = 0
			low += 1
	return A

# O(n) in time
def swap(A: List):
	len_A = len(A)
	n, i = len_A - 1, len_A - 1
	
	while i >= 0:
		if A[i] != 0:
			A[i], A[n] = A[n], A[i]
			n -= 1
		i -= 1
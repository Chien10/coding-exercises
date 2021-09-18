"""
	An inversion in an array a[] is a pair of entries a[i] and a[j] such that i < j but a[i] > a[j].
	Given an array, design a linearithmic algorithm to count the number of inversions.
"""
from typing import List

# O(n**2) in time
def brute_force(A: List[int]) -> int:
	len_A = len(A)
	count = 0

	for i, a in enumerate(A):
		j = i + 1
		for b in A[i + 1:]:
			if a > b and i < j:
				count += 1
			j += 1

	return count

def count_inversions(A: List[int]):
	len_A = len(A)
	count = 0
	
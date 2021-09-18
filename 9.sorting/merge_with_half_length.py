"""
	Suppose that the subarray a[0] to a[n−1] is sorted and the subarray a[n] to a[2∗n−1] is sorted.
	How can you merge the two subarays so that a[0] to a[2∗n−1] is sorted using an
	auxiliary array of length n (instead of 2n)?
"""
from typing import List

# O(n + n) in time and O(n) in space
def merge_with_half_length(A: List[int], B: List[int]):
	# length of A and B must be equal
	len_A, len_B = len(A), len(B)
	assert len_A == len_B

	A = A + len_B * [None]
	i, j, write_i = len_A - 1, len_B - 1, len_A + len_B - 1
	while i >= 0 and j >= 0:
		if A[i] > B[j]:
			A[write_i] = A[i]
			i -= 1
		else:
			A[write_i] = B[j]
			j -= 1
		write_i -= 1

	while j >= 0:
		A[write_i] = B[j]
		j -= 1
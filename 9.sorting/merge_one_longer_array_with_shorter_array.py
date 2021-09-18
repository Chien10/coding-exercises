"""
	Given two sort arrays, A and B, and A has empty rooms enough to fill all the elements in B.
	Merge the two arrays into the first array so that the resulting array is sorted
"""
from typing import List

# O(m + n) in time and space
def brute_force(A: List, B: List):
	C = []
	i, j = 0, 0
	len_A, len_B = len(A), len(B)
	
	while i < len_A and j < len_B:
		if A[i] < B[j]:
			C.append(A[i])
			i += 1
		else:
			C.append(B[j])
			j += 1

	while i < len_A:
		C.append(A[i])
		i += 1
	while j < len_B:
		C.append(B[j])
		j += 1

	for i, c in enumerate(C):
		A[i] = c

	return A

# O(m + n) in time and O(1) in space
def merge_two_sorted_array(A: List, B: List):
	len_A, len_B = sum([1 for a in A if a is not None]), len(B)
	A_idx, B_idx, write_idx = len_A - 1, len_B - 1, len_A + len_B - 1

	while A_idx >= 0 and B_idx >= 0:
		if A[A_idx] > B[B_idx]:
			A[write_idx] = A[A_idx]
			A_idx -= 1
		else:
			A[write_idx] = B[B_idx]
			B_idx -= 1
		write_idx -= 1

	# If all keys in B is greater than all keys in A, the remaining keys in A
	# is already in the desired positions
	while B_idx >= 0:
		A[write_idx] = B[B_idx]
		B_idx -= 1
		write_idx -= 1
	"""
		A = [5, 13, 17, None, None, None, None, None]
		B = [3, 7, 11, 19]
	"""
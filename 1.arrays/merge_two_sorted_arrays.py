from typing import List

# O(m + n) in both time and space

# O(n) in time
def rearrange_array(B: List[int], index: int):
	"""
		Move elements to the left to insert B[index] into the relevant position
	"""
	original_elem = B[index]
	index += 1
	len_B = len(B)
	while index < len_B and B[index] < original_elem:
		B[index - 1] = B[index]
		index += 1
	B[index - 1] = original_elem  

# O(m * n) in time and O(1) in space
"""
	For each element in A:
		Compare the element with B[0]:
			Swap the two elements if B[0] is lower
				Rearrange elements in B

	The final result is elements sorted from A to B
	Input:
			A = [2, 3, 8, 13]
			B = [1, 5, 9, 10, 15]
		-> A = [1, 2, 3, 5]
		   B = [8, 9, 10, 13, 15]
"""
def merge(A: List[int], B: List[int]):
	len_A = len(A)
	i = 0
	while i < len_A:
		if A[i] > B[0]:
			A[i], B[0] = B[0], A[i]
			rearrange_array(B, 0)
		i += 1

# O(min(mlogm, nlogn)) in time and O(1) in space
def merge_with_efficiency(A: List[int], B: List[int]):
	pass
	# https://www.geeksforgeeks.org/merge-two-sorted-arrays-o1-extra-space/
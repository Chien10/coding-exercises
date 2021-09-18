from typing import List
import bisect

## O(m * n) in time and O(min(m, n)) in space 
def brute_force(A: List, B: List) -> List:
	result = []
	for i, a in enumerate(A):
		if (i == 0 or a != A[i - 1]) and a in B:
			result.append(a)
	return result

# O(mlogn) in time and )(min(m, n)) in space
def intersect_with_binary_search(A: List, B: List):
	result = []
	len_A, len_B = len(A), len(B)
	for i, a in enumerate(A):
		idx = bisect.bisect_left(B, a)
		if (i == 0 or a != A[i - 1]) and idx < len_B and B[idx] == a:
			result.append(a)

	return result

def intersect_two_sorted_array(A: List, B: List):
	i, j, result = 0, 0, []
	len_A, len_B = len(A), len(B)
	while i < len_A and j < len_B:
		if A[i] == B[j]:
			if i == 0 or A[i] != A[i - 1]:
				result.append(A[i])
		elif A[i] < B[j]:
			i += 1
		else: # A[i] > B[j]
			j += 1
	return result
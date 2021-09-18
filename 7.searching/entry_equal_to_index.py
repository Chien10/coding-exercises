from typing import List

# Input is strictly sorted
# O(n) in time and space
def brute_force(A: List) -> List:
	result = []
	for i, a in enumerate(A):
		if i == a:
			result.append(a)
	return result

# O(logn) in time and O(n) in space
"""
	index 	i 	j
	entry   a   b
	Can a > i but b == j and b > a?
	=> No because if so, b = j = i + 1 <=> i < a < i + 1 (!) because a is integer
"""
def search_entry_equal_to_its_index(A: List) -> List:
	left, right = 0, len(A) - 1
	result = []

	while left <= right:
		mid = (left + right) // 2
		difference = A[mid] - mid

		if difference == 0:
			result.append(A[mid])
		elif difference > 0:
			right = mid - 1
		else:
			left = mid + 1
	return result

"""
	What if A has duplicates?
"""
import 5.binary_tree import iterative_binary_search
from typing import List

# Input is sorted
# O(logn) + O(n) in time
def brute_force(A: List, k) -> int:
	i = iterative_binary_search(A, k)
	if i == -1:
		return -1

	j = i - 1
	while j >= 0:
		if A[j] == k:
			return j
		j -= 1
	return i

# O(logn)
def search_first_of_k(A: List, k) -> int:
	left, right, result = 0, len(A) - 1, -1
	while left <= right:
		mid = (left + right) // 2
		if A[mid] > k:
			right = mid + 1
		elif A[mid] == k:
			result = mid
			right = mid - 1 # eliminate the right side
		else:
			left = mid + 1
	return result

"""

"""
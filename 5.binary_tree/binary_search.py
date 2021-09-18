from typing import Iterable

# Input must be sorted
# O(logn) in time
def recursive_binary_search(A: Iterable, low: int, high: int, key) -> int:
	if high >= low:
		mid = (high + low) // 2

		if A[mid] == key:
			return mid
		elif A[mid] > key:
			return binary_search(A, low, mid - 1, key)
		else:
			return binary_search(A, mid + 1, high, key)
	return -1

# O(logn) in time and O(1) in space
def iterative_binary_search(A: Iterable, key) -> int:
	low, high, mid = 0, len(A) - 1, 0
	while low <= high:
		mid = (low + high) // 2
		if A[mid] < key:
			low = mid + 1
		elif A[mid] > key:
			high = mid - 1
		else:
			return mid
	return -1
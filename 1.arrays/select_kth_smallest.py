"""
	Given an array of n items, find the kth smallest item
"""
from typing import List

def partition(array: List, low: int, high: int) -> int:
	i = low - 1
	pivot = array[high] # pick the last item as the pivot
	
	for j in range(low, high):
		if array[j] <= pivot:
			i += 1
			array[i], array[j] = array[j], array[i]

	array[i + 1], array[high] = array[high], array[i + 1]
	return i + 1

# O(n**2) in worst case but O(n) on average
def find_kth_smallest(array: List, k: int) -> int:
	"""
		k = [0, 1, ..., len(array) - 1]
	"""
	low, high = 0, len(array) - 1
	while high > low:
		j = partition(array, low, high)
		if j < k:
			low = j + 1
		elif j > k:
			high = j - 1
		else:
			return array[k]
	return array[k]
"""
	Counting sort requires the range of the potential items is known ahead of time
	If this range is big, the space required is huge (could be more than O(n))
	Not a comparison sort. Sorting non-integer items only.
	O(n + k) in time guarantee and O(n + k) in space where k is the number of possible
	values. In many case, k is O(n) -> O(n) in time and space
"""
from typing import List, Tuple

def find_bound(array: List) -> Tuple:
	low = float('inf')
	high = float('-inf')
	for item in array:
		if item < low:
			low = item
		if item > high:
			high = item
	return low, high

def counting_sort(array: List, low=0, high=None) -> List:
	len_array = len(array)
	
	if len_array <= 1:
		return array

	if not high:
		low, high = find_bound(array)

	counts = [0 for _ in range(low, high + 1)]
	for item in array:
		# minus from low to convert from low-indexed array to 0-indexed array index
		counts[item - low] += 1
	for i in range(1, high - low + 1):
		counts[i] += counts[i - 1]

	output = array[:]
	for i in range(len_array - 1, -1, -1):
		output[counts[array[i] - low] - 1] = array[i]
		counts[array[i] - low] -= 1
	return output
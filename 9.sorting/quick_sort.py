from insertion_sort import insertion_sort
from typing import List, Tuple
CUTOFF = 10

"""
	In average case, quick sort has 39% more compares than merge sort but faster than merge sort
	because of less data movement in practice.
	Quick sort is not stable
"""

def partition(array: List, low: int, high: int) -> Tuple[int, List]:
	i = low - 1
	pivot = array[high] # pick the last item as the pivot
	
	for j in range(low, high):
		if array[j] <= pivot:
			i += 1
			array[i], array[j] = array[j], array[i]

	array[i + 1], array[high] = array[high], array[i + 1]
	return i + 1, array

def return_median_of_three(array: List, low: int, mid: int, high: int) -> int:
	if (array[low] - array[mid]) * (array[low] - array[high]) < 0:
		return low
	if (array[mid] - array[low]) * (array[mid] - array[high]) < 0:
		return mid
	return high

def quick_sort(array: List, low: int, high: int) -> List:
	if high <= low + CUTOFF - 1:
		insertion_sort(array)
		return array

	median = return_median_of_three(array, low, low + (high - low) // 2, high)
	array[high], array[median] = array[median], array[high]

	if low < high:
		low, array = partition(array, low, high)
		array = quick_sort(array, low, high - 1)
		array = quick_sort(array, low + 1, high)
	return array

def main():
	array = [10, 2, 9, 8, 4, 5, 6, 1, 4, 2, 4]
	len_array = len(array) - 1
	sorted_array = quick_sort(array, 0, len_array - 1)

if __name__ == '__main__':
	main()
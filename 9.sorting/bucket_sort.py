"""
	Bucket sort assumes that the input is drawn from a uniform distribution and has an average-case
	running time of O(n) and O(n ** 2) in worst case.
	The idea of bucket sort is to divide the interval [0, 1) into n equal-sized
    buckets, and then distribute the n input numbers into the buckets.
    Since the inputs are uniformly distributed over [0, 1), we don't expect
    many numbers to fall into each bucket.
    We then simply sort the numbers in each bucket and  go through the buckets
    in order, listing the elements in each.
"""
from typing import List
from insertion_sort import insertion_sort

def bucket_sort(array: List, buckets: int = 10) -> List:
	B = [[] for _ in range(buckets)]
	for item in array:
		B[int(item * buckets)].append(item)

	result = []
	for i in range(buckets):
		insertion_sort(B[i])
		result.extend(B[i])

	return result
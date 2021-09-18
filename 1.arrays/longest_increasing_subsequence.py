"""
	Given an array of n elements, find the longest, strictly increasing subsequence in the array
"""
from typing import List

# O(n**2) + O(n) in time
# Only work for longest continuous increasing subsequent
def brute_force(A: List[int]) -> List[int]:
	sub_arrs = []
	for i, _ in enumerate(A[:-1]):
		temp = [A[i]]
		prev_num = A[i]
		for a in A[i + 1: ]:
			if a > prev_num:
				temp.append(a)
				prev_num = a
			else:
				break
		if len(temp) > 1:
			sub_arrs.append(temp)

	result_arr = []
	for sub_arr in sub_arrs:
		if len(sub_arr) > len(result_arr):
			result_arr = sub_arr
	return result_arr

# O(n^2) in time and O(n) in space
def dynamic_programming(A: List[int]) -> int:
	len_A = len(A)
	length = [1] * len_A

	for i in range(1, len_A):
		for j in range(0, i):
			if A[i] > A[j]:
				length[i] = max(length[i], length[j] + 1)

	maximum = 0
	for i in range(len_A):
		maximum = max(maximum, length[i])
	return maximum


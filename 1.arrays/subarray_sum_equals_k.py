"""
	Given an array of integers and an integer k, you need to find the total number of
	continuous subarrays whose sum equals to k.
"""
from typing import List

# O(n**2) in time and O(1) in space
def brute_force2(A: List[int], k: int) -> int:
	count = 0
	len_A = len(A)

	if len_A == 0:
		return count
	for i in range(len_A):
		temp = A[i]
		if temp == k:
			count += 1
		for i in range(i + 1, len_A):
			temp += A[i]
			if temp == k:
				count += 1
	return count

# O(n) + O(n**2) in time and O(n) in space
def use_cummulative_sum(A: List[int], k: int) -> int:
	len_A = len(A)
	count = 0
	# cum_sum[i] = sum_{j=0}^{i-1} A[j]
	cum_sum = [0] * (len_A + 1)

	for i in range(1, len_A + 1):
		cum_sum[i] = cum_sum[i - 1] + A[i - 1]

	for i in range(len_A - 1):
		for j in range(i + 1, len_A):
			if cum_sum[j] - cum_sum[i] == k:
				count += 1
	return count

# O(n) in time and O(n) in space
def use_hash_table(A: List[int], k: int) -> int:
	len_A = len(A)
	cum_sum = {0: 1} # sum mapped to occurence
	count, current_sum = 0, 0

	for i in range(len_A):
		current_sum += A[i]
		
		try:
			# diff + k = current_sum
			# then if diff exists, k will exist
			diff = cum_sum[current_sum - k]
			count += diff
		except:
			pass

		cum_sum[current_sum] = cum_sum.get(current_sum, 0) + 1
	return count
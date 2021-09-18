"""
	Your input is an array of integers, and you have to reorder its entries so that
	the even entries appear first
"""
# O(1) in space and O(n) in time
from typing import List

def even_first(A: List[int]) -> List[int]:
	next_even_idx, next_odd_idx = 0, len(A) - 1
	while next_even_idx < next_odd_idx:
		if A[next_even_idx] % 2 == 0:
			next_even_idx += 1
		else:
			A[next_even_idx], A[next_odd_idx] = A[next_odd_idx], A[next_even_idx]
			next_odd_idx -= 1
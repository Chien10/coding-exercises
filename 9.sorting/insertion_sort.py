from typing import List

# Insertion sort is stable
# O(n**2) in time and O(1) in space
# On average, 0.25 * N ** 2 compares and 0.25 * N ** 2 exchanges
# If the input is already sorted, N - 1 compares and 0 exchanges
# If the input's order is reversed, 0.5 * N ** 2 compares and 0.5 * N ** 2 exchanges
"""
	Inversion is a pair of keys that are out of order
	A E E L M O T R X P S has six inversions: T-R, T-P, T-S, R-P, X-P and X-S
	An array is partially sorted if the number of inversions is <= cN
"""
# For a partially sorted array, insertion sort runs in O(N) since the number of exchanges
# equal to the number of inversions
# number of compares = number of exchanges + (N - 1)
def insertion_sort(A: List[int], low: int = 0, high: int = 0):
	len_A = len(A)
	for i in range(1, len_A):
		key = A[i]

		j = i - 1
		while j >= 0 and key < A[j]:
			A[j + 1] = A[j]
			j -= 1
		A[j + 1] = key
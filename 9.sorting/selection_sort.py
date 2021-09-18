from typing import List

# Selection sort is not stable
# O(n**2) in time and O(1) in space
# N**2/2 compares and N exchanges
# Quadratic in time even if the input is already sorted
# Maintain two parts: sorted and remaining
def selection_sort(A: List[int]):
	len_A = len(A)
	for i in range(len_A):
		min = i
		for j in range(i + 1, len_A):
			if A[j] <= A[min]:
				min = j
		A[i], A[min] = A[min], A[i]
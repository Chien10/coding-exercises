from typing import List

# O(n**2) in time
def bubble_sort(A: List):
	len_A = len(A)
	for i in range(len_A):
		swapped = False
		for j in range(0, len_A - i - 1):
			if A[j] > A[j + 1]:
				A[j], A[j + 1] = A[j + 1], A[j]
				swapped = True
		if not swapped:
			break
from typing import List

# O(n**1.5) in time
# Fast for small and medium size array
# Used in embedded system and hardware sort because of the short length of code
def shell_sort(A: List[int]):
	len_A = len(A)

	h = 1
	# 3x + 1 increment sequence
	while h < len_A / 3:
		h = 3 * h + 1

	# h-sort the array
	while h >= 1:
		# insertion sort
		for i in range(h, len_A):
			j = i
			while j >= h and A[j] <= A[j - h]:
				A[j], A[j - h] = A[j - h], A[j]
				j -= h
		# move to the next increment
		h = h // 3
from typing import List
from insertion_sort import insertion_sort

# Merge sort is stable
# O(nlogn) in time and O(n) in space
# At most NlogN compares and 6NlogN array access
class MergeSort(object):
	"""
		Recursive, top-down approach
	"""
	def __init__(self, numbers: List[int]):
		self.values = numbers
		self.count = len(numbers)
		self.CUTOFF = 7

	def sort(self):
		self.merge_sort(0, self.count - 1)
		return self.values

	def merge_sort(self, low: int, high: int):
		if low < high:
			# Switch to insertion sort when the input is small
			if high <= low + self.CUTOFF - 1:
				insertion_sort(self.values, low=low, high=high)
			else:
				mid = (low + high) // 2

				self.merge_sort(low, mid)
				self.merge_sort(mid + 1, high)
				# If the biggest element in the left side is lower or equal to
				# the smallest element in the right side
				if A[mid + 1] >= A[mid]:
					self.merge(low, mid, high)

	def merge(self, low: int, mid: int, high: int):
		b = []
		i, j = low, mid + 1

		while i <= mid and j <= high:
			if self.values[i] <= self.values[j]:
				b.append(self.values[i])
				i += 1
			else:
				b.append(self.values[j])
				j += 1

		while i <= mid:
			b.append(self.values[i])
			i += 1
		while j <= high:
			b.append(self.values[j])
			j += 1

		for index, val in enumerate(b):
			self.values[low + index] = val

def merge(A: List[int], l: int, m: int, r: int):
	n1 = m - l + 1
	n2 = r - m
	
	L = [0] * n1
	R = [0] * n2

	for i in range(n1):
		L[i] = a[l + i]
	for j in range(n2):
		R[i] = a[m + i + 1]

	i, j, k = 0, 0, l
	while i < n1 and j < n2:
		if L[i] > R[j]:
			A[k] = R[j]
			j += 1
		else:
			A[k] = L[i]
			i += 1
		k += 1

	while i < n1:
		A[k] = L[i]
		i += 1
		k += 1
	while j < n2:
		A[k] = R[j]
		j += 1
		k += 1

# 10% slower the preceding version
def bottom_up_merge_sort(A: List[int]) -> List[int]:
	width = 1
	len_A = len(A)

	while width < len_A:
		l = 0
		while l < n:
			r = min(l + (width * 2 - 1), n - 1)
			m = (l + r) // 2

			if width > n // 2:
				m = r - (n % width)
			merge(a, l, m, r)

			l += width * 2
		width *= 2
	return A
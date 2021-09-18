import heapq
from typing import List

# O(klogk) in time and O(1) in space
def find_k_largest_elements(A: List[int], k: int) -> List[int]:
	heapq.heapify(A)
	return heapq.nlargest(A, k)

# O(n) in time and O(k) in space
def get_k_largest_elements(A: List[int], k: int) -> List[int]:
	max_heap = MaxHeap(A, len(A))

	result = []
	for i in range(k):
		result.append(max_heap.extract_max())
	return result
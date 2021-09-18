from typing import List
import heapq
from max_heap import MaxHeap

# O(nlogn) in time and O(n) in space
def heap_sort(A: List[int], ascending=True):
	# Create an empty priority queue
	priority_queue = []
	heapq.heapify(priority_queue)

	if ascending:
		ascending = -1
	else:
		ascending = 1

	for a in A:
		heapq.heappush(priority_queue, (ascending * a, a))

	len_A = len(A)
	i = len_A - 1
	while i >= 0:
		A[i] = heapq.heappop(priority_queue)[1]
		i -= 1
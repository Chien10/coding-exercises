import heapq # min heap

def demonstrate_min_heap():
	L = [3, 5, 0, 1, 9, 8, 4]
	heapq.heapify(L) # in-place conversion
	print(L)

	k_largest = heapq.nlargest(3, L)
	k_smallest = heapq.nsmallest(3, L)

	heapq.heappush(L, 2)
	smallest = heapq.heappop(L)
	print(L[0])
	smallest = heapq.heappushpop(L, 3)

	i = 3
	first_child_i = 2 * i + 1
	second_child_i = 2 * i + 2
	parent = (k - 1) // 2
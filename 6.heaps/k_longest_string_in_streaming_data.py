"""
	Suppose you were asked to write a program which takes a sequence of strings presented in
	"streaming" fashion: you cannot back up to read an earlier value. Your program must compute the
	k longest strings in the sequence. All that is required is the k longest strings-it is not
	required to order these strings
"""
import itertools, heapq
from typing import List

def get_top_k(k: int, stream: List[str]) -> List[str]:
	min_heap = [(len(s), s) for s in itertools.islice(stream, k)] # the first k elements
	heapq.heapify(min_heap)

	for next_string in stream:
		# O(logk)
		if len(next_string) > len(min_heap[0]):
			heapq.heappushpop(min_heap, (len(next_string), next_string))
	return [p[1] for p in heapq.nsmallest(k, min_heap)]
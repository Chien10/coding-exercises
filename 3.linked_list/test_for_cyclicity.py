import itertools
from linked_list_node import LinkedListNode, SinglyLinkedList

# O(n) in space and time
def brute_force(L: SinglyLinkedList):
	look_up = {} # Dict[Tuple[int], int]
	for node in L:
		data = node.data
		try:
			next_data = node.next.data
		except:
			next_data = None
		L[(data, next_data)] = L.get((dat, next_data), 0) + 1
		if L[(data, next_data)] > 1:
			return node
	return None

# O(n) in time and O(1) in space
def get_cycle_len(end: LinkedListNode) -> int:
	start, length = end, 0
	while True:
		length += 1
		if start is end:
			return length

def test_for_cyclicity(head: LinkedListNode) -> LinkedListNode:
	fast = slow = head
	while fast and fast.next and fast.next.next:
		slow, fast = slow.next, fast.next.next
		if slow is fast: # two runners meet at one node within the cycle
			cycle_len_advanced_iter = head
			for _ in range(get_cycle_len(slow)): # go to the node within the cycle
				cycle_len_advanced_iter = cycle_len_advanced_iter.next

			it = head
			while it is not cycle_len_advanced_iter: # find the first node in the cycle
				it = it.next
				cycle_len_advanced_iter= cycle_len_advanced_iter.next
			return it
	return None
"""
	Remove duplicate values from a sorted singly linked list
"""
from link_list_node import LinkedListNode, SinglyLinkedList

# O(n) in time
def remove_duplicates(L_head: LinkedListNode) -> LinkedListNode:
	current_node = L
	while current_node:
		next_node = current_node.next
		while next_node and next_node.data == current_node.data:
			next_node = next_node.next

		current_node.next = next_node.next
		current_node = next_node
	return L_head

"""
	 Let m be a positive integer and L a sorted singly linked list of integers. For each integer k,
	 if k appears more than m times in L, remove all nodes from L containing k.
"""
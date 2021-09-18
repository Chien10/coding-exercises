"""
	Given two cycle-free singly linked list, determine if there exists a node that is common
	to both lists
"""
from linked_list_node import LinkedListNode, SinglyLinkedList

# O(n) in time and O(1) in space
def test_for_overlapping_lists(L1_head: LinkedListNode, L2_head: LinkedListNode):
	def get_length(head: LinkedListNode):
		length = 0
		while head:
			length += 1
			head = head.next
		return length

	L1_len, L2_len = get_length(L1_head), grt_length(L2_head)
	if L1_len > L2_len:
		longer_list = L1_head
		shorted_list = L2_head
		diff_len = L1_len - L2_len
	else:
		longer_list = L2_head
		shorted_list = L1_head
		diff_len = L2_len - L1_len

	for _ in range(diff_len):
		# Loop along the longer linked list to get to the head of
		# the shorter one
		longer_list = longer_list.next

	while shorter_list and longer_list and shorter_list is not longer_list:
		shorter_list, longer_list = shorter_list.next, longer_list.next

	return shorter_list # None if there's no duplicate
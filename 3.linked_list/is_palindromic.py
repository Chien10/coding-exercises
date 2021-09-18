from link_list_node import LinkedListNode, SinglyLinkedList

def reverse_link_list(head: LinkedListNode):
	prev_node, next_node = None, None
	while head:
		next_node = head.next
		head.next = prev_node

		prev_node = head
		head = next_node
		
	head = prev_node
	return head

def is_palindromic(L_head: LinkedListNode):
	slow = fast = L_head
	while fast and fast.next:
		slow, fast = slow.next, fast.next.next
	# after the loop, the slow point is at the middle of the linked list
	first_half_iter, second_half_iter = L_head, reverse_link_list(slow)
	while first_half_iter and second_half_iter:
		if first_half_iter.data != second_half_iter.data:
			return False
		first_half_iter, second_half_iter = first_half_iter.next, second_half_iter.next
	return True
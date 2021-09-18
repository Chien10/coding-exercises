"""
	You are given two non-empty linked lists representing two non-negative integers.
	The digits are stored in reverse order, and each of their nodes contains a single digit.
	Add the two numbers and return the sum as a linked list.

	You may assume the two numbers do not contain any leading zero, except the number 0 itself.
	For instance:

					Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
					Output: 7 -> 0 -> 8
"""

class ListNode(object):
    def __init__(self, x: int):
        self.value = x
        self.next = None

def add_two_numbers(l1: ListNode, l2: ListNode):
	return add_helper(l1, l2, None, None, 0)

def add_helper(l1: ListNode, l2: ListNode, result_node: ListNode, prev_node: ListNode, carry: int):
	if not l1 or not l2:
		if carry == 1:
			prev_node.next = ListNode(1)
		return result_node

	if not l1:
		sum_value = l2.value + carry
		l2 = l2.next
	elif not l2:
		sum_value = l1.value + carry
		l1 = l1.next
	else:
		sum_value = l1.value + l2.value + carry
		l1, l2 = l1.next, l2.next

	new_node = ListNode(sum_value % 10)
	if not result_node:
		result_node = new_node
		prev_node = result_node
	else:
		prev_node.next = new_node
		prev_node = new_node

	return add_helper(l1, l2, result_node, prev_node, sum_value // 10)
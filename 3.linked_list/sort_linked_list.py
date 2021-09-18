from linked_list_node import LinkedListNode, SinglyLinkedList

def get_middle(head: LinkedListNode) -> LinkedListNode:
	if head is None:
		return head

	slow, fast = head, head
	while fast.next is not None and fast.next.next is not None:
		slow = slow.next
		fast = fast.next.next
	return slow

# O(n + m) in time and O() in space
def merge_left_and_right(left_head: LinkedListNode, right_head: LinkedListNode):
	result = None
	if left_head is None:
		return right_head
	if right_head is None:
		return left_head

	if left_head.key <= right_head.key:
		result = left_head
		result.next = merge_left_and_right(left_head.next, b)
	else:
		result = right_head
		result.next = merge_left_and_right(left_head, right_head.next)
	return result

def merge_sort(head: LinkedListNode):
	if head is None or head.next is None:
		return head

	middle = get_middle(head)
	next_to_middle = middle.next
	middle.next = None

	left_head = merge_sort(head)
	right_head = merge_sort(next_to_middle)

	sorted_linked_list = merge_left_and_right(left_head, right_head)
	return sorted_linked_list
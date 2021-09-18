from linked_list_node import LinkedListNode

def print_linked_list_in_reverse(head: LinkedListNode):
	stack = []
	while head:
		stack.append(head.data)
		head = head.next
	while stack:
		print(stack.pop())
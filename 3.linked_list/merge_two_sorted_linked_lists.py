from linked_list_node import LinkedListNode, SinglyLinkedList

# O(n + m)
def merge_two_sorted_linked_lists(L1: SinglyLinkedList, L2: SinglyLinkedList) -> SinglyLinkedList:
	dummy_head = SinglyLinkedList()
	while L1.head and L2.head:
		if L1.head.data < L2.head.data:
			dummy_head.append(L1.head.data)
			L1.head = L1.head.next
		else:
			dummy_head.append(L2.head.data)
			L2.head = L2.head.next

	while L1.head:
		dummy_head.append(L1.head.data)
		L1.head = L1.head.next
	while L2.head:
		dummy_head.append(L2.head.data)
		L2.head = L2.head.next

	return dummy_head
from typing import List

class LinkedListNode(object):
	def __init__(self, data: int, next_node=None):
		self.data = data
		self.next = next_node

	def __repr__(self):
		return repr(self.data)

	def __ge__(self, a_node):
		return self.data >= a_node.data

	def __gt__(self, a_node):
		return self.data > a_node.data

	def __le__(self, a_node):
		return self.data <= a_node.data

	def __lt__(self, a_node):
		return self.data < a_node.data

	def __eq__(self, a_node):
		return self.data == a_node.data

class SinglyLinkedList(object):
	def __init__(self, nodes: List[int] = None):
		self.head: LinkedListNode = None
		if nodes:
			current_node = LinkedListNode(data=nodes.pop(0))
			self.head = current_node
			for node_data in nodes:
				current_node.next = LinkedListNode(data=node_data)
				current_node = current_node.next

	def __repr__(self):
		if self.head is None:
			return 'None'
		nodes = []
		current_node = self.head
		while current_node:
			nodes.append(repr(current_node.data))
			current_node = current_node.next
		return 'None -> ' + ' -> '.join(nodes) + ' -> None'

	def __iter__(self):
		node = self.head
		while node:
			yield node
			node = node.next

	def __len__(self):
		count = 0
		node = self.head
		while node:
			count += 1
			node = node.next
		return count

	def prepend(self, input):
		try:
			data = input.data
			input.next = self.head
			self.head = input
		except:
			self.head = LinkedListNode(input, self.head)

	def append(self, input):
		if self.head is None:
			try:
				data = input.data
				self.head = LinkedListNode(data=data)
				return
			except:
				self.head = LinkedListNode(data=input)
				return

		for current_node in self:
			pass
		try:
			data = input.data
			current_node.next = input
		except:
			next_node = LinkedListNode(data=input)
			current_node.next = next_node

	def find(self, key) -> LinkedListNode:
		try:
			key = key.data
			for node in self:
				if node.data == key:
					return node
		except:
			for node in self:
				if node.data == key:
					return node
		return None


	def remove(self, key):
		if self.head is None:
			return

		current_node = self.head
		prev_node = None
		try:
			key = key.data
		except:
			pass

		while current_node and current_node.data != key:
			prev_node = current_node
			current_node = current_node.next

		if prev_node is None:
			self.head = current_node.next
		elif current_node:
			prev_node.next = current_node.next
			current_node.next = None

	def reverse(self):
		current_node = self.head
		prev_node, next_node = None, None
		while current_node:
			next_node = current_node.next
			current_node.next = prev_node

			prev_node = current_node
			current_node = next_node
		self.head = prev_node

class DoublyLinkedListNode(object):
	def __init__(self, data: int, prev_node=None, next_node=None):
		self.data = data
		self.prev = prev_node
		self.next = next_node

	def __repr__(self):
		return repr(self.data)

class DoublyLinkedList(object):
	def __init__(self, nodes: List[int] = None):
		self.head: DoublyLinkedListNode = None
		if nodes:
			current_node = DoublyLinkedListNode(data=nodes.pop(0))
			self.head = current_node
			for node_data in nodes:
				new_node = LinkedListNode(data=node_data)
				current_node.next = new_node
				new_node.prev = current_node
				current_node = current_node.next

	def __repr__(self):
		if self.head is None:
			return 'None'
		nodes = []
		current_node = self.head
		while current_node:
			nodes.append(repr(current_node.data))
			current_node = current_node.next
		return 'None <-> ' + ' <-> '.join(nodes) + ' <-> None'

	def __iter__(self):
		node = self.head
		while node:
			yield node
			node = node.next

	def __next__(self):
		pass

	def __len__(self):
		count = 0
		node = self.head
		while node:
			count += 1
			node = node.next
		return count

	def prepend(self, input):
		try:
			data = input.data
			input.next = self.head
			if self.head is not None:
				self.head.prev = input
			self.head = input
		except:
			temp = self.head
			self.head = DoublyLinkedListNode(input, self.head)
			temp.prev = self.head

	def append(self, input):
		if self.head is None:
			try:
				data = input.data
				self.head = DoublyLinkedListNode(data=data)
				return
			except:
				self.head = DoublyLinkedListNode(data=input)
				return

		for current_node in self:
			pass
		try:
			data = input.data
			current_node.next = input
			input.prev = current_node
		except:
			next_node = DoublyLinkedListNode(data=input)
			current_node.next = next_node
			next_node.prev = current_node

	def find(self, key) -> LinkedListNode:
		try:
			key = key.data
			for node in self:
				if node.data == key:
					return node
		except:
			for node in self:
				if node.data == key:
					return node
		return None


	def remove(self, key):
		if self.head is None:
			return

		current_node = self.head
		try:
			key = key.data
		except:
			pass

		while current_node and current_node.data != key:
			current_node = current_node.next

		if current_node.prev is None:
			self.head = current_node.next
		elif current_node:
			current_node.prev.next = current_node.next
			current_node.next.prev = current_node.prev
			current_node.next = None
			current_node.prev = None

	def reverse(self):
		pass
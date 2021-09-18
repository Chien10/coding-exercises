from typing import List

# Enq: O(1). Deq: O(n) to move elements from the first stack to the second stack
# and O(n) to move elements from the second stack back to the first stack
class QueueWithTwoStacks:
	def __init__(self):
		self.enq, self.deq = [], []

	def enqueue(self, an_element):
		self.enq.append(an_element)

	def dequeue(self):
		while self.enq:
			an_element = self.enq.pop()
			self.deq.append(an_element)

		if len(self.deq) == 0:
			raise IndexError('dequeue(): empty queue')
		deq_element = self.deq.pop(0)

		while self.deq:
			an_element = self.deq.pop()
			self.enq.append(an_element)
		return deq_element

# O(1) in time for enqueue.
# O(m) in time for dequeue to move elements from the first stack to the second stack
# while m is the number of element in the first stack
class QueueWithTwoStacksModified:
	def __init__(self):
		self.enq, self.deq = [], []

	def enqueue(self, an_element):
		self.enq.append(an_element)

	def dequeue(self):
		if self.deq != []:
			while self.enq:
				self.deq.append(self.enq.pop())

		if not self.deq:
			raise IndexError('empty queue')
		return self.deq.pop()
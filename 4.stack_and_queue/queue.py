import collections

class Queue(object):
	def __init__(self):
		self._data = collections.deque()

	def enqueue(self, x):
		self._data.append(x)

	def dequeue(self):
		return self._data.popleft()

	def max(self):
		return max(self._data)
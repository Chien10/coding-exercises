from typing import List, Tuple
import collections

# O(n) in time to find the maximum element. O(1) in space
class NaiveStack:
	def __init__(self, an_iterable: List = None):
		self.stack = an_iterable

	def __str__(self):
		if self.stack is not None:
			return '[' + ', '.join([str(element) for element in self.stack]) + ']'
		return None

	def __len__(self):
		return len(self.stack)

	def is_empty(self):
		return len(self.stack) == 0

	def push(self, an_element):
		if self.stack is None:
			self.stack = []

		self.stack.append(an_element)

	def pop(self):
		assert self.stack is not None
		if self.is_empty():
			raise IndexError('pop(): empty stack')

		return self.stack.pop()

	def get_max(self):
		if self.is_empty() or self.stack is None:
			raise IndexError('get max value from an empty stack')
		return max(self.stack)

# Using heap
# O(logn) in time to find max. O(n) in space
class StackWithHeapForMaxAPI(object):
	pass

# Using cache
# O(1) in time to find max. O(n) in space
class StackWithCache(object):
	Cache = collections.namedtuple('Cache', ('element', 'max'))

	def __init__(self):
		self.stack: List[Tuple] = []

	def is_empty(self):
		return len(self.stack) == 0

	def push(self, an_element):
		new_element = self.Cache(x, x if self.is_empty() else max(x, self.max()))
		self.stack.append(new_element)

	def pop(self):
		if self.is_empty():
			raise IndexError('pop(): empty stack')
		return self.stack.pop().element

	def get_max(self):
		if self.is_empty():
			raise IndexError('max(): empty stack')
		return self.stack[-1].max

# Using another class to record the occurence of the maximu value
# O(n) in worst case for space but if the number of distinct values are small
# or the maximum changes infrequently, the space is just O(1)
# O(1) in time to find
class StackWithMaxOccurence(object):
	class MaxWithCount:
		def __init__(self, max, count: int):
			self.max, self.count = max, count

	def __init__(self):
		self.stack = []
		self.cache: Tuple[MaxWithCount] = []

	def is_empty(self):
		return len(self.stack)

	def get_max(self):
		if self.is_empty():
			raise IndexError('max(): empty stack')
		return self.cache[-1].max

	def push(self, an_element):
		self.stack.append(an_element)

		if len(self.cache) == 0:
			self.cache.append(self.MaxWithCount(an_element, 1))
		else:
			current_max = self.cache[-1].max
			if an_element == current_max:
				self.cache[-1].count += 1
			elif an_element > current_max:
				self.cache.append(self.MaxWithCount(an_element, 1))

	def pop(self):
		if self.is_empty():
			raise IndexError('pop(): empty stack')

		pop_element = self.stack.pop()
		current_max = self.cache[-1].max

		if pop_element == current_max:
			self.cache[-1].count -= 1
			if self.cache[-1].count == 0:
				self.cache.pop()

		return pop_element
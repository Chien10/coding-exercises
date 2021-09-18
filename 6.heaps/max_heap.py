	import heapq
	from typing import List
	import math

	class MaxHeap(object):
		def __init__(self, an_array: List[int], heap_size: int):
			self.array = an_array
			self.size = heap_size
			self.max_size = len(an_array)

			self.swap_count = 0 # how many swap operations

		def get_heap(self):
			return self.array

		def get_parent(self, index: int) -> int:
			parent_idx = (index - 1) // 2
			if parent_idx < 0:
				return None
			return parent_idx

		def get_left_child(self, index: int) -> int:
			left_child_idx = 2 * index + 1
			if left_child_idx < self.size:
				return left_child_idx
			return None

		def get_right_child(self, index: int) -> int:
			right_child_idx = 2 * index + 2
			if right_child_idx < self.size:
				return right_child_idx
			return None

		def sift_up(self, index: int) -> int:
			i, parent_idx = index, None
			if i is not None:
				parent_idx = self.get_parent(i)
			if parent_idx is not None:
				while i > 0 and self.array[parent_idx] < self.array[i]:
					self.array[parent_idx], self.array[i] = \
						self.array[i], self.array[parent_idx]
					i = parent_idx

		def sift_down(self, index: int) -> int:
			max_index = index
			
			left_index = self.get_left_child(index)
			if left_index is not None and left_index < self.size and \
				self.array[left_index] > self.array[max_index]:
				max_index = left_index

			right_index = self.get_right_child(index)
			if right_index is not None and right_index < self.size and \
				self.array[right_index] > self.array[max_index]:
				max_index = right_index

			if index != max_index:
				print('{} {}'.format(index, max_index))
				self.array[index], self.array[max_index] = self.array[max_index], self.array[index]
				self.swap_count += 1
				self.sift_down(max_index)

		def insert(self, new_element: int):
			if self.size == self.max_size:
				raise IndexError('Heap is full')
			else:
				self.size += 1
				# Insert at the leftmost vacant position in the last level
				self.array[self.size - 1] = new_element
				self.sift_up(self.size - 1)

		def extract_max(self):
			if self.size > 0:
				result = self.array[0]
				# replace the root with the last leaf
				self.array[0] = self.array[self.size - 1]
				self.size -= 1
				self.sift_down(0)

				return result
			else:
				raise IndexError('Heap is empty')

		def remove(self, index: int):
			if self.size > 0:
				self.array[index] = math.inf
				self.sift_up(index)
				self.extract_max()
			else:
				raise IndexError('Heap is empty')

		def change_priority(self, index: int, new_value: int):
			try:
				old_element = self.array[index]
				self.array[index] = new_value

				if new_value > old_element:
					self.sift_up(index)
				else:
					self.sift_down(index)
			except:
				raise IndexError(f'{index} does not exist')

		def build_heap(self):
			"""
				Bottom to up, starting from small subtree
				O(n)
			"""
			i = self.size // 2
			while i >= 0:
				self.sift_down(i)
				i -= 1

		def heap_sort(self):
			self.build_heap()
			i = self.size - 1
			while i > 0:
				self.array[i], self.array[0] = self.array[0], self.array[i]
				i -= 1
				self.sift_down(0)

		def partial_sorting(self, k: int) -> List[int]:
			self.build_heap()
			result = []

			for i in range(k):
				result.append(self.extract_max())
			return result
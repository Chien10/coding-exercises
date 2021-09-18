"""
	Suppose that the Milky Way contains approximately 10**12 stars and their coordinates are stored
	in a file. The Earth coordinate is (0, 0, 0). Find the k closest stars to Earth.
"""
import math
import heapq

from typing import List, Tuple

class Star:
	def __init__(self, x, y, z):
		self.x, self.y, self.z = x, y, z

	@property
	def distance(self):
		# Distance to Earth
		self._distance = math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
		return self._distance
	
	def __lt__(self, rhs):
		return self.distance < rhs.distance

	def __gt__(self, rhs):
		return self.distance > rhs.distance

	def __eq__(self, rhs):
		return self.distance == rhs.distance

	def __ne__(self, rhs):
		return self.distance != rhs.distance

# If all the data can fit into RAM
# O(k * n) in time
def brute_force(stars: List[Star], k: int) -> List[Star]:
	result = []
	for i in range(k):
		min_dist = stars[0].distance
		min_star = stars[0]
		min_idx = 0
		for i, star in enumerate(stars):
			if star.distance < min_dist:
				min_dist = star.distance
				min_star = star
				min_idx = i
		
		result.append(min_star)
		result.pop(min_idx)
	return result

# O(nlogn) in time
def brute_force1(stars: List[Star], k: int) -> List[Star]:
	return stars.sort()[:k]

# O(n * k) in time and O(k) in space
def find_closest_k_stars(stars: List[Star], k: int) -> List[Star]:
	max_heap = []
	for star in stars:
		heapq.heappush(max_heap, (-star.distance, star))
		if len(max_heap) == k + 1:
			heapq.heappop(max_heap)

	# farthest to closest
	return [star[1] for star in heapq.nlargest(k, max_heap)]

"""
	Design an O(nlogk) time algorithm reads a sequence of n elements and for each element, starting
	from the kth element, prints the kth largest element read up to that point. The length of the
	sequence is not known in advance. Your algorithm cannot use more than O(k) additional storage.
	What are the worst-case inputs for your algorithm?
"""

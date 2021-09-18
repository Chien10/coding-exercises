"""
	Given two arrays a[] and b[], each containing n distinct 2D points in the plane,
	design a subquadratic algorithm to count the number of points that are contained both in array
	a[] and array b[].
"""
from typing import List, Tuple

# O(n^2) in time
def brute_force(a: List[Tuple[float]], b: List[Tuple[float]]) -> int:
	count = 0
	for i in a:
		for j in b:
			if i == j:
				count += 1
	return count
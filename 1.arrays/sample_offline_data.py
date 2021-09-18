"""
	Implement an algorithm that takes an array of distinct elements and a size as input and return
	a subset of the given size of the array elements. All subsets should be equally likely.
	Return the result in the input array.
	
	To efficiently build a random subset of size exactly k, it's recommended to build
	a subset of size k - 1 and then add one element selected randomly from the rest.
	Mathematically, if all subsets of size k are equally likely, then the construction
	process ensures that the subsets of size k + 1 are also equally likely.
"""
from typing import List
import random

"""
	Example: sample a subset of size three from [3, 7, 5, 11]
	i = 0
		random_number_idx = random.randint(0, 3) = 2
		A = [5, 7, 3, 11]
	i = 1
		random_number_idx = random.randint(1, 3) = 3
		A = [5, 3, 7, 11]
	i = 2
		random_number_idx = random.randint(2, 3) = 11
		A = [5, 3, 11, 7]
	return A[:3] = [5, 3, 11]
"""
# O(k) in time and O(1) in space
def sample_offline_data(A: List[int], k: int) -> List[int]:
	len_A = len(A)
	for i in range(k):
		random_number_idx = random.randint(i, len_A - 1)
		A[i], A[random_number_idx] = A[random_number_idx], A[i]
	return A[:k]

"""
The rand() function in the standard C library returns a uniformly ranom number in [0, RAND_MAX - 1]
Does rand() mode n generate a number uniformly distributed in [0, n-1]
"""
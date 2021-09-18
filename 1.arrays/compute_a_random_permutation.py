"""
	Design an algorithm that creates uniformly random permutations of {0, 1, ..., n}.
	You are given a random number generator that returns integers in the set {0, 1, ..., n}
	with equal probability
"""
from typing import List
import random

from sample_offline_data import sample_offline_data

# O(n) in space and O(nlogn) in time (on average)
def brute_force(n: int) -> List[int]:
	picked_number = {}
	all_numbers = list(range(n))
	result = []

	while True:
		a_number = random.choice(all_numbers)
		try:
			temp = all_numbers[a_number]
		except:
			result.append(a_number)
			all_numbers[a_number] = 1

		if len(result) == n:
			break
	return result

# Permutation is combination when k = n
# O(n) + O(n) in time and O(1) in space
def compute_a_random_permutation(n: int) -> List[int]:
	A = list(range(n))
	result = sample_offline_data(A, k=n)
	return result
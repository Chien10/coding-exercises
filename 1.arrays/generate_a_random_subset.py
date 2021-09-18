"""

"""
from typing import List, Dict
import random

from sample_offline_data import sample_offline_data

# O(nlogn) in time and O(n) in space
def brute_force1(n: int, k: int) -> List[int]:
	result = []
	number_picked = {}
	while True:
		random_number = random.randint(0, n - 1)
		try:
			temp = number_picked[random_number]
		except:
			number_picked[random_number] = 1
			result.append(random_number)
		if len(result) == k:
			break
	return result

# O(n) + O(k) in time and O(n) in space
def generate_random_subset_with_offline_sampling(n: int, k: int) -> List[int]:
	A = list(range(n)) # O(n) in space and time
	result = sample_offline_data(A, k) # O(k) in time
	return result
"""
	If n >> k, most of the elements in A will be left untouched
"""

# O(k) + O(k) in time and O(k) in space
def generate_a_random_subset(n: int, k: int) -> List[int]:
	picked_numbers = {}
	for i in range(k):
		random_number = random.randrange(0, n - 1)

		picked_number = picked_numbers.get(random_number, random_number)
		picked_numbers[i] = picked_number
		picked_numbers[picked_number] = i
	return [picked_numbers[i] for i in range(k)]
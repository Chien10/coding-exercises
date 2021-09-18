"""
	Given a list of numbers between [1, 100], determine the missing number without using iteration.
	Assume that one number is always missing.
"""
from typing import list

def get_missing_number(lst: List[int]):
	total_numbers = list(range(1, 100 + 1))
	return set(total_numbers).difference(set(lst))
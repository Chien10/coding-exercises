"""
	Given a string, test if it can be permutated to form a palindrome
"""
import collections

# O(n) in time to construct the hash table and O(c) in space where c is the number
# of distinct characters
def test_palindrome_permutation(s: str) -> bool:
	"""
		A string that can be permutated to form a palindrome is the one that has
		the number of characters whose frequencies is odd is at most 1.
	"""
	hash_table = collections.Counter(s)
	return sum(value % 2 for value in hash_table.values()) <= 1
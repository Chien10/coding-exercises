import collections
from typing import List

"""
	Input as a list of words and returns groups of anagrams for those words.
	Each group contains at least two words.
"""

"""
	n is the number of words, m is the length of the longest word
	O(n * mlogm) to sort and O(n*m) to insert
"""
def find_anagrams(dictionary: List[str]) -> List[List[str]]:
	sorted_string_to_anagrams = collections.defaultdict(list)
	for s in dictionary:
		sorted_string_to_anagrams[''.join(sorted(s))].append(s)
	print(sorted_string_to_anagrams)

	return [
		group for group in sorted_string_to_anagrams.values() if len(group) >= 2
	]

A = ["debitcard", "elvis", "silent", "badcredit", "lives", "freedom", "listen", "levis", "money"]
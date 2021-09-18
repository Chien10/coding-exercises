from is_palindromic import is_palindromic

"""
	Given a string s, find the longest palindromic substring in s.
	You may assume that the maximum length of s is 1000 and the string only contains digits and
	English letters

	Example:
		Input: "babad"
		Output: "bab" or
		Note: "aba" is also a valid answer.

	Example:
		Input: "cbbd"
		Output: "bb"

	Example:
		Input: "ab"
		Output: "a"
"""
from collections import Counter

# O(n**3) in time and O(1) in space
def naive_approach(a_str: str) -> str:
	result = ''
	len_str = len(a_str)

	if len_str == 1:
		return a_str

	for i, _ in enumerate(a_str):
		j = i
		while j < len_str:
			current_str = a_str[i: j + 1]
			if is_palindromic(current_str):
				temp = current_str
				if len(temp) > len(result):
					result = temp
			j += 1
	return result

def get_longest_palindromic_substring(a_str: str) -> str:
	pass
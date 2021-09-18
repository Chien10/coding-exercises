"""
	Given a string, find the length of the longest substring without repeating characters.
	Examples:
		Given "abcabcbb", the answer is "abc", which the length is 3.
		Given "bbbbb", the answer is "b", with the length of 1.
		Given "pwwkew", the answer is "wke", with the length of 3.
		Given "dvdf", the answer is "vdf", with the length of 3
	Note that the answer must be a substring, "pwke" is a subsequence and not
	a substring (substring means every character must stands next to each other in the original string)
"""
from typing import List
from collections import Counter

# O(n**2) in time and O(n) in space
def brute_force(a_str: str) -> str:
	ls = ''
	for i, _ in enumerate(a_str):
		hist = {a_str[i]: 1}
		temp_ls = a_str[i]
		for char in a_str[i + 1:]:
			temp = hist.get(char, 0)
			if temp == 0:
				temp_ls += char
				hist[char] = 1
			else:
				# If the character has already appears, we finish the search
				break
		if len(temp_ls) > len(ls):
			ls = temp_ls
	return ls

# O(n) in both time and space
# Failed!
def fail_find_lswrc(a_str: str) -> int:
	len_str = 0
	hist = {}
	for char in a_str:
		len_str += 1
		hist[char] = -1
	len_sub = [0] * len_str

	start, current_idx, dup_idx = '', None, None
	for i in range(len_str):
		if i == 0:
			len_sub[i] = 1
			start += a_str[i]
			current_idx = i
			hist[a_str[i]] = i
		else:
			if hist[a_str[i]] == -1:
				len_sub[i] = 1 + len_sub[current_idx]
				start += a_str[i]
				current_idx = i
				hist[a_str[i]] = i
			else:
				start = a_str[i]
				if dup_idx is None:
					dup_idx = i
					len_sub[i] = i - hist[a_str[dup_idx]]
				else:
					len_sub[i] = i - hist[a_str[dup_idx]]
					dup_idx = i
				current_idx = i
				hist[a_str[i]] = i
		print('hist:',hist)
		print('len_sub:',len_sub)
		print('dup_idx:',dup_idx)
		print(80*'-')
	print(len_sub)
	max_idx = -1
	max = 0
	for i, val in enumerate(len_sub):
		if val > max:
			max = val
			max_idx = i
	return max

def find_lswrc(a_str: str):

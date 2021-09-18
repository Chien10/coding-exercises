"""
	Check if a given string contains all unique characters.
	Ask if the string is an ASCII string or a Unicode string.
	There are 128 characters in the ASCII, 256 in the extended ASCII and about 143,859 characters
	in the Unicode (https://unicode.org/faq/basic_q.html)
"""

# O(n**2) in time and O(1) in space
def brute_force(a_string: str):
	unique_all = True
	len_s = len(a_string)
	i = 0
	for s in a_string:
		for j in range(i + 1, len_s):
			if s != a_string[j]:
				unique_all = False
				return unique_all
	return unique_all

# O(n) in time and O(m) in space where m is the number of unique characters
def brute_force1(a_string: str):
	hash_table = {}
	for s in a_string:
		hash_table[s] = hash_table.get(s, 0) + 1
		if hash_table[s] > 1:
			return False
	return True

def check_for_ascii_string(a_string: str):
	"""
		If ASCII
	"""
	boolean = [False] * 128
	for a in a_string:
		i = ord(a)
		if boolean[i]:
			return False
		boolean[i] = 1
	return True

# O(n) in time and O(1) in space
def check_using_bit(a_string: str):
	"""
		For a string `abc`, the `checker` variable would be 1, then 11, then 111
		If the string is `abca`, for the last `a`: 111 & 1 > 0
	"""
	checker = 0
	print('checker:', bin(checker))
	len_s = len(a_string)
	for i in range(len_s):
		val = ord(a_string[i])
		if (checker & (1 << val)) > 0:
			return False
		checker = checker | (1 << val)
		print('checker:', bin(checker))
	return True
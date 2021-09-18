"""
	Given two strings s and t, does s occur as a substring of t?
"""

# O(1) in space and O(len_s * (len_t - len_s)) in time
def brute_force(s: str, t: str) -> bool:
	len_s = len(s)
	len_t = len(t)
	return any(s == t[i: i + len(s)] for i in range(len_t - len_s))

# Rolling hash
def rehash(prev_char: str, next_char: str, current_hash: int, d: int):
	return ((current_hash - ord(prev_char)* d) << 1) + ord(next_char)

"""
	Preprocessing: O(m) in time where m is the length of the substring
	Searching time: O(n * m) in worst case but O(n + m) on average
"""
def karp_rabin_algorithm(string: str, substr: str):
	len_str, len_substr = len(string), len(substr)
	
	d = 1
	# Compute d = 2 ** (m - 1)
	for i in range(1, len_substr):
		d = d << 1

	h_string, h_substr, i = 0, 0, 0
	while i < len_substr:
		h_string = (h_string << 1) + ord(string[i])
		h_substr = (h_substr << 1) + ord(substr[i])
		i += 1
	print('window:', string[0: len_substr])
	print('h_string=', h_string)
	print(20*'-')

	# Searching
	j = 0
	while j <= len_str - len_substr:
		print('window:',string[j: len_substr + j])
		if h_string == h_substr and substr == string[j: len_substr + j]:
			return j
		h_string = rehash(string[j], string[j + len_substr], h_string, d)
		print('h_string=', h_string)
		print(20*'-')
		j += 1
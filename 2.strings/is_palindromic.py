# O(n) in time and O(1) in space
def is_palindromic(s: str) -> bool:
	# Only works for single string
	len_s = len(s)
	for i in range(len_s // 2):
		# s[i] vs s[-(i+1)] for i in [0, len_s - 1]
		if s[i] != s[~i]:
			return False
	return True

# Works for sentence. Ignores nonalphanumeric characters
# "A man, a plan, a canal, Panama." and "Able was I, ere I saw Elba!" are palindromic,
# but "Ray a Ray" is not.
# Alphanumeric characters: alphabetical and numerical characters
# O(n) in time and O(1) in space
def is_palindrome(s: str) -> bool:
	start_idx, end_idx = 0, len(s) - 1
	while start_idx < end_idx:
		while not s[start_idx].isalnum() and start_idx < end_idx:
			start_idx += 1
		while not s[end_idx].isalnum() and start_idx < end_idx:
			end_idx -= 1
		if s[start_idx].lower() != s[end_idx].lower():
			return False
		start_idx, end_idx = start_idx + 1, end_idx - 1
	return True
"""
	Run-length encoding (RLE) of 'aaaabcccaa' is '4a1b3c2a'. The decoding of '3e4f2e' is 'eeeffffee'
"""
# O(n) in time and O(1) in space
def encode(s: str) -> str:
	result, count = [], 1
	len_s = len(s)
	for i in range(1, len_s + 1):
		if i == len_s or s[i] != s[i - 1]:
			result.append(str(count) + s[i - 1])
			count += 1
		else:
			count += 1
	return ''.join(result)

def decode(s: str) -> str:
	count, result = 0, []
	for c in s:
		if c.isdigit():
			count = count * 10 + int(c)
		else:
			result.append(c * count)
			count = 0
	return ''.join(result)
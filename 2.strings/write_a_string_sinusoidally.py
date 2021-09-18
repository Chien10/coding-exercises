def compute_snake_string(s: str) -> str:
	results = []
	len_s = len(s)
	for i in range(1, len_s, 4): # s[1], s[5], s[9], etc.
		results.append(s[i])
	for i in range(0, len_s, 2): # s[0], s[2], s[4], etc.
		results.append(s[i])
	for i in range(3, len_s, 4): # s[3], s[7], s[11], etc.
		results.append(s[i])
	return ''.join(results)

def compute_snake_string_pythonic(s: str) -> str:
	return s[1::4] + s[::2] + s[3::4]
"""
	Convert integer into string and string into integer in base 10
"""
# O(n) + O(n) in time and O(1) in space
def str_to_int(s: str) -> int:
	is_negative = s[0] == '-'
	if is_negative:
		start_idx = 1
	else:
		start_idx = 0

	len_s = len(s)
	result = 0
	while start_idx < len_s:
		result = result * 10 + (ord(s[start_idx]) - ord('0'))
		start_idx += 1

	if is_negative:
		return -1 * result
	return result

# O(n) + O(n) time in and O(1) in space
def int_to_str(x: int) -> str:
	if x < 0:
		x, is_negative = -x, True
	else:
		is_negative = False

	result = []
	while True:
		result.append(chr(ord('0') + x % 10))
		x = x // 10
		if x == 0:
			break

	return ('-' if is_negative else '') + ''.join(reversed(result))
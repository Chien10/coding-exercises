"""
	Suppose A = 1, convert a spreadsheet column id to the corresponding integers,
	i.e., D = 4, ZZ = 702
"""
# O(n) in time and O(1) in space
def str_to_int_base_26(column: str):
	len_s = len(column)
	result, start_idx = 0, 0
	while start_idx < len_s:
		result = result * 26 + (ord(column[start_idx]) - (ord('A') + 1))
		start_idx += 1

	return result

# When A = 0
def str_to_int_base_26_when_A_0(column: str):
	len_s = len(column)
	result, start_idx = 0, 0
	while start_idx < len_s:
		result = result * 26 + (ord(column[start_idx]) - (ord('A')))
		start_idx += 1

	return result

# Integer into spreadsheet column

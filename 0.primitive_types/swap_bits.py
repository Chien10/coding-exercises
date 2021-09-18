# O(1)
def brute_force(x, first_index, second_index) -> int:
	first_bit = (x >> first_index) & 1
	second_bit = (x >> second_index) & 1
	if first_bit == second_bit:
		return x
	if first_bit == 1:
		x = x & ~(1 << first_index)
		x = x | (1 << second_index)
	else:
		x = x & ~(1 << second_index)
		x = x | (1 << first_index)
	return x

def swap_bits(x, first_index, second_index) -> int:
	"""
		73 = 01001001, first_index = 1 (0), second_index = 6 (1)
		bit_mask = (1 << first_index) | (1 << second_index)
				 = 00000001 |
				   01000000
				 = 01000001
		01001001 = 01001001 ^
				   01000001
				 = 00001000 = 8
	"""
	first_bit = (x >> first_index) & 1
	second_bit = (x >> second_index) & 1
	if first_bit == second_index:
		return x
	bit_mask = (1 << first_index) | (1 << second_index)
	x = x ^ bit_mask
	return x
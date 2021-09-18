# Results in 0 or an power of two with an exponent equal to the bit index
def get_bit(value: int, bit_index: int) -> int:
	"""
		12 = 1100
		1 = 0001
		1 << 4 = 1000
		12 & (1 << 4) = 
						1100
					   &
					    1000
					   =1000
	"""
	return value & (1 << bit_index)

# Gets the bit at a particular position
def get_bit_normalized(value: int, bit_index: int) -> int:
		"""
		12 = 1100
		1 = 0001
		12 >> 3 = 0001
		(12 >> 3) & 1 = 
						0001
					   &
					    0001
					   =0001
	"""
	return (value >> bit_index) & 1
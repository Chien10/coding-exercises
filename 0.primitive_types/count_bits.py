"""
Space: O(1)
Time: O(n)
"""
def count_bits_naive(x: int) -> int:
	"""
		Counts the number of bits that are set to 1 in a positive integer
	"""
	num_bits = 0
	while x:
		num_bits += x & 1
		x >>= 1
	return num_bits
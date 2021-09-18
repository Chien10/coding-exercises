# O(n) where n is a word size
def brute_force_1(x: int):
	result = 0
	while x:
		result += x & 1
		x = x >> 1
	return result % 2

def brute_force_2(x: int):
	result = 0
	while x:
		result ^= x & 1
		x >>= 1
	return result

###
def turn_off_the_right_most_bit(x):
	"""
		12 & (12 - 1) = 8
		12 = 1100
		8 = 0100
	"""
	return x & (x - 1)

def isolate_the_lowest_1(x):
	# The lowest = the rightmost
	return x & ~(x - 1)
###

# O(# of 1s)
def count_number_of_1_with_trick(x):
	result = 0
	while x:
		result ^= 1
		x = x & (x - 1)
	return result

"""Two keys to optimization are processing multiple bits at once and caching results
1. Caching:
- 
"""

# Caching: O(n/L) where L = MASK_SIZE 
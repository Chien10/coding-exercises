# O(n) in time
def reverse_digits(x: int) -> int:
	"""
		Input:
				x (int): a positive or negative integer
		Output:
				x whose digits are reversed
	"""
	x_reversed, x_remaining = 0, abs(x)
	while x_remaining:
		x_reversed = x_reversed * 10 + x_remaining % 10
		x_remaining = x_remaining // 10
	if x < 0:
		x_reversed = -1 * x_reversed
	return x_reversed
import math
from reverse_digits import reverse_digits

# O(n) in time
def is_palindrome_with_reverse_digits(x: int) -> True:
	reversed_x = reverse_digits(x)
	if x <= 0:
		return False
	if x == reverse_digits:
		return True

# O(n) in time and O(1) in space
def is_palindrome_with_masks(x: int) -> True:
	if x <= 0:
		return False

	num_digits = math.floor(math.log10(x)) + 1
	most_significant_digit_mask = 10 ** (num_digits - 1)
	least_significant_digit_mask  = 10
	for _ in range(num_digits // 2):
		ms_digit = x // most_significant_digit_mask # most significant digit
		ls_digit = x % least_significant_digit_mask # least significant digit
		if ms_digit != ls_digit:
			return False
		# Remove the most and least significant digits
		x = x % most_significant_digit_mask
		x = x // least_significant_digit_mask
		# Update the most significant digit mask
		most_significant_digit_mask = most_significant_digit_mask // 10 ** 2
	return True
"""
	Given a three-digit number, check if all the digit is the same without checking each digit.
"""
def brute_force(a_number: int) -> bool:
	a_str = str(a_number)
	return a_str[0] * len(a_str) == a_str

def get_remain(a_number: int) -> bool:
	a_str = str(a_number)
	ones = int('1' * len(a_str))
	if a_number % ones == 0:
		return True
	return False
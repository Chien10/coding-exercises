# O(n) in time
def brute_force(a_number: int) -> int:
	# a_number >= 0
	for i in range(0, a_number):
		if i ** 2 == a_number:
			return i
	return -1

# O(logn) in time
"""
	For a_number = 25:
	[0, 25] -> [0, 11] -> [6, 11] -> [6, 7] -> [6, 5] -> 6 - 1 = 5
"""
def square_root(a_number: int) -> int:
	left, right = 0, a_number
	while left <= right:
		mid = (left + right) // 2
		
		mid_squared = mid * mid
		if mid_squared <= k:
			left = mid + 1
		else:
			right = mid - 1
	return left - 1
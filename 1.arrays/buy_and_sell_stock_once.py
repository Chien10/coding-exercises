"""
Find the pair that has the highest difference given an array of positive integers
"""

from typing import Tuple, List

# O(n**2) in time and O(1) in space
def brute_force(A: List[int]) -> Tuple[int]:
	max_diff = 0
	buy, sell = None, None
	for i, a in enumerate(A[:-1]):
		for b in A[i + 1:]:
			diff = b - a
			if diff > max_diff:
				max_diff = diff
				buy, sell = a, b
				print('Buy: {}. Sell: {}'.format(buy, sell))
	return (buy, sell)

# O(nlogn) in time and O(1) in space
def get_extreme(an_array: List[int], return_max=True) -> int:
	if len(an_array) == 0:
		return 0
	if return_max:
		return max(an_array)
	return min(an_array)

def divide_and_conquer(A: List[int]) -> int:
	len_A = len(A)
	if len_A <= 1:
		return 0 # there's no profit here

	left = A[: len_A // 2]
	right = A[len_A // 2 + 1: ]
	
	# Find the best result in the left
	best_left = divide_and_conquer(left)
	# Find the best reult in the right
	best_right = divide_and_conquer(right)
	# In case the optimum buy and sell take place in different sub-arrays
	best_cross = get_extreme(right) - get_extreme(left, return_max=False)

	return max(best_left, best_right, best_cross)

def get_max(list_pairs: List[Tuple[int]]) -> Tuple[int]:
	first_pair, second_pair, third_pair = list_pairs[0], list_pairs[1], list_pairs[2]
	diff1 = first_pair[1] - first_pair[0]
	diff2 = second_pair[1] - second_pair[0]
	diff3 = third_pair[1] - third_pair[0]

	if diff1 > diff2:
		if diff1 > diff3:
			return first_pair
		return third_pair
	if diff2 > diff3:
		return second_pair
	return third_pair

def divide_and_conquer1(an_array: List[int]) -> Tuple[int, int]:
	len_arr = len(an_array)
	if len_arr == 0:
		return (float('inf'), 0)
	if len_arr == 1:
		return (an_array[0], an_array[0])

	left = an_array[: len_arr // 2]
	right = an_array[len_arr // 2 + 1: ]
	
	best_left = divide_and_conquer1(left)
	best_right = divide_and_conquer1(right)
	best_cross = (get_extreme(left, return_max=False), get_extreme(right))

	return get_max([best_left, best_right, best_cross])

"""
Notice that the maximum profit that can be made by selling on a specific day is determined by
the minimum of the stock prices over the previous days. Since the maximum profit corresponds to
selling onsome day, the following algorithm correctly computes the maximum profit.
"""
# O(n) in time and O(1) in space
def buy_and_sell_stock_once(A: List[int]) -> Tuple[int]:
	"""
		If the input is monotonically decreasing, the result will be (`last price`, -1)
	"""
	min_price_so_far, max_profit = float('inf'), 0.
	buy, sell = -1, -1
	for price in A:
		current_profit = price - min_price_so_far
		
		if current_profit > max_profit:
			max_profit = current_profit
			sell = price
		if min_price_so_far > price:
			min_price_so_far = price
			buy = price
		else:
			buy = min_price_so_far
	return buy, sell

def buy_and_sell_stock_once1(A: List[int]) -> int:
	min_price_so_far, max_profit = float('inf'), 0.
	for price in A:
		current_profit = price - min_price_so_far
		max_profit = max(max_profit, current_profit)
		min_price_so_far = min(min_price_so_far, price)
	return max_profit
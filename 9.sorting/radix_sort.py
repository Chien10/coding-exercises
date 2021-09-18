"""
	The input has item having d digits where digit 1 is the lowest-order digit and
	digit d is the highest-order one.
	Non-comparative sorting algorithm.
	Running time of radix sort is O(d * (k + n)) guarantee where d is the number of digits and
	k is the number of possible values. If d is constant and k = O(n) -> O(n) in time.
	Space is O(k + n)
"""
from typing import List

def counting_sort_on_digit(arry: List, digit: int) -> List:
	div = 10 ** (digit - 1)

    counts = [0 for _ in range(10)]
    for value in array:
        digit = (value // div) % 10
        counts[digit] += 1
    for i in range(1, 10):
        counts[i] += counts[i - 1]

    output = array[:]
    for i in range(len(array) - 1, -1, -1):
        digit = (array[i] // div) % 10
        output[counts[digit] - 1] = array[i]
        counts[digit] -= 1
    return output

def radix_sort(array: List, digit: int) -> List:
	i = 10
	for i in range(1, digit + 1):
		array = counting_sort_on_digit(array, i)
	return array
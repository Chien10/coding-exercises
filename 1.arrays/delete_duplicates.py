# Delete duplicates from a sorted array of integers

from typing import List

# O(n^2) in time and O(n) in space
def brute_force_3(A: List[int]) -> List[int]:
	new_A = []
	for i in A:
		if i not in new_A:
			new_A.append(A)
	return new_A

# O(n) in time and O(n) in space
def brute_force_2(A: List[int]) -> List[int]:
	new_A = {}
	for a in A:
		new_A[a] = new_A.get(a, 0) + 1
	result = [a for a in new_A]
	return result

# O(n^2) in time and O(1) in space
def brute_force_3(A: List[int]) -> List[int]:
	n = len(A)
	i = 1
	while i < n:
		while A[i] == A[i - 1]:
			for j in range(i, n - 1):
				A[j] = A[j + 1]
			n -= 1
		i += 1
	return A[:n]

# O(n) in time and O(1) in space
"""
	Instead of thinking "do when it's equal", "do when it's not equal"
"""
def move_one_element(A: List[int], debug = False) -> List[int]:
	write_index = 1
	len_A = len(A)
	for i in range(1, len_A):
		if debug:
			print('A = {}'.format(A))
			print('i = {}, write_index = {}'.format(i, write_index))
		if A[write_index - 1] != A[i]:
			A[write_index] = A[i]
			write_index += 1
		if debug:
			print('A = {}'.format(A))
			print(20*'-')

	return A[: write_index]

"""
Implement a function which takes as input an array and a key, and updates the array so
that all occurrences of the input key have been removed and the remaining elements have been
shifted left to fill the emptied indices. Return the number of remaining elements. There are no
requirements as to the values stored beyond the last valid element.
"""
def brute_force_1(A: List[int], key: int) -> List[int]:
	new_A = []
	for a in A:
		if a != key:
			new_A.append(a)
	return new_A

def remove_key(A: List[int], key: int) -> List[int]:
	len_A = len(A)
	write_index = 0
	for i in range(0, len_A):
		if A[i] != key:
			A[write_index] = A[i]
			write_index += 1
	return A[: write_index]

"""
	This framework might be usefull if you encounter task requiring removing element
"""

"""
Write a program which takes as input a sorted atay A of integers and a positive integer m,
and updates A so that if x appears m times in A it appears exactly min(2, m) times in A. The update
to A should be performed in one pass, and no additional storage may be allocated.
"""
def normalize_occurances(A: List[int], m: int) -> List[int]:
	if m <= 0:
		print('m must be positive')
		return A
	count = 0

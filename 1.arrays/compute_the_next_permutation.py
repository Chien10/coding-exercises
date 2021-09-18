"""
	There are exactly n! permutations of n elements. These permutations can be represented
	using the dictionary ordering. For three elements (a, b, c), we have six posible permutations
	represented by the following six permutation P's:
					<0, 1, 2>, <0, 2, 1>, <1, 0, 2>, <1, 2, 0>, <2, 0, 1>, <2, 1, 0>
	Write a program that takes as input a permutation, and returns the next permutation under
	dictionary ordering. If the permutation is the last permutation, return the empty array.
	For example, if the input is <1, 0, 2> your function should retum <1, 2, 0>.
	If the input is <2, 1, 0>, return O.
"""
def get_inversion_point(P: List[int]) -> int:
	"""
		Finds the longest decreasing sub-array and returns the index of the element from
		the right of this sub-array
	"""
	inversion_point = len(P) - 2
	while inversion_point >= 0 and P[inversion_point] > P[inversion_point + 1]:
		inversion_point -= 1
	return inversion_point

def find_smallest_greater(an_array: List[int], start: int, end: int, index: int) -> int:
	"""
		Finds a smallest number in `an_array` that is greater than `a_number`
		`an_array` is sorted in decreasing order
		Since I use this function for the next permutation computation task,
		an_array must contains such a number that sastifies our need
	"""
	for i in reversed(range(start, end)):
		if an_array[i] > an_array[index]:
			return i

def swap_elements(an_array, i1: int, i2: int):
	an_array[i1], an_array[i2] = an_array[i2], an_array[i1]
	return an_array

def reverse_sorted_array(an_array: List[int], start_idx: int, end_idx: int):
	an_array[start_idx: end_idx] = reversed(an_array[start_idx: end_idx])
	return an_array

# O(n) in time and O(1) in space
def compute_the_next_permutation(P: List[int]) -> List[int]:
	len_P = len(P)

	inversion_point  = get_inversion_point(P)
	if inversion_point == -1:
		return [] # reached the last permutation

	i = find_smallest_greater(P, inversion_point + 1, len_P, inversion_point)
	P = swap_elements(P, inversion_point, i)

	P = reverse_sorted_array(P, inversion_point + 1, len_P)

	return P

"""
Compute the kth permutation under dictionary ordering, starting from the identity permutation
(which is the first permutation in dictionary ordering).
"""
# O(n * k!) in time
def compute_k_permutations(k: int) -> List[List[int]]:
	results = []

	identity_permutation = list(range(0, k))
	results.append(identity_permutation)

	i = 1
	while True:
		prev_perm = results[i - 1].copy()
		new_P = compute_the_next_permutation(prev_perm)
		if new_P == []:
			break
		else:
			results.append(new_P)
			i += 1

	return results

"""
Given a permutation p, return the permutation corresponding to the previous permutation
of p under dictionary ordering.
"""
def compute_the_previous_permutation(P: List[int]) -> List[int]:
	len_P = len(P)

	inversion_point = len_P - 2
	while inversion_point >= 0 and P[inversion_point] < P[inversion_point + 1]:
		inversion_point -= 1

	if inversion_point == -1:
		return []

	for i in reversed(range(inversion_point + 1, len_P)):
		if P[i] < P[inversion_point]:
			P[i], P[inversion_point] = P[inversion_point], P[i]
			break

	P[inversion_point + 1:] = reversed(P[inversion_point + 1:])
	return P
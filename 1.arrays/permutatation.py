"""
	Given an arrayA of n elements and a permutation P, apply P to A.
	For instance:
					A = [a, b, c, d]
					P = [2, 0, 1, 3]
				=> 	A = [b, c, a, d]
"""

# O(n) in both time and space
def brute_force_1(A: List, P: List[int]) -> List:
	new_A = [0] * len(A)
	i = 0
	for index in P:
		new_A[index] = A[i]
		i += 1
	return new_A

"""
	Every permutation can be represented as a collection of independent cyclic permutation.
	For example, the permutation from [a, b, c, d] to [b, c, a, d] can be decomposed into
	two independent cyclic sub-permutations: [a -> b -> c -> a] and [d -> d].
	| a b c d |
	| b c a d |
	How many ways are there to decompose the original permutation?
"""
def permutate_by_swapping(A: List, P: List[int], debug=False) -> List:
	len_A = len(A)
	for i in range(len_A):
		next = i
		if debug:
			print('next = ', next)
			print('P before swapping = ', format(P))
		while P[next] >= 0:
			if debug:
				print('\tSwapping {} and {}'.format(A[i], A[P[next]]))
			A[i], A[P[next]] = A[P[next]], A[i]

			temp = P[next]
			P[next] -= len_A # Mark the current position as visited
			next = temp # Move to the next position
			if debug:
				print('\tP = {}'.format(P))
				print('\tA = {}'.format(A))
				print('\tnext = {}'.format(next))
		if debug:
			print('After i = {}, A = {}'.format(i, A))
			print(40 * '-')
	return A
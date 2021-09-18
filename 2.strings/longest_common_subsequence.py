"""
	Longest common subsequence between two strings
	Solution: https://www.ics.uci.edu/~eppstein/161/960229.html
"""
from typing import Iterable, Tuple

# O(2^n) in time but there are only (len_A + 1) * (len_B + 1) subproblems
def find_lcs_with_recursion(A: Iterable, B: Iterable) -> int:
	assert A is not None
	assert B is not None

	if len(A) == 0 or len(B) == 0:
		return 0
	elif A[0] == B[0]:
		return 1 + find_lcs_with_recursion(A[1:], B[1:])
	return max(find_lcs_with_recursion(A, B[1:]), find_lcs_with_recursion(A[1:], B))

# Top down approach
# O(n * m) in space and time
def compute_lcs_length(A: Iterable, B: Iterable) -> Tuple[int, List[List[int]]]:
	len_A, len_B = len(A), len(B) # m, n
	L = [[-1] * len_B for _ in range(len_A)]

	lcs = find_lcs_with_dynamic_programming(A, B, 0, 0, L)
	return lcs, L

def find_lcs_with_dynamic_programming(A: Iterable, B: Iterable,
									  A_idx: int, B_idx: int, L: List[List[int]]) -> int:
	try:
		if L[A_idx][B_idx] < 0:
			if A[A_idx] == B[B_idx]:
				L[A_idx][B_idx] = 1 + find_lcs_with_dynamic_programming(A, B, A_idx + 1, B_idx + 1, L)
			else:
				L[A_idx][B_idx] = max(find_lcs_with_dynamic_programming(A, B, A_idx + 1, B_idx, L),
									  find_lcs_with_dynamic_programming(A, B, A_idx, B_idx + 1, L))
		return L[A_idx][B_idx]
	except:
		return 0

def find_lcs_with_dp(A: Iterable, B: Iterable) -> List[List[int]]:
	len_A, len_B = len(A), len(B)
	L = [[-1] * (len_B + 1) for _ in range(len_A + 1)]

	for A_idx in range(len_A + 1):
		for B_idx in range(len_B + 1):
			print('A_idx={}, B_idx={}'.format(A_idx, B_idx))
			if A_idx == 0 or B_idx == 0:
				print('A_idx or B_idx is zero')
				L[A_idx][B_idx] = 0
				print(L)
			elif A[A_idx - 1] == B[B_idx - 1]:
				print('{} = 1 + {}'.format(L[A_idx][B_idx], L[A_idx - 1][B_idx - 1]))
				L[A_idx][B_idx] = 1 + L[A_idx - 1][B_idx - 1]
				print(L)
			else:
				print('{} = max({}, {})'.format(L[A_idx][B_idx], L[A_idx - 1][B_idx], \
												L[A_idx][B_idx - 1]))
				L[A_idx][B_idx] = max(L[A_idx - 1][B_idx], L[A_idx][B_idx - 1])
				print(L)
		print(80*'-')
	return L[len_A][len_B], L
"""
	Given two sorted arrays of different sizes, return the median of the two sorted arrays
"""
from typing import List
import math

# O(n + m) in space and time
def brute_force1(A: List[int], B: List[int]) -> float:
	C = []
	len_A, len_B = len(A), len(B)
	A_idx, B_idx = 0, 0

	if len_A == 0 and len_B == 0:
		return None

	while A_idx < len_A:
		if B_idx < len_B:
			b = B[B_idx]
			a = A[A_idx]

			if a <= b:
				C.append(a)
				A_idx += 1
			else:
				C.append(b)
				B_idx += 1
		else:
			break

	while A_idx < len_A:
		C.append(A[A_idx])
		A_idx += 1

	while B_idx < len_B:
		C.append(B[B_idx])
		B_idx += 1

	if (len_A + len_B) % 2 == 0:
		return (C[(len_A + len_B ) // 2] + C[(len_A + len_B ) // 2 - 1]) / 2
	return (C[(len_A + len_B) // 2])

# O(n + m) in time, O(1) in space
def brute_force2(A: List[int], B: List[int]) -> float:
	"""
		This function does not work when B is empty
	"""
	len_A, len_B = len(A), len(B)
	A_idx, B_idx = 1, 0

	if len_A == 0 and len_B == 0:
		return None		

	while A_idx <= len_A:
		print(A)
		print(B)
		print('\t',A[A_idx - 1])
		print('\t',B[B_idx])
		if A[A_idx - 1] < B[B_idx]:
			print('\t{}<{}'.format(A[A_idx-1],B[B_idx]))
			A_idx += 1
		else:
			print('\t{}>{}'.format(A[A_idx-1],B[B_idx]))
			A[A_idx-1], B[B_idx] = B[B_idx], A[A_idx-1]
			A_idx += 1
	print('A=',A)
	while B_idx < len_B:
		b = B.pop(0)
		print('\tb=',b)
		A.append(b)
		print('\tA=',A)
		B_idx += 1

	if (len_A + len_B) % 2 == 0:
		return (A[(len_A + len_B) // 2] + A[(len_A + len_B) // 2 - 1]) / 2
	return A[(len_A + len_B) // 2] / 2

# O(1) in both time and space
def get_median(an_array: List[int], len_array: int) -> float:
	if len_array % 2 == 0:
		return (an_array[len_array // 2] + an_array[len_array // 2 - 1]) / 2
	return an_array[len_array // 2]

# O(logn) when n = m in time, O(1) in space
def divide_and_conquer(A: List[int], B: List[int]) -> float:
	"""
		A and B must have the same length
	"""
	len_A = len(A)
	print('A=', A)
	print('B=', B)

	if len_A == 0:
		print('len_A=0')
		return -1
	elif len_A == 1:
		print('len_A=1')
		return (A[0] + B[0]) / 2
	elif len_A == 2:
		print('len_A=2')
		return (max(A[0], B[0]) + min(A[1], B[1])) / 2
	else:
		median_A = get_median(A, len_A)
		median_B = get_median(B, len_A)

		if median_A == median_B:
			print('median_A==median_B')
			return median_A
		elif median_A > median_B:
			print('median_A > median_B')
			if len_A % 2 == 0:
				print('\tlen_A % 2 == 0')
				return divide_and_conquer(A[:len_A // 2 + 1],
										  B[len_B // 2 - 1:])
			print('\tlen_A % 2 != 0')
			return divide_and_conquer(A[:len_A // 2 + 1],
									  B[len_A // 2:])
		else:
			print('median_A < median_B')
			if len_A % 2 == 0:
				print('\tlen_A % 2 == 0')
				return divide_and_conquer(A[len_A // 2 - 1:],
										  B[:len_A // 2 + 1])
			print('\tlen_A % 2 != 0')
			return divide_and_conquer(A[len_A // 2:],
									  B[:len_A // 2 + 1])

# https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
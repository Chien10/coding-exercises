"""
	Write a program that takes an integer argument and retums
	all the primes between 1 and that integer.
"""
from typing import List
import math

def is_prime(a_number: int) -> bool:
	# O(n)
	if a_number > 1:
		for i in range(2, a_number):
			if a_number % i == 0:
				return False
		return True
	return False

"""
	If n has a divisor other than 1 and itself, it must also have a divisor
	that is no greater than its square root.
"""
def is_prime_hack(a_number: int) -> bool:
	# O(n^0.5)
	if a_number > 1:
		for i in range(2, math.floor(math.sqrt(a_number))):
			if a_number % i == 0:
					return False
			return True
	return False

# Space O(1) (not account for the prime_numbers list)
def brute_force(a_number: int) -> List[int]:
	prime_numbers = []
	for i in range(2, a_number + 1):
		if is_prime(i):
			prime_numbers.append(i)
	return prime_numbers

# Space O(n)
# Time O(n * (n/2 + n/3 + n/5 + ...)) = O(nloglogn)
def generate_primes_with_sieve(a_ number: int) -> List[int]:
	prime_numbers = []
	is_prime = [False, False] + (a_number - 1) * [True]
	for i in range(2, a_number + 1):
		if is_prime[i]:
			prime_numbers.append(i)
			# Any multiples of i is not a prime number
			for m in range(i, a_number + 1, i):
				is_prime[m] = False
	return prime_numbers
"""
	Given two strings, check if one is a permutation of the other
"""
import collections

# max(O(nlogn), O(mlogm)) in time and max(O(m),O(n)) in space
def is_permutation_with_sort(a: str, b: str):
	"""
		Case-sensitive, white space counted
	"""
	a_sorted = sorted(a)
	b_sorted = sorted(b)

	if len(a_sorted) != len(b_sorted):
		return False
	return a_sorted == b_sorted

# max(O(n), O(m)) in time and space
def is_permutation_with_hash_table(a: str, b: str):
	if len(a) != len(b):
		return False

	result = True
	a_hash_t = collections.Counter(a)

	for j in b:
		try:
			a_hash_t[j] -= 1
			if a_hash_t[j] < 0:
				result = False
				break
		except:
			result = False
			break
	return result
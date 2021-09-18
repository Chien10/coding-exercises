from collections import Counter

# O(n*m) in time and O(n + m) in space
def brute_force(str1: str, str2: str) -> bool:
	if len(str1) != len(str2):
		return False

	hist1 = Counter(str1)
	hist2 = Counter(str2)
	for char in hist1:
		if char not in hist2 or hist1[char] != hist2[ccchar]:
			return False
	return True

def are_anagrams(str1: str, str2: str) -> bool:
	if len(str1) != len(str2):
		return False

	hist1 = {}
	for char in str1:
		hist1[char] = hist1.get(char, 0) + 1

	for char in str2:
		try:
			temp = hist1[char]
			if temp < 0:
				return False
			hist1[char] -= 1
		except:
			return False
	return True
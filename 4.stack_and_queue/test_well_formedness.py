# O(n) in time and O(1) in space
def is_well_formed(s: str) -> bool:
	left_chars, lookup = [], {'(': ')', '{': '}', '[': ']'}

	for c in s:
		try:
			temp = lookup.get(c)
			left_chars.append(c)
		except:
			#  If a right-side character appears but there's no
			# corresponding left-side character
			if not left_chars or lookup[left_chars.pop()] != c:
				return False
	return not left_chars
"""
	Given a search string s and the text t, find the first occurence of s in t.
"""
import functools

# O(n**2) in time and O(1) in space
def brute_force(s: str, t: str) -> int:
	not_answer = False
	for i, _ in enumerate(t):
		for j, _ in enumerate(s):
			if t[i] != s[j]:
				not_answer = True
				break
		if not not_answer:
			return i

"""
	Rabin Karp uses hash function to map sub-string to integer value and rolling hash technique to
	calculate a new hash value without rehashing the entire string.
"""
class RollingHash(object):
	def __init__(self, text: str, size_word: int):
		self.text = text
		self.hash = 0
		self.size_word = size_word
		self.len_text = len(text)
		self.BASE = 26

		for i in range(0, size_word):
			character = ord(self.text[i])
			# The Rabin-Karp Rolling Hash
			self.hash += (character - ord("a") + 1) * (self.BASE ** (size_word - i - 1))

		self.window_start = 0
		self.window_end = size_word

	def move_window(self):
		if self.window_end <= self.len_text - 1:
			character = self.text[self.window_start]
			self.hash -= (ord(character) - ord("a") + 1) * \
							self.BASE ** (self.size_word - 1)

			self.hash *= self.BASE
			character = self.text[self.window_end]
			self.hash += ord(character) - ord("a") + 1

			self.window_start += 1
			self.window_end += 1

	def get_window_text(self) -> str:
		return self.text[self.window_start: self.window_end]

def rabin_karp(s: str, t: str):
	if s == "" or t == "":
		return -1
	len_s, len_t = len(s), len(t)
	if len_s > len_t:
		return -1

	t_rolling_hash = RollingHash(t, len_t)
	s_rolling_hash = RollingHash(s, len_s)

	for i in range(len_t - len_s + 1):
		if t_rolling_hash.hash == s_rolling_hash.hash:
			if t_rolling_hash.get_window_text() == s:
				return i
		t_rolling_hash.move_window()

	return -1
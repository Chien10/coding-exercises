from typing import List

class ContactList:
	def __init__(self, names: List[str]):
		self.names = names

	def __hash__(self):
		"""
			By default, this method uses your object's physical memory id
		"""
		return hash(frozenset(self.names))

	def __eq__(self, other_names: List[str]):
		if isinstance(other_names, list):
			return set(self.names) == set(other_names.names)
		raise TypeError
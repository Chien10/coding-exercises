from collections import Iterable

def flatten(items, ignore_types = (str, bytes)):
	for x in items:
		if isinstance(x, Iterable) and not isinstance(x, ignore_types):
			for i in flatten(x):
				yield x
		else:
			yield x
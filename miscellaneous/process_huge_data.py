"""
	A huge amount of data needs processing but the entire data cannot fit into your memory
"""
import os, re
import fnmatch
import gzip, bz2

#####################################################################################
def gen_find(filepat: str, top: str):
	"""
		Finds all filenames in a directory tree that match a shell pattern
	"""
	for path, dirlist, filelist in os.walk(top):
		for name in fnmatch.filter(filelist, filepat):
			yield os.path.join(path, name)

def gen_opener(filenames):
	"""
		Opens a sequence of filenames producing a file object
	"""
	for filename in filenames:
		if filename.endswith('.gz'):
			f = gzip.open(filename, 'rt')
		elif filename.endswith('.bz2'):
			f = bz2.open(filename, 'rt')
		else:
			f = open(filename, 'rt')

		yield f
		f.close()

def gen_concatenate(iterators):
	"""
		Chains a sequence of iterators together into a single sequence
	"""
	for it in iterators:
		yield from it
#####################################################################################

# Processing functions
def gen_grep(pattern, lines):
	"""
		Look for a regex pattern in a sequence of lines
	"""
	pat = re.compile(pattern)
	for line in lines:
		if pat.search(line):
			yield line

# Add more processing functions

"""
	More on system programming: http://www.dabeaz.com/generators/ and http://dabeaz.com/coroutines/
"""
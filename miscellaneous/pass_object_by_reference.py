"""
	Is Python pass-by-value or pass-by-reference?
"""
from typing import List
import dis

def reassign(a: List[int]):
	print('a before modification:', a)
	for i in a:
		print('\t{}'.format(i))
	a = [0, 1]
	print('a after modification:', a)

def append(a: List[int]):
	print('a before modification:', a)
	for i in a:
		print('\t{}'.format(i))
	a.append(10)
	print('a after modification:', a)

def main1():
	a = [1, 2, 3]
	print(80*'-')
	reassign(a)
	print('After applying reassign:', a)
	print(80*'-')
	append(a)
	print('After applying append:',a)

"""
	Ok, you could be like: 'What the heck?'
	We can examine the two functions more closely
"""
def reassign(a: List[int]):
	print('a before modification:', a)
	print('id of a before modification:', id(a))
	for i in a:
		print('\t{}'.format(i))
	a = [0, 1]
	print('a after modification:', a)
	print('id of a after modification:', id(a))

def append(a: List[int]):
	print('a before modification:', a)
	print('id of a before modification:', id(a))
	for i in a:
		print('\t{}'.format(i))
	a.append(10)
	print('a after modification:', a)
	print('id of a after modification:', id(a))

def main2():
	a = [1, 2, 3]
	print(80*'-')
	reassign(a)
	print('After applying reassign:', a)
	print(80*'-')
	append(a)
	print('After applying append:',a)

"""
	Turn out, the variable `a` before applying reassigning is different from the variable `a`
	after reassigning. But in the `append` function, the function uses the same variable `a`.
	In Python, variable and object are different:
				a  =  10
				|     |
			variable  object
	Python is a pass-by-object-reference language. The usual pass-by-value and pass-by-reference
	can be rephrased as pass-by-variable-value and pass-by-variable-reference.
	Therefore, in Python, the object is passed by reference, the number 10, while the variable is not.

	In the first function, reassign, when assigning a variable `a` to a list, the function creates
	that `a` variable instead of using the `a` variable passed in.

						def reassign(a):
							# Before assigning, the function uses the variable `a`
							a = [0, 1]
							# The above assignment creates a new variable `a` and assign
							# it with [0, 1]
							# Before asigning, the newly created variable `a` assigns to the
							# same object as the passed-in variable `a`, [1, 2, 3]
							# There are two variables `a` now

							a  ---------
										\
									[1, 2, 3]
										/
							a  ---------

							a  ---------
										\
									[1, 2, 3]
										
							a  ---------
										\
									  [0, 1]

	In the second function, append, the function also creates a new variable `a` but assigned to the
	same object.
							a  ---------
										\
									[1, 2, 3]
										/
							a  ---------

							a  ---------
										\
									[1, 2, 3, 10]
										/
					 append(a) ---------
"""

print(dis.dis(reassign))
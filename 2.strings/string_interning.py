"""
	String interning is a method of storing only one copy of each distinct string value
	More about string interning in Python: http://guilload.com/python-string-interning/
	More about memory in Python: https://dzone.com/articles/python-memory-issues-tips-and-tricks
"""
import sys

a = 'jian'
b = 'jian'
print(a is b) # correct because string interning is applied

a = 'jian      '
b = 'jian      '
print(a is b) # nope

a = sys.intern(a)
b = sys.intern(b)
print(a is b) # yeah
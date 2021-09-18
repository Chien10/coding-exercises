"""
	A sort is stable if it preserves the relative order of items having equal keys.
	What is key? What is item? Sometimes, key and item are the same ([1, 2, 3], ['a', 'c', 'z'])
	but they can be different if the array contains tuples of (key, item) pairs
		[(1, 'c'), (2, 'd'), (5, 'z')]
	
	Sorted by key
"""
from operator import itemgetter

def main():
	print(itemgetter(1)('Chien'))

	data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
	print('Stable sort result: ', sorted(data, key=itemgetter(0)))
	data = [('red', 1), ('blue', 1), ('red', 2), ('blue', 2)]
	print('Stable sort result: ', sorted(data))

	data = [(1, 'chien'), (2, 'thang'), (2, 'jian'), (1, 'chian')]
	print('Stable sort result: ', sorted(data, key=itemgetter(0)))
	data = [(1, 'chien'), (2, 'thang'), (2, 'jian'), (1, 'chian')]
	print('Unstable sort result: ', sorted(data))

	class Student:
	    def __init__(self, name, grade, age):
	        self.name = name
	        self.grade = grade
	        self.age = age
	    def __repr__(self):
	        return repr((self.name, self.grade, self.age))

	student_objects = [
	    Student('john', 'A', 15),
	    Student('jane', 'B', 12),
	    Student('dave', 'B', 10),
	]

import bisect, collections
from typing import List, Tuple

def get_the_first_index_gte(A: List, target) -> int:
	"""
		Returns the index of the first entry that is greater or equal to
		the `target`.
		Returns the length of `A` if there's such a number.
		`A` is sorted.
	"""
	return bisect.bisect_left(A, target)

def get_the_first_index_gt(A: List, target) -> int:
	"""
		Returns the index of the first entry that is greater than
		the `target`.
		Returns the length of `A` if there's such a number.
		`A` is sorted.
	"""
	return bisect.bisect_right(A, target)

def left_insert_into_sorted_list(A: List, lo: int, high: int, target):
	bisect.insort_left(A, target, lo=lo, hi=hi)

def right_insert_into_sorted_list(A: List, lo: int, high: int, target):
	bisect.insort_right(A, target, lo=lo, hi=hi)

Student = collections.namedtuple('Student', ('name', 'grade_point_average'))

def compute_gpa(student: collections.namedtuple) -> Tuple[float, str]:
	return (-student.grade_point_average, student.name)

def search_student(students: List[str], target: collections.namedtuple, compute_gpa) -> int:
	i = bisect.bisect_left(
		[compute_gpa(student) for student in students], \
		compute_gpa(target)
	)
	if 0 <= i < len(students) and students[i] == target:
		return i
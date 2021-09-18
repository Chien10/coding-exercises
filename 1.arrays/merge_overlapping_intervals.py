"""
	You're given a list of interval pairs (each has a start and end timestamp)
	which are sorted by starting timestamp. Merge overlapping intervals and return new output array

	Input:
			(1, 5), (3, 7), (4, 6), (6, 8) -> (1, 8)
			(10, 15), (12, 15) -> (12, 15)
"""
import collections
from typing import List

Interval = collections.namedtuple('Interval', ('start', 'end'))




"""
	A=[Interval(1,3),Interval(2,4),Interval(5,7),Interval(6,8)]
"""
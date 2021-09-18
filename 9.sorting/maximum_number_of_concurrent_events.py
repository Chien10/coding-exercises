import collections
from typing import List

Event = collections.namedtuple('Event', ('start', 'finish'))

# O(n**2) in time
def brute_force(events: List[Event]) -> List[Event]:
	result = []
	max_num = 0
	num_events = len(events)
	i = 0

	while i < num_events:
		event = events[0]
		concurrent_events = []
		start_time = event.start
		finish_time = event.finish

		removed = events.pop(0)
		concurrent_events.append(removed)

		for possible_result in events:
			if possible_result.start >= start_time and possible_result.finish < finish_time:
				concurrent_events.append(possible_result)
			elif possible_result.finish > start_time and possible_result.finish < finish_time:
				concurrent_events.append(possible_result)

		num_concurrent_events = len(concurrent_events) 
		if num_concurrent_events > max_num:
			max_num = num_concurrent_events
			result = concurrent_events

		events.append(removed)
		i += 1

	return result


"""
	The sweep line algorithm: An imaginary vertical sweep line passes through a given set of geometric
	objects, from left to right.
"""
# 'time' is either 'start' or 'finish'. If 'time' is 'start', 'is_start' will be True
Endpoint = collections.namedtuple('Endpoint', ('time', 'is_start'))


def main():
	events = [Event(1, 5), Event(6, 10), Event(11, 13), Event(14, 15), Event(2, 7),
		Event(8, 9), Event(12, 15), Event(4, 5), Event(9, 17)]

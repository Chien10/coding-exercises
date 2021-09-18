"""
	In course2 folder
"""
from typing import List
from collections import namedtuple
import heapq

form min_heap import MinHeap

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


# O(n * m) in time and O(m) in space
def brute_force(n_workers: int, jobs: List[int]) -> List[int]:
	"""
		n_worker: size m
		jobs: time to finish each job (size n)
	"""
    result = []
    next_free_time = [0] * n_workers

    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result

# O(n * logm) in time and O(m) in space
def assign_job_with_min_heap(n_workers: int, jobs: List[int]) -> List[int]:
	result = []
	next_free_time = [(0, worker) for worker in range(n_workers)]
	next_free_time = MinHeap(next_free_time, n_workers)

	for job in jobs:
		next_worker = next_free_time.extract_min()
		result.append(AssignedJob(next_worker, next_worker[0]))

		next_free_time.insert((next_worker[0] + job, next_worker[1]))
	return result

def main():
	#n_workers = 4
	#jobs = [1] * 20
	n_workers = 2
	jobs = [1, 2, 3, 4, 5]

	assigned_jobs = brute_force(n_workers, jobs)
	for job in assigned_jobs:
		print(job.worker, job.started_at)
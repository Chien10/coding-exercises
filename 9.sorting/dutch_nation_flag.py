"""
	Given an array of nn buckets, each containing a red, white, or blue pebble, sort them by color.
	The allowed operations are:

	- swap(i,j):  swap the pebble in bucket ii with the pebble in bucket jj.
	- color(i): determine the color of the pebble in bucket ii.
	
	The performance requirements are as follows:

	- At most n calls to color().
	- At most n calls to swap().
	- Constant extra space.
"""
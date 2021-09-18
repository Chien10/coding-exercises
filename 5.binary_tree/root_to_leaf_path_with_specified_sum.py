"""
	Write a program which takes as input an integer and a binary tree with integer node weights, and
	checks if there exists a leaf whose path weight equals the given integer.
"""
from binary_tree import BinaryTreeNode
from typing import List

# O(n) in time and O(h) in space
def has_path_sum(node: BinaryTreeNode, remaining_weight: int) -> bool:
	if not node:
		return False

	# If `node` is leaf
	if not node.left and not node.right:
		return node.key == remaining_weight

	# Check if the left or the right side has path sum
	return has_path_sum(node.left, remaining_weight - node.key) or
			has_path_sum(node.right, remaining_weight - node.key)

def get_all_path_sum(node: BinaryTreeNode, weight: int, result: List = []) -> List[BinaryTreeNode]:
	"""
		Find all the paths to leaves whose weight equal weight
	"""
	pass
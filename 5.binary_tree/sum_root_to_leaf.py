from binary_tree import BinaryTreeNode

# O(n) in time and O(h) in space
def get_sum_root_to_leaf(node: BinaryTreeNode, partial_path_sum: int = 0) -> int:
	if not node:
		return 0

	partial_path_sum = partial_path_sum * 2 + node.key

	if not node.left and not node.right:
		return partial_path_sum
	return get_sum_root_to_leaf(node.left, partial_path_sum) + \
			get_sum_root_to_leaf(node.right, partial_path_sum)
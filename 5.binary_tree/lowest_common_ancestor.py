"""
	The lowest common ancestor (LCA) of any two nodes in a binary tree is the node farthest from
	the root that is an ancestor of both nodes.
"""
import collections
from binary_tree import BinaryTreeNode

# O(n) in time and O(h) in space
def does_node_exist_with_preorder(node, key):
	"""
		Tranverse a tree in preorder and check if the given node exists
		in a tree rooted at `node`
	"""
	if node is None:
		return False

	if node.key == key:
		return True

	left_result = does_node_exist_with_preorder(node.left, key)
	right_result = does_node_exist_with_preorder(node.right, key)
	return left_result or right_result

# O(n) in time and O(h) in space
def is_in_same_left_subtree(root: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode):
	if root == None:
		return False # no tree

	if does_node_exist_with_preorder(root.left, node0) and \
		does_node_exist_with_preorder(root.left, node1):
		return True

	return False

def is_in_same_right_subtree(root: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode):
	if root == None:
		return False # no tree

	if does_node_exist_with_preorder(root.right, node0) and \
		does_node_exist_with_preorder(root.right, node1):
		return True

	return False

def is_in_same_subtree(root: BinaryTreeNode, node0: BinaryTreeNode, node1: BinaryTreeNode):
	if root == None:
		return False # no tree

	if does_node_exist_with_preorder(root.left, node0) and \
		does_node_exist_with_preorder(root.left, node1):
		return True

	if does_node_exist_with_preorder(root.right, node0) and \
		does_node_exist_with_preorder(root.right, node1):
		return True

	return False

def find_path(root, path: list, k):
	"""
	Finds the path from root node to given root of the tree.
	Stores the path in a list path[], returns true if path exists otherwise false
	"""
	if root is None:
		return False

	path.append(root.key)
	print('after append:', path)
	if root.key == k:
		return True

	if root.left is not None and find_path(root.left, path, k) or \
		root.right is not None and find_path(root.right, path, k):
		return True

	# The following indicates that the tranverse reaches the bottom of the tree
	# which implies that we haven't found the desired `k`. We start popping out
	# the last element. Eventually, the `path` will empty if `k` does not
	# exist in the tree
	path.pop()
	print('after pop:', path)
	return False

# O(n) in time
def find_lca(root, node1, node2):
	path1, path2 = [], []

	node1_in_tree = find_path(root, path1, node1)
	node2_in_tree = find_path(root, path2, node2)
	print('path1:', path1)
	print('path2:', path2)
	if not node1_in_tree or not node2_in_tree:
		return -1

	i = 0
	len_1, len_2 = len(path1), len(path2)
	while i < len_1 and i < len_2:
		if path1[i] != path2[i]:
			break
		i += 1

	return path1[i - 1]

def find_lca2(root, node1, node2) -> BinaryTreeNode:
	if root is None:
		return None

	if root.key == node1 or root.key == node2:
		return root

	left_lca = find_lca2(root.left, node1, node2)
	right_lca = find_lca2(root.right, node1, node2)

	# Two nodes in the different side
	if left_lca and right_lca:
		return root

	if left_lca is not None:
		return left_lca
	return right_lca

def get_depth(a_node: BinaryTreeNode) -> int:
	depth = 0
	while a_node:
		depth += 1
		a_node = a_node.parent
	return depth

# O(n) in time and O(1) in space
def find_lca_when_node_has_parent(node_0: BinaryTreeNode, node_1: BinaryTreeNode):
	depth_0, depth_1 = get_depth(node_0), get_depth(node_1)
	# Get the deeper node
	if depth_0 < depth_1:
		node_0, node_1 = node_1, node_0

	# Ascend from the deeper node
	depth_diff = abs(depth_0 - depth_1)
	while depth_diff:
		node_0 = node_0.parent
		depth_diff -= 1

	# Ascend in tandem until they meet
	while node_0 is not node_1:
		node_0, node_1 = node_0.parent, node_1.parent
	return node_0
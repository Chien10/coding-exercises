from binary_tree import BinaryTreeNode
from typing import List

# O(n) in time and O(h) in space
def get_inorder_recursive(node: BinaryTreeNode, inorder: List = []):
	if node:
		get_inorder_recursive(node.left, inorder)
		inorder.append(node.key)
		get_inorder_recursive(node.right, inorder)

def get_preorder_recursive(node: BinaryTreeNode, preorder: List = []):
	if node:
		preorder.append(node.key)
		get_preorder_recursive(node.left, preorder)
		get_preorder_recursive(node.right, preorder)

def get_postorder_recursive(node: BinaryTreeNode, postorder: List = []):
	if node:
		get_postorder_recursive(node.left, postorder)
		get_postorder_recursive(node.right, postorder)
		postorder.append(node.key)

def get_preorder(node: BinaryTreeNode) -> List[BinaryTreeNode]:
	path, result = [node], []
	while path:
		current_node = path.pop()
		if current_node:
			result.append(current_node.key)
			path += [current_node.right, current_node.left] # pop will get left first
	return result

def get_inorder(node: BinaryTreeNode) -> List[BinaryTreeNode]:
	path, result = [], []

	while path or node:
		if node:
			node = node.left
		else:
			node = path.pop()
			result.append(node.key)
			node = node.right
	return result

def get_postorder(node: BinaryTreeNode) -> List[BinaryTreeNode]:
	path, result = [], []

	while path or node:
		if node:
			node = node.right
		else:
			node = path.pop()
			result.append(node.key)
			node = node.left
	return result
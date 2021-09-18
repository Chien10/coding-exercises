def check_symmetric(subtree_0, subtree_1):
	if not subtree_0 and not subtree_1:
		return True
	elif subtree_0 and subtree_1:
		return (subtree_0.key == subtree_1.key and
				check_symmetric(subtree_0.left, subtree_1.right) and
				check_symmetric(subtree_0.right, subtree_1.left))
	return False

# O(n) in time and O(h) in space
def is_symmetric(root):
	# False only if root is not None and the tree is asymmetric
	return not root or check_symmetric(root.left, root.right)
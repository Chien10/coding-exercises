class BinaryTreeNode(object):
	def __init__(self, parent=None, data=None, left=None, right=None, visited=False):
		self.key = data
		self.left = left
		self.right = right
		self.parent = None
		self.visited = visited

# O(h) in time and O(1) in space
def get_tree_height(root):
	if root is None:
		return 0
	return 1 + max(get_tree_height(root.left), get_tree_height(root.right))

# O(n) in time and O(h) in space
def tranverse_tree(root):
	if root:
		print('Preorder: {}'.format(root.data))
		tranverse_tree(root.left)
		
		print('Inorder : %d' % root.data)
		tranverse_tree(root.right)

		print('Postorder: ', root.data)

def tree_insert(root, key):
	if root is None:
		return BinaryTreeNode(root)
	else:
		if root.key == key:
			return root
		elif root.key < key:
			root.right = insert(root.right, key)
		else:
			root.left = insert(root.left, key)
	return root

def get_min_value(node: BinaryTreeNode) -> BinaryTreeNode:
	current = node
	while current.left is not None:
		current = current.left
	return current

def delete_node(node: BinaryTreeNode, key):
	if node is None:
		return node

	if key < node.key:
		node.left = delete_node(node.left, key)
	elif key > node.key:
		node.right = delete_node(node.right, key)
	else:
		if node.left is None:
			temp = node.right
			node = None
			return temp
		elif nod.right is None:
			temp = node.left
			node = None
			return temp
		# Node with two children
		# Move the smallest node in the right subtree
		temp = get_min_value(node.right)
		node.key = temp.key
		node.right = delete_node(node.right, temp.key)
	return node
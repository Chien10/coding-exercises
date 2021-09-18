import ast

class PythonKernel:
	"""
		A tiny persistent kernal for Python code
	"""
	def __init__(self, name='kernel'):
		self.globals, self.locals, self.name = {}, {}, name

	def compile(self, tree):
		if isinstance(tree, ast.Expr):
			mode, c = 'eval', ast.Expression(tree.value)
		else:
			mode, c = 'exec', ast.Module([tree], type_ignores=[])
		return compile(c, self.name, mode)

	def __call__(self, code):
		res = None
		for tree in ast.parse(code).body:
			res = eval(self.compile(tree), self.globals, self.locals)
		return res
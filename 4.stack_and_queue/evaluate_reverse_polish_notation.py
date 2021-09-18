DELIMITER = ','
OPERATORS = {
	'+': lambda y, x: x + y, '-': lambda y, x: x - y,
	'*': lambda y, x: x * y, '/': lambda y, x: x // y
}


# O(n) in time and O(1) in space
def evaluate_RPN(RPN_expression: str):
	"""
		RPN_expression is a string of RPN expressions seperated by ','
		For instance, RPN_expression = '3,4,+,2,*,1'
	"""
	intermediate_results = []
	for token in RPN_expression.split(DELIMITER):
		try:
			intermediate_results.append(
				OPERATORS[token](intermediate_results.pop(),
								intermediate_results.pop())
			)
		except:
			intermediate_results.append(int(token))
	return intermediate_results[-1]

def evaluate_PN(PN_expression: str):
	intermediate_results = []
	list_PN_expression = PN_expression.split(DELIMITER)
	while list_PN_expression:
		token = list_PN_expression.pop(0)
		try:
			intermediate_results.append(
				OPERATORS[token](int(list_PN_expression.pop(0)),
								int(list_PN_expression.pop(0)))
			)
		except:
			intermediate_results.append(int(token))
	return intermediate_results[-1]
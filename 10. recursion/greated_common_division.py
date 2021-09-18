def get_gcd(x, y):
	return x if y == 0 else get_gcd(y, x % y)
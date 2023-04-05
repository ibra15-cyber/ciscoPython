import sys
""" example module: extra.iota """

# a function that is inside a module
def funI():
	return "Iota"

# a module can also output a result
if __name__ == "__main__":
	print("I prefer to be a module")
	sys.exit
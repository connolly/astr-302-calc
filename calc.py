#!/usr/bin/env python
#
# A simple command-line scientific calculator.
#

import sys, math



def die_with_usage(message):
	print("\n****\n**** error: {}\n****\n".format(message), file=sys.stderr)
	print("usage:\n\n    {} <operator> [arg1 [arg2 [...]]]\n".format(sys.argv[0]), file=sys.stderr)
	print(", where <operator> can be one of:\n", file=sys.stderr)
	for (op, func) in operators.items():
		print("    {}: {}".format(op, func.__doc__), file=sys.stderr)
	print("", file=sys.stderr)
	exit(-1)

#
# The operators.
#
# These functions must take the necessary number of arguments, and return
# the result of the operation. They must have a short docstring explaining
# what they do (it will be printed by the die_with_usage() function).
#
# Exceptions:
#   - If an incorrect number of arguments is passed, the function must raise a TypeError.
#   - If there's a problem with argument values (e.g., a negative number passed to log),
#     the function must raise a ValueError.
#

def add(*args):
	"""Add a list of numbers"""
	sum = 0.0
	for arg in args:
		sum += arg
	return sum

def sub(*args):
	"""Subtracts a list of numbers from the first number entered"""
	"""check for length of array"""
	return args[0] - sum(args[1:])
		

def log10(x):
	"""Return a base-10 logarithm of x"""

	return math.log10(x)

def sqrt(*args):
	"""find the square root of a number, a^0.5"""
	value = (args[0]) ** (0.5)
	return value

def ln(x):
	"""Return the base-e logarithm of x"""
	if x == 0:
		raise ValueError('The natural logarithm is undefined at x=0')
	else:
		return math.log(x)
  
def div(*args):
    """
    Divide a list of numbers sequentially, and return the resulting quotient.
    """    
    quotient = arg[0]
    for arg in args[1:]:
        if arg==0:
            raise ZeroDivisionError("Trying to define by ZERO(0). Dividing by ZERO(0) is undefined. Try again without using the number ZERO(0).")
        quotient /= arg
    return quotient

def exp(x):
	"""Return e raised to the power x"""
	return math.exp(x)

def fact(x):
	"""Returns the factorial of x"""
  return math.factorial(x)

def inv(x):
	"""Return the inverse of x"""
	return 1/x

#
# The dictionary that maps the command-line name of the operation,
# to the function that performs it. There can be multiple names
# for the same operator (e.g., 'add' and 'sum').
#
operators = {
	'add': add,
	'sum': add,
	'sub': sub,
	'subtract': sub,
	'minus': sub,
	'log10': log10,
	'sqrt' : sqrt,
	'ln': ln,
  'div': div,
  'divide': div,
	'exp': exp,
	'exponential': exp,
	'fact': fact,
  'inv': inv,
}

if __name__ == "__main__":
	#
	# Collect and parse arguments
	#
	try:
		op = sys.argv[1]
		args = [ float(arg) for arg in sys.argv[2:] ]
	except IndexError:
		die_with_usage("Insufficient number of arguments.")
	except ValueError as e:
		die_with_usage(e)

	#
	# Run the requested operation, and print the result
	#
	try:
		print(operators[op](*args))
	except KeyError:
		die_with_usage("Unknown operator '{}'.".format(op))
	except TypeError as e:
		die_with_usage(e)
	except ValueError as e:
		die_with_usage(e)

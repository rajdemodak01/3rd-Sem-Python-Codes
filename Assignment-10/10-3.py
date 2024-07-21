''' In Python, write an interactive calculator. Take input as command line arguments, which is assumed to be a formula that consist of a number, an operator (at least + and -), and another number, separated by white space (e.g. 1 + 1). Check whether the input arguments are valid before computing the result:

If the input does not consist of 3 elements, raise a FormulaError, which is a custom Exception.

Try to convert the first and third input to a float (like so: float_value = float(str_value)). Catch any ValueError that occurs, and instead raise a FormulaError

If the second input is not '+' or '-', again raise a FormulaError

If the input is valid, perform the calculation and print the result, else  print appropriate error messages and quit.'''

import sys
l=[]
l=sys.argv
'''if(len(sys.argv)==4):
	try:
		l[1]=float(l[1])
		l[3]=float(l[3])
		if(l[2]=='+'):
			print(l[1]+l[3])
		elif(l[2]=='-'):
			print(l[1]-l[3])
		else:
			print("FormulaError")
			pass
	except ValueError:
		print("Arguments are not valid")
else:
	print("FormulaError")'''
	
class FormulaError(Exception):
	pass

try:	
	if(len(sys.argv)==4):
		try:
			l[1]=float(l[1])
			l[3]=float(l[3])
			if(l[2]=='+'):
				print(l[1]+l[3])
			elif(l[2]=='-'):
				print(l[1]-l[3])
			else:
				print("FormulaError")
				pass
		except ValueError:
			print("Arguments are not valid")
	else:
		raise FormulaError()
except FormulaError:
	print ("FormulaError")


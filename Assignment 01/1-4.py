#Use comparison operator to find out whether a given variable ‘a’ is greater than ‘b’ or not. For example, take a=34, b=80.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
if a>b:
	print(a,"is greater than",b)
elif b>a:
	print(a,"is less than",b)
else:
	print(a,"is equal to",b)

#Write a Python function to find the Max of three numbers.
def max(a,b,c):
	if(a>=b and a>=c):
		return a
	elif(b>=a and b>=c):
		return b
	else:
		return c
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
print("The maximum amongst these typed number is",max(a,b,c))


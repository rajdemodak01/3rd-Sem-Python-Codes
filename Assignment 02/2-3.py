#Write a program to find the factorial of a number.
n=int(input("Enter the number of which you want factorial "))
fact=1
for i in range(1,n+1):
	fact=fact*i
if(n<0):
	print("Enter a valid input.")
elif(n==0):
	print("The factorial of zero is 1.")
else:
	print("The factorial of",n,"is",fact)

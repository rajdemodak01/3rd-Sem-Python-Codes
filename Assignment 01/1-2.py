#Write a python program to find remainder when a number is divided by z.
a=int(input("Enter the number to check "))
z=int(input("Enter the number by which to divide "))
if a%z==0:
	print("The remainder is zero")
else:
	print("The reminder when",a,"is divided by",z,"is",a%z)

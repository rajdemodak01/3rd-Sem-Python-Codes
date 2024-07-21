#Write a program to print a table of a number accepted from the user.
a=int(input("Enter the number of which you want a table "))
for i in range(1,11):
	print(a,"x",i,"=",a*i)

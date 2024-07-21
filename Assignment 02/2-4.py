#Write a program to print all prime numbers that fall between two numbers including both (accept two numbers from the user)
a=int(input("Enter the first number: "))
b=int(input("Enter the secpnd number: "))
for i in range(a,b+1):
	for j in range(2,i):
		if(i%j==0):
			break
	else:
		print(i)

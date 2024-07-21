#Write a program that keeps on accepting numbers from the user until the user enters Zero. Display the sum and average of all the numbers.
count=0
n=int(input("Enter a number and type '0' to exit: "))
sum=n
while(n!=0):
	n=int(input("Enter a number and type '0' to exit: "))
	sum=sum+n
	count=count+1
avg=sum/count
print("The sum of all the numbers is",sum)
print("The average of all the numbers is",avg)

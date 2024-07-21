#Write a Python program to count Even and Odd numbers in a List.
l=[]
even=0
odd=0
n=int(input("Enter the number of elements you want to put: "))
for i in range(0,n):
	a=int(input("Enter number: "))
	l.append(a)
	if(a%2==0):
		even=even+1
	else:
		odd=odd+1
print("The numbers of Even numbers present in the list is:",even,"and the numbers of Odd numbers present in the list is:",odd)

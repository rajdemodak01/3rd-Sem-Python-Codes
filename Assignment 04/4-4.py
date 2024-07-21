#Write a Python program to find second largest number in a list.
l=[]
even=0
odd=0
n=int(input("Enter the number of elements you want to put: "))
for i in range(0,n):
	a=int(input("Enter number: "))
	l.append(a)
large=l[0]
largest=l[0]
for j in range (1,n):
	if(l[j]>=large and l[j]>=largest):
		large=largest		
		largest=l[j]
	elif(l[j]>=large):
		large=l[j]
print("The second largest number in the list is:",large)

#Write a Python program to count positive and negative numbers in a list.
l=[]
positive=0
negative=0
n=int(input("Enter the number of elements you want to put: "))
for i in range(0,n):
	a=int(input("Enter number: "))
	l.append(a)
	if(a>0):
		positive=positive+1
	elif(a<0):
		negative=negative+1
print("The numbers of positive numbers present in the list is:",positive,"and the numbers of negative numbers present in the list is:",negative)

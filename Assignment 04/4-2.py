#Write a python program to Reverse a List.
l=[]
n=int(input("Enter the number of elements you want to put: "))
for i in range(0,n):
	a=int(input("Enter number: "))
	l.append(a)
for j in range(0,int(n/2)):
	temp=l[j]
	l[j]=l[n-j-1]
	l[n-j-1]=temp
print("After reversing the list, the list is: ")
print(l)

#1. Python program to interchange first and last elements in a list.
l=[]
n=int(input("Enter the numjber of elements you want to put: "))
for i in range(0,n):
	a=int(input("Enter number: "))
	l.append(a)
temp=l[0]
l[0]=l[-1]
l[-1]=temp
print("After interchanging the fisrt and last element of the list, the list is: ")
print(l)

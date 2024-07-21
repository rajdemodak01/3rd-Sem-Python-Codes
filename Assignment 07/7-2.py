'''Write a Python function to multiply all the numbers in a list.

     Sample List: [8, 2, 3, -1, 7]

     Expected Output: -336'''
def mul_all(l):
	ans=1
	for x in l:
		ans=ans*x
	return ans
l=[]
while(1):
	a=input("Enter the number you want to append in list: ")
	if(a==''):
		break
	l.append(int(a))
print("The multiplication of all the elements of the list using function is",mul_all(l))

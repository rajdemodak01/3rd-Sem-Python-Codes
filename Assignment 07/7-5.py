'''Write a Python program, where N number of integer arguments are passed to a function make_sum(), which will print the sum of all the passed integers'''
def sum_all(l):
	ans=0
	for x in l:
		ans=ans+x
	return ans
l=[]
while(1):
	a=input("Enter the number you want to append in list: ")
	if(a==''):
		break
	l.append(int(a))
print("The addition of all is",sum_all(l))
	

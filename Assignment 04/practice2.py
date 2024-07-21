l=[]
while(True):
	a=int(input("1. Enter 1 to push: \n2. Enter 2 to pop: \n3. Enter 3 to peek: \n4. Enter other than 1/2/3 to Quit: \n"))
	if(a==1):
		b=int(input("Enter a number to push: "))
		l.append(b)
	elif(a==2):
		if(l!=[]):
			print("The popped element is:",l.pop())
		else:
			print("Stack is empty")
	elif(a==3):
		if(l!=[]):
			print("The top element is:",l[-1])
		else:
			print("Stack is empty")
	else:
		break

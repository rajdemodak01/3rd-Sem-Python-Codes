#1. Python program to interchange first and last elements in a list.
l=[]
'''
input1=input("Type the number or Press Enter to exit: ")
if(input1!=""):
		l.append(input1)
while(input1!=""):
	input1=input("Type the number or Press Enter to exit: ")
	if(input1!=""):
		l.append(input1)'''
input1=input("Type the number with space or Press Enter to exit: ")
l=input1.split(" ")
l[-1],l[0]=l[0],l[-1]
print(l)

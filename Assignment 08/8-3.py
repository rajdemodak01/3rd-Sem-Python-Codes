'''Write a Python program to write a list to a file.'''
filename=input("Enter the name of the file: ")
f=open(filename,"a")
l=[]
while(1):
	a=input("Enter the number you want to append in list: ")
	if(a==''):
		break
	l.append(int(a))
'''for i in range(len(l)):
	f.write(str(l[i]))
	f.write(" ")'''
f.write(str(l))
f=open(filename,"r")
print(f.read())

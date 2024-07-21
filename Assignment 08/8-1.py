'''Write a Python program to read first n lines of a file'''
filename=input("Enter the name of the file: ")
f=open(filename,"r")
print(f.read(),end="")
f.close()

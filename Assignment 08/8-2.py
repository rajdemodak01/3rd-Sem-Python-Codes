'''Write a Python program to count the number of lines in a text file. '''
filename=input("Enter the name of the file: ")
f=open(filename,"r")
print("The number of lines in the file is",len(f.readlines()))
f.close()

#Write a Python program to copy the contents of a file to another file .
file_name1=input("Type the name of the file: ")
f1=open(file_name1,"r")
str=f1.read()
print(str,end="")

file_name2=input("Type the name of the file where you want to write: ")
f2=open(file_name2,"w")
f2.write(str)

f2=open(file_name2,"r")
print(f2.read(),end="")

f1.close()
f2.close()


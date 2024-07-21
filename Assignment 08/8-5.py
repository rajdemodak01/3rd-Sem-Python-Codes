#Write a Python program to take a file name and a string pattern from the user. Now print the number of occurrence of the pattern string found in the file.
filename=input("Enter the name of the file: ")
f=open(filename,"r")
print("The content of the file is: ")
print(f.read(),end="")

str2=input("Enter the string you want to find in the file: ")
print("The number of times",str2,"appear in the file is: ")

f.seek(0,0)
print(f.read().count(str2))

f.close()

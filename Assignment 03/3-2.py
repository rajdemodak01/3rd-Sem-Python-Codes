#Write a Python program to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2). 

str=input("Enter the string of minimum length 2: ")
words=str[-2:]
words=words*4
print(words)

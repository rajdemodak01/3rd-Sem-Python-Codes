# Write a Python program to sort a string lexicographically.
str=input("Enter the Strings: ")
words=str.split()
words.sort()
for i in words:
	print(i)

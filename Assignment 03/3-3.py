#Write a python program to check the string is anagram or not.

str1=input("Enter the first String to check anagram or not: ")
str2=input("Enter the second String to check anagram or not: ")
if(sorted(str1)==sorted(str2)):
	print(str1,"and",str2,"is anagram")
else:
	print(str1,"and",str2,"is not an anagram")

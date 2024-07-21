# Write a Python Program to insert a string in the middle of a string

str1=input("Enter the first String more than length of 5 ")
str2=input("Enter the second String ")
str3=str1[0:5]+str2+str1[5:]
print(str3)

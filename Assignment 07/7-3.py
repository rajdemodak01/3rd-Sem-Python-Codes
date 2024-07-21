'''Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 

     Sample Input: 'The quick Brown Fox'

     Expected Output:

     No. of Upper case characters: 3

     No. of Lower case Characters: 12'''
def upper(str1):
	upper=0
	lower=0
	for i in range(len(str1)):
		if(str1[i]>='A' and str1[i]<='Z'):
			upper=upper+1
		elif(str1[i]>='a' and str1[i]<='z'):
			lower=lower+1
	print("The numbers of upper case letters in string is",upper)
	print("The numbers of lower case letters in string is",lower)
a=input("Enter the string: ")
upper(a)	

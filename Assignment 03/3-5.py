#Write a Python program to add a prefix text to all of the words in a string.
str=input("Enter the Strings: ")
prefix=input("Enter the prefix: ")
words=str.split()
modified=' '.join([prefix+ word for word in words])
print(modified)
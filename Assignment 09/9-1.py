#Write a Python program to generate a random alphabetical string, random value between two integers (inclusive) and a random multiple of 7 between 0 and 70.
import random
import string
a=int(input("Enter the first range of the integers: "))
b=int(input("Enter the second range of the integers: "))
len=int(input("Enter the length of the string: "))

print(random.randint(1,10)*7)

print(random.randint(a,b))

letters=string.ascii_letters
a=''.join(random.choice(letters) for i in range(len))
print(a)




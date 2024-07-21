#Write a Python program to generate a random integer between 0 and 6 - excluding 6, random integer between 5 and 10 - excluding 10, random integer between 0 and 10, with a step of 3 and random date between two dates.
import random

print(random.randrange(0,6))
print(random.randrange(0,10))
print(random.randrange(0,10,3))

l=[]
l.append(random.randint(1,30))
l.append(random.randint(1,12))
l.append(random.randint(2000,2023))
d="-".join(str(p) for p in l)
print(d)

#Write a Python program to create a list of tuples from given list having number and its cube in each tuple. (e.g. (2,8),(3,27),....).
n=5
list1=[]
for i in range(2,n+1):
    list1.append((i,i*i))
print(list1)
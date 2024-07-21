#Write a python program to Add Tuple to List and vice – versa.
'''tuple1=(1,5,7,9,5)
list1=[45,89,656,8965,563,555]
list1=list1+list(tuple1)
print(list1)'''
tuple1=(1,5,7,9,5)
list1=[45,89,656,8965,563,555]
tuple1=tuple(list(tuple1)+list1)
print(tuple1)

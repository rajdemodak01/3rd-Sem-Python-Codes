#Input two tuples and write a python program to find Modulo of tuple elements and store in a third tuple.
tuple1 = (1, 2)
tuple2 = (3, 4)
list1=[]
for i in range(0,len(tuple1)):
    list1.append(tuple1[i]%tuple2[i])
tuple3=tuple(list1)
print(tuple3)
f=open('temp.txt','w')
l=[]
while(1):
    a=(input("Enter number else 0 "))
    if(a=='0'):
        break
    l.append(a)
str=','.join(l)
f.write(str)
f.write('\n')
f.write(str)
f=open('temp.txt','r')
print(f.read())
f.seek(0,0)
print(len(f.readlines()))
f.close()
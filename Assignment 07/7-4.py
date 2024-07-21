'''Write a Python function that prints out the first n rows of Pascal's triangle.

     Note: Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.

     Sample Pascal's triangle:'''


n=int(input("Enter the number of rows: "))
l=[[]for _ in range(n)]
for i in range(n):
	l[i]=[None]*(i+1)
for i in range(n):
	l[i][0]=1
	l[i][i]=1
	for j in range(1,i):
		l[i][j]=l[i-1][j-1]+l[i-1][j]
for p in range(n):
	for j in range(n-p-1):
		print(" ",end="")
	for k in range(p+1):
		print(l[p][k],end=" ")
	print()

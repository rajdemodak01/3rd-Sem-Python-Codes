# Write a Python program to calculate surface volume and area of a cylinder. Go to the editor
import math
pi=math.pi
def area(r,l):
	x=(2*pi*r*r+2*pi*r*l)
	return x
def volume(r,l):
	x=pi*r*r*l
	return x

r=int(input("Enter the radius of the cylinder: "))
l=int(input("Enter the height of the cylinder: "))

print("Area of the cylinder: ")
print(area(r,l))


print("Volume of the cylinder: ")
print(volume(r,l))

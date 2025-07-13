import math as m
r,h=map(float,input("Enter the radius and height of the cylinder: ").split())
def volume(r,h):
    v=round(m.pi*r**2*h,2)
    print(f"Volume of the cylinder: {v}")
def area(r,h):
    a=round(2*m.pi*r*(r+h),2)
    print(f"Area of the cylinder: {a}")
volume(r,h)
area(r,h)
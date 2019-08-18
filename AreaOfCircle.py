import math #used to get all the math operations and values such as pi
print("Type in a radius")
radius=float(input()) 
area=math.pi*radius**2 #math.pi is python's 3.14
circumference=2*math.pi*radius
arearound=round(area,3)
circumferenceround=round(circumference,3)
print("This is the area",arearound) 
print("This is circumference" ,circumferenceround)
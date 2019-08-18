print("Please select a shape: (Triangle or Trapezoid)")
shape=input()
if(shape=="Triangle"):
  print("Type in an angle:")
  angle1=int(input())
  print("Type in a second angle:")
  angle2=int(input()) #Make sure when you are adding numbers, put int or float before the input so Python knows that the input is an actual number
  print("The third angle is:")
  angle3=180-(angle1+angle2)
  print(angle3)
  print("Thanks for using my lines of code!! ^_^")
if(shape=="Trapezoid"):
  print("Type in an angle:")
  TrapAngle1=int(input())
  TrapAngle2=360-(TrapAngle1*2)
  TrapAngle3=TrapAngle2/2
  print("Your opposite 2 angles each are:", TrapAngle3)
print("Insert the grades for each students:")
print("Jack's grade:")
jack=float(input())
print("Sally's grade:")
sally=float(input())
print("Tyler's grade:")
tyler=float(input())
print("Kate's grade:")
kate=float(input())
print("Gopher's grade:")
gopher=float(input())
average=(jack+sally+tyler+kate+gopher)/5 #you need to use BEDMAS because without it, it would only divide gopher by 5.
print("Class average:" ,average)
if(jack>average):
  print("Jack has a greater score than the class average")
if(jack<average):
  print("Jack has a lower score than the class average")
if(sally>average):
  print("Sally has a greater score than the class average")
if(sally<average):
  print("Sally has a lower score than the class average")
if(tyler>average):
  print("Tyler has a greater score than the class average")
if(tyler<average):
  print("Tyler has a lower score than the class average")
if(kate>average):
  print("Kate has a greater score than the class average")
if(kate<average):
  print("Kate has a lower score than the class average")
if(gopher>average):
  print("Gopher has a greater score than the class average")
if(gopher<average):
  print("Gopher has a lower score than the class average")
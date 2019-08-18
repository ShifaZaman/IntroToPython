print("Enter activity season")
activityseason = input()
if(activityseason=="summer"):
  print("What is the weather outside(sunny,rainy)")
  weather = input()
  if(weather=="rainy"):
    print("Its raining, stay inside!")
  elif(weather=="sunny"):
    print("What is the temperature outside?")
    temperature = int(input())
    if(temperature>20):
      print("Go play outside!")
    else:
      print("Better to stay inside")
    

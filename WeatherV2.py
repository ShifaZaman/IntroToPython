'''
Ask the user for the season(summer,winter)
Ask for the weather outside(rainy,sunny,humid)
Ask for the temperature degrees celsius.

depending upon the season, weather, and temperature, tell the user tp stay inside or go outside

'''

print("Which season is it currently? (winter or summer)")
season=input()
if(season=="summer"):
  print("What is the weather outside?(sunny,cloudy,rainy)")
  weather=input()
  if(weather=="rainy"):
    print("It's raining! Better to stay inside!")
  elif(weather=="sunny"):
    print("What's the temperature outside? (°C)")
    temp=int(input())
    if(temp>20):
      print("Go out and play!!")
  elif(weather=="cloudy"):
    print("What's the temperature outside? (°C)")
    temp=int(input())
    if(temp>20):
     print("Go out and play!!")

if(season=="winter"):
  print("What is the weather outside?(sunny,snowy,cloudy)")
  weather=input()
  if(weather=="cloudy"):
    print("What's the temperature outside? (°C)")
    temp=int(input())
    if(temp>-20):
     print("Put on your winter gear!! Go out and play!!")
    else:
      print("It's too cold!! Stay inside!!")
  if(weather=="snowy"):
    print("What's the temperature outside? (°C)")
    temp=int(input())
    if(temp>(-20)):
     print("Put on your winter gear!! Go out and play in the snow!!")
    elif(temp<(-20)):
      print("It's too cold!! Stay inside!!")
  if(weather=="sunny"):
    print("What's the temperature outside? (°C)")
    temp=int(input())
    if(temp>-20):
     print("Put on your winter gear!! Go out and play in the snow!!")
    else:
      print("It's too cold!! Stay inside!!")
print("Type hours in 24-hour mode")
hours=int(input())
hoursnew=hours%12 #% - gives you the remainder. Modulus of something that is smaller will be itself e.g 11 is smaller than 12 so it will be 11

if((hours>24)|(hours<1)): # If comparing two things, put brackets around both so it does bedmas and evaluates brackets first. | = OR operator, & = AND Operator. 
  print("This time does not exist")

elif(hours==24): # Elif runs if if statement is false
  print("Your time in 12-hour mode is:12am")
#these spaces dont have to be here
elif(hours>12):
  print("Your time in 12-hour mode is:" ,hoursnew, "pm")

elif(hours==12):
  print("Your time in 12-hour mode is: 12pm")

else: 
  print("Your time in 12-hour mode is:" ,hoursnew, "am") #else comes when none of the others apply

#You can comment out several lines of code using ''' to have your code saved for later but not run by python

'''example program '''


'''if((hours>24)| (hours<1)):
  print("This does not exist")
elif((hours>12) & (hours<24)):
  print("Your time in 12-hour mode is:" ,hoursnew, "pm")
elif(hours==24):
  print("Your time in 12-hour mode is:12am")
elif(hours==12):
  print("Your time in 12-hour mode is: 12pm")

else:
  print("Your time in 12-hour mode is:" ,hoursnew, "am")'''
#this is the less complex one

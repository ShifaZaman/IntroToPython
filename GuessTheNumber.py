import random
import sys #Import for system functions(ie; ends program)
print("***Guess The Number***")
print("") #This adds a space between the 2 lines.
print("How to play: You have 4 tries to guess a random number from 1 -100. If you guess a number, it will tell you if you are low,   high or close. If you guess the number you win, if you don't   you lose. Goodluck!!")
number = random.randint(1,100)
'''print(number) #REMOVE THIS LATER'''
print("") #This adds a space between the 2 lines.
print("Input your first guess:")
guess1 = int(input())
if((guess1>number) & (guess1<number+10)):
  print("Close, but high!")
elif(guess1==number+10):
  print("Too high!")
elif((guess1>number) & (guess1>number+11)):
  print("Too high!")
elif((guess1<number) & (guess1>number-10)):
  print("Close, but low!")
elif((guess1<number) & (guess1<number+10)):
  print ("Too low!")
elif(guess1==number-10):
  print("Too low!")
elif(guess1==number):
  print("***Congratulations!! You got it right!! Thanks for playing!!***")
  sys.exit()
print("") #This adds a space between the 2 lines. THIS PART 


#IS REPEATED BUT I CHANGED THE WORDING! GUESS 1 IS NOW 2!
# Second Guess
print("Input your second guess:")
guess2 = int(input())
if((guess2>number) & (guess2<number+10)):
  print("Close, but high!")
elif(guess2==number+10):
  print("Too high!")
elif((guess2>number) & (guess2>number+11)):
  print("Too high!")
elif((guess2<number) & (guess2>number-10)):
  print("Close, but low!")
elif((guess2<number) & (guess2<number+10)):
  print ("Too low!")
elif(guess2==number-10):
  print("Too low!")
elif(guess2==number):
  print("***Congratulations!! You got it right!! Thanks for playing!!***")
  sys.exit()
print("") #This adds a space between the 2 lines. THIS IS REPEATED AGAIN...


#*Third Guess*
print("Input your third guess:")
guess3 = int(input())
if((guess3>number) & (guess3<number+10)):
  print("Close, but high!")
elif(guess3==number+10):
  print("Too high!")
elif((guess3>number) & (guess3>number+11)):
  print("Too high!")
elif((guess3<number) & (guess3>number-10)):
  print("Close, but low!")
elif((guess3<number) & (guess3<number+10)):
  print ("Too low!")
elif(guess3==number-10):
  print("Too low!")
elif(guess3==number):
  print("***Congratulations!! You got it right!! Thanks for playing!!***")
  sys.exit() # Ends the program to prevent continous runs
print("")#THIS IS WHERE IT CHANGES!!


# 4th Guess
print("Input your last guess:")
guess4 = int(input())
print("")
if(guess4==number):
  print("***Congratulations!! You got it right!! Thanks for playing!!***")
else:
  print("***GAMEOVER!!! You did not guess it right!! The number was",number,"! Try again next time!!***")
  print("***Thanks for playing!! This game was created by Shifa!! Click run to replay!!***")
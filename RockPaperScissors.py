import random
import sys
userpoints=0 #My points
computerpoints=0 


#while statement runs stuff indented aslong as the stuff in the brackets is true
#!= means not equal

print("***Rock, Paper, Scissors!!***")
print("***How to Play***")
print("Type in your either rock, paper or scissors (All lowercase!)   Then the computer will randomly choose one too. First to 2     points win!!  Goodluck!!")
while((computerpoints!=2)|(userpoints!=2)):
  RandomNumber = random.randint(0,2) # Technically 3 #'s, 0,1,2
  computers = ["rock","scissors","paper"]
  computersanswer = computers[RandomNumber] #This randomly generates rock, paper or scissors. If RandomNumber is 1, then computers list gets the item in the 2nd position, so gets scissors

  userinput1 =input()
  print(computersanswer)
  if((userinput1=="paper")&(computersanswer=="rock")):
    print("Paper beats Rock, You Win!")
    userpoints = userpoints + 1 #Updates your score
    print("Your Score:",userpoints)
    print("Computer's Score:",computerpoints)

  if((userinput1=="paper")&(computersanswer=="scissors")):
    print("Scissors beats Paper, Computer Win!")
    computerpoints = computerpoints + 1 #updates computer score
    print("Your Score:",userpoints)
    print("Computer's Score:",computerpoints)

  if((userinput1=="paper")&(computersanswer=="paper")):
    print("It's a tie!")
    print("Your Score:",userpoints)
    print("Computer's Score:",computerpoints)

  if((userinput1=="rock")&(computersanswer=="scissors")):
    print("Rock beats Scissors, You Win!")
    userpoints = userpoints + 1
    print("Your Score:",userpoints)
    print("Computer's Score:",computerpoints)

  if((userinput1=="rock")&(computersanswer=="paper")):
    print("Paper beats Rock, Computer Wins!")
    computerpoints = computerpoints + 1
    print("Your Score:",userpoints)
    print("Computer's Score:",computerpoints)

  if((userinput1=="rock")&(computersanswer=="rock")):
    print("It's a tie!")
    print("Your Score:",userpoints)
    print("Computer's Score:",computerpoints)

  if((userinput1=="scissors")&(computersanswer=="rock")):
    print("Rock beats Scissors, Computer Wins!")
    computerpoints = computerpoints + 1
    print("Your Score:",userpoints)
    print("Computer's Score:",computerpoints)

  if((userinput1=="scissors")&(computersanswer=="paper")):
    print("Scissors beats Paper, You Win!")
    userpoints = userpoints + 1
    print("Your Score:",userpoints)
    print("Computer's Score:",computerpoints)

  if((userinput1=="scissors")&(computersanswer=="scissors")):
    print("It's a tie!")
    print("Your Score:",userpoints)
    print("Computer's Score:",computerpoints)
  print("") #adds a empty space after every input


  # ***WINNER VERIFIER***
  if((userpoints==2)&(computerpoints<2)): # iF YOU WIN
    print("Congradulations! You Win!")
    print("Your Score:",userpoints)
    print("Computer's Score:",computerpoints)
    sys.exit() #Ends the program

  elif((userpoints<2)&(computerpoints==2)): #if COMPUTER WINS
    print("Sorry, You lose.")
    print("Your Score:",userpoints)
    print("Computer's Score:",computerpoints)
    sys.exit
#Idea: input total marks and the marks for each student. Calculate the percentage of each student and the class average.
print("What was the test out of?")
totalmarks=int(input())
print("What is Sally's mark?")
sally=float(input())
print("What is Ryan's mark?")
ryan=float(input())
print("What is Amy's mark?")
amy=float(input())
print("What is Andrew's mark?")
andrew=float(input())
print("What is May's mark?")
may=float(input())
print("The results:")
sallyscore=(sally/totalmarks)*100
print("Sally's score:", sallyscore, "%")
ryanscore=(ryan/totalmarks)*100
print("Ryan's score:", ryanscore, "%")
amyscore=(amy/totalmarks)*100
print("Amy's score:", amyscore, "%")
andrewscore=(andrew/totalmarks)*100
print("Andrew's score:", andrewscore, "%")
mayscore=(may/totalmarks)*100
print("May's score:", mayscore, "%")
average=(sallyscore+ryanscore+amyscore+andrewscore+mayscore)/5
print("Class average:", average, "%")
print("Thanks for using my lines of code! ^_^")
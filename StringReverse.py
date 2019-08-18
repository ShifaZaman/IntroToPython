name = "Shrubby"
nameReverse = ""
for x in range(len(name)-1,-1,-1): # First number in the loop tells you where to start. Second number is where it ends. third number is how much it goes down by each time in the loop
  nameReverse= nameReverse+name[x] # add the string name to the empty string each time
print(nameReverse)

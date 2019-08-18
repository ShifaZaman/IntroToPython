import random
print("***Welcome to The Random Name Generator***")
print(" Please type in the first person's name:")
person1 = input ()
print(" Please type in the second person's name:")
person2 = input ()
print(" Please type in the third person's name:")
person3 = input ()
nameslist = [person1, person2, person3]
number=random.randint(0,2)
print("The random person is:")
print(nameslist[number]) 
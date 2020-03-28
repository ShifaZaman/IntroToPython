a=0
while(a<101):
  print(a)
  a=a+1

print("**********************")
a=0
while(a!=101):
  print(a)
  a=a+1
  #!= means does not equal

print("**********************")
for x in range(0,11):
  print(x)
  #x is a number in a given range. For e.g. if you have a range, 0,11, this is the same as 1,10 BASICALLY IT DOESN'T INCLUDE THE LAST open

  #In summary, while loops are like if statements that do a loop but you have to increase the munber each time, For loops are like while loops but they do the incrementing on their own

print("***********************")
for x in range(0,16,3):
  print(x)
  #the thrid number basically means how much the loop increments by. If you leave it as nothing, it will increase by 1.

#challenge: make it go from 100-0
print("*************************")
b=100
while(b>-1):
  print(b)
  b=b-1

print("*************************")
for x in range(100,-1,-1):
  print(x)
  #the 3 number which is -1 means it decreases by -1 otherwise it would increase by 1 and it will get confused
a=[1,2,5,10]
print(len(a))  #len means length

i=0
while(i<len(a)):
  print(a[i])
  i=i+1
  #i=0 means i is in the first position of the list. then you print the value of a in the position of i and then you update i for the next postition (i=i+1 equals the next position)

print("************")
print(" ")
for x in range(0,len(a)):
  print(a[x])

print(" ")

print("TOTAL SUM COMPUTATION")
total=0 # maintains total sum
i = 0 # index OR position in the list
while(i<len(a)):
  total = total + a[i] #update the total by adding the value seen
  i = i + 1 #update for next index to read
print(total) #once loops completes, print the total sum

print(" ")

print("TOTAL SUM COMPUTATION - FOR LOOPS")
total1 = 0
for x in range (0,len(a)):
  total1 = total1 + a[x]
print(total1)

#OMG I DID IT!!!!!!!!!!! without help too!
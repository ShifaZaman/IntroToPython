print("Type price of oranges")
oranges=float(input())#converts input to decimal
print("Type price of apples")
apples=float(input())
print("Type price of bananas")
bananas=float(input())
print("Type price of candy")
candy=float(input())
print("Type price of muffins")
muffins=float(input())
total=apples+oranges+bananas+candy+muffins#total sum
tax=round(total*1.13,2)#round total to 2 decimal places
print("Total price is ",tax)#prints total with tax
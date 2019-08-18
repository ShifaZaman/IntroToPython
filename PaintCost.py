print("Your budget is ($):")
budget=int(input())
print("The paint cost per m² ($):")
paintcost=int(input())
print("The length of the wall is (m):")
length=int(input())
print("The width of the wall is (m):")
width=int(input())
area=width*length
print("Your total area is:", area,"m²") 
totalcost=paintcost*area
print("The total cost for paint is: $", totalcost)
if(totalcost<budget):
  print("The paint cost is within your budget.")
  leftover=budget-totalcost
  print("You have $", leftover, "leftover!")
elif(totalcost==budget):
  print("The paint cost is within your budget.")
  print("You have used all the money in your budget.")
elif(totalcost>budget):
  print("The paint cost is greater than your budget.")
  overspent=totalcost-budget
  print("You have spent $", overspent, "over your budget.")
print("Thank you for using my lines of code!! ^_^")
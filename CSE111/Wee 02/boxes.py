import math

#Ask the user for two integers: the number of manufactured items and the number of items that the user will pack per box.

m = int(input(f"Please enter the number of manufactured items: "))
p = int(input(f"Please enter the number of items that the user will pack per box: "))

#Compute the number of boxes necessary to hold the items

boxes = math.ceil(m / p)

#Display the output to the user

print(f"For {m} items, packing {p}"
f" items in each box, you will need {boxes} boxes.")




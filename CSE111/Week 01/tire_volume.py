import math

#Prompt the user to enter the three numbers of the size of a car tire
w = float(input("Please enter the first number: "))  
a = float(input("Please enter the second number: ")) 
d = float(input("Please enter the third number: "))

#Computes the volume of space inside that tire by using the formula

v = round((math.pi * w**2 * a * (w*a+(2540*d)))/10000000,1)

#Output the result
print('The approximate volume is', v , "milliliters")

# Import the datatime module so that
# it can be used in this program.
from datetime import datetime

# Call the now() method to get the current date and
# time as a datetime object from the computer's clock.
current_date_and_time = datetime.now()

# Open a text file named dimensions.txt in append mode.
with open("volumes.txt", "at") as volumes_file:

    # Print a car's model and dimensions to the file
    print(f"{current_date_and_time}, {w}, {a}, {d}, {v}", file=volumes_file)


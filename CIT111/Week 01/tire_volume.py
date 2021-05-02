import math

#Prompt the user to enter the three numbers of the size of a car tire
w = float(input("Please enter the first number: "))  
a = float(input("Please enter the second number: ")) 
d = float(input("Please enter the third number: "))

#Computes the volume of space inside that tire by using the formula

v = round((math.pi * w**2 * a * (w*a+(2540*d)))/10000000,1)

#Output the result
print('The approximate volume is', v , "milliliters")


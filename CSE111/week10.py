import math

def main():

    ##prompt user for how many circles they have
    numberOfCircles= promtNumberOfCircles()
    
    ## get area for each
    areas=loopForCircles(numberOfCircles)

    ## display are for each
    print(areas)


def loopForCircles(numberOfCircles):
    area= []
    for _ in range (0, numberOfCircles):
        r = proptForRadius()
        a = computeCircleArea(r)
        area.append(a)
    return area
        

def promtForRadius():
    return int(input("Please enter the radius: "))

def promtNumberOfCircles():
    num= input("Please enter the number of circles you are working with: ")  
      
    return int(num)
def computeCircleArea(radius):
    return math.pi* radius**2


main()    
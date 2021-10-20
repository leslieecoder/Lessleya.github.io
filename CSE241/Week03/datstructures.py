oddNumbers = []

eveNumbers = []

num = 1
while num != 0:
    num = int(input("Enter a number (0 to quit): "))
    if num != 0:
 
        if (num % 2 == 0):

            eveNumbers.append(num)
    
        else:
            oddNumbers.append(num)
    
    else:
   

        for num in oddNumbers:
            print("Odd numbers: ")
            print (num)

        for num in eveNumbers:
            print("Even numbers: ")
            print (num)




    





   


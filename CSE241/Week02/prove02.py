#Prompt the user for a filename.

def prompt_filename():
    filename = input("Please enter the data file: ")
    return filename 

#Open the requested file and read through it line by line.
def read_file(filename):
    python_file = open(filename, "r")
    average = 0.0 
    lowComm = 5000
    maxComm = 0.0
    total = 0
    lineMax = ''
    lineMin = ''

    for line in python_file:

        try:
            #skip the first line
            if (total>0):
                p = float(line.split(",")[6])
                average += p
                if (maxComm < p):
                    maxComm = p
                    lineMax =line
                if (lowComm < p):
                    lowComm = p
                    lineMax = total   
                # maxComm = max(maxComm,p)
                # lowComm = min(lowComm,p)
            total += 1
        except:
            return 0.0, "Bad", "Bad", "", ""
    average = average/float(total-1)
    python_file.close()
    return average, maxComm, lowComm, lineMin, lineMax

def display(utilityName, zipCode, state, commRate):
    print("{} ({}, {}) - ${}" .format(utilityName,zipCode,state,commRate))


def main():
    name = prompt_filename()
    print()
    average, maxRate, minRate, minLine, maxLine =read_file(name)
    print("The average commercial rate is: {}".format(average))
    print()
    print("The highest rate is:")
    maxLineArray = maxLine.split(",")
    display(maxLineArray[2], maxLineArray[0], maxLineArray[3], float(maxLineArray[6]))
    print()
    print("The lowest rate is:")
    minLineArray = minLine.split(",")
    display(minLineArray[2], minLineArray[0], minLineArray[3], float(minLineArray[6]))
    print()

if __name__ == "__main__":
    main()

            


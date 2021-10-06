import random
from random import randint

print("Welcome to the number guessing game!")
seed= random.seed(input("Enter random seed: "))
num = randint(1,100)
playAgain = True
numGuess = 1
print("")

while playAgain == True:
    guessStr= input("Please enter a guess: ")
    guess = int(guessStr)
    while guess!= num:
        if (guess > num):
            numGuess+= 1
            print("Lower")
            print("")
        elif (num > guess):
            numGuess+= 1
            print("Higher")
            print("")
        guessStr= input("Please enter a guess: ")
        guess = int(guessStr)
    print("Congratulations. You guessed it!")
    print("It took you " +  str(numGuess)  + " guesses.")
    print("")
    playAgainStr = input("Would you like to play again (yes/no)? ")
    if (playAgainStr != 'yes'):
        playAgain = False
        print("Thank you. Goodbye.")
    numGuess = 1
    num = randint(1,100)
    if (playAgainStr == 'yes'):
        print("")












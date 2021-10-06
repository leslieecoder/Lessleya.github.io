import random
from random import randint

random.seed(the_seed_value)

def main():

    print("I'm thinking of a number between 1 and 100.")
    print("Try to guess it!")
    print()

    prompt = "Please enter an integer between 1 and 100: "
    answer = randint(1, 100)
    guess = -1
    tries = 0

    while guess != answer:
        # Get a guess from the user.
        guess = int(input(prompt))
        tries += 1

        # Compare the user's guess to the answer.
        if guess < answer:
            prompt = "Higher: "
        elif guess > answer:
            prompt = "Lower: "

    print()
    print("Congratulations. You guessed it!")
    print(f"It took you {tries} guesses.")

if __name__ == "__main__":
    main()
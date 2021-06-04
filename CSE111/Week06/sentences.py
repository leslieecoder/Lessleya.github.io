import random 


def main():

    quantity = input("Please enter 1 or 2: ")
    tense = input("Please enter a tense (future, past or tense):")

    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)

    # Print the results for the user to see.
    print(f" {determiner} {noun} {verb} ")
    pass


def get_determiner(quantity): 

    if quantity == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):

    if quantity == 1:
        words = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    else:
        words = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_verb(quantity, tense):
   

    if tense == "past":
        words = [ "drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote" ]

   

    elif tense == "present" and quantity == 1:

        words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]




    elif tense == "prensent" and quantity != 1:

        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]




    elif tense == "future":

        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

main()

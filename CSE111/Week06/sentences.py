import random 


def main():

    # quantity = input("Please enter 1 or 2: ")
    # tense = input("Please enter a tense (future, past or present):")

    # determiner = get_determiner(quantity)
    # noun = get_noun(quantity)
    # verb = get_verb(quantity, tense)
    # phrase = get_prepositional_phrase(quantity)

    # Print the results for the user to see.

   
    print(f"{get_determiner(1)} {get_noun(1)} {get_verb(1,'past')} {get_prepositional_phrase(1)} ")
    print(f"{get_determiner(2)} {get_noun(2)} {get_verb(1,'past')} {get_prepositional_phrase(2)} ")
    print(f"{get_determiner(1)} {get_noun(1)} {get_verb(1,'present')} {get_prepositional_phrase(1)} ")
    print(f"{get_determiner(2)} {get_noun(2)} {get_verb(1,'present')} {get_prepositional_phrase(2)} ")
    print(f"{get_determiner(1)} {get_noun(1)} {get_verb(1,'future')} {get_prepositional_phrase(1)} ")
    print(f"{get_determiner(2)} {get_noun(2)} {get_verb(1,'future')} {get_prepositional_phrase(2)} ")

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




    elif tense == "present" and quantity != 1:

        words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]




    elif tense == "future":

        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word



def get_prepositional_phrase(quantity):
        """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """   
        preposition = get_preposition()
        determiner = get_determiner(quantity)
        noun = get_noun(quantity)

        phrase = preposition + " " + determiner + " " + noun

        return phrase



def get_preposition():
    
    words = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]

    word = random.choice(words)
    return word


if __name__ == "__main__":
    main()

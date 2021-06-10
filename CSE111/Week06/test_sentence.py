from sentences import get_determiner, get_noun, get_verb, get_prepositional_phrase, get_preposition
import pytest


def test_get_determiner():
    # Test the singular determiners.
    singular_determiners = ["the", "one"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners
    

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["some", "many"]
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    
    get_preposition = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    
    for _ in range(12):
        word = get_noun(1)

       
        assert word in get_preposition

   
    plural_nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    for _ in range(4):
        word = get_noun(2)

        assert word in plural_nouns

def test_get_verb():
    
    past_verbs = [ "drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote" ]
    
    for _ in range(12):
        word = get_verb(1,"past")

        assert word in past_verbs

    present_singular_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(12):
        word = get_verb(1, "present")

        assert word in present_singular_verbs 

    present_plural_verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    for _ in range(12):
        word = get_verb(2, "present")

        assert word in present_plural_verbs 

    future_verbs =  ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]  
    for _ in range(12):
        word = get_verb(1,"future")
        

        assert word in future_verbs

def test_get_prepositional_phrase():

    phrase = get_prepositional_phrase(1)

    phrase = phrase.split(" ")

    assert len(phrase) == 3


def test_get_preposition():

    preposition = ["about", "above", "across", "after", "along","around", "at", "before", "behind", "below","beyond", "by", "despite", "except", "for","from", "in", "into", "near", "of","off", "on", "onto", "out", "over","past", "to", "under", "with", "without"]
    
    for _ in range(12):
        word = get_preposition()

       
        assert word in preposition


        


pytest.main(["-v", "--tb=line", "-rN", "test_sentence.py"])
from sentences import get_determiner, get_noun
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
    # Test the singular nouns.
    singular_nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(12):
        word = get_noun(1)

        # Verify that the word returned from get_noun is
        # one of the words in the singular_noun list.
        assert word in singular_nouns

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural nouns.
    plural_nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    for _ in range(4):
        word = get_noun(2)

        # Verify that the word returned from get_nouns
        # is one of the words in the plural_nouns list.
        assert word in plural_nouns



pytest.main(["-v", "--tb=line", "-rN", "test_sentence.py"])
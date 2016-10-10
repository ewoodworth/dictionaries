"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    #if I wanted to be thorough, and punctuation is part of a word, I'd want to ignore it for the count do "do" and "do!" get counted together.
    word_counts = {}
    phrase = phrase.split(" ")
    for i in range(len(phrase)):
        word_counts[phrase[i]] = word_counts.get(phrase[i], 0) + 1   
    return word_counts


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """
    melon_prices = {"Watermelon": 2.95,
                    "Cantaloupe": 2.50,
                    "Musk": 3.25,
                    "Christmas": 14.25}
    try:                
        melon_price = melon_prices[melon_name]
    ##Custom error message
    except KeyError:
        return "No price found"
    return melon_price


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

def word_length_sorted(words):
    max_word_length = list({len(word) for word in words})[-1]
    max_word_length = int(max_word_length)
    word_lengths = {i:[] for i in range(max_word_length)}
    print word_lengths
    for k, v in word_lengths.items():
        for word in words:
            if len(word) == k:
                try:
                    v.append(word)
                except:
                    pass
    return word_lengths


def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    english_pirate = {"sir":"matey", "hotel":"fleabag inn", "student":"swabbie", "man":"matey", "professor":"foul blaggart", "restaurant":"galley", "your":"yer", "excuse":"arr", "students":"swabbies", "are":"be", "restroom":"head", "my":"me", "is":"be"}

    phrase = phrase.split(" ")
    translation = ""
    for word in phrase:
        try:
            word = english_pirate[word]
            translaation += word
            translation +=" "
        except:
            translation += word
            translation += " "
            pass
    translation = translation.rstrip()
    return translation


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Another example:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """
    reply = names[0]
    names_dict = {name:[names.index(name), 1] for name in names}
    for name, value in names_dict.items():
        #ignore entries where dictionary[1]=0
        if value[1] > 0:
                #THIS THING BELOW. it keeps picking up where it left off rather than starting from names[0]
                #THIS IS WHAT IS BROKEN#
                for name in names:
                    #find a word in the list that starts with reply[-1]
                    if name[0] == reply[-1]:
                        new_word = name
                        #add it to the reply
                        reply = reply + " " +new_word
                        #deduct from dictionary entry[1]
                        value[1] = value[1] - 1
    return reply

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print

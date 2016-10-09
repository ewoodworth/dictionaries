"""Dictionaries Practice

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def without_duplicates(words):
    """Given a list of words, return list with duplicates removed.

    For example::
        >>> sorted(without_duplicates(
        ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
        ['a', 'is', 'rose']

    You should treat differently-capitalized words as different:

        >>> sorted(without_duplicates(
        ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
        ['Rose', 'a', 'is', 'rose']

        An empty list should return an empty list::

        >>> sorted(without_duplicates(
        ...     []))
        []

    The function should work for a list containing integers::

        >>> sorted(without_duplicates([111111, 2, 33333, 2]))
        [2, 33333, 111111]
    """

    words_set = {word for word in words}
    words_list = [word for word in words_set]
    return words_list

def find_unique_common_items(items1, items2):
    """Produce the set of *unique* common items in two lists.

    Given two lists, return a list of the *unique* common items
    shared between the lists.

    **IMPORTANT**: you may not use `'if ___ in ___``
    or the method `list.index()`.

    This should find [1, 2]::

        >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
        [1, 2]

    However, now we only want unique items, so for these lists,
    don't show more than 1 or 2 once::

        >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
        [1, 2]

    The elements should not be treated as duplicates if they are
    different data types::

        >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
        [2]
    """
    # Thisis similar to a tactic I took last week, and could have done even fewer lines, but this is the only way I see it. Something for advising.
    items1_set = {item for item in items1}
    items2_set = {item for item in items2}
    intersection = items1_set & items2_set
    unique_common_items = [item for item in intersection]
    return unique_common_items


from itertools import combinations

def get_sum_zero_pairs(numbers):
    """Given list of numbers, return list of pair summing to 0.

    Given a list of numbers, add up each individual pair of numbers.
    Return a list of each pair of numbers that adds up to 0.

    For example::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
        [[-2, 2], [-1, 1]]

        >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
        [[-3, 3], [-2, 2], [-1, 1]]

    This should always be a unique list, even if there are
    duplicates in the input list::

        >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
        [[-2, 2], [-1, 1]]

    Of course, if there are one or more zeros to pair together,
    that's fine, too (even a single zero can pair with itself)::

        >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
        [[-1, 1], [0, 0]]
    """
    #Zero is a special case from everything that follows. We'll need an empty list to populate later, but our empty list actually needs to contain 0,0 if it's available.
    for i in range(len(numbers)):
        if numbers[i] == 0:
            sum_zero_pairs = [(0,0)]
        else:
            sum_zero_pairs = []
    #Create a set of tuples of all 2-member combinations of members of "numbers".
    pairs = combinations(numbers, 2)
    #Sort the contents of these tuples and create a set of (necessarily) unique tuples. Takes a couple type cpnversions
    pairs_set = {tuple(sorted(list(i))) for i in pairs}
    #read the set into a dictionary with members of the set as the key, and their contents' sum as the value
    pairs_dictionary = {i:(i[0]+i[1]) for i in pairs_set}
    #Create a new dictionary of those tuples which sum to zero
    zero_pairs = {i:pairs_dictionary[i] for i in pairs_dictionary if pairs_dictionary[i] == 0}
    #Create an empty list to fill with zero sum pairs
    #append zero sum pairs to this list
    for key in zero_pairs.keys():
        sum_zero_pairs.append(key)
    #return list
    return sum_zero_pairs


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """
    #first,strip out spaces
    phrase = phrase.replace(" ", "")
    #Create a dictionsry of characters and counts
    letter_counts = {}
    letter_counts_list = []
    top_chars = []
    for letter in phrase:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1        
    # Dictionary did the counting work, now sort it's contents. It'd be nice to trim the highest count and anything matching but dictionaries don't roll like that. Lists, tho...
    letter_counts_list = [(letter_counts[i],i) for i in letter_counts]
    #get the high counts to the end
    letter_counts_list.sort()
    #set aside and mark the very highest count
    highest_count = letter_counts_list[-1][0]
    #pull any letters with that count
    for i in range(len(letter_counts_list)):
        if letter_counts_list[i][0] == highest_count:
            #and set them aside in one place
            top_chars.append(letter_counts_list[i][1])
    #I'm pretty sure the above sort will make this next line redundant, but just in case...
    top_chars.sort()
    return top_chars

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

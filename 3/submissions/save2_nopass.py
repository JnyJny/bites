import os
import urllib.request
import collections

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)
scrabble_scores = [(1, "E A O I N R T L S U"), (2, "D G"), (3, "B C M P"),
                   (4, "F H V W Y"), (5, "K"), (8, "J X"), (10, "Q Z")]
LETTER_SCORES = {letter: score for score, letters in scrabble_scores
                 for letter in letters.split()}


# start coding

def load_words():
    """load the words dictionary (DICTIONARY constant) into a list and return it"""
    clean = lambda w: w.strip()
    return [clean(w) for w in open(DICTIONARY).readlines()]
        


def calc_word_value(word):
    """given a word calculate its value using LETTER_SCORES"""
    counts = collections.Counter(word)
    value = 0
    for letter, count in counts.items():
        for score, letters in scrabble_scores:
            if letter in letters:
                value += score * count
    return value
def max_word_value(words=None):
    """given a list of words return the word with the maximum word value"""
    pass
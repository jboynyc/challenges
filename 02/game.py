#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from random import shuffle
from itertools import permutations
from collections import Counter
from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def draw_from_pouch(n):
    """Pop n randomly chosen letters out of pouch."""
    shuffle(POUCH)
    for _ in range(n):
        yield POUCH.pop()


def all_possible_words(letters):
    """Return set of all words that can be formed with given letters."""
    words = set()
    for wordlen in range(len(letters)):
        words.update(''.join(w) for w in permutations(letters, wordlen))
    return set(word.upper() for word in DICTIONARY).intersection(words)


def is_dictionary_word(word):
    return word.upper() in map(lambda s: s.upper(), DICTIONARY)


def is_word_permissible(word, letters):
    if not Counter(word.upper()) - Counter(''.join(letters).upper()): 
        valid_letters = True
    else:
        valid_letters = False
    return valid_letters and is_dictionary_word(word)


def main():
    rounds = 0
    total_score = 0
    total_optimal = 0
    letters_on_hand = []
    while True:
        try:
            letters_needed = NUM_LETTERS - len(letters_on_hand)
            if letters_needed > len(POUCH):
                print('Not enough letters remaining in pouch. '
                      'Quitting... total score after {} rounds was {:.1%}.'.format(rounds, total_score/total_optimal))
                break
            letters_on_hand += list(draw_from_pouch(letters_needed))
            possible_words = all_possible_words(letters_on_hand)
            optimal_word = max_word_value(possible_words)
            optimal_score = calc_word_value(optimal_word)
            print('Letters drawn:', ', '.join(letters_on_hand))
            print('Choose a word: ', end='')
            chosen_word = input()
            while not is_word_permissible(chosen_word, letters_on_hand):
                print('Choose a valid word: ', end='')
                chosen_word = input()
            chosen_word = chosen_word.upper()
            user_score = calc_word_value(chosen_word)
            for letter in chosen_word:
                letters_on_hand.pop(letters_on_hand.index(letter))
            print('Word chosen: {} (score: {})'.format(chosen_word, user_score))
            print('Optimal word: {} (score: {})'.format(optimal_word, optimal_score))
            print('Your score: {:.1%}'.format(user_score/optimal_score))
            rounds += 1
            total_score += user_score
            total_optimal += optimal_score
        except KeyboardInterrupt:
            print('Quitting... total score after {} rounds was {:.1%}.'.format(rounds, total_score/total_optimal))
            break



if __name__ == "__main__":
    main()

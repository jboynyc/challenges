from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as dictionary:
        words = dictionary.readlines()
    return [word.strip() for word in words]


def score_letter(letter):
    """Return the score for the given letter (if any) using
    imported constant mapping LETTER_SCORES"""
    return LETTER_SCORES.get(letter.upper(), 0)


def score_word(word):
    """Calculate the value of the word entered into function"""
    return sum(score_letter(char) for char in word)


def max_word_value(word_list=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    scored_words = {word: score_word(word) for word in word_list}
    return max(scored_words.items(), key=lambda i: i[1])[0]


calc_word_value = score_word


if __name__ == "__main__":
    pass  # run unittests to validate

# read words_alpha.txt and return list of words
def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())
        word_file.close()
    return list(valid_words)

def load_words_with_meaning():
    dictionary = dict()
    with open('words_meaning.txt') as word_file:
        word, meaning = set(word_file.read().split().split(':'))
        dictionary[word] = meaning
    return dictionary
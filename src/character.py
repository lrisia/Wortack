import random as rd
# from service.word_handle import load_words    # word from old file
from service.word_handle_nltk import load_words # word from new file with meaning

CHARACTERS = {"Cool guy": "đ", "Angry boy": "đ€Ź", "Cowboy": "đ€ ", "The Clown": "đ€Ą", "Nerd guy": "đ€",
              "Happy demon": "đ", "Angry demon": "đż", "Oni": "đč", "Goblin": "đș", "Ghost": "đ»",
              "Alien": "đœ", "Alien Monster": "đŸ", "Robot The Destroyer": "đ€", "Tiger": "đ",
              "Google Trex": "đŠ", "Dragon in my Jeans": "đ", "My Anaconda": "đ", "Octopus The artist": "đ",
              "Doppelganger": "đ„", "The King": "đ€Ž", "Angel": "đŒ", "Santa Claus": "đ", "Superman": "đŠž",
              "Magicial": "đŠč", "Gran Draft The Grey": "đ§", "Poseidon": "đ§", "Sleeper": "đ"
             }
WORDS = load_words()
MAX_HP = 0

# set new max hp
def setup_player(max_hp=3):
    global MAX_HP
    MAX_HP = max_hp

# player emoji controller
def player(hp):
    low = int(MAX_HP/3)
    middle = low*2
    if hp > middle and hp <= MAX_HP: return "đđȘ"
    elif hp > low and hp <= middle: return "đđȘ"
    elif hp > 0 and hp <= low: return "đđȘ"
    return "đđȘ"

def random_enemy(bounty=0):
    character = rd.choice(list(CHARACTERS.items()))[0]
    word = random_word(bounty)
    return Enemy(character, word)

def random_word(bounty):
    if bounty <= 2: length_range = (3, 4)
    elif bounty <= 3: length_range = (4, 5)
    elif bounty <= 5: length_range = (5, 6)
    elif bounty <= 8: length_range = (6, 7)
    else: length_range = (7, 10)
    word = ""
    while not (len(word) >= length_range[0] and len(word) <= length_range[1]):
        word = rd.choice(list(WORDS))
    return word

class Enemy:
    def __init__(self, character, word) -> None:
        self.character = character
        self.emoji = CHARACTERS[character]
        self.word = word.lower()
        self.hp = len(word)
        self.hidding_word = "".join(["_" for i in range(self.hp)])
        self.shaffle_word = " ".join([i.upper() for i in self.shuffling_letter()])
        self.word_dict = self.word_to_dict(word.lower())
        self.meaning = WORDS[word]

    # count letter and save in dictionary
    def word_to_dict(self, word):
        word_dict = dict()
        for ch in word: word_dict[ch] = word.count(ch)
        return word_dict

    # compare answer length with input length
    def check_ch_amount(self, word):
        miss_letter = [ch for ch in self.word_dict if ch not in word]
        correct = [ch for ch in self.word_dict if ch in word]
        miss_letter += [ch for ch in correct if word.count(ch) != self.word_dict[ch]]
        return list(set(miss_letter)), not len(miss_letter)

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            self.emoji = "đ"

    def check_lenght(self, answer):
        if len(answer) == len(self.word): return True
        return False

    def check_answer(self, answer):
        correct = 0
        hidding = list(self.hidding_word)
        for i in range(len(answer)):
            if answer[i] == self.word[i] and hidding[i] == '_':
                hidding[i] = answer[i].upper()
                correct += 1
        self.hidding_word = "".join(hidding)
        self.take_damage(correct)
        return correct
    
    def shuffling_letter(self):
        temp = list(self.word)
        rd.shuffle(temp)
        return temp

setup_player()
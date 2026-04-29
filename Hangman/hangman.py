"""
Hangman / Wordle clone
Pick a word from a list; player guesses letters/words with feedback per attempt.  
Skills: string slicing, sets, file reading (word list), terminal output formatting.
"""
import random

class Hangman:
    def __init__(self):
        self.word_list = self.getWordList()
        self.rnd = random.randint(0, len(self.word_list))
        self.rnd_word = self.word_list[self.rnd]
        self.guessed_chars = []
    
    def run(self):
        print(50 * "=")
        print("Hangman Game - presented by Tobi")
        print(50 * "=")

        print(self.rnd_word)
        
    def getWordList(self):
        file = open("Hangman/word-list.txt", "r")
        content = file.readlines()
        file.close()
        return content
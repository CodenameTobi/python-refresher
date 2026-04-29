"""
Hangman / Wordle clone
Pick a word from a list; player guesses letters/words with feedback per attempt.  
Skills: string slicing, sets, file reading (word list), terminal output formatting.
"""
import random


class Hangman:
    def __init__(self, max_guesses=10):
        self.word_list = self.get_word_list()
        self.rnd = random.randint(0, len(self.word_list))
        self.rnd_word = self.word_list[self.rnd].strip()

        # Guesses
        self.guessed_chars = []
        self.guessed_word = ""

        # Game settings
        self.guess_ctr = max_guesses

    def get_word_list(self):
        file = open("Hangman/word-list.txt", "r")
        content = file.readlines()
        file.close()
        return content

    def is_valid_guess(self, guess: str):
        if guess in self.guessed_chars:
            print(f"🔄️ You already guessed {guess}. Try another one!")
            return False
        return guess.lower().strip() in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    def get_character_guess(self):
        guess = 'aa'
        while not self.is_valid_guess(guess):
            print(
                f"You have guessed the following characters so far: {self.guessed_chars}.")
            guess = input("Enter your guess: ")

        # Since we check for duplicated guesses in is_valid_guess, we can simply add the guess here without checking for duplicates.
        self.guessed_chars.append(guess)
        self.guessed_chars = sorted(self.guessed_chars)

        return guess

    def run(self):
        print(50 * "=")
        print("Hangman Game - presented by Tobi")
        print(50 * "=")

        # Name the game rules.
        print(f"You have {self.guess_ctr} guesses in total. Your guesses have to be single characters.\nRepeated characters are not counted as attempts. Good luck🍀\n")
        self.guessed_word = '_' * len(self.rnd_word)

        while self.guessed_word != self.rnd_word and self.guess_ctr > 0:
            print(
                f"You have guessed so far: {self.guessed_word}.\nYou have {self.guess_ctr} guess{"" if self.guess_ctr == 1 else "es"} remaining.\n")

            guess = self.get_character_guess()

            if guess in self.rnd_word:
                print("✅ Horrayy🥳\n")
                guessed_list = list(self.guessed_word)
                guessed_list = [l if l in self.guessed_chars else '_' for l in self.rnd_word]
                self.guessed_word = ''.join(guessed_list)
            else:
                self.guess_ctr -= 1
                print("❌ That wasn't it! Better luck next time.\n")

        if self.guessed_word == self.rnd_word:
            print(f"You won🥳 The word was {self.rnd_word.upper()}.")
        else:
            print(f"You lost🤒 The word was {self.rnd_word.upper()}.")

"""
Number guessing game  
Computer picks a number; user guesses with hot/cold feedback. Add difficulty levels and score tracking.  
Skills: `input()`, `random`, `while` loops, exception handling on bad input.
""" 
import random  

class NumberGuesser:

    def __init__(self):
        self.rnd = random.randint(1, 100)
    
    def run(self):
        print(50 * "=")
        print("Number Guessing Game")
        print(50 * "=")
        
        guess = -1
        count = 0
        
        while guess != self.rnd:
            count += 1
            
            try:
                guess = int(input("Please type in your guess in range (1 - 100): "))
            except:
                print("Not a valid input! Only numbers between 1 and 100 are allowed.")
                continue
            
            if guess == self.rnd:
                print(f"Congrats!!! You got the number on your {count} try🥳 The number is {self.rnd}.")
            elif guess < self.rnd:
                print("You might want to go higher!")
            else:
                print("You might want to go lower!")
        
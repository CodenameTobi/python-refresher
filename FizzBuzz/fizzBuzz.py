"""
Print numbers 1-N, replacing multiples of 3/5 with words.  
**Skills:** control flow, modulo, list comprehensions, basic functions.
"""

class FizzBuzz:
    def __init__(self, n: int, fizz=3, buzz=5):
        self.fizz = fizz
        self.buzz = buzz
        self.n = n
    
    def run(self):
        print(50 * "=")
        print(f"Now running fizz buzz for n={self.n}, fizz/buzz={self.fizz}/{self.buzz}.")
        print(50 * "=", '\n')
        
        for i in range(1, self.n):
            is_fizz, is_buzz = i % self.fizz == 0, i % self.buzz == 0
            if is_fizz and is_buzz:
                print("FizzBuzz")
            elif is_fizz:
                print("Fizz")
            elif is_buzz:
                print("Buzz")
            else:
                print(i)
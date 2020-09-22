import random
import sys

from .phrase import Phrase

class Game:

    def __init__(self):

        self.missed = 0
        self.phrases = [Phrase("cat in the hat"), Phrase("boy who cried wolf"), Phrase("the fox and the hound"), Phrase("the sword in the stone"), Phrase("robin hood")]
        self.active_phrase = None
        self.guesses = []


    def start(self):

        self.welcome()
        self.active_phrase = self.get_random_phrase()
        print(self.active_phrase)
        # creates game loop
        while True:            
            self.active_phrase.display(self.guesses)
            
            # calls get_guess()
            guess = self.get_guess()
            # adds player's guess to the guesses list
            self.guesses.append(guess)
            print(self.guesses)
            self.active_phrase.check_letter(guess)
            # increments missed if guess incorrect
            if not self.active_phrase.check_letter(guess):
                self.missed += 1
                print(f"{guess} isn't in the phrase!")
                print(f"You have {5 - self.missed} lives left!")
            # calls game_over()
            if self.active_phrase.check_complete(self.guesses):
                self.game_over()


    def get_random_phrase(self):

        return random.choice(self.phrases)


    def welcome(self):

        print("\n\nP-H-R-A-S-E--H-U-N-T-E-R!!\n")

    
    def get_guess(self):

        # get guess from user, verifies it's a letter and hasn't been guessed yet
        guess = ""
        while not guess.isalpha():
            guess = input("Enter a letter to guess >> ").lower()

            if guess in self.guesses:
                print("You've alread guessed that letter!")
                print(f"Past Guesses: {self.guesses}")
                guess = ""

        return guess

    def game_over(self):

        # print win or lose message
        print("Game Over!")

        replay = ""
        while replay != "y" and replay != "n":
            replay = input("Play again? [y/n] >> ").lower()
        
        if replay == "y":
            game = Game()
            game.start()
        elif replay == "n":
            sys.exit()

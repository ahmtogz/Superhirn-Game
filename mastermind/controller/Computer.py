import random
from typing import List

from mastermind.controller.IPlayer import IPlayer


class Computer(IPlayer):
    def __init__(self, role, num_colors, board_size):
        self.ROLE = role
        self.num_colors = num_colors
        self.board_size = board_size
        self.current_guess = [0] * board_size
        self.all_guesses = []
        self.possible_moves = []



    def create_code(self):
        code = random.sample(range(1, self.num_colors + 1), self.board_size)
        random.shuffle(code)
        return code

    def initial_guess(self):
        """
        Erstellt die initiale Vermutung nach dem Knuth-Algorithmus.
        """
        return random.choice(self.possible_moves)  # Eine Standard-Anfangsvermutung nach Knuth

    def make_guess(self):
        """
        Rät den Code basierend auf dem Knuth-Algorithmus und speichert ihn als letzten geratenen Code.
        """
        if not self.last_guess:
            guess = self.initial_guess()
        else:
            # Entfernt alle Codes aus den Möglichkeiten, die nicht dasselbe Feedback erzeugen würden,
            # wenn sie der tatsächliche Code wären.
            self.possibilities = [code for code in self.possibilities if self.evaluate_guess(code) == self.evaluate_guess(self.current_guess)]
            guess = self.possibilities[0] if self.possibilities else self.initial_guess()

        self.solutions.append(guess)
        self.last_guess = guess


        return guess


    def receive_current_state(self, new_guesses):
        self.all_guesses = new_guesses
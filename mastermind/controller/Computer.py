import itertools
import random
from typing import List

from mastermind.controller.Evalutor import Evaluator
from mastermind.controller.IPlayer import IPlayer


class Computer(IPlayer):
    def __init__(self, num_colors, board_size):
        self.num_colors = num_colors
        self.board_size = board_size
        self.current_guess = [0] * board_size
        self.all_guesses = []
        self.possible_moves = self.generate_all_moves()
        self.all_feedbacks = []
        self.evaluator = Evaluator()

    def create_code(self):
        code = random.sample(range(1, self.num_colors + 1), self.board_size)
        random.shuffle(code)
        return code

    def get_random_guess(self):
        """
        Erstellt die initiale Vermutung nach dem Knuth-Algorithmus.
        """
        return random.choice(self.possible_moves)  # Eine Standard-Anfangsvermutung nach Knuth

    def make_guess(self):
        """
        Rät den Code basierend auf dem Knuth-Algorithmus und speichert ihn als letzten geratenen Code.
        """
        if not self.current_guess:
            guess = self.get_random_guess()
        else:
            # Entfernt alle Codes aus den Möglichkeiten, die nicht dasselbe Feedback erzeugen würden,
            # wenn sie der tatsächliche Code wären.
            if self.all_feedbacks:
                self.filter_moves()
            guess = self.get_random_guess()

        self.all_guesses.append(guess)
        self.current_guess = guess

        return guess

    def generate_all_moves(self):
        color_iterable = range(1, self.num_colors + 1)
        all_combinations_as_tuples = list(itertools.product(color_iterable, repeat=self.board_size))
        return [list(combination) for combination in all_combinations_as_tuples]

    def filter_moves(self):

        latest_feedback = self.all_feedbacks[-1]
        black_pins, white_pins = latest_feedback.get_pins()
        filtered_moves = []

        for code in self.possible_moves:
            if self.evaluator.evaluate_guess(code, self.current_guess.copy()) == (black_pins, white_pins):
                filtered_moves.append(code)

        self.possible_moves = filtered_moves

    def receive_feedback(self, guess_with_pins):
        self.all_feedbacks.append(guess_with_pins)

    def get_latest_guess(self):
        return self.current_guess
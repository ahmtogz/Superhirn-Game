import itertools
import random
from typing import List

from mastermind.controller.Evaluator import Evaluator
from mastermind.controller.IPlayer import IPlayer


class Computer(IPlayer):
    def __init__(self, num_colors, board_size):
        """
        Initializes a Computer player with the specified number of colors and board size.

        Args:
            num_colors (int): The number of colors available for each guess.
            board_size (int): The size of the game board.

        Returns:
            None
        """
        self.num_colors = num_colors
        self.board_size = board_size
        self.current_guess = [0] * board_size
        self.all_guesses = []
        self.possible_moves = self.generate_all_moves()
        self.all_feedbacks = []
        self.evaluator = Evaluator()

    def create_code(self):
        """
        Creates and returns a secret code for the computer player.

        Returns:
            list: The secret code created by the computer player.
        """
        code = []
        for _ in range(self.board_size):
            code.append(random.randint(1, self.num_colors))
        return code

    def get_random_guess(self):
        """
        Erstellt die initiale Vermutung nach dem Knuth-Algorithmus.
        Makes a guess based on the Knuth algorithm and updates the current guess.

        Returns:
            list: The guess made by the computer player.
        """
        return random.choice(self.possible_moves)  # Eine Standard-Anfangsvermutung nach Knuth

    def make_guess(self):
        """
        Rät den Code basierend auf dem Knuth-Algorithmus und speichert ihn als letzten geratenen Code.
        Makes a guess based on the Knuth algorithm and updates the current guess.

        Returns:
            list: The guess made by the computer player.
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
        """
        Generates all possible combinations of colors for the game board.

        Returns:
            List[List[int]]: A list containing all possible code combinations.
        """
        color_iterable = range(1, self.num_colors + 1)
        all_combinations_as_tuples = list(itertools.product(color_iterable, repeat=self.board_size))
        return [list(combination) for combination in all_combinations_as_tuples]

    def filter_moves(self):
        """
        Filters the possible moves based on the latest feedback.

        Returns:
            None
        """
        latest_feedback = self.all_feedbacks[-1]
        black_pins, white_pins = latest_feedback.get_pins()
        filtered_moves = []

        for code in self.possible_moves:
            if self.evaluator.evaluate_guess(code, self.current_guess.copy()) == (black_pins, white_pins):
                filtered_moves.append(code)

        self.possible_moves = filtered_moves

    def receive_feedback(self, guess_with_pins):
        """
        Receives feedback for the last guess made by the computer player.

        Args:
            guess_with_pins (Guess): The guess along with feedback pins.

        Returns:
            None
        """
        self.all_feedbacks.append(guess_with_pins)

    def get_latest_guess(self):
        """
        Gets the latest guess made by the computer player.

        Returns:
            list: The latest guess made by the computer player.
        """
        return self.current_guess

from typing import List

from mastermind.controller.IPlayer import IPlayer


class Computer(IPlayer):
    def __init__(self, role, num_colors, board_size):
        self.ROLE = role
        self.num_colors = num_colors
        self.board_size = board_size
        self.current_guess = [0] * board_size
        self.all_guesses = []

    def create_code(self):
        return [0] * self.board_size

    def make_guess(self):
        return [0] * self.board_size

    def receive_current_state(self, new_guesses):
        self.all_guesses = new_guesses
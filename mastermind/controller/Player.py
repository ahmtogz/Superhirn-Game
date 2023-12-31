from random import random

from mastermind.controller.IPlayer import IPlayer
from mastermind.controller.InputHandler import InputHandler


class Player(IPlayer):
    MIN_COLOR = 1
    MAX_POSSIBLE_COLOR = 8
    def __init__(self, num_color, board_size):
        self.handler = InputHandler()
        #self.ROLE = role
        self.board_size = board_size
        self.current_guess = [0] * board_size

        self.num_color = num_color

    def create_code(self):
        return self.play()

        #return [random.randint(1, 8) for _ in range(self.board_size)]
        # return [0] * self.board_size

    def make_guess(self):
        latest_guess = self.play()
        self.current_guess = latest_guess
        return latest_guess

    def create_gamer_id(self):
        return self.handler.get_gamer_id()

    def create_board_size(self):
        self.board_size = self.handler.get_board_size()
        return self.board_size

    def get_num_colors(self):
        return self.handler.get_color(self.MIN_COLOR, self.MAX_POSSIBLE_COLOR)  # TODO fix magic numbers

    def play(self):
        colors = []
        for _ in range(self.board_size):
            colors.append(self.handler.get_color(self.MIN_COLOR, self.num_color))  # TODO fix magic numbers

        return colors
    def receive_feedback(self, guess_with_pins):
        #no-op
        pass

    def get_latest_guess(self):
        return self.current_guess

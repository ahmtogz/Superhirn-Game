from random import random

from mastermind.controller.IPlayer import IPlayer
from mastermind.controller.InputHandler import InputHandler


class Player(IPlayer):

    MIN_COLOR = 1
    MAX_POSSIBLE_COLOR = 8
    def __init__(self, num_color, board_size):
        """
        Initializes a Player object with the specified number of colors and board size.

        Args:
            num_color (int): The number of colors available for each guess.
            board_size (int): The size of the game board.

        Returns:
            None
        """
        self.handler = InputHandler()
        #self.ROLE = role
        self.board_size = board_size
        self.current_guess = [0] * board_size

        self.num_color = num_color

    def create_code(self):
        """
        Creates and returns the secret code for the player.

        Returns:
            list: The secret code created by the player.
        """
        return self.play()

        #return [random.randint(1, 8) for _ in range(self.board_size)]
        # return [0] * self.board_size

    def make_guess(self):
        """
        Makes a guess and returns the latest guess made by the player.

        Returns:
            list: The latest guess made by the player.
        """
        latest_guess = self.play()
        self.current_guess = latest_guess
        return latest_guess

    def create_gamer_id(self):
        """
        Creates and returns the gamer ID for the player.

        Returns:
            str: The gamer ID created by the player.
        """
        return self.handler.get_gamer_id()

    def create_board_size(self):
        """
        Creates and returns the board size for the player.

        Returns:
            int: The board size selected by the player.
        """
        self.board_size = self.handler.get_board_size()
        return self.board_size

    def get_num_colors(self):
        """
        Gets the number of colors selected by the player.

        Returns:
            int: The number of colors selected by the player.
        """
        return self.handler.get_color(self.MIN_COLOR, self.MAX_POSSIBLE_COLOR)  # TODO fix magic numbers

    def play(self):
        """
        Simulates the player's turn, getting a sequence of colors as a guess.

        Returns:
            list: A list representing the guess made by the player.
        """
        colors = []
        for _ in range(self.board_size):
            colors.append(self.handler.get_color(self.MIN_COLOR, self.num_color))  # TODO fix magic numbers

        return colors
    def receive_feedback(self, guess_with_pins):
        #no-op
        pass

    def get_latest_guess(self):
        """
        Gets the latest guess made by the player.

        Returns:
            list: The latest guess made by the player.
        """
        return self.current_guess

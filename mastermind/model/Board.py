from mastermind.model.Guess import Guess


class Board:
    def __init__(self, board_size, num_colors, num_rounds):
        """
        Initializes a Board object with the specified parameters.

        Args:
            board_size (int): The size of the game board.
            num_colors (int): The number of colors available for each guess.
            num_rounds (int): The total number of rounds in the game.

        Returns:
            None
        """
        self.board_size = board_size
        self.num_colors = num_colors
        self.num_rounds = num_rounds
        self.all_guesses = []
        #self.player_code = [0] * num_colors

    def get_player_code(self):
        """
        Gets the player's secret code.

        Returns:
            list: The player's secret code.
        """
        return self.player_code

    def set_player_code(self, player_code):
        """
        Sets the player's secret code.

        Args:
            player_code (list): The player's secret code.

        Returns:
            None
        """
        self.player_code = player_code

    def get_num_rounds(self):
        """
        Gets the total number of rounds in the game.

        Returns:
            int: The total number of rounds.
        """
        return self.num_rounds

    def receive_guess(self, current_guess):
        """
        Receives and records a player's guess.

        Args:
            current_guess (Guess): The current guess made by the player.

        Returns:
            None
        """
        #TODO rework
        self.all_guesses.append(current_guess)

    def get_all_guesses(self):
        """
        Gets all the guesses made during the game.

        Returns:
            list: A list of Guess objects representing all the guesses.
        """
        return self.all_guesses

    def get_guess_for_round(self, round_num):
        """
        Gets the guess made during a specific round.

        Args:
             round_num (int): The round number.

        Returns:
            Guess: The Guess object representing the guess made in the specified round.
        """
        return self.all_guesses[round_num]
from mastermind.model.Guess import Guess


class Board:
    def __init__(self, board_size, num_colors, num_rounds):
        self.board_size = board_size
        self.num_colors = num_colors
        self.num_rounds = num_rounds
        self.all_guesses = []
        #self.player_code = [0] * num_colors

    def get_player_code(self):
        return self.player_code

    def set_player_code(self, player_code):
        self.player_code = player_code

    def get_num_rounds(self):
        return self.num_rounds

    def receive_guess(self, current_guess):
        #TODO rework
        self.all_guesses.append(current_guess)

    def get_all_guesses(self):
        return self.all_guesses

    def get_guess_for_round(self, round_num):
        return self.all_guesses[round_num]
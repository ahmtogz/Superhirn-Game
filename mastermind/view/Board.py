class Board:
    def __init__(self, board_size, num_colors, num_rounds):
        self.board_size = board_size
        self.num_colors = num_colors
        self.num_rounds = num_rounds
        self.all_guesses = [None] * num_rounds
        self.player_code = [0] * num_colors

    def get_player_code(self):
        return self.player_code

    def set_player_code(self, player_code):
        self.player_code = player_code

    def get_num_
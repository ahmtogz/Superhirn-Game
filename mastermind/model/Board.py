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

    def get_num_rounds(self):
        return self.num_rounds

    def receive_guess(self, current_round, current):
        pins = self.generate_pins(current)
        self.all_guesses[current_round] = Guess(current, pins)

    def get_all_guesses(self):
        return self.all_guesses

    def get_guess_for_round(self, round_num):
        return self.all_guesses[round_num]

    def generate_pins(self, current):
        return None

    class Guess:
        def __init__(self, current, pins):
            self.current = current
            self.pins = pins

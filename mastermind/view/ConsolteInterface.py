from mastermind.view.IUserInterface import IUserInterface


class ConsoleInterface(IUserInterface):
    def display_game_state(self, board):
        current_board_state = board.get_all_guesses()

        for guess in current_board_state:
            black_pins, white_pins = guess.get_pins()
            print(str(guess.get_guess()) + ", Black Pins: " + str(black_pins) + ", White Pins: " + str(white_pins))

        print("\n")

    def display_message(self, message):
        print(message)

    def display_win_message(self, message):
        print(message)

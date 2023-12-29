from random import randrange

from mastermind.controller.Computer import Computer
from mastermind.controller.Evalutor import Evaluator
from mastermind.controller.IGameManager import IGameManager
from mastermind.controller.Player import Player
from mastermind.controller.network.Package import Package
from mastermind.model.Board import Board
from mastermind.model.Guess import Guess


class NetworkGameManager(IGameManager):
    NUM_ROUNDS = 10

    PLAYER_GUESSER = 0
    COMPUTER_GUESSER = 1

    CREATOR = 2
    GUESSER = 3
    NONE = 4

    def __init__(self, ui, sender, num_colors, board_size):
        self.sender = sender

        self.ui = ui
        self.game_id = None
        self.gamer_id = None
        self.positions = board_size
        self.colors = num_colors

        self.human_player = Player(board_size)

        self.player_guess = None

        self.guessing_role = None
        self.true_code = None

        self.current_round = 1

        self.board = None

        self.game_over = False

        self.evaluator = Evaluator()

    def __init__(self, ui, sender):
        self.ui = ui
        self.sender = sender

        self.ui = ui
        self.game_id = None
        self.gamer_id = None
        self.positions = None
        self.colors = None

        self.human_player = Player(None)

        self.player_guess = None

        self.guessing_role = None
        self.true_code = None

        self.board = None

        self.game_over = False
        self.evaluator = Evaluator()

    def init_game(self):
        init_game_id = 0
        gamer_id = self.human_player.create_gamer_id()
        self.gamer_id = gamer_id

        positions = self.human_player.create_board_size()
        self.positions = positions

        num_colors = self.human_player.get_num_colors()
        self.colors = num_colors

        self.board = Board(positions, num_colors, self.NUM_ROUNDS)
        package = Package(init_game_id, gamer_id, positions, num_colors, "")

        self.receive_init_result(self.sender.send_package(package))

    def receive_init_result(self, package):
        self.game_id = package.game_id

        while not self.game_over:
            self.start_round()

    def check_game_over(self):
        if self.current_round >= self.board.get_num_rounds():
            # CREATOR hat gewonnen
            return self.CREATOR
        else:
            last_guess = self.player_guess.get_latest_guess()
            player_code = self.true_code

            if last_guess == player_code:
                # GUESSER hat gewonnen
                return self.GUESSER
        return self.NONE

    def start_game(self):
        self.ui.display_message("1. Kodierer, 2. Rater: ")
        mode = input()

        computer = Computer(self.colors, self.positions)

        if mode == "1":
            self.player_guess = computer
            self.guessing_role = self.COMPUTER_GUESSER

            self.ui.display_message("Erstelle den Code: ")
            self.true_code = self.human_player.create_code()
        if mode == "2":
            self.player_guess = self.human_player
            self.guessing_role = self.PLAYER_GUESSER

            self.ui.display_message("Der Computer erstellt den Code...")
            self.true_code = computer.create_code()
        # TODO switch to pattern matching and add default

        return self.true_code

    def start_round(self):
        match self.guessing_role:
            case self.PLAYER_GUESSER:
                self.handle_player_guesser()
            case self.COMPUTER_GUESSER:
                self.handle_computer_guesser()
            case _:
                # TODO Error handling
                pass


    def clean_up(self):
        # TODO display Board

        self.ui.display_game_state()

        winner = self.check_game_over()

        if winner != self.NONE:
            win_message = "Der Codierer hat gewonnen!" if winner == self.CREATOR else "Der Guesser hat gewonnen"
            win_message += "\n Der Farbcode war: "  # TODO Farbcode anzeigen
            self.ui.display_win_message(win_message)

            self.ui.display_message("Thanks for playing!")
            self.game_over = True

        self.current_round += 1

    def handle_player_guesser(self):
        self.ui.display_message(f"Bitte gib deinen Rateversuch für Runde {self.current_round} ab: ")

        current_guess = self.validate_guess()

        package = Package(self.game_id, self.gamer_id, self.positions, self.colors, self.parse_guess(current_guess))
        self.handle_evaluation_result(self.sender.send_package(package), current_guess)  # evaluation_result

    def handle_computer_guesser(self):
        current_guess = self.player_guess.make_guess()

        package = Package(self.game_id, self.gamer_id, self.positions, self.colors, self.parse_guess(current_guess))
        self.handle_evaluation_result(self.sender.send_package(package), current_guess)  # evaluation_result

    def handle_evaluation_result(self, package, guess):
        unparsed_evaluation = package.value

        if unparsed_evaluation is not None and len(unparsed_evaluation) > 0:
            black_pins, white_pins = self.parse_eval_from_package_ammount(unparsed_evaluation)
            guess_with_pins = Guess(guess, (black_pins, white_pins))

            self.board.receive_guess(self.current_round, guess_with_pins)
            self.player_guess.receive_feedback(guess_with_pins)

    def evaluate_guess(self, current_guess):
        if self.true_code is not None:
            return self.evaluator.evaluate_guess(self.true_code, current_guess)
        return None

    def parse_guess(self, guess):
        parsed_guess = ""

        for color in guess:
            parsed_guess += str(color)

        return parsed_guess

    def parse_eval_from_package_ammount(self, evaluation):
        # assuming the format would be value = "21" meaning 2 black pins and 1 white pin
        black_pins = int(evaluation[0])
        white_pins = int(evaluation[1])

        return black_pins, white_pins

    def parse_eval_from_package_row(self, evaluation):
        # assuming the format would be value = "887" meaning 2 black pins and 1 white pin

        black_pins = evaluation.count(str(8))
        white_pins = evaluation.count(str(7))

        return black_pins, white_pins

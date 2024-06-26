from mastermind.controller.Evaluator import Evaluator
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

        self.human_player = Player(num_colors, board_size)

        self.player_guess = None

        self.guessing_role = None
        self.true_code = None

        self.current_round = 1

        self.board = None

        self.game_over = False
        self.latest_result = None

        self.evaluator = Evaluator()

    def start_game(self):
        # assuming the network would always handle the code
        self.player_guess = self.human_player
        self.guessing_role = self.PLAYER_GUESSER

        self.ui.display_message("Der Server im Netz erstellt den Code...")

        self.init_game()

    def start_round(self):
        match self.guessing_role:
            case self.PLAYER_GUESSER:
                self.handle_player_guesser()
            case self.COMPUTER_GUESSER:
                self.handle_computer_guesser()
            case _:
                self.ui.display_win_message("Etwas ist beim Setup-Prozess schief gelaufen. Spiel wird geschlossen.")
                exit()

    def init_game(self):
        init_game_id = 0
        gamer_id = self.human_player.create_gamer_id()
        self.gamer_id = gamer_id

        self.board = Board(self.positions, self.colors, self.NUM_ROUNDS)
        package = Package(init_game_id, self.gamer_id, self.positions, self.colors, "")

        self.receive_init_result(self.sender.send(package))

    def receive_init_result(self, package):
        self.game_id = package.game_id

        while not self.game_over:
            self.start_round()

    def check_game_over(self):
        if self.current_round >= self.board.get_num_rounds():
            return self.CREATOR
        else:
            if self.latest_result is not None:
                num_black_pins = self.latest_result.get_pins()[0]
                if num_black_pins == self.board.board_size:
                    return self.GUESSER
        return self.NONE

    def clean_up(self):
        self.ui.display_game_state()

        winner = self.check_game_over()

        if winner != self.NONE:
            win_message = "Der Codierer hat gewonnen!" if winner == self.CREATOR else "Der Guesser hat gewonnen"
            # win_message += "\n Der Farbcode war: "  # TODO Farbcode anzeigen (Woher kriegt man den Farbcode?)
            self.ui.display_win_message(win_message)

            self.ui.display_message("Thanks for playing!")
            self.game_over = True

        self.current_round += 1

    def handle_player_guesser(self):
        self.ui.display_message(f"Bitte gib deinen Rateversuch für Runde {self.current_round} ab: ")

        current_guess = self.validate_guess()

        package = Package(self.game_id, self.gamer_id, self.positions, self.colors, self.parse_guess(current_guess))
        self.handle_evaluation_result(self.sender.send(package), current_guess)  # evaluation_result

    def handle_computer_guesser(self):
        current_guess = self.player_guess.make_guess()

        package = Package(self.game_id, self.gamer_id, self.positions, self.colors,
                          self.parse_guess(current_guess))
        self.handle_evaluation_result(self.sender.send(package), current_guess)  # evaluation_result

    def handle_evaluation_result(self, package, guess):
        unparsed_evaluation = package.value

        if unparsed_evaluation is not None and len(unparsed_evaluation) > 0:
            black_pins, white_pins = self.parse_eval_from_package_ammount(unparsed_evaluation)
            guess_with_pins = Guess(guess, (black_pins, white_pins))

            self.board.receive_guess(self.current_round, guess_with_pins)
            self.player_guess.receive_feedback(guess_with_pins)

            self.latest_result = guess_with_pins

    def evaluate_guess(self, current_guess):
        if self.true_code is not None:
            return self.evaluator.evaluate_guess(self.true_code, current_guess.copy())
        return None

    def validate_guess(self):
        validated = False
        current_guess = None

        while not validated:
            current_guess = self.player_guess.make_guess()
            validated = self.validate_input(current_guess)

        return current_guess

    def validate_input(self, current_input):
        """
        Validates the input for correctness.

        Args:
            current_input (list): The current input to be validated.

        Returns:
            bool: True if the input is in the correct format, False otherwise.
        """

        correct_format = True

        for color in current_input:
            if not 1 <= color <= self.colors:
                self.ui.display_message(f"Ungültige Eingabe. Geben sie den Code erneut ein: ")
                correct_format = False
                break

        return correct_format

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

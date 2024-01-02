from mastermind.controller.Computer import Computer
from mastermind.controller.Evaluator import Evaluator
from mastermind.controller.IGameManager import IGameManager
from mastermind.controller.Player import Player
from mastermind.model.Board import Board
from mastermind.model.Guess import Guess


class GameManager(IGameManager):
    PLAYER_GUESSER = 0
    COMPUTER_GUESSER = 1

    CREATOR = 2
    GUESSER = 3
    NONE = 4

    def __init__(self, ui, board_size, num_colors, num_rounds, player_role):
        """
        Initializes a GameManager object with the specified parameters.

        Args:
            ui: The user interface for displaying messages and game state.
            board_size (int): The size of the game board.
            num_colors (int): The number of colors available for each guess.
            num_rounds (int): The total number of rounds in the game.
            player_role (int): The role the player chose to play as.

        Returns:
                None
        """
        self.ui = ui

        self.currentRound = 1
        self.currentTurn = 0
        self.board = Board(board_size, num_colors, num_rounds)

        self.player_guess = None

        self.guessing_role = 0

        self.num_colors = num_colors
        self.board_size = board_size
        self.player_role = player_role
        self.game_over = False
        self.true_code = None

        self.evaluator = Evaluator()

    def start_game(self):
        """
        Starts the Mastermind game, prompting the user to choose a role and initializing players accordingly.

        Returns:
            None
        """
        player = Player(self.num_colors, self.board_size)
        computer = Computer(self.num_colors, self.board_size)

        if self.player_role == 1:
            self.player_guess = computer
            self.guessing_role = self.COMPUTER_GUESSER

            self.ui.display_message("Erstelle den Code: ")
            self.true_code = self.validate_code(player)
        elif self.player_role == 2:
            self.player_guess = player
            self.guessing_role = self.PLAYER_GUESSER

            self.ui.display_message("Der Computer erstellt den Code...")
            self.true_code = computer.create_code()
        else:
            self.ui.display_win_message("Etwas ist beim Setup-Prozess schief gelaufen. Spiel wird geschlossen.")
            exit()

        while not self.game_over:
            self.start_round()

    def start_round(self):
        """
        Starts a new round in the Mastermind game, handling the turn based on the current role.

        Returns:
                None
        """
        match self.guessing_role:
            case self.PLAYER_GUESSER:
                self.handle_player_guesser()
            case self.COMPUTER_GUESSER:
                self.handle_computer_guesser()
            case _:
                self.ui.display_win_message("Etwas ist beim Setup-Prozess schief gelaufen. Spiel wird geschlossen.")
                exit()

    def handle_player_guesser(self):
        """
        Handles the turn when the player is the guesser.

        Returns:
            None
        """
        self.ui.display_message(f"Bitte gib deinen Rateversuch für Runde {self.currentRound} ab: ")

        current_guess = self.validate_guess()
        black_pins, white_pins = self.evaluator.evaluate_guess(self.true_code, current_guess.copy())

        guess_with_pins = Guess(current_guess, (black_pins, white_pins))

        self.board.receive_guess(guess_with_pins)
        self.clean_up()

    def validate_guess(self):
        """
        Validates the player's guess for correctness.

        Returns:
            list: The validated guess made by the player.
        """
        validated = False
        current_guess = None

        while not validated:
            current_guess = self.player_guess.make_guess()
            validated = self.validate_input(current_guess)

        return current_guess

    def validate_code(self, player):
        """
        Validates the player's secret code for correctness.

        Args:
            player: The player object creating the secret code.

        Returns:
            list: The validated secret code created by the player.
        """
        validated = False
        current_code = None

        while not validated:
            current_code = player.create_code()
            validated = self.validate_input(current_code)

        return current_code

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
            if not 1 <= color <= self.num_colors:
                self.ui.display_message(f"Ungültige Eingabe. Geben sie den Code erneut ein: ")
                correct_format = False
                break

        return correct_format

    def handle_computer_guesser(self):
        """
        Handles the turn when the computer is the guesser.

        Returns:
            None
        """
        current_guess = self.player_guess.make_guess()

        black_pins, white_pins = self.evaluator.evaluate_guess(self.true_code, current_guess.copy())
        guess_with_pins = Guess(current_guess, (black_pins, white_pins))

        self.board.receive_guess(guess_with_pins)
        self.player_guess.receive_feedback(guess_with_pins)

        self.clean_up()

    def clean_up(self):
        """
        Cleans up after a turn, displaying the game state and checking if the game is over.

        Returns:
            None
        """
        self.ui.display_game_state(self.board)

        winner = self.check_game_over()

        if winner != self.NONE:
            win_message = "Der Codierer hat gewonnen!" if winner == self.CREATOR else "Der Rater hat gewonnen!"
            win_message += "\nDer Farbcode war: " + str(self.true_code)
            self.ui.display_win_message(win_message)

            self.ui.display_message("Danke für's Spielen!")
            self.game_over = True

        self.currentRound += 1

    def check_game_over(self):
        """
        Checks if the game is over based on the current round and the correctness of the last guess.

        Returns:
            int: The winner identifier (CREATOR, GUESSER, NONE).
        """
        last_guess = self.player_guess.get_latest_guess()
        player_code = self.true_code
        if last_guess == player_code:
            return self.GUESSER
        elif self.currentRound >= self.board.get_num_rounds():
            return self.CREATOR
        else:
            return self.NONE

from abc import ABC, abstractmethod

from mastermind.controller.Computer import Computer
from mastermind.controller.Evalutor import Evaluator
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

    def __init__(self, ui, board_size, num_colors, num_rounds):
        self.ui = ui

        self.currentRound = 1
        self.currentTurn = 0
        self.board = Board(board_size, num_colors, num_rounds)

        self.player_guess = None

        self.guessing_role = 0

        self.num_colors = num_colors
        self.board_size = board_size
        self.game_over = False
        self.true_code = None

        self.evaluator = Evaluator()

    def start_game(self):
        self.ui.display_message("1. Kodierer, 2. Rater: ")
        mode = input()

        player = Player(self.num_colors, self.board_size)
        computer = Computer(self.num_colors, self.board_size)

        if mode == "1":
            self.player_guess = computer
            self.guessing_role = self.COMPUTER_GUESSER

            self.ui.display_message("Erstelle den Code: ")
            self.true_code = self.validate_code(player)
        if mode == "2":
            self.player_guess = player
            self.guessing_role = self.PLAYER_GUESSER

            self.ui.display_message("Der Computer erstellt den Code...")
            self.true_code = computer.create_code()
        # TODO switch to pattern matching and add default

        while not self.game_over:
            self.start_round()

    def start_round(self):
        match self.guessing_role:
            case self.PLAYER_GUESSER:
                self.handle_player_guesser()
            case self.COMPUTER_GUESSER:
                self.handle_computer_guesser()
            case _:
                # TODO Error handling
                pass

    def handle_player_guesser(self):
        self.ui.display_message(f"Bitte gib deinen Rateversuch für Runde {self.currentRound} ab: ")

        current_guess = self.validate_guess()
        black_pins, white_pins = self.evaluator.evaluate_guess(self.true_code, current_guess.copy())

        guess_with_pins = Guess(current_guess, (black_pins, white_pins))

        self.board.receive_guess(guess_with_pins)
        self.clean_up()

    def validate_guess(self):
        validated = False
        current_guess = None

        while not validated:
            current_guess = self.player_guess.make_guess()
            validated = self.validate_input(current_guess)

        return current_guess

    def validate_code(self, player):
        validated = False
        current_code = None

        while not validated:
            current_code = player.create_code()
            validated = self.validate_input(current_code)

        return current_code

    def handle_computer_guesser(self):
        current_guess = self.player_guess.make_guess()

        black_pins, white_pins = self.evaluator.evaluate_guess(self.true_code, current_guess.copy())
        guess_with_pins = Guess(current_guess, (black_pins, white_pins))

        self.board.receive_guess(guess_with_pins)
        self.player_guess.receive_feedback(guess_with_pins)

        self.clean_up()

    """
    def check_guess(self, current_guess):
        if len(current_guess) != self.num_slots:
            return False
        elif not current_guess.isdigit():
            return False
        elif any(int(digit) >= self.num_colors for digit in current_guess):
            return False
        else:
            correct_num_guesses = 0
            correct_num_colors = 0

            true_code_array = [int(digit) for digit in self.true_code]
            current_guess_array = [int(digit) for digit in current_guess]

            for i in range(len(true_code_array)):
                if true_code_array[i] == current_guess_array[i]:
                    correct_num_guesses += 1
                    true_code_array[i] = -1

            # Check for correct colors (correct_num_colors)
            for digit in true_code_array:
                if digit != -1 and digit in current_guess_array:
                    correct_num_colors += 1
                    current_guess_array.remove(digit)

            # Display results
            self.ui.display_message(f"Anzahl richtiger Farben an korrekter Position: {correct_num_guesses}")
            self.ui.display_message(f"Anzahl richtiger Farben an falscher Position: {correct_num_colors}")

            return True

    """

    def clean_up(self):
        # TODO display Board

        self.ui.display_game_state(self.board)

        winner = self.check_game_over()

        if winner != self.NONE:
            win_message = "Der Codierer hat gewonnen!" if winner == self.CREATOR else "Der Rater hat gewonnen"
            win_message += "\nDer Farbcode war: " + str(self.true_code)  # TODO Farbcode anzeigen
            self.ui.display_win_message(win_message)

            self.ui.display_message("Thanks for playing!")
            self.game_over = True

        self.currentRound += 1

    def check_game_over(self):
        if self.currentRound >= self.board.get_num_rounds():
            # CREATOR hat gewonnen
            return self.CREATOR
        else:
            last_guess = self.player_guess.get_latest_guess()
            player_code = self.true_code

            if last_guess == player_code:
                # GUESSER hat gewonnen
                return self.GUESSER
        return self.NONE

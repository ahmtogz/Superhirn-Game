from abc import ABC, abstractmethod


class IGameManager(ABC):

    def validate_guess(self):
        while True:
            current_guess = self.player_guess.make_guess()
            correct_format = True

            for color in current_guess:
                if not 1 <= color <= self.num_colors:
                    self.ui.display_message(f"Ungültige Eingabe. Geben sie den Code erneut ein: ")
                    correct_format = False
                    break

            if correct_format:
                break
        return current_guess
    @abstractmethod
    def check_game_over(self):
        pass
    @abstractmethod
    def start_game(self):
        pass
    @abstractmethod
    def start_round(self):
        pass

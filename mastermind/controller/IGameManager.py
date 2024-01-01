from abc import ABC, abstractmethod


class IGameManager(ABC):

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



    @abstractmethod
    def check_game_over(self):
        pass

    @abstractmethod
    def start_game(self):
        pass

    @abstractmethod
    def start_round(self):
        pass

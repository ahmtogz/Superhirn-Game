from abc import ABC, abstractmethod


class IEvaluator(ABC):
    @abstractmethod
    def evaluate_guess(self, code, guess):
        """
        Abstract method to evaluate a guess by comparing it to the secret code and providing feedback.

        Args:
            code (list): The secret code to be guessed.
            guess (list): The guess made by the player.

        Returns:
            tuple: A tuple containing the evaluation results, typically the number of black and white pins.
        """
        pass


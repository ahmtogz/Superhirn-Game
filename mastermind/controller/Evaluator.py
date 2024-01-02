from mastermind.controller.IEvaluator import IEvaluator


class Evaluator(IEvaluator):
    def evaluate_guess(self, code, guess):
        """
        Evaluates a guess by comparing it to the secret code and counting black and white pins.

        Args:
            code (list): The secret code to be guessed.
            guess (list): The guess made by the player.

        Returns:
            tuple: A tuple containing the number of black and white pins.
        """
        black_pins = 0
        white_pins = 0

        code_copy = code.copy()

        for i in range(len(code_copy)):
            if code_copy[i] == guess[i]:
                black_pins += 1
                code_copy[i] = -1
                guess[i] = -2

        for color in guess:
            if color in code_copy:
                code_copy.remove(color)
                white_pins += 1

        return black_pins, white_pins

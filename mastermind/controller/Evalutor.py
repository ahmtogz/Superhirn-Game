from mastermind.controller.IEvaluator import IEvaluator
from mastermind.model.Guess import Guess


class Evaluator(IEvaluator):
    def evaluate_guess(self, code, guess):
        black_pins = 0
        white_pins = 0

        code_copy = code.copy()

        for i in range(len(code_copy)):
            if code_copy[i] == guess[i]:
                black_pins += 1
                code_copy[i] = -1

        for color in guess:
            if color in code_copy:
                code_copy.remove(color)
                white_pins += 1

        return black_pins, white_pins




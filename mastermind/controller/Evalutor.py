from mastermind.controller.IEvaluator import IEvaluator
from mastermind.model.Guess import Guess


class Evaluator(IEvaluator):
    def evaluate_guess(self, code, guess):
        black_pins = 0
        white_pins = 0

        for i in range(len(code)):
            if code[i] == guess[i]:
                black_pins += 1
                guess[i] = -1

        for color in guess:
            if color in code:
                white_pins += 1

        return black_pins, white_pins




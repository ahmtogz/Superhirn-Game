import unittest
from mastermind.controller.Evaluator import Evaluator

class TestEvaluator(unittest.TestCase):
    def setUp(self):
        # Set up an Evaluator instance for testing
        self.evaluator = Evaluator()

    def test_evaluate_guess_correct_guess(self):
        """Test evaluate_guess with a correct guess."""
        code = [1, 2, 3, 4]
        guess = [1, 2, 3, 4]

        result = self.evaluator.evaluate_guess(code, guess)
        self.assertEqual(result, (4, 0))  # All pegs are correct, so 4 black pins and 0 white pins

    def test_evaluate_guess_partial_correct_guess(self):
        """Test evaluate_guess with a partially correct guess."""
        code = [1, 2, 3, 4]
        guess = [5, 2, 4, 6]

        result = self.evaluator.evaluate_guess(code, guess)
        self.assertEqual(result, (1, 1))  # 1 black pin (position 2) and 1 white pins (4)

    def test_evaluate_guess_wrong_guess(self):
        """Test evaluate_guess with a completely wrong guess."""
        code = [1, 2, 3, 4]
        guess = [5, 6, 7, 8]

        result = self.evaluator.evaluate_guess(code, guess)
        self.assertEqual(result, (0, 0))  # No pegs are correct

if __name__ == '__main__':
    unittest.main()

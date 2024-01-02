import unittest
from mastermind.model.Guess import Guess

class TestGuess(unittest.TestCase):
    """Test cases for the Guess class."""

    def setUp(self):
        """Set up common elements for testing."""
        # Setting up a sample guess
        self.sample_guess = Guess(guess=[1, 2, 3, 4], pins=(2, 1))

    def test_get_guess(self):
        """Test the get_guess method."""
        self.assertEqual(self.sample_guess.get_guess(), [1, 2, 3, 4])

    def test_get_pins(self):
        """Test the get_pins method."""
        self.assertEqual(self.sample_guess.get_pins(), (2, 1))

    def test_empty_guess(self):
        """Test with an empty guess."""
        empty_guess = Guess(guess=[], pins=(0, 0))
        self.assertEqual(empty_guess.get_guess(), [])
        self.assertEqual(empty_guess.get_pins(), (0, 0))

    def test_max_elements_guess(self):
        """Test with the maximum number of elements in the guess."""
        max_elements_guess = Guess(guess=[1, 2, 3, 4, 5, 6, 7, 8], pins=(0, 0))
        self.assertEqual(max_elements_guess.get_guess(), [1, 2, 3, 4, 5, 6, 7, 8])
        self.assertEqual(max_elements_guess.get_pins(), (0, 0))


if __name__ == '__main__':
    unittest.main()

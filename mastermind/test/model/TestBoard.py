import unittest
from mastermind.model.Board import Board, Guess

class TestBoard(unittest.TestCase):


    def setUp(self):
        """Set up common elements for testing."""
        # Setting up a Board instance for testing
        self.board = Board(board_size=4, num_colors=6, num_rounds=10)
        # Setting up a sample player code
        self.player_code = [1, 2, 3, 4]
        # Setting up a sample guess
        self.sample_guess = Guess(guess=[5, 3, 2, 1], pins=(2, 1))

    def test_get_player_code(self):
        """Test the get_player_code method."""
        self.board.set_player_code(self.player_code)
        self.assertEqual(self.board.get_player_code(), self.player_code)

    def test_get_num_rounds(self):
        """Test the get_num_rounds method."""
        self.assertEqual(self.board.get_num_rounds(), 10)

    def test_receive_guess(self):
        """Test the receive_guess method."""
        self.board.receive_guess(self.sample_guess)
        self.assertEqual(len(self.board.get_all_guesses()), 1)

    def test_get_all_guesses(self):
        """Test the get_all_guesses method."""
        self.board.receive_guess(self.sample_guess)
        guesses = self.board.get_all_guesses()
        self.assertIsInstance(guesses, list)
        self.assertEqual(len(guesses), 1)
        self.assertIsInstance(guesses[0], Guess)

    def test_get_guess_for_round(self):
        """Test the get_guess_for_round method."""
        self.board.receive_guess(self.sample_guess)
        retrieved_guess = self.board.get_guess_for_round(0)
        self.assertIsInstance(retrieved_guess, Guess)
        self.assertEqual(retrieved_guess.get_guess(), [5, 3, 2, 1])
        self.assertEqual(retrieved_guess.get_pins(), (2, 1))

if __name__ == '__main__':
    unittest.main()

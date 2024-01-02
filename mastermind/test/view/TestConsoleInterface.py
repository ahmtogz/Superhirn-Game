import unittest
from unittest.mock import patch, MagicMock
from mastermind.model.Board import Board
from mastermind.model.Guess import Guess
from mastermind.view.ConsoleInterface import ConsoleInterface

class TestConsoleInterface(unittest.TestCase):

    def setUp(self):
        """Set up common elements for testing."""
        self.console_interface = ConsoleInterface()

    @patch('builtins.print')  # Mocking the print function
    def test_display_message(self, mock_print):
        """Test the display_message method."""
        message = "This is a test message"
        self.console_interface.display_message(message)
        mock_print.assert_called_with(message)

    @patch('builtins.print')  # Mocking the print function
    def test_display_win_message(self, mock_print):
        """Test the display_win_message method."""
        win_message = "Congratulations! You won!"
        self.console_interface.display_win_message(win_message)
        mock_print.assert_called_with(win_message)

    @patch('builtins.print')  # Mocking the print function
    def test_display_game_state_empty_board(self, mock_print):
        """Test the display_game_state method with an empty board."""
        board = Board(board_size=4, num_colors=6, num_rounds=10)
        self.console_interface.display_game_state(board)
        mock_print.assert_called_with('\n')


if __name__ == '__main__':
    unittest.main()

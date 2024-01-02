import unittest
from unittest.mock import patch
from mastermind.controller.InputHandler import InputHandler

class TestInputHandler(unittest.TestCase):
    @patch('builtins.input', side_effect=['1'])
    def test_get_game_mode_valid_input(self, mock_input):
        """Test get_game_mode method with valid input."""
        input_handler = InputHandler()
        result = input_handler.get_game_mode()
        self.assertEqual(result, 1)

    @patch('builtins.input', side_effect=['0', '3', '1'])
    def test_get_game_mode_invalid_then_valid_input(self, mock_input):
        """Test get_game_mode method with invalid then valid input."""
        input_handler = InputHandler()
        result = input_handler.get_game_mode()
        self.assertEqual(result, 1)

    @patch('builtins.input', side_effect=['a', '2'])
    def test_get_game_mode_invalid_then_valid_numeric_input(self, mock_input):
        """Test get_game_mode method with invalid non-numeric then valid numeric input."""
        input_handler = InputHandler()
        result = input_handler.get_game_mode()
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=['2'])
    def test_get_game_mode_valid_max_input(self, mock_input):
        """Test get_game_mode method with valid maximum input."""
        input_handler = InputHandler()
        result = input_handler.get_game_mode()
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=['5'])
    def test_get_color_valid_input(self, mock_input):
        """Test get_color method with valid input."""
        input_handler = InputHandler()
        result = input_handler.get_color(2, 8)
        self.assertEqual(result, 5)

    @patch('builtins.input', side_effect=['0', '9', '3'])
    def test_get_color_invalid_then_valid_input(self, mock_input):
        """Test get_color method with invalid then valid input."""
        input_handler = InputHandler()
        result = input_handler.get_color(2, 8)
        self.assertEqual(result, 3)

    @patch('builtins.input', side_effect=['a', '2'])
    def test_get_color_invalid_then_valid_numeric_input(self, mock_input):
        """Test get_color method with invalid non-numeric then valid numeric input."""
        input_handler = InputHandler()
        result = input_handler.get_color(2, 8)
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=['8'])
    def test_get_color_valid_max_input(self, mock_input):
        """Test get_color method with valid maximum input."""
        input_handler = InputHandler()
        result = input_handler.get_color(2, 8)
        self.assertEqual(result, 8)

    @patch('builtins.input', side_effect=['', 'Gamer123'])
    def test_get_gamer_id_invalid_then_valid_input(self, mock_input):
        """Test get_gamer_id method with invalid then valid input."""
        input_handler = InputHandler()
        result = input_handler.get_gamer_id()
        self.assertEqual(result, 'Gamer123')



    @patch('builtins.input', side_effect=['5'])
    def test_get_board_size_valid_input(self, mock_input):
        """Test get_board_size method with valid input."""
        input_handler = InputHandler()
        result = input_handler.get_board_size()
        self.assertEqual(result, 5)

    @patch('builtins.input', side_effect=['0', '6', '4'])
    def test_get_board_size_invalid_then_valid_input(self, mock_input):
        """Test get_board_size method with invalid then valid input."""
        input_handler = InputHandler()
        result = input_handler.get_board_size()
        self.assertEqual(result, 4)



    @patch('builtins.input', side_effect=['5'])
    def test_get_board_size_valid_max_input(self, mock_input):
        """Test get_board_size method with valid maximum input."""
        input_handler = InputHandler()
        result = input_handler.get_board_size()
        self.assertEqual(result, 5)

    @patch('builtins.input', side_effect=['1'])
    def test_get_player_role_valid_input(self, mock_input):
        """Test get_player_role method with valid input."""
        input_handler = InputHandler()
        result = input_handler.get_player_role()
        self.assertEqual(result, 1)

    @patch('builtins.input', side_effect=['0', '3', '2'])
    def test_get_player_role_invalid_then_valid_input(self, mock_input):
        """Test get_player_role method with invalid then valid input."""
        input_handler = InputHandler()
        result = input_handler.get_player_role()
        self.assertEqual(result, 2)

    @patch('builtins.input', side_effect=['a', '1'])
    def test_get_player_role_invalid_then_valid_numeric_input(self, mock_input):
        """Test get_player_role method with invalid non-numeric then valid numeric input."""
        input_handler = InputHandler()
        result = input_handler.get_player_role()
        self.assertEqual(result, 1)

    @patch('builtins.input', side_effect=['2'])
    def test_get_player_role_valid_max_input(self, mock_input):
        """Test get_player_role method with valid maximum input."""
        input_handler = InputHandler()
        result = input_handler.get_player_role()
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()

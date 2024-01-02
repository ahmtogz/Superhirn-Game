
import unittest
from unittest.mock import patch, MagicMock, Mock
from mastermind.controller.GameManager import GameManager
from mastermind.view.ConsoleInterface import ConsoleInterface

class TestGameManager(unittest.TestCase):
    @patch('builtins.input', side_effect=['1', '2', '3', '4'])
    def test_start_game_invalid_role_exit(self, mock_input):
        # Create a mock for the user interface
        ui_mock = Mock()

        # Instantiate GameManager with the mock UI
        game_manager = GameManager(ui_mock, board_size=4, num_colors=6, num_rounds=2, player_role=3)

        with self.assertRaises(SystemExit):
            game_manager.start_game()

    def test_start_round_player_guesser(self):
        game_manager = GameManager(self.ui_mock, board_size=4, num_colors=6, num_rounds=2, player_role=1)
        game_manager.handle_player_guesser = MagicMock()

        game_manager.start_round()

        game_manager.handle_player_guesser.assert_called_once()


    @patch('builtins.input', side_effect=['2'])
    def test_start_game_player_guesser(self, mock_input):
        """Test start_game when the player is the guesser."""
        ui = ConsoleInterface()
        board_size = 4
        num_colors = 6
        num_rounds = 10
        player_role = 2

        with patch('mastermind.controller.Computer.Computer.create_code', return_value=[1, 2, 3, 4]):
            with patch('mastermind.controller.Player.Player.make_guess', return_value=[4, 5, 2, 6]):
                game_manager = GameManager(ui, board_size, num_colors, num_rounds, player_role)
                game_manager.start_game()

        self.assertEqual(game_manager.currentRound, 11)  # Should play all rounds
        self.assertEqual(game_manager.game_over, True)  # Game should be over


    @patch('builtins.input', side_effect=['1'])
    def test_start_round_player_guesser(self, mock_input):
        """Test start_round when the player is the guesser."""
        ui = ConsoleInterface()
        board_size = 4
        num_colors = 6
        num_rounds = 10
        player_role = 2

        game_manager = GameManager(ui, board_size, num_colors, num_rounds, player_role)
        game_manager.handle_player_guesser = MagicMock()

        game_manager.start_round()

        game_manager.handle_player_guesser.assert_called_once()

    @patch('builtins.input', side_effect=['1'])
    def test_handle_player_guesser(self, mock_input):
        """Test handle_player_guesser method."""
        ui = ConsoleInterface()
        board_size = 4
        num_colors = 6
        num_rounds = 10
        player_role = 2

        game_manager = GameManager(ui, board_size, num_colors, num_rounds, player_role)
        game_manager.validate_guess = MagicMock(return_value=[1, 2, 3, 4])
        game_manager.evaluator.evaluate_guess = MagicMock(return_value=(4, 0))
        game_manager.clean_up = MagicMock()

        game_manager.handle_player_guesser()

        game_manager.validate_guess.assert_called_once()
        game_manager.evaluator.evaluate_guess.assert_called_once_with(game_manager.true_code, [1, 2, 3, 4])
        game_manager.clean_up.assert_called_once()

    @patch('builtins.input', side_effect=['1'])
    def test_validate_input_valid(self, mock_input):
        """Test validate_input with valid input."""
        ui = ConsoleInterface()
        board_size = 4
        num_colors = 6
        num_rounds = 10
        player_role = 2

        game_manager = GameManager(ui, board_size, num_colors, num_rounds, player_role)

        result = game_manager.validate_input([1, 2, 3, 4])
        self.assertTrue(result)  # Should be True for valid input

    @patch('builtins.input', side_effect=['1'])
    def test_validate_input_invalid(self, mock_input):
        """Test validate_input with invalid input."""
        ui = ConsoleInterface()
        board_size = 4
        num_colors = 6
        num_rounds = 10
        player_role = 2

        game_manager = GameManager(ui, board_size, num_colors, num_rounds, player_role)

        result = game_manager.validate_input([7, 2, 3, 4])
        self.assertFalse(result)  # Should be False for invalid input

if __name__ == '__main__':
    unittest.main()


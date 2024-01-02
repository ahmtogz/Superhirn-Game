import unittest
from unittest.mock import patch
from mastermind.controller.InputHandler import InputHandler
from mastermind.controller.Player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Set up a Player instance for testing
        self.player = Player(num_color=6, board_size=4)


    @patch('mastermind.controller.Player.InputHandler.get_color')
    def test_create_code(self, mock_get_color):
        # Mocking user input for create_code method
        mock_get_color.side_effect = [1, 5, 3, 2]
        result = self.player.create_code()
        self.assertEqual(result, [1, 5, 3, 2])

    @patch('mastermind.controller.Player.InputHandler.get_color')
    def test_make_guess(self, mock_get_color):
        # Mocking user input for make_guess method
        mock_get_color.side_effect = [4, 1, 7, 8]
        result = self.player.make_guess()
        self.assertEqual(result, [4, 1, 7, 8])

    @patch('mastermind.controller.Player.InputHandler.get_gamer_id')
    def test_create_gamer_id(self, mock_get_gamer_id):
        # Mocking user input for create_gamer_id method
        mock_get_gamer_id.return_value = "test_id"
        result = self.player.create_gamer_id()
        self.assertEqual(result, "test_id")

    @patch('mastermind.controller.Player.InputHandler.get_board_size')
    def test_create_board_size(self, mock_get_board_size):
        # Mocking user input for create_board_size method
        mock_get_board_size.return_value = 5
        result = self.player.create_board_size()
        self.assertEqual(result, 5)

    @patch('mastermind.controller.Player.InputHandler.get_color')
    def test_get_num_colors(self, mock_get_color):
        # Mocking user input for get_num_colors method
        mock_get_color.return_value = 3
        result = self.player.get_num_colors()
        self.assertEqual(result, 3)

    @patch('mastermind.controller.Player.InputHandler.get_color')
    def test_play(self, mock_get_color):
        # Mocking user input for play method
        mock_get_color.side_effect = [1, 5, 3, 4]
        result = self.player.play()
        self.assertEqual(result, [1, 5, 3, 4])

    def test_receive_feedback(self):
        # Test receive_feedback method (no actual behavior to test)
        self.player.receive_feedback([1, 5, 3, 2])  # No assertion, just ensure it doesn't raise an error

    def test_get_latest_guess(self):
        # Test get_latest_guess method
        self.player.current_guess = [4, 1, 6, 8]
        result = self.player.get_latest_guess()
        self.assertEqual(result, [4, 1, 6, 8])

if __name__ == '__main__':
    unittest.main()


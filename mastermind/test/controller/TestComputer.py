import unittest
from unittest.mock import patch, MagicMock
from mastermind.controller.Computer import Computer
from mastermind.controller.Evaluator import Evaluator
from mastermind.model.Guess import Guess

class TestComputer(unittest.TestCase):
    def setUp(self):
        # Set up a Computer instance for testing
        self.computer = Computer(num_colors=6, board_size=4)

    @patch('mastermind.controller.Computer.random.choice')
    def test_get_random_guess(self, mock_random_choice):
        """Test get_random_guess method."""
        # Mocking random.choice to always return [5, 2, 1, 4]
        mock_random_choice.return_value = [5, 2, 1, 4]
        result = self.computer.get_random_guess()
        self.assertEqual(result, [5, 2, 1, 4])

    @patch('mastermind.controller.Computer.random.choice')
    def test_make_guess_initial(self, mock_random_choice):
        """Test make_guess method with an initial guess."""
        # Mocking random.choice to always return [1, 2, 3, 4]
        mock_random_choice.return_value = [1, 2, 3, 4]
        result = self.computer.make_guess()
        self.assertEqual(result, [1, 2, 3, 4])
        self.assertEqual(self.computer.current_guess, [1, 2, 3, 4])

    @patch('mastermind.controller.Computer.random.choice')
    def test_make_guess_filtered_moves(self, mock_random_choice):
        """Test make_guess method with filtered moves."""
        # Set up initial state
        self.computer.all_feedbacks.append(Guess([1, 2, 3, 4], (2, 1)))
        self.computer.possible_moves = [[1, 2, 3, 4], [1, 2, 4, 3], [2, 1, 3, 4], [2, 1, 4, 3]]
        # Mocking random.choice to always return [1, 2, 4, 3]
        mock_random_choice.return_value = [1, 2, 4, 3]
        result = self.computer.make_guess()
        self.assertEqual(result, [1, 2, 4, 3])
        self.assertEqual(self.computer.current_guess, [1, 2, 4, 3])

    def test_generate_all_moves(self):
        """Test generate_all_moves method."""
        result = self.computer.generate_all_moves()
        self.assertEqual(len(result), 6**4)  # Check the number of combinations

    def test_filter_moves(self):
        """Test filter_moves method."""
        # Set up initial state
        self.computer.current_guess = [1, 2, 3, 4]
        self.computer.all_feedbacks.append(Guess([1, 2, 3, 4], (2, 1)))
        self.computer.possible_moves = [[1, 2, 3, 4], [1, 2, 4, 3], [2, 1, 3, 4], [2, 1, 4, 3]]
        self.computer.filter_moves()
        self.assertNotIn([1, 2, 3, 4], self.computer.possible_moves)


    def test_receive_feedback(self):
        """Test receive_feedback method."""
        # Set up initial state
        feedback = Guess([1, 2, 3, 4], (2, 1))
        self.computer.receive_feedback(feedback)
        self.assertEqual(self.computer.all_feedbacks, [feedback])

    def test_get_latest_guess(self):
        """Test get_latest_guess method."""
        # Set up initial state
        self.computer.current_guess = [1, 2, 3, 4]
        result = self.computer.get_latest_guess()
        self.assertEqual(result, [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()


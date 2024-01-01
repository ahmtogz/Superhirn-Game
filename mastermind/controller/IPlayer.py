from abc import ABC, abstractmethod

class IPlayer(ABC):
    """An abstract base class representing a player in the Mastermind game."""

    @abstractmethod
    def create_code(self):
        """
        Abstract method for creating and returning a secret code.

        Returns:
            list: The secret code created by the player.
        """
        pass

    @abstractmethod
    def make_guess(self):
        pass

    @abstractmethod
    def receive_feedback(self, guess_with_pins):
        """
        Abstract method for receiving and processing feedback for a guess.

        Args:
            guess_with_pins (tuple): A tuple containing a guess and corresponding feedback pins.

        Returns:
            None
        """
        pass

    def get_latest_guess(self):
        """
        Abstract method for getting the latest guess made by the player.

        Returns:
            list: The latest guess made by the player.
        """
        pass



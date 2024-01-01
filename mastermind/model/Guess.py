class Guess:
    def __init__(self, guess, pins):
        """
        Initializes a Guess object with the given guess and pins.

        Args:
            guess (list): The guess made by the player.
            pins (tuple): A tuple containing the number of black and white pins.

        Returns:
            None
        """
        self.guess = guess
        self.pins = pins

    def get_guess(self):
        """
        Gets the guess made by the player.

        Returns:
            list: The guess made by the player.
        """
        return self.guess

    def get_pins(self):
        """
        Gets the number of black and white pins for the guess.

        Returns:
            tuple: A tuple containing the number of black and white pins.
        """
        return self.pins

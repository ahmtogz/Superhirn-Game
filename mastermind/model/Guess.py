class Guess:
    def __init__(self, guess, pins):
        self.guess = guess
        self.pins = pins

    def get_guess(self):
        return self.guess

    def get_pins(self):
        return self.pins

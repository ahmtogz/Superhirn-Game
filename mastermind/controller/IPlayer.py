from abc import ABC, abstractmethod

class IPlayer(ABC):

    @abstractmethod
    def create_code(self):
        pass

    @abstractmethod
    def make_guess(self):
        pass

    @abstractmethod
    def receive_feedback(self, guess_with_pins):
        pass

    def get_latest_guess(self):
        pass



from abc import ABC, abstractmethod

class IPlayer(ABC):

    @abstractmethod
    def create_code(self):
        pass

    @abstractmethod
    def make_guess(self):
        pass

    @abstractmethod
    def receive_current_state(self, board):
        pass


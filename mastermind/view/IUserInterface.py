from abc import ABC, abstractmethod


class IUserInterface(ABC):
    @abstractmethod
    def display_win_message(self, message):
        pass

    @abstractmethod
    def display_game_state(self, board):
        pass

    @abstractmethod
    def display_message(self, message):
        pass

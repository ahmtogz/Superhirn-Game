from abc import ABC, abstractmethod


class IGameManager(ABC):

    @abstractmethod
    def check_game_over(self):
        pass

    @abstractmethod
    def start_game(self):
        pass

    @abstractmethod
    def start_round(self):
        pass

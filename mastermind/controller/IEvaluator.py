from abc import ABC, abstractmethod


class IEvaluator(ABC):
    @abstractmethod
    def evaluate_guess(self, code, guess):
        pass


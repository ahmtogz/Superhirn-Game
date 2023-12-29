from abc import ABC, abstractmethod


class INetworkReceiver(ABC):

    @abstractmethod
    def receive_eval(self):
        pass

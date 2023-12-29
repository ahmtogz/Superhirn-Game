from abc import ABC, abstractmethod


class INetworkSender(ABC):

    @abstractmethod
    def send(self, package):
        pass

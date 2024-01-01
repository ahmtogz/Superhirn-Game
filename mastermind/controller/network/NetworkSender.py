import requests
from requests import RequestException

from mastermind.controller.network.INetworkSender import INetworkSender
from mastermind.controller.network.Package import Package


class NetworkSender(INetworkSender):

    def __init__(self, ip, port):
        """
        Initializes a NetworkSender object with the specified IP address and port.

        Args:
            ip (str): The IP address for the network communication.
            port (int): The port for the network communication.

        Returns:
            None
        """
        self.ip = ip
        self.port = port

        self.url = "http://" + self.ip + ":" + str(self.port)

    def send(self, package):
        """
        Sends a network request with the provided package.

        Args:
            package (Package): The package to be sent.

        Returns:
            Package: The response package received from the network.
        """
        package_json = package.to_json()
        headers = {'Content-Type': 'application/json'}

        try:
            response = requests.post(self.url, data=package_json, headers=headers)
            if response.status_code == 200:
                return Package.from_json(response.json())

        except RequestException as e:
            print(e)

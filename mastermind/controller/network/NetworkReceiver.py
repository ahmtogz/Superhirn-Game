import json

from mastermind.controller.Evalutor import Evaluator
from mastermind.controller.network.INetworkReceiver import INetworkReceiver
from flask import app, Flask, request, jsonify

from mastermind.controller.network.NetworkGameManager import NetworkGameManager
from mastermind.controller.network.NetworkSender import NetworkSender
from mastermind.controller.network.Package import Package
from mastermind.view.ConsolteInterface import ConsoleInterface


class NetworkReceiver(INetworkReceiver):

    def __init__(self, ip, port, true_code):
        """
        Initializes a NetworkReceiver object.

        Args:
            ip (str): The IP address for the network communication.
            port (int): The port for the network communication.
            true_code (list): The true secret code for the game.

        Returns:
            None
        """
        self.game_id = 1

        self.evaluator = Evaluator()
        self.true_code = true_code

        self.ip = ip
        self.port = port


        self.url = "http://" + self.ip + ":" + str(self.port)
        self.app = Flask(__name__)

        self.app.add_url_rule("/evaluation", "receive_package", self.receive_eval, methods=["POST"])
        self.app.add_url_rule("/game/init", "receive_game_init", self.receive_init, methods=["POST"])

    def receive_eval(self):
        """
        Receives and processes a network request for evaluating a guess.

        Returns:
            tuple: A tuple containing the response package as a JSON-formatted string and the HTTP status code.
        """
        data = request.data
        package = Package.from_json(data)

        parsed_guess = self.parse_request_guess(package.value)

        evaluation = self.evaluator.evaluate_guess(self.true_code, parsed_guess)

        if evaluation is not None:
            response_package = Package(package.game_id, package.gamer_id,
                                       package.positions, package.colors, self.parse_guess_for_package(evaluation))

            return response_package.to_json(), 200

        else:
            response_package = Package(package.game_id, package.gamer_id,
                                       package.positions, package.colors, "")
            return response_package.to_json(), 200

    def receive_init(self):
        """
        Receives and processes a network request for initializing a game.

        Returns:
            tuple: A tuple containing the response package as a JSON-formatted string and the HTTP status code.
        """
        data = request.data
        package = Package.from_json(data)

        game_id = package.game_id

        response_package = Package(game_id, package.gamer_id, package.positions, package.colors, "")

        self.game_id += 1

        return response_package.to_json(), 200

    def start_server(self):
        """Starts the Flask server for handling network requests."""
        self.app.run(host=self.ip, port=self.port)

    def parse_request_guess(self, guess):
        """
        Parses the guess from the request package.

        Args:
            guess (str): The guess as a string from the request package.

        Returns:
            list: The parsed guess as a list of integers.
        """
        parsed_guess = []

        for color in guess:
            parsed_guess.append(int(color))

        return parsed_guess

    def parse_guess_for_package(self, guess):
        """
        Parses the guess for inclusion in the response package.

        Args:
            guess (list): The guess as a list of integers.

        Returns:
            str: The parsed guess as a string.
        """
        parsed_guess = ""

        for color in guess:
            parsed_guess += str(color)

        return parsed_guess

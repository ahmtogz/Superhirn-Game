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
        data = request.data
        package = Package.from_json(data)

        game_id = package.game_id

        response_package = Package(game_id, package.gamer_id, package.positions, package.colors, "")

        self.manager_dict[game_id] = NetworkGameManager(ConsoleInterface(), NetworkSender(self.ip, self.port))
        self.game_id += 1

        return response_package.to_json(), 200

    def start_server(self):
        self.app.run(host=self.ip, port=self.port)

    def parse_request_guess(self, guess):
        parsed_guess = []

        for color in guess:
            parsed_guess.append(int(color))

        return parsed_guess

    def parse_guess_for_package(self, guess):
        parsed_guess = ""

        for color in guess:
            parsed_guess += str(color)

        return parsed_guess

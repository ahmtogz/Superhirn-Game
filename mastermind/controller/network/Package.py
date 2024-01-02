import json


class Package:
    def __init__(self, game_id, gamer_id, positions, colors, value):
        """
        Initializes a Package object with the specified attributes.

        Args:
            game_id (int): The ID of a certain game. 0 if you want to start a new game.
            gamer_id (str): The ID (String) of the gamer. Freely selectable at the beginning of the game.
            positions (int): How many positions (>=1, <=9) does the pattern to be guessed have?. Selectable at the
            beginning of the game.
            colors (int): What is the maximum number of different colors (>=1, <=8) in the pattern to be guessed?.
            Selectable at the beginning of the game.
            value (str): Either the attempt to be evaluated (request to the server) or the evaluation (response from the
            server). Empty String at game start.

        Returns:
            None
        """
        self.game_id = game_id
        self.gamer_id = gamer_id
        self.positions = positions
        self.colors = colors
        self.value = value

    def to_json(self):
        """
        Converts the Package object to a JSON-formatted string.

        Returns:
            str: The JSON-formatted string representing the Package object.
        """
        package = {
            'game_id': self.game_id,
            'gamer_id': self.gamer_id,
            'positions': self.positions,
            'colors': self.colors,
            'value': self.value
        }

        return json.dumps(package)

    @staticmethod
    def from_json(package_json):
        """
        Creates a Package object from a JSON-formatted string.

        Args:
            package_json (str): The JSON-formatted string representing the Package object.

        Returns:
            Package: The Package object created from the JSON string.
        """
        package_data = json.loads(package_json)

        return Package(
            game_id=package_data["game_id"],
            gamer_id=package_data["gamer_id"],
            positions=package_data["positions"],
            colors=package_data["colors"],
            value=package_data["value"]
        )

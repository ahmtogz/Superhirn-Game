import json


class Package:
    def __init__(self, game_id, gamer_id, positions, colors, value):
        self.game_id = game_id
        self.gamer_id = gamer_id
        self.positions = positions
        self.colors = colors
        self.value = value

    def to_json(self):
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
        package_data = json.loads(package_json)

        return Package(
            game_id=package_data["game_id"],
            gamer_id=package_data["gamer_id"],
            positions=package_data["positions"],
            colors=package_data["colors"],
            value=package_data["value"]
        )

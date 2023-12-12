from mastermind.controller.IPlayer import IPlayer
from mastermind.controller.InputHandler import InputHandler


class Player(IPlayer):
    def init(self, board_size, role):
        self.handler = InputHandler()
        self.ROLE = role
        self.board_size = board_size
        self.current_guess = [0] * board_size

    def create_code(self):
        return [0] * self.board_size

    def make_guess(self):
        for i in range(self.board_size):
            self.current_guess[i] = self.handler.get_color()  # TODO: vielleicht andere Art und Weise, Inputs einzulesen
        return self.current_guess

    def receive_current_state(self, board):
        pass
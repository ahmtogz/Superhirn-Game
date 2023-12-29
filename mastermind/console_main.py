from mastermind.controller.GameManager import GameManager
from mastermind.controller.InputHandler import InputHandler
from mastermind.controller.network.NetworkGameManager import NetworkGameManager
from mastermind.controller.network.NetworkReceiver import NetworkReceiver
from mastermind.controller.network.NetworkSender import NetworkSender
from mastermind.view.ConsolteInterface import ConsoleInterface


class ConsoleMain:
    def __init__(self):
        self.game_manager = None
        self.ip = "0.0.0.0"
        self.port = 5000

    def start_game(self):
        print("Welcome to Superhirn")
        handler = InputHandler()
        num_rounds = 10

        game_mode = int(input("Wähle den Spielmodus: 1. Lokal, 2. Online: "))

        board_size = handler.get_board_size()
        num_colors = handler.get_color()

        match game_mode:
            case 1:
                game_manager = GameManager(ConsoleInterface(), board_size, num_colors, num_rounds)
                game_manager.start_game()

            case 2:
                game_manager = NetworkGameManager(ConsoleInterface(), NetworkSender(self.ip, self.port),
                                                  num_colors, board_size)

                true_code = game_manager.start_game()
                receiver = NetworkReceiver(self.ip, self.port, true_code)

                # TODO rework logic
                receiver.start_server()
                game_manager.init_game()

    """           
    def start(self):
        while True:
            try:
                mode = int(input("Wähle einen Spielmodus (1 Lokales Spiel vs. Computer, 2 Internetspiel vs. Mensch): "))
                if mode == 1:
                    self.players.append(Player(self.num_slots, self.GUESSER))
                    self.players.append(Computer(self.CREATOR, self.num_colors, self.num_slots))
                    self.true_code = self.players[1].createCode
                    break
                elif mode == 2:
                    self.players.append(Player())
                    self.players.append(Player())
                    break
                else:
                    self.ui.display_message("Ungültige Eingabe. Bitte versuche es erneut.")
            except ValueError:
                self.ui.display_message("Ungültige Eingabe. Bitte gib eine Zahl ein.")

        while True:
            try:
                self.num_colors = int(input("Wähle die Anzahl an Farben (mindestens 2, höchstens 8"))
                if 1 < self.num_colors < 9:
                    break
                else:
                    self.ui.display_message("Ungültige Eingabe. Bitte gib eine Zahl zwischen 2 und 8 ein.")
            except ValueError:
                self.ui.display_message("Ungültige Eingabe. Bitte gib eine Zahl zwischen 2 und 8 ein.")

        while True:
            try:
                self.num_slots = int(input("Wähle die Anzahl der Stellen (4 oder 5): "))
                if self.num_slots in {4, 5}:
                    break
                else:
                    self.ui.display_message("Ungültige Eingabe. Bitte gib entweder 4 oder 5 ein.")
            except ValueError:
                self.ui.display_message("Invalid choice. Bitte gib entweder 4 oder 5 ein.")

        self.board = Board(self.num_slots, self.num_colors, 10)
        """


def main():
    console_main = ConsoleMain()
    console_main.start_game()


if __name__ == "__main__":
    main()

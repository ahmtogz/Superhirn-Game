import art

from mastermind.controller.GameManager import GameManager
from mastermind.controller.InputHandler import InputHandler
from mastermind.controller.network.NetworkGameManager import NetworkGameManager
from mastermind.controller.network.NetworkSender import NetworkSender
from mastermind.view.ConsoleInterface import ConsoleInterface
import socket


class ConsoleMain:
    def __init__(self):
        self.game_manager = None
        self.ip = "0.0.0.0"
        self.port = 5000

    def start_game(self):
        """Starts the Superhirn Mastermind game."""
        handler = InputHandler()
        num_rounds = 10
        min_color = 2
        max_color = 8

        game_mode = handler.get_game_mode()

        board_size = handler.get_board_size()
        num_colors = handler.get_color(min_color, max_color)

        match game_mode:
            case 1:
                player_role = handler.get_player_role()
                game_manager = GameManager(ConsoleInterface(), board_size, num_colors, num_rounds, player_role)
                game_manager.start_game()

            case 2:
                self.ip = socket.gethostbyname(socket.gethostname())
                game_manager = NetworkGameManager(ConsoleInterface(), NetworkSender(self.ip, self.port),
                                                  num_colors, board_size)

                game_manager.start_game()

    def play(self):
        while True:
            art.tprint("Wilkommen bei Superhirn!")
            print("\n----- Menü -----")
            print("1. Spiel starten")
            print("0. Spiel beenden")
            print("")
            choice = input("Wähle eine Option: ")

            if choice == "1":
                self.start_game()
            elif choice == "0":
                print("Spiel beendet. Auf Wiedersehen!")
                break
            else:
                print("Ungültige Eingabe. Bitte wähle eine gültige Option.")

def main():
    """The entry point of the Superhirn console application."""
    console_main = ConsoleMain()
    console_main.play()


if __name__ == "__main__":
    main()

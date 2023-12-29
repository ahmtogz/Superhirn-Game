class InputHandler:
    def get_color(self):
        while True:
            try:
                color_input = int(input("Bitte geben Sie eine Zahl für die Farbe ein (1-8): "))
                if color_input in range(1, 9):
                    return color_input
                else:
                    print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 8 eingeben.")
            except ValueError:
                print("Ungültige Eingabe. Bitte eine Zahl eingeben.")

    def get_gamer_id(self):
        while True:
            gamer_id_input = str(input("Bitte geben sie ihren Gamer Tag an: "))
            if gamer_id_input is not None and len(gamer_id_input) > 0:
                return gamer_id_input
            else:
                print("Ungültige Eingabe. Bitte geben sie einen nicht leeren Gamer Tag an")

    def get_board_size(self):
        try:
            board_size_input = int(input("Bitte geben Sie eine Zahl für die Länge der Rateversuche an (1-9): "))
            if board_size_input in range(1, 10):
                return board_size_input
            else:
                print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 9 eingeben.")
        except ValueError:
            print("Ungültige Eingabe. Bitte eine Zahl eingeben.")
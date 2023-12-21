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

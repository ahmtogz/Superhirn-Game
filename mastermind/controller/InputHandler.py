class InputHandler:
    """A class responsible for handling user input in the Mastermind game."""
    def get_color(self, min_color, max_color):
        """
        Gets a color input from the user within a specified range.

        Args:
            min_color (int): The minimum allowed color value.
            max_color (int): The maximum allowed color value.

        Returns:
            int: The selected color input from the user.
        """
        while True:
            try:
                color_input = int(input(
                    "Bitte geben Sie eine Zahl für die Farbe ein (" + str(min_color) + "-" + str(max_color) + "): "))
                if color_input in range(min_color, max_color + 1):
                    return color_input
                else:
                    print("Ungültige Eingabe. Bitte eine Zahl zwischen " + str(min_color) + " und " + str(
                        max_color) + " eingeben.")
            except ValueError:
                print("Ungültige Eingabe. Bitte eine Zahl eingeben.")

    def get_gamer_id(self):
        """
        Gets a gamer ID input from the user.

        Returns:
            str: The gamer ID input from the user.
        """
        while True:
            gamer_id_input = str(input("Bitte geben sie ihren Gamer Tag an: "))
            if gamer_id_input is not None and len(gamer_id_input) > 0:
                return gamer_id_input
            else:
                print("Ungültige Eingabe. Bitte geben sie einen nicht leeren Gamer Tag an")

    def get_board_size(self):
        """
        Gets the board size input from the user within a specified range.

        Returns:
            int: The selected board size input from the user.
        """
        min_size = 4
        max_size = 5

        while True:
            try:
                board_size_input = int(input(
                    "Bitte geben Sie eine Zahl für die Anzahl an Steckplätzen an (" + str(min_size) + "-" + str(
                        max_size) + "): "))
                if board_size_input in range(min_size, max_size + 1):
                    return board_size_input
                else:
                    print("Ungültige Eingabe. Bitte eine Zahl zwischen " + str(min_size) + " und " + str(
                        max_size) + " eingeben.")
            except ValueError:
                print("Ungültige Eingabe. Bitte eine Zahl eingeben.")

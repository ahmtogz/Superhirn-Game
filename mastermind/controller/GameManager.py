class GameManager:
    def __init__(self, ui):
        self.ui = ui
        self.CREATOR = 0
        self.GUESSER = 1
        self.NONE = 2
        self.currentRound = 0
        self.currentTurn = 0
        self.board = None
        self.players = []
        self.num_colors = None
        self.num_slots = None
        self.game_over = False
        self.true_code = None

    def start_game(self):
        while True:
            mode = input("Wähle einen Spielmodus (1 Lokales Spiel vs. Computer, 2 Internetspiel vs. Mensch): ")

            if mode == '1':
                self.players.append(Player())
                self.players.append(Computer())
                self.true_code = Computer.create_code()
                break
            elif mode == '2':
                self.players.append(Player())
                self.players.append(Player())
                break
            else:
                self.ui.display_message("Ungültige Eingabe. Bitter versuche es erneut.")
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
        while self.game_over == false:
            self.start_round()


    def start_round(self):
        if self.currentRound is None:
            self.currentRound = 1
        current_guess = input("Bitte gib deinen Rateversuch für Runde " + self.currentRound + " ab: ")
        self.check_guess(current_guess = current_guess)
        self.clean_up()

    def check_guess(self, current_guess):
        if len(current_guess) != self.board.get_num_slots():
            return False
        elif not current_guess.isdigit():
            return False
        elif any(int(digit) >= self.num_colors for digit in current_guess):
            return False
        else:
            correct_num_guesses = 0
            correct_num_colors = 0

            true_code_array = [int(digit) for digit in self.true_code]
            current_guess_array = [int(digit) for digit in current_guess]

            for i in range(len(true_code_array)):
                if true_code_array[i] == current_guess_array[i]:
                    correct_num_guesses += 1
                    true_code_array[i] = -1

            # Check for correct colors (correct_num_colors)
            for digit in true_code_array:
                if digit != -1 and digit in current_guess_array:
                    correct_num_colors += 1
                    current_guess_array.remove(digit)

            # Display results
            self.ui.display_message(f"Anzahl richtiger Farben an korrekter Position: {correct_num_guesses}")
            self.ui.display_message(f"Anzahl richtiger Farben an falscher Position: {correct_num_colors}")

            return True

    def clean_up(self):
        game_over = self.check_game_over()
        if game_over != self.NONE:
            win_message = "Der Codierer hat gewonnen!" if game_over == self.CREATOR else "Der Guesser hat gewonnen"
            self.ui.display_message(win_message)
            # TODO: Das Spiel beenden
            play_again = input("Willst du nochmal spielen? (j/n): ")
            if play_again.lower() == 'j':
                self.start_game()
            else:
                self.ui.display_message("Thanks for playing!")
                self.game_over = true
        self.currentRound += 1

    def check_game_over(self):
        if self.currentRound >= self.board.get_num_rounds():
            # CREATOR hat gewonnen
            return self.CREATOR
        else:
            last_guess = self.board.get_guess_for_round(self.currentRound)
            player_code = self.board.get_player_code()

            if last_guess.get_guess() == player_code:
                # GUESSER hat gewonnen
                return self.GUESSER
        return self.NONE


class IGameManager:
    def check_guess(self, current_guess):
        pass

    def check_game_over(self):
        pass

    def start_game(self):
        pass

    def start_round(self):
        pass

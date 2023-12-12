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

    def start_game(self):
        pass

    def start_round(self):
        pass

    def check_guess(self, current_guess):
        # TODO: Farbcode validieren - Überprüfen, ob der Spieler eine korrekte Eingabe gemacht hat
        # Beenden, wenn ein gültiger Tipp gemacht wurde
        while True:
            break
        self.clean_up()

    def clean_up(self):
        game_over = self.check_game_over()
        if game_over != self.NONE:
            win_message = "Der Codierer hat gewonnen!" if game_over == self.CREATOR else "Der Guesser hat gewonnen"
            self.ui.display_message(win_message)
            # TODO: Das Spiel beenden
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

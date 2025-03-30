from src.player import Player


class Game:

    def __init__(self) -> None:
        """
        Initializes the game with default values and starts the game loop.

        Returns:
            None
        """

        self.wind_of_the_round = "East"
        self.winds_advanced_count = 0
        self.current_round = 0
        self.players = {}

    def set_player(self, name: str) -> None:
        if len(self.players) == 0:
            wind = "East"
        elif len(self.players) == 1:
            wind = "South"
        elif len(self.players) == 2:
            wind = "West"
        elif len(self.players) == 3:
            wind = "North"
        else:
            raise ValueError("Cannot add more than 4 players.")

        self.players[name] = Player(name, wind)

    def score_game(self, winner: str) -> None:

        self.current_round += 1

        for name in self.players.keys():
            self.score_player(name, winner)

        for name in self.players.keys():
            self.players[name].round_score = 0

        if self.players[winner].wind != self.wind_of_the_round:
            self.advance_winds()

    def score_player(self, name: str, winner_name: str = False) -> None:
        """
        Scores an individual player.

        Parameters:
            name (str): the name of the player
            winner_name (str): the name of the winner

        Returns:
            None
        """

        round_score = self.players[name].round_score

        if name == winner_name:
            if self.players[name].wind == self.wind_of_the_round:
                self.players[name].points += round_score * 6
            else:
                self.players[name].points += round_score * 4

        else:
            for other_name in self.players.keys():
                if other_name == name:
                    continue

                if other_name == winner_name:
                    score_change = self.players[other_name].round_score * -1

                else:
                    score_change = (
                        self.players[name].round_score
                        - self.players[other_name].round_score
                    )

                if (
                    self.players[name].wind == self.wind_of_the_round
                    or self.players[other_name].wind == self.wind_of_the_round
                ):
                    score_change *= 2

                self.players[name].points += score_change

    def advance_winds(self):
        """
        Advances the winds for the next round.

        Returns:
            None
        """

        for name in self.players.keys():
            self.players[name].advance_wind()

        self.winds_advanced_count += 1
        if self.winds_advanced_count == 4:
            self.winds_advanced_count = 0
            self.advance_wind_of_the_round()
            print(self.wind_of_the_round)

    def advance_wind_of_the_round(self) -> None:
        """ "
        Advances the wind of the round to the next wind in the cycle.

        Returns:
            None
        """

        if self.wind_of_the_round == "East":
            self.wind_of_the_round = "South"
        elif self.wind_of_the_round == "South":
            self.wind_of_the_round = "West"
        elif self.wind_of_the_round == "West":
            self.wind_of_the_round = "North"
        elif self.wind_of_the_round == "North":
            self.wind_of_the_round = "East"

    def name_in_use(self, name: str) -> bool:
        """
        Checks if a name is already in use.

        Parameters:
            name (str): the name to check

        Returns:
            bool: True if the name is in use, False otherwise
        """

        return name in self.players.keys()

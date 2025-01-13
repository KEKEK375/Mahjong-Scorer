from src.player import Player
from src.utils.printing import Printing
from src.utils.sortingAlgorithms import SortingAlgorithms


class Game:
    """
    A class to represent a Mahjong game.

    ...

    Attributes
    ----------
    winds : dict
        a dictionary mapping player indices to wind directions
    wind_of_the_round : str
        the current wind of the round
    current_round : int
        the current round number
    wind_won : bool
        a flag indicating if the wind of the round won the round
    players : dict
        a dictionary of players in the game

    Methods
    -------
    __init__():
        Initializes the game and starts the game loop.
    run_game_loop() -> None:
        Runs the main game loop.
    set_players() -> dict:
        Prompts for player names and sets up the players.
    score_game() -> None:
        Scores the game for the current round.
    score_player(player: Player):
        Scores an individual player.
    display_scores():
        Displays the current scores of all players.
    display_info():
        Displays information about the current game state.
    reset_round():
        Resets the round state for all players.
    valid_name(name: str) -> bool:
        Checks if a given name is valid.
    get_players() -> dict:
        Returns the players in the game.
    get_player_names() -> list:
        Returns a list of player names.
    """

    def __init__(self) -> None:
        """
        Initializes the game with default values and starts the game loop.

        Returns:
            None
        """

        self.winds = {0: "East", 1: "South", 2: "West", 3: "North"}
        self.wind_of_the_round = self.winds[0]
        self.current_round = 0
        self.round_wind_lost = 0
        self.wind_won = False

    def set_players(self, player_names: list) -> dict:
        """
        Sets up the players with the given names.

        Parameters:
            player_names (list): A list of player names.

        Returns:
            dict: A dictionary mapping player indices to Player objects.
        """

        self.players = {}

        for i in range(4):
            self.players[i] = Player(player_names[i], self.winds[i])

        return self.players

    def score_game(self, winner: str, scores: list) -> None:
        """
        Scores the game for the current round.

        Returns:
            None
        """

        self.current_round += 1

        for i in range(4):
            self.players[i].round_score = int(scores[i])

            if self.players[i].name == winner:
                self.players[i].is_winner = True

        for i in range(4):
            self.score_player(self.players[i])

    def score_player(self, player: Player) -> None:
        """
        Scores an individual player.

        Parameters:
            player (Player): The player to score.

        Returns:
            None
        """

        if player.is_winner:
            if player.wind == self.wind_of_the_round:
                player.points += player.round_score * 6
                self.wind_won = True
            else:
                player.points += player.round_score * 4
        else:
            for other_player in self.players.values():
                if player.get_id() != other_player.get_id():
                    if other_player.is_winner:
                        score_change = other_player.round_score * -1
                    else:
                        score_change = player.round_score - other_player.round_score
                    if (
                        player.wind == self.wind_of_the_round
                        or other_player.wind == self.wind_of_the_round
                    ):
                        score_change = score_change * 2
                    player.points += score_change

    def get_names_and_scores(self) -> tuple[list, list]:
        """
        Displays the current scores of all players.

        Returns:
            None
        """

        player_list = []
        score_list = []
        for player in self.players.values():
            player_list.append(player.name)
            score_list.append(player.points)

        score_list, player_list = SortingAlgorithms.sort_scores(score_list, player_list)

        return player_list, score_list

    def get_scores(self) -> list:
        """
        Returns the current scores of all players.

        Returns:
            list: A list of strings representing the current scores of all players.
        """

        player_list = []
        score_list = []
        for player in self.players.values():
            player_list.append(player.name)
            score_list.append(player.points)

        score_list, player_list = SortingAlgorithms.sort_scores(score_list, player_list)

        scores = []
        for i in range(4):
            scores.append(f"{player_list[i]}:{score_list[i]}")

        return scores

    def get_info(self) -> list:
        """
        Returns information about the current game state.

        Returns:
            list: A list of strings representing the current game state.
        """

        info = []
        info.append(f"Round:{self.current_round}")
        for player in self.players.values():
            info.append(f"{player.name}:{player.wind}:{player.points}")

        return info

    def reset_round(self) -> None:
        """
        Resets the round state for all players.

        Returns:
            None
        """

        if not self.wind_won:
            self.rounds_wind_lost += 1
            if self.rounds_wind_lost == 4:
                for i in range(len(self.winds)):
                    if self.wind_of_the_round == self.winds[i]:
                        pos = i
                        break
                if pos == 3:
                    self.wind_of_the_round = self.winds[0]
                    print(f"wind: {self.wind_of_the_round}")
                else:
                    self.wind_of_the_round = self.winds[i + 1]
                    print(f"wind: {self.wind_of_the_round}")
                    

        for player in self.players.values():
            player.reset_after_round(self.wind_won)
        self.wind_won = False

    def valid_name(self, name: str) -> bool:
        """
        Checks if a given name is valid.

        Parameters:
            name (str): The name to check.

        Returns:
            bool: True if the name is in the list of player names, False otherwise.
        """

        return name in self.get_player_names()

    def get_players(self) -> list:
        """
        Returns the players in the game.

        Returns:
            list: A list of Player objects.
        """
        return self.players.values()

    def get_player_names(self) -> list:
        """
        Returns a list of player names.

        Returns:
            list: A list of player names.
        """

        names = []
        for player in self.get_players():
            names.append(player.name)

        return names

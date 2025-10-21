from src.game import Game
from src.utils.printing import Printing


class CLI:
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

        self.game = Game()
        self.run_game_loop()

    def run_game_loop(self) -> None:
        """
        Runs the main game loop. The loop will continue until the user chooses to quit.

        Returns:
            None
        """

        self.set_players()

        choice = ""

        while choice != "q":

            Printing.clear()
            print("Enter an option: ")
            print("- (s)tart next round")
            print("- (i)nformation about current game")
            print("- (q)uit")
            choice = input(">: ")

            Printing.clear()

            if choice.lower() == "s":
                self.score_game()
                Printing.clear()
                self.display_scores()

            elif choice.lower() == "i":
                self.display_info()

            elif choice.lower() == "q":
                pass

            else:
                print("Invalid option...")

    def set_players(self) -> None:
        """
        Prompts for player names and sets up the players.

        Returns:
            None
        """

        winds = ["East", "South", "West", "North"]
        for i in range(4):
            self.game.set_player(input(f"Enter {winds[i]} player's name: "))

    def score_game(self) -> None:
        """
        Scores the game for the current round.

        Returns:
            None
        """

        winner = input("Who won the round? ")
        while not self.valid_name(winner):
            winner = input("Invalid name, try again. Who won the round? ")

        for name in self.game.players.keys():
            score = int(input(f"What was {name}'s score: "))
            while type(score) != int or score < 0:
                score = input(f"Invalid score. What was {name}'s score: ")

            self.game.players[name].round_score = score

        self.game.score_game(winner)

    def display_scores(self) -> None:
        """
        Displays the current scores of all players.

        Returns:
            None
        """

        player_list = [name for name in self.game.players.keys()]
        score_list = [self.game.players[name].points for name in player_list]

        print("Current Scores:")
        for i in range(4):
            print(f"{player_list[i]}: {score_list[i]}")

        input("\nEnter to continue...")

    def display_info(self):
        """
        Displays information about the current game state.

        Returns:
            None
        """

        # =======================
        # | Round x             |
        # |---------------------|
        # | names   N1 N2 N3 N4 |
        # | wind    w1 w2 w3 w4 |
        # | points  p1 p1 p1 p1 |
        # =======================
        prefix = "| "
        suffix = " |"
        row_length = 16
        columns = []
        columns.append(["Names ", "Wind  ", "Points"])

        for player in self.game.players.values():
            column = [player.name, player.wind, str(player.points)]
            Printing.align_column(column)
            row_length += len(column[0])
            columns.append(column)

        round_row = "Round " + str(self.game.current_round)
        while len(round_row) < row_length - 2:
            round_row += " "

        ends = "=" * (row_length + 2)
        separator = "-" * row_length

        names_row = ""
        wind_row = ""
        points_row = ""
        for column in columns:
            names_row += column[0] + "  "
            wind_row += column[1] + "  "
            points_row += column[2] + "  "

        print(ends)
        print(prefix + round_row + suffix)
        print(prefix[0] + separator + suffix[1])
        print(prefix + names_row[0:-2] + suffix)
        print(prefix + wind_row[0:-2] + suffix)
        print(prefix + points_row[0:-2] + suffix)
        print(ends)
        input("\nEnter to continue...")

    def valid_name(self, name: str) -> bool:
        """
        Checks if a given name is valid.

        Parameters:
            name (str): The name to check.

        Returns:
            bool: True if the name is in the list of player names, False otherwise.
        """

        return self.game.name_in_use(name)

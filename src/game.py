from src.player import Player
from src.utils.printing import Printing
from src.utils.sortingAlgorithms import SortingAlgorithms

class Game:

    def __init__(self) -> None:
        self.winds = {0: "East", 1: "South", 2: "West", 3: "North"}
        self.wind_of_the_round = self.winds[0]
        self.current_round = 0
        self.wind_won = False
        self.run_game_loop()

    def run_game_loop(self):
        self.players = self.set_players()

        choice = ""

        while choice != "q":

            Printing.clear()
            print("Enter an option: ")
            print("- (s)tart next round")
            print("- (i)nformation about current game")
            print("- (q)uit")
            choice = input(">: ")

            Printing.clear()

            match choice.lower():
                case "s":
                    self.current_round += 1
                    self.score_game()
                    self.reset_round()
                    Printing.clear()
                    self.display_scores()

                case "i":
                    self.display_info()

                case "q":
                    pass

                case _:
                    print("Invalid option...")

    def set_players(self) -> dict:
        players = {}

        for i in range(4):
            player_name = input(f"({self.winds[i]}) Enter player {i +1}'s name: ")
            players[i] = Player(i, player_name, self.winds[i])

        return players

    def score_game(self) -> None:
        winner = input("Who won the round? ")
        while not self.valid_name(winner):
            winner = input("Invalid name, try again. Who won the round? ")

        for i in range(4):
            try:
                self.players[i].round_score = int(
                    input(f"What was {self.players[i].name}'s score: ")
                )
            except:
                raise Exception("Invalid score entered")

            if self.players[i].name == winner:
                self.players[i].is_winner = True

        for i in range(4):
            self.score_player(self.players[i])

    def score_player(self, player: Player) -> None:

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

    def display_scores(self) -> None:
        player_list = []
        score_list = []
        for player in self.players.values():
            player_list.append(player.name)
            score_list.append(player.points)

        score_list, player_list = SortingAlgorithms.sort_scores(score_list, player_list)

        for i in range(4):
            print("Current Scores:")
            print(f"{player_list[i]}: {score_list[i]}")

        input("\nEnter to continue...")

    def display_info(self):
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

        for player in self.players.values():
            column = [player.name, player.wind, str(player.points)]
            Printing.align_column(column)
            row_length += len(column[0])
            columns.append(column)

        round_row = "Round " + str(self.current_round)
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

    def reset_round(self):
        for player in self.players.values():
            player.reset_after_round(self.wind_won)
        self.wind_won = False

    def valid_name(self, name) -> bool:
        return name in self.get_player_names()

    def get_players(self) -> dict:
        return self.players.values()

    def get_player_names(self) -> list:
        names = []
        for player in self.get_players():
            names.append(player.name)

        return names
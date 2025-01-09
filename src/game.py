from src.player import Player
from src.utils.printing import Printing
from src.utils.sortingAlgorithms import SortingAlgorithms

class Game:

    def __init__(self) -> None:
        self.winds = {0: "East", 1: "South", 2: "West", 3: "North"}
        self.windOfTheRound = self.winds[0]
        self.currentRound = 0
        self.windWon = False
        self.runGameLoop()

    def runGameLoop(self):
        self.players = self.setPlayers()

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
                    self.currentRound += 1
                    self.scoreGame()
                    self.resetRound()
                    Printing.clear()
                    self.displayScores()

                case "i":
                    self.displayInfo()

                case "q":
                    pass

                case _:
                    print("Invalid option...")

    def setPlayers(self) -> dict:
        players = {}

        for i in range(4):
            playerName = input(f"({self.winds[i]}) Enter player {i +1}'s name: ")
            players[i] = Player(i, playerName, self.winds[i])

        return players

    def scoreGame(self) -> None:
        winner = input("Who won the round? ")
        while not self.validName(winner):
            winner = input("Invalid name, try again. Who won the round? ")

        for i in range(4):
            try:
                self.players[i].roundScore = int(
                    input(f"What was {self.players[i].name}'s score: ")
                )
            except:
                raise Exception("Invalid score entered")

            if self.players[i].name == winner:
                self.players[i].isWinner = True

        for i in range(4):
            self.scorePlayer(self.players[i])

    def scorePlayer(self, player: Player) -> None:

        if player.isWinner:
            if player.wind == self.windOfTheRound:
                player.points += player.roundScore * 6
                self.windWon = True
            else:
                player.points += player.roundScore * 4
        else:
            for otherPlayer in self.players.values():
                if player.getId() != otherPlayer.getId():
                    if otherPlayer.isWinner:
                        scoreChange = otherPlayer.roundScore * -1
                    else:
                        scoreChange = player.roundScore - otherPlayer.roundScore
                    if (
                        player.wind == self.windOfTheRound
                        or otherPlayer.wind == self.windOfTheRound
                    ):
                        scoreChange = scoreChange * 2
                    player.points += scoreChange

    def displayScores(self) -> None:
        playerList = []
        scoreList = []
        for player in self.players.values():
            playerList.append(player.name)
            scoreList.append(player.points)

        scoreList, playerList = SortingAlgorithms.sortScores(scoreList, playerList)

        for i in range(4):
            print("Current Scores:")
            print(f"{playerList[i]}: {scoreList[i]}")

        input("\nEnter to continue...")

    def displayInfo(self):
        # =======================
        # | Round x             |
        # |---------------------|
        # | names   N1 N2 N3 N4 |
        # | wind    w1 w2 w3 w4 |
        # | points  p1 p1 p1 p1 |
        # =======================
        prefix = "| "
        suffix = " |"
        rowLength = 16
        columns = []
        columns.append(["Names ", "Wind  ", "Points"])

        for player in self.players.values():
            column = [player.name, player.wind, str(player.points)]
            Printing.alignColumn(column)
            rowLength += len(column[0])
            columns.append(column)

        roundRow = "Round " + str(self.currentRound)
        while len(roundRow) < rowLength - 2:
            roundRow += " "

        ends = "=" * (rowLength + 2)
        separator = "-" * rowLength

        namesRow = ""
        windRow = ""
        pointsRow = ""
        for column in columns:
            namesRow += column[0] + "  "
            windRow += column[1] + "  "
            pointsRow += column[2] + "  "

        print(ends)
        print(prefix + roundRow + suffix)
        print(prefix[0] + separator + suffix[1])
        print(prefix + namesRow[0:-2] + suffix)
        print(prefix + windRow[0:-2] + suffix)
        print(prefix + pointsRow[0:-2] + suffix)
        print(ends)
        input("\nEnter to continue...")

    def resetRound(self):
        for player in self.players.values():
            player.resetAfterRound(self.windWon)
        self.windWon = False

    def validName(self, name) -> bool:
        return name in self.getPlayerNames()

    def getPlayers(self) -> dict:
        return self.players.values()

    def getPlayerNames(self) -> list:
        names = []
        for player in self.getPlayers():
            names.append(player.name)

        return names


if __name__ == "__main__":
    myGame = Game()

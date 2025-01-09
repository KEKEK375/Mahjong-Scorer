class Player:
    def __init__(self, id: int, name: str, wind: str, currentScore: int = 0):
        self.__id = id
        self.name = name
        self.wind = wind
        self.points = currentScore
        self.isWinner = False
        self.roundScore = 0

    def __repr__(self):
        return f"{self.name}. Currently {self.wind.lower()} wind. Current score: {str(self.points)}."

    def __str__(self):
        return self.name

    def resetAfterRound(self, windWon):
        self.isWinner = False
        self.roundScore = 0
        if not windWon:
            self.setWind(self.nextWind())

    def nextWind(self) -> str:
        match self.wind.lower():
            case "east":
                return "North"
            case "south":
                return "East"
            case "west":
                return "South"
            case "north":
                return "West"
            case _:
                if not self.isValidWind():
                    raise Exception(f"Invalid wind assigned: {self.wind}")

    def isValidWind(self, wind: str = None) -> bool:
        if not wind:
            wind = self.wind
        if not wind.lower() in ["east", "south", "west", "north"]:
            return False
        return True

    def setWind(self, wind: str):
        if self.isValidWind(wind):
            self.wind = wind
        else:
            raise Exception(f"Invalid wind provided: {wind}")

    def getId(self):
        return self.__id

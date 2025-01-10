class Player:
    def __init__(self, id: int, name: str, wind: str, current_score: int = 0):
        self.__id = id
        self.name = name
        self.wind = wind
        self.points = current_score
        self.is_winner = False
        self.round_score = 0

    def __repr__(self):
        return f"{self.name}. Currently {self.wind.lower()} wind. Current score: {str(self.points)}."

    def __str__(self):
        return self.name

    def reset_after_round(self, wind_won):
        self.is_winner = False
        self.round_score = 0
        if not wind_won:
            self.set_wind(self.next_wind())

    def next_wind(self) -> str:
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
                if not self.is_valid_wind():
                    raise Exception(f"Invalid wind assigned: {self.wind}")

    def is_valid_wind(self, wind: str = None) -> bool:
        if not wind:
            wind = self.wind
        if not wind.lower() in ["east", "south", "west", "north"]:
            return False
        return True

    def set_wind(self, wind: str):
        if self.is_valid_wind(wind):
            self.wind = wind
        else:
            raise Exception(f"Invalid wind provided: {wind}")

    def get_id(self):
        return self.__id

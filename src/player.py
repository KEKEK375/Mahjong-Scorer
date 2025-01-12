from itertools import count


class Player:
    """
    A class to represent a player in the game.

    ...

    Attributes
    ----------
    id : int
        a unique identifier for the player
    name : str
        the name of the player
    wind : str
        the wind of the player
    points : int
        the total points of the player
    is_winner : bool
        whether the player won the round
    round_score : int
        the score of the player for the current round

    Methods
    -------
    reset_after_round(wind_won: bool)
        Resets the player after a round.
    next_wind() -> str
        Returns the next wind of the player.
    is_valid_wind(wind: str) -> bool
        Checks if the wind is valid.
    set_wind(wind: str)
        Sets the wind of the player.
    get_id() -> int
        Returns the player's id.
    """

    _id = count()

    def __init__(self, name: str, wind: str, current_score: int = 0):
        """
        Initializes a player with the given id, name, wind, and current score.

        Parameters:
            name (str): the name of the player
            wind (str): the wind of the player
            current_score (int): the total points of the player

        Returns:
            None
        """

        self.__id = next(Player._id)
        self.name = name
        self.wind = wind
        self.points = current_score
        self.is_winner = False
        self.round_score = 0

    def __repr__(self) -> str:
        """
        Returns a string representation of the Player class.

        Returns:
            str: a string representation of the player
        """

        return f"{self.name}. Currently {self.wind.lower()} wind. Current score: {str(self.points)}."

    def __str__(self) -> str:
        """
        Returns the player's name.

        Returns:
            str: the name of the player
        """
        return self.name

    def reset_after_round(self, wind_won: bool) -> None:
        """
        Resets the player after a round.

        Parameters:
            wind_won (bool): whether the player won the round

        Returns:
            None
        """

        self.is_winner = False
        self.round_score = 0
        if not wind_won:
            self.set_wind(self.next_wind())

    def next_wind(self) -> str:
        """
        Returns the next wind the player will be assigned.

        Returns:
            str: the next wind the player will be assigned
        """

        if self.wind.lower() == "east":
            return "North"
        elif self.wind.lower() == "south":
            return "East"
        elif self.wind.lower() == "west":
            return "South"
        elif self.wind.lower() == "north":
            return "West"
        else:
            if not self.is_valid_wind():
                raise Exception(f"Invalid wind assigned: {self.wind}")

    def is_valid_wind(self, wind: str = None) -> bool:
        """
        Checks if the wind is valid.

        Parameters:
            wind (str): the wind to check

        Returns:
            bool: whether the wind is valid
        """

        if not wind:
            wind = self.wind
        if not wind.lower() in ["east", "south", "west", "north"]:
            return False
        return True

    def set_wind(self, wind: str):
        """
        Sets the wind of the player.

        Parameters:
            wind (str): the wind to set

        Returns:
            None
        """

        if self.is_valid_wind(wind):
            self.wind = wind
        else:
            raise Exception(f"Invalid wind provided: {wind}")

    def get_id(self):
        """
        Returns the player's id.

        Returns:
            int: the player's id
        """

        return self.__id

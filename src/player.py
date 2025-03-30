class Player:

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
        self._name = name
        self._wind = wind
        self._points = current_score
        self._round_score = 0

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

    def advance_wind(self) -> None:
        """
        Advances the player's wind to the next wind in the cycle.

        Returns:
            None
        """

        if self.wind.lower() == "east":
            self.wind = "North"
        elif self.wind.lower() == "north":
            self.wind = "West"
        elif self.wind.lower() == "west":
            self.wind = "South"
        elif self.wind.lower() == "south":
            self.wind = "East"
        else:
            raise ValueError(f"Invalid wind value assigned to {self.name}: {self.wind}")

    @property
    def name(self) -> str:
        """
        Returns the player's name.

        Returns:
            str: the name of the player
        """

        return self._name

    @name.setter
    def name(self, name: str) -> None:
        """
        Sets the player's name.

        Parameters:
            name (str): the name of the player

        Returns:
            None
        """

        self._name = name

    @property
    def wind(self) -> str:
        """
        Returns the player's wind.

        Returns:
            str: the wind of the player
        """

        return self._wind

    @wind.setter
    def wind(self, wind: str) -> None:
        """
        Sets the player's wind.

        Parameters:
            wind (str): the wind of the player

        Returns:
            None
        """

        self._wind = wind

    @property
    def points(self) -> int:
        """
        Returns the player's points.

        Returns:
            int: the player's points
        """

        return self._points

    @points.setter
    def points(self, points: int) -> None:
        """
        Sets the player's score.

        Parameters:
            points (int): the player's points

        Returns:
            None
        """

        self._points = points

    @property
    def round_score(self) -> int:
        """
        Returns the player's round score.

        Returns:
            int: the round score of the player
        """

        return self._round_score

    @round_score.setter
    def round_score(self, score: int) -> None:
        """
        Sets the player's round score.

        Parameters:
            round_score (int): the round score of the player

        Returns:
            None
        """

        self._round_score = score

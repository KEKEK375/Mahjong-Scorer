class Tile:

    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} {self.suit}"

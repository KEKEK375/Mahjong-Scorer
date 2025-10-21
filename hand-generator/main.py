from random import randint
from Tile import Tile


class Generator:

    def __init__(self) -> None:
        self.flowers_num = 0
        self.deck, self.special, self.flowers = self.generate_tile_deck()

        key = ""
        while key != "q":
            self.hand = []
            print("\n" * 20)
            self.generate_hand()
            for tile in self.hand:
                print(tile)
            key = input("Next hand? ('q' to exit)")

    def generate_tile_deck(self):
        suits = ["Characters", "Sticks", "Circles"]
        values = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        deck = [
            Tile(suit, value) for suit in suits for value in values for i in range(4)
        ]

        winds = ["East", "South", "West", "North"]
        dragons = ["Red", "Green", "White"]

        special = []

        special_suits = ["Flower", "Season"]
        special_values = ["1", "2", "3", "4"]

        for i in range(4):
            for value in winds:
                special.append(Tile("Wind", value))
            for value in dragons:
                special.append(Tile("Dragon", value))

        flowers = [
            Tile(suit, value) for suit in special_suits for value in special_values
        ]

        return deck, special, flowers

    def generate_hand(self):
        hand_layout = self.generate_hand_layout()
        for set in hand_layout:
            match set:
                case "r":
                    self.generate_run()
                case "s":
                    self.generate_set(3)
                case "f":
                    self.generate_set(4)
                case "p":
                    self.generate_set(2)

            self.hand.append("")

        self.generate_flowers()

    def generate_hand_layout(self):
        sets = ["r", "r", "r", "r", "s", "s", "s", "s", "f"]
        hand_layout = ["p"]
        for i in range(4):
            set = randint(0, len(sets) - 1)
            hand_layout.append(sets[set])

        self.flowers_num = randint(0, 3)

        return hand_layout

    def generate_set(self, tile_num: int = 3) -> None:
        deck_type = randint(0, 7)
        if deck_type < 7:
            deck = self.deck
        else:
            deck = self.special

        tile = deck[randint(0, len(deck) - 1)]
        for i in range(tile_num):
            self.hand.append(tile)

    def generate_run(self) -> None:
        tile_pos = randint(0, len(self.deck) - 1)

        self.hand.append(self.deck[tile_pos])
        if self.deck[tile_pos].value != "9":
            self.hand.append(self.deck[tile_pos + 4])
            if self.deck[tile_pos].value != "1":
                self.hand.append(self.deck[tile_pos - 4])
            else:
                self.hand.append(self.deck[tile_pos + 8])
        else:
            self.hand.append(self.deck[tile_pos - 4])
            self.hand.append(self.deck[tile_pos - 8])

    def generate_flowers(self) -> None:
        for i in range(self.flowers_num):
            self.hand.append(self.flowers[randint(0, len(self.flowers) - 1)])


if __name__ == "__main__":
    gen = Generator()

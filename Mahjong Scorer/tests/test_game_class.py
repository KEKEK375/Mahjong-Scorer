from unittest import TestCase
from src.game import Game

from unittest.mock import patch


class TestPlayer(TestCase):
    def setUp(self):
        print("Setting up test environment...")
        self.test_game = Game()

    def tearDown(self):
        print("Tearing down test environment...")
        self.test_game = None

    def test_init(self):
        # Test
        self.assertEqual(self.test_game.wind_of_the_round, "East")
        self.assertEqual(self.test_game.winds_advanced_count, 0)
        self.assertEqual(self.test_game.current_round, 0)
        self.assertEqual(self.test_game.players, {})

    def test_set_player(self):
        # Execute
        self.test_game.set_player("test")

        # Test
        self.assertEqual(self.test_game.players["test"].name, "test")
        self.assertEqual(self.test_game.players["test"].wind, "East")

    def test_set_player_invalid(self):
        # Setup
        self.test_game.set_player("test1")
        self.test_game.set_player("test2")
        self.test_game.set_player("test3")
        self.test_game.set_player("test4")

        # Execute
        with self.assertRaises(ValueError) as context:
            self.test_game.set_player("test5")
        
        # Test
        self.assertEqual(str(context.exception), "Cannot add more than 4 players.")

    def test_score_game_wind_won(self):
        # Setup
        players = ["n1", "n2", "n3", "n4"]
        for i in range(4):
            self.test_game.set_player(players[i])

        winner = "n1"
        scores = [100, 10, 20, 30]

        for i, name in enumerate(players):
            self.test_game.players[name].round_score = scores[i]

        # Execute
        self.test_game.score_game(winner)

        # Test
        self.assertEqual(self.test_game.players["n1"].round_score, 0)
        self.assertEqual(self.test_game.players["n2"].round_score, 0)
        self.assertEqual(self.test_game.players["n3"].round_score, 0)
        self.assertEqual(self.test_game.players["n4"].round_score, 0)

        self.assertEqual(self.test_game.players["n1"].points, 600)
        self.assertEqual(self.test_game.players["n2"].points, -230)
        self.assertEqual(self.test_game.players["n3"].points, -200)
        self.assertEqual(self.test_game.players["n4"].points, -170)

        self.assertEqual(self.test_game.players["n1"].wind, "East")
        self.assertEqual(self.test_game.players["n2"].wind, "South")
        self.assertEqual(self.test_game.players["n3"].wind, "West")
        self.assertEqual(self.test_game.players["n4"].wind, "North")

    def test_score_game_wind_lost(self):
        # Setup
        players = ["n1", "n2", "n3", "n4"]
        for i in range(4):
            self.test_game.set_player(players[i])

        winner = "n2"
        scores = [32, 68, 16, 512]

        for i, name in enumerate(players):
            self.test_game.players[name].round_score = scores[i]

        # Execute
        self.test_game.score_game(winner)

        # Test
        self.assertEqual(self.test_game.players["n1"].round_score, 0)
        self.assertEqual(self.test_game.players["n2"].round_score, 0)
        self.assertEqual(self.test_game.players["n3"].round_score, 0)
        self.assertEqual(self.test_game.players["n4"].round_score, 0)

        self.assertEqual(self.test_game.players["n1"].points, -1064)
        self.assertEqual(self.test_game.players["n2"].points, 272)
        self.assertEqual(self.test_game.players["n3"].points, -596)
        self.assertEqual(self.test_game.players["n4"].points, 1388)

        self.assertEqual(self.test_game.players["n1"].wind, "North")
        self.assertEqual(self.test_game.players["n2"].wind, "East")
        self.assertEqual(self.test_game.players["n3"].wind, "South")
        self.assertEqual(self.test_game.players["n4"].wind, "West")

    def test_advance_winds(self):
        # Setup
        players = ["n1", "n2", "n3", "n4"]
        for i in range(4):
            self.test_game.set_player(players[i])

        # Execute & Test
        self.assertEqual(self.test_game.players["n1"].wind, "East")
        self.assertEqual(self.test_game.players["n2"].wind, "South")
        self.assertEqual(self.test_game.players["n3"].wind, "West")
        self.assertEqual(self.test_game.players["n4"].wind, "North")
        
        self.test_game.advance_winds()
        self.assertEqual(self.test_game.players["n1"].wind, "North")
        self.assertEqual(self.test_game.players["n2"].wind, "East")
        self.assertEqual(self.test_game.players["n3"].wind, "South")
        self.assertEqual(self.test_game.players["n4"].wind, "West")
        
        self.test_game.advance_winds()
        self.assertEqual(self.test_game.players["n1"].wind, "West")
        self.assertEqual(self.test_game.players["n2"].wind, "North")
        self.assertEqual(self.test_game.players["n3"].wind, "East")
        self.assertEqual(self.test_game.players["n4"].wind, "South")
        
        self.test_game.advance_winds()
        self.assertEqual(self.test_game.players["n1"].wind, "South")
        self.assertEqual(self.test_game.players["n2"].wind, "West")
        self.assertEqual(self.test_game.players["n3"].wind, "North")
        self.assertEqual(self.test_game.players["n4"].wind, "East")
        
        self.test_game.advance_winds()
        self.assertEqual(self.test_game.players["n1"].wind, "East")
        self.assertEqual(self.test_game.players["n2"].wind, "South")
        self.assertEqual(self.test_game.players["n3"].wind, "West")
        self.assertEqual(self.test_game.players["n4"].wind, "North")

    def test_advance_wind_of_the_round(self):
        # Setup
        self.test_game.wind_of_the_round = "East"

        # Execute & Test
        self.assertEqual(self.test_game.wind_of_the_round, "East")

        self.test_game.advance_wind_of_the_round()
        self.assertEqual(self.test_game.wind_of_the_round, "South")
        
        self.test_game.advance_wind_of_the_round()
        self.assertEqual(self.test_game.wind_of_the_round, "West")
        
        self.test_game.advance_wind_of_the_round()
        self.assertEqual(self.test_game.wind_of_the_round, "North")
        
        self.test_game.advance_wind_of_the_round()
        self.assertEqual(self.test_game.wind_of_the_round, "East")

    def test_name_in_use(self):
        # Setup
        self.test_game.set_player("test1")
        
        # Execute & Test
        self.assertTrue(self.test_game.name_in_use("test1"))
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
        self.assertEqual(self.test_game.winds, {0: "East", 1: "South", 2: "West", 3: "North"})
        self.assertEqual(self.test_game.wind_of_the_round, "East")
        self.assertEqual(self.test_game.current_round, 0)
        self.assertEqual(self.test_game.rounds_wind_lost, 0)
        self.assertFalse(self.test_game.wind_won, False)

    def test_set_players(self):
        # Setup
        players = ["n1", "n2", "n3", "n4"]
        
        # Execute
        self.test_game.set_players(players)

        # Test
        self.assertEqual(self.test_game.players[0].name, "n1")
        self.assertEqual(self.test_game.players[0].wind, "East")
        self.assertEqual(self.test_game.players[1].name, "n2")
        self.assertEqual(self.test_game.players[1].wind, "South")
        self.assertEqual(self.test_game.players[2].name, "n3")
        self.assertEqual(self.test_game.players[2].wind, "West")
        self.assertEqual(self.test_game.players[3].name, "n4")
        self.assertEqual(self.test_game.players[3].wind, "North")

    def test_score_game(self):
        # Setup
        players = ["n1", "n2", "n3", "n4"]
        self.test_game.set_players(players)
        
        winner = "n2"
        scores = [32, 68, 16, 512]

        # Execute
        self.test_game.score_game(winner, scores)

        # Test
        # self.assertEqual(self.test_game.players[0].points, -1064)
        # self.assertEqual(self.test_game.players[0].points, 272)
        # self.assertEqual(self.test_game.players[0].points, -596)
        # self.assertEqual(self.test_game.players[0].points, 1388)

        self.assertEqual(self.test_game.players[0].round_score, 32)
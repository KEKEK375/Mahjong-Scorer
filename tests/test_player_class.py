from unittest import TestCase
from src.player import Player

from unittest.mock import patch


class TestPlayer(TestCase):
    def setUp(self):
        print("Setting up test environment...")
        self.test_player = Player("test", "East", 0)

    def tearDown(self):
        print("Tearing down test environment...")
        self.test_player = None

    def test_init(self):
        # Test
        self.assertEqual(self.test_player.name, "test")
        self.assertEqual(self.test_player.wind, "East")
        self.assertEqual(self.test_player.points, 0)
        self.assertEqual(self.test_player.round_score, 0)

    def test_repr(self):
        # Setup
        print_string = "test. Currently east wind. Current score: 0."

        # Test
        self.assertEqual(repr(self.test_player), print_string)

    def test_str(self):
        self.assertEqual(str(self.test_player), "test")

    def test_advance_wind(self):
        # Setup
        self.test_player.wind = "East"

        # Test
        self.test_player.advance_wind()
        self.assertEqual(self.test_player.wind, "North")
        self.test_player.advance_wind()
        self.assertEqual(self.test_player.wind, "West")
        self.test_player.advance_wind()
        self.assertEqual(self.test_player.wind, "South")
        self.test_player.advance_wind()
        self.assertEqual(self.test_player.wind, "East")

    def test_advance_wind_invalid(self):
        # Setup
        self.test_player.wind = "InvalidWind"

        # Test
        with self.assertRaises(ValueError) as context:
            self.test_player.advance_wind()

        self.assertEqual(str(context.exception), "Invalid wind value assigned to test: InvalidWind")

    def test_name_property(self):
        # Setup
        self.test_player.name = "new_name"

        # Test
        self.assertEqual(self.test_player.name, "new_name")

    def test_wind_property(self):
        # Setup
        self.test_player.wind = "North"

        # Test
        self.assertEqual(self.test_player.wind, "North")

    def test_points_property(self):
        # Setup
        self.test_player.points = 10

        # Test
        self.assertEqual(self.test_player.points, 10)

    def test_round_score_property(self):
        # Setup
        self.test_player.round_score = 5

        # Test
        self.assertEqual(self.test_player.round_score, 5)
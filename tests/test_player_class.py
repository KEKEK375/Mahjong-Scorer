from unittest import TestCase
from src.player import Player

from unittest.mock import patch


class TestPlayer(TestCase):
    def setUp(self):
        print("Setting up test environment...")
        self.test_player = Player(0, "test", "East", 0)

    def tearDown(self):
        print("Tearing down test environment...")
        self.test_player = None

    def test_init(self):
        self.assertEqual(self.test_player.get_id(), 0)
        self.assertEqual(self.test_player.name, "test")
        self.assertEqual(self.test_player.wind, "East")
        self.assertEqual(self.test_player.points, 0)
        self.assertFalse(self.test_player.is_winner)
        self.assertEqual(self.test_player.round_score, 0)

    def test_repr(self):
        # Setup
        print_string = "test. Currently east wind. Current score: 0."
        self.assertEqual(repr(self.test_player), print_string)

    def test_str(self):
        self.assertEqual(str(self.test_player), "test")

    def test_reset_after_round_not_wind_won(self):
        # Setup
        self.test_player.is_winner = True
        self.test_player.round_score = 100
        self.assertEqual(self.test_player.wind, "East")

        # Execute
        self.test_player.reset_after_round(wind_won=False)

        # Test
        self.assertFalse(self.test_player.is_winner)
        self.assertEqual(self.test_player.round_score, 0)
        self.assertEqual(self.test_player.wind, "North")

    def test_reset_after_round_wind_won(self):
        # Setup
        self.test_player.is_winner = True
        self.test_player.round_score = 100
        self.assertEqual(self.test_player.wind, "East")

        # Execute
        self.test_player.reset_after_round(wind_won=True)

        # Test
        self.assertFalse(self.test_player.is_winner)
        self.assertEqual(self.test_player.round_score, 0)
        self.assertEqual(self.test_player.wind, "East")

    def test_next_wind_fails(self):
        # Setup
        self.test_player.wind = "invalid"

        # Execute
        with self.assertRaises(Exception) as context:
            self.test_player.next_wind()

        # Test
        self.assertEqual(str(context.exception), "Invalid wind assigned: invalid")

    def test_next_wind(self):
        # Setup
        self.assertEqual(self.test_player.wind, "East")

        # Execute and Test
        self.assertEqual(self.test_player.next_wind(), "North")
        self.test_player.wind = "North"
        self.assertEqual(self.test_player.next_wind(), "West")
        self.test_player.wind = "West"
        self.assertEqual(self.test_player.next_wind(), "South")
        self.test_player.wind = "South"
        self.assertEqual(self.test_player.next_wind(), "East")

    def test_is_valid_wind_no_wind_fails(self):
        # Setup
        self.test_player.wind = "invalid"

        # Execute and Test
        self.assertFalse(self.test_player.is_valid_wind())

    def test_is_valid_wind_no_wind(self):
        # Execute and Test
        self.assertTrue(self.test_player.is_valid_wind())

    def test_is_valid_wind_wind_fails(self):
        # Execute and Test
        self.assertFalse(self.test_player.is_valid_wind("invalid"))

    def test_is_valid_wind_wind(self):
        # Execute and Test
        self.assertTrue(self.test_player.is_valid_wind("South"))

    def test_set_wind_fails(self):
        # Execute
        with self.assertRaises(Exception) as context:
            self.test_player.set_wind("invalid")

        # Test
        self.assertEqual(str(context.exception), "Invalid wind provided: invalid")

    def test_set_wind(self):
        # Setup
        self.assertEqual(self.test_player.wind, "East")

        # Execute
        self.test_player.set_wind("South")

        # Test
        self.assertEqual(self.test_player.wind, "South")

    def test_get_id(self):
        # Execute and Test
        self.assertEqual(self.test_player.get_id(), 0)

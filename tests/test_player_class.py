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
        self.assertEqual(self.test_player.getId(), 0)
        self.assertEqual(self.test_player.name, "test")
        self.assertEqual(self.test_player.wind, "East")
        self.assertEqual(self.test_player.points, 0)
        self.assertFalse(self.test_player.isWinner)
        self.assertEqual(self.test_player.roundScore, 0)

    def test_repr(self):
        # Setup
        printString = "test. Currently east wind. Current score: 0."
        self.assertEqual(repr(self.test_player), printString)

    def test_str(self):
        self.assertEqual(str(self.test_player), "test")

    def test_resetAfterRound_not_windWon(self):
        # Setup
        self.test_player.isWinner = True
        self.test_player.roundScore = 100
        self.assertEqual(self.test_player.wind, "East")

        # Execute
        self.test_player.resetAfterRound(windWon=False)

        # Test
        self.assertFalse(self.test_player.isWinner)
        self.assertEqual(self.test_player.roundScore, 0)
        self.assertEqual(self.test_player.wind, "North")

    def test_resetAfterRound_windWon(self):
        # Setup
        self.test_player.isWinner = True
        self.test_player.roundScore = 100
        self.assertEqual(self.test_player.wind, "East")

        # Execute
        self.test_player.resetAfterRound(windWon=True)

        # Test
        self.assertFalse(self.test_player.isWinner)
        self.assertEqual(self.test_player.roundScore, 0)
        self.assertEqual(self.test_player.wind, "East")

    def test_nextWind_fails(self):
        # Setup
        self.test_player.wind = "invalid"

        # Execute
        with self.assertRaises(Exception) as context:
            self.test_player.nextWind()

        # Test
        self.assertEqual(str(context.exception), "Invalid wind assigned: invalid")

    def test_nextWind(self):
        # Setup
        self.assertEqual(self.test_player.wind, "East")

        # Execute and Test
        self.assertEqual(self.test_player.nextWind(), "North")
        self.test_player.wind = "North"
        self.assertEqual(self.test_player.nextWind(), "West")
        self.test_player.wind = "West"
        self.assertEqual(self.test_player.nextWind(), "South")
        self.test_player.wind = "South"
        self.assertEqual(self.test_player.nextWind(), "East")

    def test_isValidWind_no_wind_fails(self):
        # Setup
        self.test_player.wind = "invalid"

        # Execute and Test
        self.assertFalse(self.test_player.isValidWind())

    def test_isValidWind_no_wind(self):
        # Execute and Test
        self.assertTrue(self.test_player.isValidWind())

    def test_isValidWind_wind_fails(self):
        # Execute and Test
        self.assertFalse(self.test_player.isValidWind("invalid"))

    def test_isValidWind_wind(self):
        # Execute and Test
        self.assertTrue(self.test_player.isValidWind("South"))

    def test_setWind_fails(self):
        # Execute
        with self.assertRaises(Exception) as context:
            self.test_player.setWind("invalid")

        # Test
        self.assertEqual(str(context.exception), "Invalid wind provided: invalid")

    def test_setWind(self):
        # Setup
        self.assertEqual(self.test_player.wind, "East")

        # Execute
        self.test_player.setWind("South")

        # Test
        self.assertEqual(self.test_player.wind, "South")

    @patch("src.player.Player.getId")
    def test_try_mock(self, mock_get_id):
        # Setup
        mock_get_id.return_value = 16

        # Execute
        self.test_player.getId()

        # Test
        mock_get_id.assert_called()
        self.assertEqual(self.test_player.getId(), 16)

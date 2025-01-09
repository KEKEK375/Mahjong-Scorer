from unittest import TestCase
from unittest.mock import patch
from src.game import Game


class TestGame(TestCase):
    @patch("builtins.input")
    def test_game_loop_succeeds(self, mock_input):
        # mock_get_input.return_value = "mocked output"
        mock_input.side_effect = ["a", "a", "a", "a","q"]

        game = Game()

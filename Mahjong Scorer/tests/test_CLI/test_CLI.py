from unittest import TestCase
from unittest.mock import patch, call
from src.CLI.main import CLI


class TestGame(TestCase):
    def setUp(self):
        print("Setting up test environment...")

    def tearDown(self):
        print("Tearing down test environment...")

    @patch("builtins.input")
    @patch("builtins.print")
    def test_invalid_option(self, mock_print, mock_input):
        # Setup
        mock_input.side_effect = ["n1", "n2", "n3", "n4", "", "q"]

        # Execute
        game = Game()

        # Test
        expected_calls = [
            call("\n" * 20),
            call("Enter an option: "),
            call("- (s)tart next round"),
            call("- (i)nformation about current game"),
            call("- (q)uit"),
            call("\n" * 20),
            call("Invalid option..."),
        ]
        mock_print.assert_has_calls(expected_calls, any_order=False)

    @patch("builtins.input")
    def test_game_loop_quit(self, mock_input):
        mock_input.side_effect = ["n1", "n2", "n3", "n4", "q"]

        game = Game()

    @patch("builtins.input")
    def test_display_info(self, mock_input):
        mock_input.side_effect = ["n1", "n2", "n3", "n4", "i", "", "q"]

        game = Game()

    @patch("builtins.input")
    def test_score_round_wind_wins_valid_input(self, mock_input):
        mock_input.side_effect = [
            "n1",
            "n2",
            "n3",
            "n4",
            "s",
            "n1",
            "0",
            "0",
            "0",
            "0",
            "",
            "q",
        ]

        game = Game()

    @patch("builtins.input")
    def test_score_round_wind_loses_valid_input(self, mock_input):
        mock_input.side_effect = [
            "n1",
            "n2",
            "n3",
            "n4",
            "s",
            "n2",
            "0",
            "0",
            "0",
            "0",
            "",
            "q",
        ]

        game = Game()

    @patch("builtins.input")
    def test_score_round_invalid_name_valid_input(self, mock_input):
        mock_input.side_effect = [
            "n1",
            "n2",
            "n3",
            "n4",
            "s",
            "",
            "n2",
            "0",
            "0",
            "0",
            "0",
            "",
            "q",
        ]

        game = Game()

    @patch("builtins.input")
    def test_score_round_invalid_score(self, mock_input):
        mock_input.side_effect = ["n1", "n2", "n3", "n4", "s", "n2", "invalid"]

        with self.assertRaises(Exception) as context:
            game = Game()

        self.assertEqual(str(context.exception), "Invalid score entered")

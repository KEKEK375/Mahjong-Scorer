from unittest import TestCase
from unittest.mock import patch
from src.utils.printing import Printing


class TestPrinting(TestCase):
    def setUp(self):
        print("Setting up test environment...")

    def tearDown(self):
        print("Tearing down test environment...")

    @patch("builtins.print")
    def test_clear(self, mock_print):
        Printing.clear()
        mock_print.assert_called_with("\n" * 20)

    def test_align_columns_single_item_and_item(self):
        test_columns = [["test1"]]
        Printing.alignColumn(test_columns)

    def test_align_columns_asc(self):
        test_columns = ["test1", "test22", "test333"]
        Printing.alignColumn(test_columns)

    def test_align_columns_desc(self):
        test_columns = ["test333", "test22", "test1"]
        Printing.alignColumn(test_columns)

    def test_align_columns(self):
        test_columns = ["test1", "test2", "test3"]
        Printing.alignColumn(test_columns)

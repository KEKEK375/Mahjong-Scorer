from unittest import TestCase
from src.utils.sortingAlgorithms import SortingAlgorithms

class TryTesting(TestCase):
    def setUp(self):
        print("Setting up test environment...")

    def tearDown(self):
        print("Tearing down test environment...")
    
    def test_sort_scores_player_list_too_big(self):
        # Execute
        with self.assertRaises(Exception) as context:
            SortingAlgorithms.sortScores([1, 2, 3], [1, 2, 3, 4])
        
        # Test
        self.assertEqual(str(context.exception), "List of differing lengths provided.")
    
    def test_sort_scores_player_list_too_small(self):
        # Execute
        with self.assertRaises(Exception) as context:
            SortingAlgorithms.sortScores([1, 2, 3], [1, 2])
        
        # Test
        self.assertEqual(str(context.exception), "List of differing lengths provided.")

    def test_sort_scores_lists_empty(self):
        # Execute
        result = SortingAlgorithms.sortScores([], [])
        
        # Test
        self.assertEqual(result, ([], []))

    def test_sort_scores_lists_one_element(self):
        # Execute
        result = SortingAlgorithms.sortScores([1], [1])
        
        # Test
        self.assertEqual(result, ([1], [1]))

    def test_sort_scores(self):
        # Execute
        result = SortingAlgorithms.sortScores([3, 2, 1], ["C", "B", "A"])
        
        # Test
        self.assertEqual(result, ([1, 2, 3], ["A", "B", "C"]))
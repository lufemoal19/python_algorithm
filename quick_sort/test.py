import unittest
from quick_sort import quick_sort

class TestQuickSort(unittest.TestCase):
    def test_sort_positive_numbers(self):
        # Test sorting a list of positive numbers
        input_data = [9, 10, 54, 31, 0, 23, 5, 4, 10, 14, 2, 7, 90, 0, 2, 6, 67, 9]
        expected_output = sorted(input_data)  # Use Python's built-in sort function for comparison
        result = quick_sort(input_data)
        self.assertEqual(result, expected_output, "Failed to sort positive numbers")

    def test_sort_mixed_numbers(self):
        # Test sorting a list of mixed positive and negative numbers
        input_data = [-1, -2, -5, -9, -7, -6, -4, -3, -8, 0]
        expected_output = sorted(input_data)
        result = quick_sort(input_data)
        self.assertEqual(result, expected_output, "Failed to sort mixed numbers")

    def test_sort_duplicates(self):
        # Test sorting a list with duplicate elements
        input_data = [0, 1, 0, 1, 0, 1, 0, 0, 1, 0]
        expected_output = sorted(input_data)
        result = quick_sort(input_data)
        self.assertEqual(result, expected_output, "Failed to sort with duplicates")

    def test_sort_empty_list(self):
        # Test sorting an empty list
        input_data = []
        expected_output = []
        result = quick_sort(input_data)
        self.assertEqual(result, expected_output, "Failed to handle empty list")

    def test_sort_single_element_list(self):
        # Test sorting a list with a single element
        input_data = [42]
        expected_output = [42]
        result = quick_sort(input_data)
        self.assertEqual(result, expected_output, "Failed to handle single element list")

if __name__ == '__main__':
    unittest.main()

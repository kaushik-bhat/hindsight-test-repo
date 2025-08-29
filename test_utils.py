# hindsight-test-repo/test_utils.py
import unittest
from utils import calculate_average

class TestUtils(unittest.TestCase):
    def test_average_with_valid_list(self):
        """Tests the average function with a standard list of numbers. This should pass."""
        self.assertAlmostEqual(calculate_average([1, 2, 3, 4, 5]), 3.0)

    def test_average_with_empty_list(self):
        """
        Tests the average function with an empty list.
        This test will trigger a ZeroDivisionError and cause the build to fail.
        """
        calculate_average([])

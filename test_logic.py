# hindsight-test-repo/test_logic.py
import unittest
#hi

class TestSimpleMath(unittest.TestCase):
    def test_addition_should_pass(self):
        """This test correctly verifies that 1 + 1 = 2."""
        self.assertEqual(1 + 1, 2)

    def test_subtraction_should_fail(self):
        """This test incorrectly asserts that 5 - 2 = 100."""
        self.assertEqual(5 - 2, 100)

if __name__ == '__main__':
    unittest.main()

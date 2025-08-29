# hindsight-test-repo/test_example.py
import unittest

class TestDeliberateFailure(unittest.TestCase):
    def test_strings_should_not_match(self):
        """
        This test is designed to always fail for demonstration purposes.
        It asserts that two different strings are equal.
        """
        self.assertEqual("hello", "world", "This is an intentional test failure.")

if __name__ == '__main__':
    unittest.main()

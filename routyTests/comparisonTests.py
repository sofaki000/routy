import unittest
import math
from routy import Comparison


class ComparisonTestCase(unittest.TestCase):

    def setUp(self):
        self.comparison = Comparison()

    def test_function_call(self):
        """Test function call"""

        result = self.comparison.compare_short_routes(None, None)
        self.assertEqual(result, True)




if __name__ == '__main__':
    unittest.main()
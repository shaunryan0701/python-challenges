import unittest


def calculate_daily_return(open, close):
    return round((close / open - 1) * 100, 2)


class TestCalculateDailyReturn(unittest.TestCase):
    def test_positive_return(self):
        actual = calculate_daily_return(349.0, 360.0)
        expected = 3.15
        self.assertAlmostEqual(actual, expected)

    def test_negative_return(self):
        actual = calculate_daily_return(349.0, 340.0)
        expected = -2.58
        self.assertAlmostEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
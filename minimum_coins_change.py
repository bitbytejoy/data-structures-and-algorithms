def min_coins(change, coin_values):
    minimums = {}
    for sub_change in range(change + 1):
        minimum = sub_change
        for coin_value in [c for c in coin_values if c <= sub_change]:
            if minimums[sub_change - coin_value] + 1 < minimum:
                minimum = minimums[sub_change - coin_value] + 1
        minimums[sub_change] = minimum
    return minimums[change]

import unittest
class CoinsTest(unittest.TestCase):
    def test_coins(self):
        self.assertEqual(2, min_coins(50, [1, 5, 10, 25]))
        self.assertEqual(5, min_coins(53, [1, 5, 10, 25]))
        self.assertEqual(3, min_coins(63, [1, 5, 10, 21, 25]))

if __name__ == "__main__":
    unittest.main()

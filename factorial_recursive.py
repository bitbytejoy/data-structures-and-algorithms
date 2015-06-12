def factorial(number):
    if number < 0:
        raise NegativeNumberError()
    if number <= 1:
        return 1
    return number * factorial(number - 1)

class NegativeNumberError(Exception):
    pass

import unittest
class FactorialTest(unittest.TestCase):
    def test_factorial(self):
        with self.assertRaises(NegativeNumberError):
            factorial(-1)
        with self.assertRaises(NegativeNumberError):
            factorial(-100)
        self.assertEqual(1, factorial(0))
        self.assertEqual(1, factorial(1))
        self.assertEqual(2, factorial(2))
        self.assertEqual(6, factorial(3))
        self.assertEqual(24, factorial(4))
        self.assertEqual(120, factorial(5))

if __name__ == "__main__":
    unittest.main()

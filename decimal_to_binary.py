from stack import Stack

def non_negative_to_binary(decimal):
    if decimal < 0:
        raise NegativeNumberError()
    if decimal == 0:
        return "0"
    binary_digits = Stack()
    while decimal > 0:
        binary_digits.push(decimal % 2)
        decimal //= 2
    binary = ""
    while not binary_digits.is_empty():
        binary += str(binary_digits.pop())
    return binary

class NegativeNumberError(Exception):
    pass

import unittest
class ToBinaryTest(unittest.TestCase):
    def test_exception_when_negative(self):
        with self.assertRaises(NegativeNumberError):
            non_negative_to_binary(-1)
        with self.assertRaises(NegativeNumberError):
            non_negative_to_binary(-100)
    def test_positive_numbers(self):
        self.assertEqual("0", non_negative_to_binary(0))
        self.assertEqual("10", non_negative_to_binary(2))
        self.assertEqual("1001", non_negative_to_binary(9))

if __name__ == "__main__":
    unittest.main()

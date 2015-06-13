def fibonacci_recursive(n0, n1, elements_count):
    if elements_count <= 0:
        return [n1]
    new_element = [n1]
    elements_count -= 1
    if n0 == 0:
        new_element = [n0, n1]
        elements_count -= 2
    return new_element + fibonacci_recursive(n1, n0 + n1, elements_count)

import unittest
class FibonacciTest(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual([0, 1, 1], fibonacci_recursive(0, 1, 3))
        self.assertEqual([0, 1, 1, 2], fibonacci_recursive(0, 1, 4))
        self.assertEqual([0, 1, 1, 2, 3], fibonacci_recursive(0, 1, 5))
        self.assertEqual([0, 1, 1, 2, 3, 5], fibonacci_recursive(0, 1, 6))
        self.assertEqual([0, 1, 1, 2, 3, 5, 8], fibonacci_recursive(0, 1, 7))
        expected = [0, 1, 1, 2, 3, 5, 8, 13]
        self.assertEqual(expected, fibonacci_recursive(0, 1, len(expected)))
        expected = [
            0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987,
            1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393,
            196418, 317811
        ]
        self.assertEqual(expected, fibonacci_recursive(0, 1, len(expected)))

if __name__ == "__main__":
    unittest.main()

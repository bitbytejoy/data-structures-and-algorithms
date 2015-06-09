def sum_list(numbers_list):
    if len(numbers_list) == 0:
        return 0
    return numbers_list[0] + sum_list(numbers_list[1:])

import unittest
class ListSumTest(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(0, sum_list([]))
    def test_one_element_list(self):
        self.assertEqual(1, sum_list([1]))
    def test_multiple_elements_list(self):
        self.assertEqual(10, sum_list([1, 2, 3, 4]))

if __name__ == "__main__":
    unittest.main()

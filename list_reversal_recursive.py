def reverse_list_recursive(l):
    if len(l) == 0:
        return []
    if len(l) == 1:
        return l
    return [l[-1]] + reverse_list_recursive(l[:-1])

import unittest
class ListReversalTest(unittest.TestCase):
    def test_reverse_list(self):
        self.assertEqual([], reverse_list_recursive([]))
        self.assertEqual([1], reverse_list_recursive([1]))
        self.assertEqual([2, 1], reverse_list_recursive([1, 2]))
        self.assertEqual([3, 2, 1], reverse_list_recursive([1, 2, 3]))

if __name__ == "__main__":
    unittest.main()

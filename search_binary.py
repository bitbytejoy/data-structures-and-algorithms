def binary_search(some_list, item):
    if len(some_list) == 0:
        return False
    start = 0
    mid = len(some_list) // 2
    end = len(some_list) - 1
    while True:
        if some_list[mid] == item:
            return True
        if end - start < 0:
            return False
        if item < some_list[mid]:
            end = mid - 1
            mid = (end - start) // 2 + start
            continue
        if item > some_list[mid]:
            start = mid + 1
            mid = (end - start) // 2 + start
            continue

def binary_search_recursive(some_list, item, start = 0, end = None):
    if end is None:
        end = len(some_list) - 1
    if end - start < 0:
        return False
    mid = (end - start) // 2 + start
    if some_list[mid] == item:
        return True
    if item > some_list[mid]:
        return binary_search_recursive(some_list, item, mid + 1, end)
    if item < some_list[mid]:
        return binary_search_recursive(some_list, item, start, mid - 1)

import unittest
class SearchTest(unittest.TestCase):
    def test_binary_search(self):
        self.assertFalse(binary_search([], 1))
        self.assertFalse(binary_search([1, 2], 3))
        self.assertFalse(binary_search([1, 2], 0))
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 1))
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 2))
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 3))
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 4))
        self.assertTrue(binary_search([1, 2, 3, 4, 5], 5))
    def test_binary_search_recursive(self):
        self.assertFalse(binary_search_recursive([], 1))
        self.assertFalse(binary_search_recursive([1, 2], 3))
        self.assertFalse(binary_search_recursive([1, 2], 0))
        self.assertTrue(binary_search_recursive([1, 2, 3, 4, 5], 1))
        self.assertTrue(binary_search_recursive([1, 2, 3, 4, 5], 2))
        self.assertTrue(binary_search_recursive([1, 2, 3, 4, 5], 3))
        self.assertTrue(binary_search_recursive([1, 2, 3, 4, 5], 4))
        self.assertTrue(binary_search_recursive([1, 2, 3, 4, 5], 5))

if __name__ == "__main__":
    unittest.main()

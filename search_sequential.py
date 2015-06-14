def search(alist, item):
    for i in alist:
        if i == item:
            return True
    return False

def search_ordered_asc(ordered_list, item):
    for i in ordered_list:
        if i > item:
            return False
        if i == item:
            return True
    return False

import unittest
class SearchTest(unittest.TestCase):
    def test_search(self):
        self.assertFalse(search([], "a"))
        self.assertFalse(search(["a", "b"], "c"))
        self.assertTrue(search(["a", "b", "c"], "c"))
    def test_search_ordered_asc(self):
        self.assertFalse(search([], 1))
        self.assertFalse(search([2, 3], 1))
        self.assertTrue(search([1, 2, 3], 2))

if __name__ == "__main__":
    unittest.main()

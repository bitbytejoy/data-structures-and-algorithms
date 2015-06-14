def selection_sort(some_list):
    dest = len(some_list) - 1
    for i in range(len(some_list)):
        src = 0
        for j in range(dest + 1):
            if some_list[j] > some_list[src]:
                src = j
        some_list[src], some_list[dest] = some_list[dest], some_list[src]
        dest -= 1
    return some_list

import unittest
class SelectionSortTest(unittest.TestCase):
    def test_selection_sort(self):
        self.assertEqual([], selection_sort([]))
        self.assertEqual([1], selection_sort([1]))
        self.assertEqual([1, 2, 3, 4, 5], selection_sort([5, 3, 4, 1, 2]))

if __name__ == "__main__":
    unittest.main()

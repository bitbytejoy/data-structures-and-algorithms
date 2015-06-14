def bubble_sort(some_list):
    for i in range(1, len(some_list)):
        for j in range(1, len(some_list) - i + 1):
            if some_list[j - 1] > some_list[j]:
                some_list[j - 1], some_list[j] = some_list[j], some_list[j - 1]
    return some_list

def short_bubble_sort(some_list):
    is_sorted = False
    for i in range(1, len(some_list)):
        if is_sorted:
            break
        is_sorted = True
        for j in range(1, len(some_list) - i + 1):
            if some_list[j - 1] > some_list[j]:
                some_list[j - 1], some_list[j] = some_list[j], some_list[j - 1]
                is_sorted = False
    return some_list

import unittest
class BubbleSortTest(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual([], bubble_sort([]))
        self.assertEqual([1], bubble_sort([1]))
        self.assertEqual([1, 2, 3, 4, 5], bubble_sort([5, 3, 4, 1, 2]))
    def test_short_bubble_sort(self):
        self.assertEqual([], short_bubble_sort([]))
        self.assertEqual([1], short_bubble_sort([1]))
        self.assertEqual([1, 2, 3, 4, 5], short_bubble_sort([5, 3, 4, 1, 2]))

if __name__ == "__main__":
    unittest.main()

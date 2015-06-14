def insertion_sort(some_list):
    for i in range(1, len(some_list)):
        element = some_list[i]
        j = i
        while element < some_list[j - 1] and j > 0:
            some_list[j] = some_list[j - 1]
            j -= 1
        some_list[j] = element
    return some_list

import unittest
class InsertionSortTest(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual([], insertion_sort([]))
        self.assertEqual([1], insertion_sort([1]))
        self.assertEqual([1, 2, 3, 4, 5], insertion_sort([5, 3, 4, 1, 2]))

if __name__ == "__main__":
    unittest.main()

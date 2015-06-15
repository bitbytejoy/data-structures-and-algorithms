def quick_sort(li, start = 0, end = None):
    if end is None:
        end = len(li) - 1
    if end - start <= 0:
        return li
    pivot = start
    lcursor = start + 1
    rcursor = end
    while lcursor < rcursor + 1:
        if li[lcursor] <= li[pivot]:
            lcursor += 1
            continue
        if li[rcursor] > li[pivot]:
            rcursor -= 1
            continue
        li[lcursor], li[rcursor] = li[rcursor], li[lcursor]
    li[pivot], li[rcursor] = li[rcursor], li[pivot]
    quick_sort(li, start, rcursor - 1)
    quick_sort(li, rcursor + 1, end)
    return li

import unittest
class QuickSortTest(unittest.TestCase):
    def test_quick_sort(self):
        self.assertEqual([], quick_sort([]))
        self.assertEqual([1], quick_sort([1]))
        self.assertEqual([1, 2], quick_sort([2, 1]))
        self.assertEqual([1, 2, 3], quick_sort([3, 2, 1]))
        self.assertEqual([1, 2, 3, 4], quick_sort([3, 4, 2, 1]))
        self.assertEqual([1, 2, 3, 4, 5], quick_sort([5, 3, 4, 1, 2]))
        unsorted = [25, 99, 73, 11, 33, 95, 53, 33, 44, 91, 1, 15, 35]
        expected = [1, 11, 15, 25, 33, 33, 35, 44, 53, 73, 91, 95, 99]
        self.assertEqual(expected, quick_sort(unsorted))

if __name__ == "__main__":
    unittest.main()

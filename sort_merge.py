def merge_sort(some_list):
    if len(some_list) <= 1:
        return some_list
    list1 = merge_sort(some_list[:len(some_list) // 2])
    list2 = merge_sort(some_list[len(some_list) // 2:])
    merged = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    while i < len(list1):
        merged.append(list1[i])
        i += 1
    while j < len(list2):
        merged.append(list2[j])
        j += 1
    return merged

def merge_sort_optimized(some_list, start = 0, end = None):
    if end is None:
        end = len(some_list) - 1
    if end - start <= 0:
        return some_list
    mid = (end - start) // 2 + start
    merge_sort_optimized(some_list, start, mid)
    merge_sort_optimized(some_list, mid + 1, end)
    merged = []
    i = start
    j = mid + 1
    ith = some_list[i]
    while i <= mid and j <= end:
        if some_list[i] < some_list[j]:
            merged.append(some_list[i])
            i += 1
        else:
            merged.append(some_list[j])
            j += 1
    while i <= mid:
        merged.append(some_list[i])
        i += 1
    while j <= end:
        merged.append(some_list[j])
        j += 1
    k = start
    for e in merged:
        some_list[k] = e
        k += 1
    return some_list

import unittest
class MergeSortTest(unittest.TestCase):
    def test_merge_sort(self):
        self.assertEqual([], merge_sort([]))
        self.assertEqual([1], merge_sort([1]))
        self.assertEqual([1, 2, 3, 4, 5], merge_sort([5, 3, 4, 1, 2]))
        unsorted = [25, 99, 73, 11, 33, 95, 53, 33, 44, 91, 1, 15, 35]
        expected = [1, 11, 15, 25, 33, 33, 35, 44, 53, 73, 91, 95, 99]
        self.assertEqual(expected, merge_sort(unsorted))
    def test_merge_sort_optimized(self):
        self.assertEqual([], merge_sort_optimized([]))
        self.assertEqual([1], merge_sort_optimized([1]))
        self.assertEqual([1, 2, 3, 4, 5], merge_sort_optimized([5, 3, 4, 1, 2]))
        unsorted = [25, 99, 73, 11, 33, 95, 53, 33, 44, 91, 1, 15, 35]
        expected = [1, 11, 15, 25, 33, 33, 35, 44, 53, 73, 91, 95, 99]
        self.assertEqual(expected, merge_sort_optimized(unsorted))

if __name__ == "__main__":
    unittest.main()

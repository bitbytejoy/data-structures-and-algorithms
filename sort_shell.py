def shell_sort(some_list):
    sublists = len(some_list) // 2
    while sublists > 0:
        gap = sublists
        for i in range(sublists):
            position = i + gap
            while position < len(some_list):
                current = some_list[position]
                while position >= gap and some_list[position - gap] > current:
                    some_list[position] = some_list[position - gap]
                    position -= gap
                some_list[position] = current
                position += gap
        sublists //= 2
    return some_list

import unittest
class ShellSortTest(unittest.TestCase):
    def test_shell_sort(self):
        self.assertEqual([], shell_sort([]))
        self.assertEqual([1], shell_sort([1]))
        self.assertEqual([1, 2, 3, 4, 5], shell_sort([5, 3, 4, 1, 2]))
        unsorted = [25, 99, 73, 11, 33, 95, 53, 33, 44, 91, 1, 15, 35]
        expected = [1, 11, 15, 25, 33, 33, 35, 44, 53, 73, 91, 95, 99]
        self.assertEqual(expected, shell_sort(unsorted))

if __name__ == "__main__":
    unittest.main()

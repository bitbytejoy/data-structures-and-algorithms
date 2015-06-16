class BinaryHeap:
    def __init__(self):
        self.items = [0]
        self.items_count = 0
    def _swap_up(self, i):
        while i // 2 >= 1:
            parent = i // 2
            if self.items[parent] > self.items[i]:
                tmp = self.items[parent]
                self.items[parent] = self.items[i]
                self.items[i] = tmp
            else:
                break
            i = parent
    def insert(self, value):
        self.items.append(value)
        self.items_count += 1
        self._swap_up(self.items_count - 1)
    def _swap_down(self, i):
        while i * 2 <= self.items_count:
            child = i * 2
            min_child = self.items[i * 2]
            if (i * 2 + 1 <= self.items_count and
                self.items[i * 2 + 1] < min_child):
                child = i * 2 + 1
            if self.items[child] < self.items[i]:
                tmp = self.items[child]
                self.items[child] = self.items[i]
                self.items[i] = tmp
            else:
                break
            i = child
    def del_min(self):
        if self.items_count == 0:
            raise EmptyHeapError()
        deleted = self.items[1]
        self.items[1] = self.items[self.items_count]
        self.items.pop()
        self.items_count -= 1
        self._swap_down(1)
        return deleted
    def build_heap(self, some_list):
        self.items = [0] + some_list[:]
        self.items_count = len(some_list)
        for i in range(len(some_list) // 2, 0, -1):
            self._swap_down(i)

class EmptyHeapError(Exception):
    pass

import unittest
class BinaryHeapTest(unittest.TestCase):
    def test_binary_heap(self):
        # []
        h = BinaryHeap()
        with self.assertRaises(EmptyHeapError):
            h.del_min()
        # [1, 9, 15, 25]
        h.insert(15)
        h.insert(1)
        h.insert(25)
        h.insert(9)
        # [9, 15, 25] --> 1
        self.assertEqual(1, h.del_min())
        # [15, 25] --> 9
        self.assertEqual(9, h.del_min())
        # [25] --> 15
        self.assertEqual(15, h.del_min())
        # [] --> 25
        self.assertEqual(25, h.del_min())
        with self.assertRaises(EmptyHeapError):
            h.del_min()
        # [1, 25, 30, 99, 100]
        h.build_heap([99, 25, 100, 30, 1])
        # [25, 30, 99, 100] --> 1
        self.assertEqual(1, h.del_min())
        # [30, 99, 100] --> 25
        self.assertEqual(25, h.del_min())
        # [99, 100] --> 30
        self.assertEqual(30, h.del_min())
        # [100] --> 99
        self.assertEqual(99, h.del_min())
        # [] --> 100
        self.assertEqual(100, h.del_min())
        with self.assertRaises(EmptyHeapError):
            h.del_min()

if __name__ == "__main__":
    unittest.main()

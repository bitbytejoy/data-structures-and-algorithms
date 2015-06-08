class OrderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.items_count = 0
    def size(self):
        return self.items_count
    def is_empty(self):
        return self.size() == 0
    def index(self, item):
        if self.is_empty():
            return -1
        current = self.head
        i = 0
        while current is not None:
            if current["data"] == item:
                return i
            current = current["next"]
            i += 1
        return -1
    def contains(self, item):
        return self.index(item) != -1
    def add(self, item):
        node = {"data": item, "next": None}
        if self.is_empty():
            self.head = node
            self.tail = node
            self.items_count += 1
            return
        if self.contains(item):
            raise DuplicateItemError()
        if self.head["data"] > node["data"]:
            node["next"] = self.head
            self.head = node
            self.items_count += 1
            return
        if self.tail["data"] < node["data"]:
            self.tail["next"] = node
            self.tail = node
            self.items_count += 1
            return
        previous = self.head
        current = self.head["next"]
        while current is not None:
            if current["data"] > node["data"]:
                node["next"] = current
                previous["next"] = node
                self.items_count += 1
                return
            previous = current
            current = current["next"]
    def remove(self, item):
        if self.is_empty():
            return
        if self.size() == 1:
            self.head = None
            self.tail = None
            self.items_count = 0
            return
        if self.head["data"] == item:
            previous = self.head
            self.head = self.head["next"]
            previous["next"] = None
            self.items_count -= 1
            return
        if self.tail["data"] == item:
            pre_last = self.head
            while pre_last["next"] is not self.tail:
                pre_last = pre_last["next"]
            pre_last["next"] = None
            self.tail = pre_last
            self.items_count -= 1
            return
        previous = self.head
        current = self.head["next"]
        while current is not None:
            if current["data"] == item:
                previous["next"] = current["next"]
                current["next"] = None
                self.items_count -= 1
                return
            previous = current
            current = current["next"]
    def pop_at(self, position):
        if position < 0 or position > self.size() - 1:
            raise IndexOutOfBoundsError()
        if self.size() == 1:
            item = self.head["data"]
            self.head = None
            self.tail = None
            self.items_count -= 1
            return item
        if position == 0:
            first = self.head
            self.head = self.head["next"]
            first["next"] = None
            self.items_count -= 1
            return first["data"]
        if position == self.size() - 1:
            last = self.tail
            pre_last = self.head
            while pre_last["next"] is not self.tail:
                pre_last = pre_last["next"]
            pre_last["next"] = None
            self.tail = pre_last
            self.items_count -= 1
            return last["data"]
        previous = self.head
        current = self.head["next"]
        i = 1
        while current is not None:
            if i == position:
                previous["next"] = current["next"]
                current["next"] = None
                self.items_count -= 1
                return current["data"]
            previous = current
            current = current["next"]
    def pop(self):
        return self.pop_at(self.size() - 1)

class DuplicateItemError(Exception):
    pass

class IndexOutOfBoundsError(Exception):
    pass

import unittest
class OrderedListTest(unittest.TestCase):
    def test_ordered_list(self):
        # []
        l = OrderedList()
        self.assertEqual(0, l.size())
        self.assertTrue(l.is_empty())
        self.assertEqual(-1, l.index(1))
        self.assertFalse(l.contains(1))
        # [1]
        l.add(1)
        with self.assertRaises(DuplicateItemError):
            l.add(1)
        self.assertEqual(1, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(0, l.index(1))
        self.assertTrue(l.contains(1))
        # [0, 1]
        l.add(0)
        with self.assertRaises(DuplicateItemError):
            l.add(0)
        self.assertEqual(2, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(0, l.index(0))
        self.assertTrue(l.contains(0))
        self.assertEqual(1, l.index(1))
        self.assertTrue(l.contains(1))
        # [0, 1, 2]
        l.add(2)
        with self.assertRaises(DuplicateItemError):
            l.add(2)
        self.assertEqual(3, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(0, l.index(0))
        self.assertTrue(l.contains(0))
        self.assertEqual(1, l.index(1))
        self.assertTrue(l.contains(1))
        self.assertEqual(2, l.index(2))
        self.assertTrue(l.contains(2))
        # [-2, 0, 1, 2]
        l.add(-2)
        with self.assertRaises(DuplicateItemError):
            l.add(-2)
        self.assertEqual(4, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(0, l.index(-2))
        self.assertTrue(l.contains(-2))
        self.assertEqual(1, l.index(0))
        self.assertTrue(l.contains(0))
        self.assertEqual(2, l.index(1))
        self.assertTrue(l.contains(1))
        self.assertEqual(3, l.index(2))
        self.assertTrue(l.contains(2))
        # [-2, -1, 0, 1, 2]
        l.add(-1)
        with self.assertRaises(DuplicateItemError):
            l.add(-1)
        self.assertEqual(5, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(0, l.index(-2))
        self.assertTrue(l.contains(-2))
        self.assertEqual(1, l.index(-1))
        self.assertTrue(l.contains(-1))
        self.assertEqual(2, l.index(0))
        self.assertTrue(l.contains(0))
        self.assertEqual(3, l.index(1))
        self.assertTrue(l.contains(1))
        self.assertEqual(4, l.index(2))
        self.assertTrue(l.contains(2))
        # [-2, -1, 0, 1, 2, 4]
        l.add(4)
        with self.assertRaises(DuplicateItemError):
            l.add(4)
        self.assertEqual(6, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(0, l.index(-2))
        self.assertTrue(l.contains(-2))
        self.assertEqual(1, l.index(-1))
        self.assertTrue(l.contains(-1))
        self.assertEqual(2, l.index(0))
        self.assertTrue(l.contains(0))
        self.assertEqual(3, l.index(1))
        self.assertTrue(l.contains(1))
        self.assertEqual(4, l.index(2))
        self.assertTrue(l.contains(2))
        self.assertEqual(5, l.index(4))
        self.assertTrue(l.contains(4))
        # [-2, -1, 0, 1, 2, 3, 4]
        l.add(3)
        with self.assertRaises(DuplicateItemError):
            l.add(3)
        self.assertEqual(7, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(0, l.index(-2))
        self.assertTrue(l.contains(-2))
        self.assertEqual(1, l.index(-1))
        self.assertTrue(l.contains(-1))
        self.assertEqual(2, l.index(0))
        self.assertTrue(l.contains(0))
        self.assertEqual(3, l.index(1))
        self.assertTrue(l.contains(1))
        self.assertEqual(4, l.index(2))
        self.assertTrue(l.contains(2))
        self.assertEqual(5, l.index(3))
        self.assertTrue(l.contains(3))
        self.assertEqual(6, l.index(4))
        self.assertTrue(l.contains(4))
        # [-1, 0, 1, 2, 3, 4] Removed -2
        l.remove(-2)
        l.remove(-2) # Should do nothing
        self.assertEqual(6, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(-1, l.index(-2))
        self.assertFalse(l.contains(-2))
        self.assertEqual(0, l.index(-1))
        self.assertTrue(l.contains(-1))
        self.assertEqual(1, l.index(0))
        self.assertTrue(l.contains(0))
        self.assertEqual(2, l.index(1))
        self.assertTrue(l.contains(1))
        self.assertEqual(3, l.index(2))
        self.assertTrue(l.contains(2))
        self.assertEqual(4, l.index(3))
        self.assertTrue(l.contains(3))
        self.assertEqual(5, l.index(4))
        self.assertTrue(l.contains(4))
        # [-1, 0, 2, 3, 4] Removed 1
        l.remove(1)
        l.remove(1) # Should do nothing
        self.assertEqual(5, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(-1, l.index(1))
        self.assertFalse(l.contains(1))
        self.assertEqual(0, l.index(-1))
        self.assertTrue(l.contains(-1))
        self.assertEqual(1, l.index(0))
        self.assertTrue(l.contains(0))
        self.assertEqual(2, l.index(2))
        self.assertTrue(l.contains(2))
        self.assertEqual(3, l.index(3))
        self.assertTrue(l.contains(3))
        self.assertEqual(4, l.index(4))
        self.assertTrue(l.contains(4))
        # [-1, 0, 2, 3] Removed 4
        l.remove(4)
        l.remove(4) # Should do nothing
        self.assertEqual(4, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(-1, l.index(4))
        self.assertFalse(l.contains(4))
        self.assertEqual(0, l.index(-1))
        self.assertTrue(l.contains(-1))
        self.assertEqual(1, l.index(0))
        self.assertTrue(l.contains(0))
        self.assertEqual(2, l.index(2))
        self.assertTrue(l.contains(2))
        self.assertEqual(3, l.index(3))
        self.assertTrue(l.contains(3))
        # [0, 2, 3] Removed -1
        popped = l.pop_at(0)
        with self.assertRaises(IndexOutOfBoundsError):
            l.pop_at(3)
        self.assertEqual(3, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(-1, popped)
        self.assertEqual(-1, l.index(-1))
        self.assertFalse(l.contains(-1))
        self.assertEqual(0, l.index(0))
        self.assertTrue(l.contains(0))
        self.assertEqual(1, l.index(2))
        self.assertTrue(l.contains(2))
        self.assertEqual(2, l.index(3))
        self.assertTrue(l.contains(3))
        # [0, 3] Removed 2
        popped = l.pop_at(1)
        with self.assertRaises(IndexOutOfBoundsError):
            l.pop_at(2)
        self.assertEqual(2, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(2, popped)
        self.assertEqual(-1, l.index(2))
        self.assertFalse(l.contains(2))
        self.assertEqual(0, l.index(0))
        self.assertTrue(l.contains(0))
        self.assertEqual(1, l.index(3))
        self.assertTrue(l.contains(3))
        # [0] Removed 3
        popped = l.pop()
        self.assertEqual(1, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(3, popped)
        self.assertEqual(-1, l.index(3))
        self.assertFalse(l.contains(3))
        self.assertEqual(0, l.index(0))
        self.assertTrue(l.contains(0))
        # [] Removed 0
        popped = l.pop()
        self.assertEqual(0, l.size())
        self.assertTrue(l.is_empty())
        self.assertEqual(0, popped)
        self.assertEqual(-1, l.index(0))
        self.assertFalse(l.contains(0))
        with self.assertRaises(IndexOutOfBoundsError):
            l.pop()

if __name__ == "__main__":
    unittest.main()

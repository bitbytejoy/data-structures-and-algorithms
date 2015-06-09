class UnorderedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.items_count = 0
    def size(self):
        return self.items_count
    def is_empty(self):
        return self.size() == 0
    def index(self, item):
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
            self.items_count = 1
            return
        if self.contains(item):
            raise RepeatedElementError()
        node["next"] = self.head
        self.head = node
        self.items_count += 1
    def append(self, item):
        node = {"data": item, "next": None}
        if self.is_empty():
            self.head = node
            self.tail = node
            self.items_count = 1
            return
        if self.contains(item):
            raise RepeatedElementError()
        self.tail["next"] = node
        self.tail = node
        self.items_count += 1
    def insert(self, position, item):
        if position < 0 or position > self.size():
            raise IndexOutOfBoundsError()
        node = {"data": item, "next": None}
        if self.is_empty():
            self.head = node
            self.tail = node
            self.items_count = 1
            return
        if self.contains(item):
            raise RepeatedElementError()
        if position == 0:
            node["next"] = self.head
            self.head = node
            self.items_count += 1
            return
        if position == self.size():
            self.tail["next"] = node
            self.tail = node
            self.items_count += 1
            return
        previous = self.head
        current = self.head["next"]
        i = 1
        while i < position:
            previous = current
            current = current["next"]
            i += 1
        previous["next"] = node
        node["next"] = current
        self.items_count += 1
    def remove(self, item):
        if self.is_empty():
            return
        if self.size() == 1:
            if self.head["data"] == item:
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
            current = previous["next"]
    def pop_at(self, position):
        if position < 0 or position > self.size() - 1:
            raise IndexOutOfBoundsError()
        if self.size() == 1:
            item = self.head["data"]
            self.head = None
            self.tail = None
            self.items_count = 0
            return item
        if position == 0:
            previous = self.head
            self.head = self.head["next"]
            previous["next"] = None
            self.items_count -= 1
            return previous["data"]
        if position == self.size() - 1:
            pre_last = self.head
            while pre_last["next"] is not self.tail:
                pre_last = pre_last["next"]
            pre_last["next"] = None
            item = self.tail["data"]
            self.tail = pre_last
            self.items_count -= 1
            return item
        previous = self.head
        current = self.head["next"]
        i = 1
        while current is not None:
            if i == position:
                item = current["data"]
                previous["next"] = current["next"]
                current["next"] = None
                self.items_count -= 1
                return item
            previous = current
            current = previous["next"]
            i += 1
    def pop(self):
        return self.pop_at(self.size() - 1)

class IndexOutOfBoundsError(Exception):
    pass

class RepeatedElementError(Exception):
    pass

import unittest
class ListTest(unittest.TestCase):
    def test_list(self):
        # []
        l = UnorderedList()
        self.assertEqual(0, l.size())
        self.assertTrue(l.is_empty())
        self.assertEqual(-1, l.index(0))
        self.assertFalse(l.contains(0))
        # [0]
        l.add(0)
        with self.assertRaises(RepeatedElementError):
            l.add(0)
        self.assertEqual(1, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(0, l.index(0))
        self.assertTrue(l.contains(0))
        # [0, 1]
        l.append(1)
        with self.assertRaises(RepeatedElementError):
            l.append(1)
        self.assertEqual(2, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(0, l.index(0))
        self.assertTrue(l.contains(0))
        self.assertEqual(1, l.index(1))
        self.assertTrue(l.contains(1))
        # [0, 1, 2]
        l.append(2)
        with self.assertRaises(RepeatedElementError):
            l.append(2)
        self.assertEqual(3, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(0, l.index(0))
        self.assertTrue(l.contains(0))
        self.assertEqual(1, l.index(1))
        self.assertTrue(l.contains(1))
        self.assertEqual(2, l.index(2))
        self.assertTrue(l.contains(2))
        # [0, 1, 2, 3]
        l.append(3)
        with self.assertRaises(RepeatedElementError):
            l.append(3)
        self.assertEqual(4, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(0, l.index(0))
        self.assertTrue(l.contains(0))
        self.assertEqual(1, l.index(1))
        self.assertTrue(l.contains(1))
        self.assertEqual(2, l.index(2))
        self.assertTrue(l.contains(2))
        self.assertEqual(3, l.index(3))
        self.assertTrue(l.contains(3))
        # [-1, 0, 1, 2, 3]
        l.add(-1)
        with self.assertRaises(RepeatedElementError):
            l.add(-1)
        with self.assertRaises(RepeatedElementError):
            l.append(-1)
        self.assertEqual(5, l.size())
        self.assertFalse(l.is_empty())
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
        # [-2, -1, 0, 1, 2, 3]
        l.add(-2)
        with self.assertRaises(RepeatedElementError):
            l.add(-2)
        with self.assertRaises(RepeatedElementError):
            l.append(-2)
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
        self.assertEqual(5, l.index(3))
        self.assertTrue(l.contains(3))
        # [-2, -1, 1, 2, 3] Removed 0
        l.remove(0)
        l.remove(0) # Should do nothing
        self.assertEqual(5, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(-1, l.index(0))
        self.assertFalse(l.contains(0))
        self.assertEqual(0, l.index(-2))
        self.assertTrue(l.contains(-2))
        self.assertEqual(1, l.index(-1))
        self.assertTrue(l.contains(-1))
        self.assertEqual(2, l.index(1))
        self.assertTrue(l.contains(1))
        self.assertEqual(3, l.index(2))
        self.assertTrue(l.contains(2))
        self.assertEqual(4, l.index(3))
        self.assertTrue(l.contains(3))
        # [-1, 1, 2, 3] Removed -2
        l.remove(-2)
        l.remove(-2) # Should do nothing
        self.assertEqual(4, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(-1, l.index(-2))
        self.assertFalse(l.contains(-2))
        self.assertEqual(0, l.index(-1))
        self.assertTrue(l.contains(-1))
        self.assertEqual(1, l.index(1))
        self.assertTrue(l.contains(1))
        self.assertEqual(2, l.index(2))
        self.assertTrue(l.contains(2))
        self.assertEqual(3, l.index(3))
        self.assertTrue(l.contains(3))
        # [-1, 1, 2] Removed 3
        l.remove(3)
        l.remove(3) # Should do nothing
        self.assertEqual(3, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(-1, l.index(3))
        self.assertFalse(l.contains(3))
        self.assertEqual(0, l.index(-1))
        self.assertTrue(l.contains(-1))
        self.assertEqual(1, l.index(1))
        self.assertTrue(l.contains(1))
        self.assertEqual(2, l.index(2))
        self.assertTrue(l.contains(2))
        # [-1, 2] Removed 1
        l.remove(1)
        l.remove(1) # Should do nothing
        self.assertEqual(2, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(-1, l.index(1))
        self.assertFalse(l.contains(1))
        self.assertEqual(0, l.index(-1))
        self.assertTrue(l.contains(-1))
        self.assertEqual(1, l.index(2))
        self.assertTrue(l.contains(2))
        # [2] Removed -1
        l.remove(-1)
        l.remove(-1) # Should do nothing
        self.assertEqual(1, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(-1, l.index(-1))
        self.assertFalse(l.contains(-1))
        self.assertEqual(0, l.index(2))
        self.assertTrue(l.contains(2))
        # [] Removed 2
        l.remove(2)
        l.remove(2) # Should do nothing
        self.assertEqual(0, l.size())
        self.assertTrue(l.is_empty())
        self.assertEqual(-1, l.index(2))
        self.assertFalse(l.contains(2))
        # [1, 2, 3, 4, 5, 6]
        l.append(1)
        l.append(2)
        l.append(3)
        l.append(4)
        l.append(5)
        l.append(6)
        # [2, 3, 4, 5, 6] Popped 1 (index 0)
        popped = l.pop_at(0)
        l.remove(1) # Should do nothing
        self.assertEqual(1, popped)
        self.assertEqual(5, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(-1, l.index(1))
        self.assertFalse(l.contains(1))
        self.assertEqual(0, l.index(2))
        self.assertTrue(l.contains(2))
        self.assertEqual(1, l.index(3))
        self.assertTrue(l.contains(3))
        self.assertEqual(2, l.index(4))
        self.assertTrue(l.contains(4))
        self.assertEqual(3, l.index(5))
        self.assertTrue(l.contains(5))
        self.assertEqual(4, l.index(6))
        self.assertTrue(l.contains(6))
        # [2, 3, 5, 6] Popped 4 (index 2)
        popped = l.pop_at(2)
        l.remove(4) # Should do nothing
        self.assertEqual(4, popped)
        self.assertEqual(4, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(-1, l.index(4))
        self.assertFalse(l.contains(4))
        self.assertEqual(0, l.index(2))
        self.assertTrue(l.contains(2))
        self.assertEqual(1, l.index(3))
        self.assertTrue(l.contains(3))
        self.assertEqual(2, l.index(5))
        self.assertTrue(l.contains(5))
        self.assertEqual(3, l.index(6))
        self.assertTrue(l.contains(6))
        # [2, 3, 5] Popped 6 (index 3)
        popped = l.pop_at(3)
        l.remove(6) # Should do nothing
        self.assertEqual(6, popped)
        self.assertEqual(3, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(-1, l.index(6))
        self.assertFalse(l.contains(6))
        self.assertEqual(0, l.index(2))
        self.assertTrue(l.contains(2))
        self.assertEqual(1, l.index(3))
        self.assertTrue(l.contains(3))
        self.assertEqual(2, l.index(5))
        self.assertTrue(l.contains(5))
        # [2, 3] Popped 5
        popped = l.pop()
        l.remove(5) # Should do nothing
        self.assertEqual(5, popped)
        self.assertEqual(2, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(-1, l.index(5))
        self.assertFalse(l.contains(5))
        self.assertEqual(0, l.index(2))
        self.assertTrue(l.contains(2))
        self.assertEqual(1, l.index(3))
        self.assertTrue(l.contains(3))
        # [2] Popped 3
        popped = l.pop()
        l.remove(3) # Should do nothing
        self.assertEqual(3, popped)
        self.assertEqual(1, l.size())
        self.assertFalse(l.is_empty())
        self.assertEqual(-1, l.index(3))
        self.assertFalse(l.contains(3))
        self.assertEqual(0, l.index(2))
        self.assertTrue(l.contains(2))
        with self.assertRaises(IndexOutOfBoundsError):
            l.pop_at(1)
        # [] Popped 2
        popped = l.pop()
        l.remove(2) # Should do nothing
        self.assertEqual(2, popped)
        self.assertEqual(0, l.size())
        self.assertTrue(l.is_empty())
        self.assertEqual(-1, l.index(2))
        self.assertFalse(l.contains(2))
        with self.assertRaises(IndexOutOfBoundsError):
            l.pop_at(1)
        with self.assertRaises(IndexOutOfBoundsError):
            l.pop()

if __name__ == "__main__":
    unittest.main()

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
        if self.is_empty():
            raise EmptyListError()
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

class EmptyListError(Exception):
    pass

import unittest
class ListTest(unittest.TestCase):
    def test_list(self):
        l = UnorderedList()
        self.assertTrue(l.is_empty())
        self.assertEqual(0, l.size())
        self.assertFalse(l.contains(1))
        self.assertEqual(-1, l.index(1))
        l.add(1) # [1]
        self.assertFalse(l.is_empty())
        self.assertEqual(1, l.size())
        self.assertTrue(l.contains(1))
        self.assertEqual(0, l.index(1))
        l.append(2) # [1, 2]
        self.assertFalse(l.is_empty())
        self.assertEqual(2, l.size())
        self.assertTrue(l.contains(2))
        self.assertEqual(1, l.index(2))
        l.remove(1) # [2]
        self.assertFalse(l.is_empty())
        self.assertEqual(1, l.size())
        self.assertFalse(l.contains(1))
        self.assertEqual(-1, l.index(1))
        self.assertTrue(l.contains(2))
        self.assertEqual(0, l.index(2))
        l.remove(2) # []
        self.assertTrue(l.is_empty())
        self.assertEqual(0, l.size())
        l.add(1) # [1]
        l.add(2) # [2, 1]
        self.assertEqual(1, l.pop()) # [2]
        self.assertEqual(2, l.pop()) # []
        l.add(1) # [1]
        l.add(2) # [2, 1]
        self.assertEqual(2, l.pop_at(0)) # [1]
        self.assertEqual(1, l.pop_at(0)) # []
        with self.assertRaises(IndexOutOfBoundsError):
            l.insert(1, 1)
        self.assertEqual(None, l.remove(2))
        with self.assertRaises(EmptyListError):
            l.pop()
        with self.assertRaises(EmptyListError):
            l.pop_at(1)

if __name__ == "__main__":
    unittest.main()

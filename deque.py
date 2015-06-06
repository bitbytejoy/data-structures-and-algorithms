class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.items_count = 0
    def addFront(self, item):
        self.items_count += 1
        node = {"previous": None, "data": item, "next": None}
        if self.front is None:
            self.front = node
            self.rear = node
            return
        node["previous"] = self.front
        self.front["next"] = node
        self.front = node
    def addRear(self, item):
        self.items_count += 1
        node = {"previous": None, "data": item, "next": None}
        if self.front is None:
            self.front = node
            self.rear = node
            return
        node["next"] = self.rear
        self.rear["previous"] = node
        self.rear = node
    def size(self):
        return self.items_count
    def is_empty(self):
        return self.size() == 0
    def removeFront(self):
        if self.is_empty():
            raise EmptyDequeError()
        self.items_count -= 1
        item = self.front["data"]
        if self.front is self.rear:
            self.front = None
            self.rear = None
            return item
        self.front = self.front["previous"]
        self.front["next"] = None
        return item
    def removeRear(self):
        if self.is_empty():
            raise EmptyDequeError()
        self.items_count -= 1
        item = self.rear["data"]
        if self.front is self.rear:
            self.front = None
            self.rear = None
            return item
        self.rear = self.rear["next"]
        self.rear["previous"] = None
        return item

class EmptyDequeError(Exception):
    pass

import unittest
class DequeTest(unittest.TestCase):
    def test_deque(self):
        # Rear <-- [] <-- Front
        d = Deque()
        self.assertTrue(d.is_empty())
        self.assertEqual(0, d.size())
        with self.assertRaises(EmptyDequeError):
            d.removeFront()
        with self.assertRaises(EmptyDequeError):
            d.removeRear()
        # Rear <-- [1] <-- Front
        d.addFront(1)
        self.assertFalse(d.is_empty())
        self.assertEqual(1, d.size())
        self.assertEqual(1, d.removeFront())
        # Rear <-- [] <-- Front
        self.assertTrue(d.is_empty())
        self.assertEqual(0, d.size())
        with self.assertRaises(EmptyDequeError):
            d.removeFront()
        with self.assertRaises(EmptyDequeError):
            d.removeRear()
        # Rear <-- [1] <-- Front
        d.addRear(1)
        self.assertFalse(d.is_empty())
        self.assertEqual(1, d.size())
        self.assertEqual(1, d.removeRear())
        # Rear <-- [] <-- Front
        self.assertTrue(d.is_empty())
        self.assertEqual(0, d.size())
        with self.assertRaises(EmptyDequeError):
            d.removeFront()
        with self.assertRaises(EmptyDequeError):
            d.removeRear()
        # Rear <-- [1] <-- Front
        d.addFront(1)
        self.assertFalse(d.is_empty())
        self.assertEqual(1, d.size())
        self.assertEqual(1, d.removeRear())
        # Rear <-- [] <-- Front
        self.assertTrue(d.is_empty())
        self.assertEqual(0, d.size())
        with self.assertRaises(EmptyDequeError):
            d.removeFront()
        with self.assertRaises(EmptyDequeError):
            d.removeRear()
        # Rear <-- [1] <-- Front
        d.addRear(1)
        self.assertFalse(d.is_empty())
        self.assertEqual(1, d.size())
        self.assertEqual(1, d.removeFront())
        # Rear <-- [] <-- Front
        self.assertTrue(d.is_empty())
        self.assertEqual(0, d.size())
        with self.assertRaises(EmptyDequeError):
            d.removeFront()
        with self.assertRaises(EmptyDequeError):
            d.removeRear()
        # Rear <-- [1, 2] <-- Front
        d.addFront(1)
        d.addFront(2)
        self.assertFalse(d.is_empty())
        self.assertEqual(2, d.size())
        self.assertEqual(2, d.removeFront())
        self.assertEqual(1, d.removeFront())
        # Rear <-- [1, 2] <-- Front
        d.addFront(1)
        d.addFront(2)
        self.assertFalse(d.is_empty())
        self.assertEqual(2, d.size())
        self.assertEqual(1, d.removeRear())
        self.assertEqual(2, d.removeRear())
        # Rear <-- [1, 2] <-- Front
        d.addRear(2)
        d.addRear(1)
        self.assertFalse(d.is_empty())
        self.assertEqual(2, d.size())
        self.assertEqual(1, d.removeRear())
        self.assertEqual(2, d.removeRear())
        # Rear <-- [1, 2] <-- Front
        d.addRear(2)
        d.addRear(1)
        self.assertFalse(d.is_empty())
        self.assertEqual(2, d.size())
        self.assertEqual(2, d.removeFront())
        self.assertEqual(1, d.removeFront())
        # Rear <-- [] <-- Front
        self.assertTrue(d.is_empty())
        self.assertEqual(0, d.size())
        with self.assertRaises(EmptyDequeError):
            d.removeFront()
        with self.assertRaises(EmptyDequeError):
            d.removeRear()

if __name__ == "__main__":
    unittest.main()

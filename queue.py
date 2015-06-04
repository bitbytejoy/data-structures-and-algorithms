class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.item_count = 0
    def enqueue(self, item):
        self.item_count += 1
        node = {"data":item, "next":None}
        if self.first == None:
            self.first = node
            self.last = self.first
            return
        self.last["next"] = node
        self.last = node
    def dequeue(self):
        if self.first == None:
            raise EmptyQueueError()
        self.item_count -= 1
        dequeued = self.first["data"]
        if self.first == self.last:
            self.first = None
            self.last = None
        else:
            self.first = self.first["next"]
        return dequeued
    def is_empty(self):
        return self.size() == 0
    def size(self):
        return self.item_count

class EmptyQueueError(Exception):
    pass

import unittest
class QueueTest(unittest.TestCase):
    def test_queue(self):
        q = Queue()
        # []
        self.assertEqual(0, q.size())
        self.assertTrue(q.is_empty())
        with self.assertRaises(EmptyQueueError):
            q.dequeue()
        # [1]
        q.enqueue(1)
        self.assertEqual(1, q.size())
        self.assertFalse(q.is_empty())
        # [1 -> 2]
        q.enqueue(2)
        self.assertEqual(2, q.size())
        self.assertFalse(q.is_empty())
        # 1 [2]
        self.assertEqual(1, q.dequeue())
        self.assertEqual(1, q.size())
        self.assertFalse(q.is_empty())
        # 2 []
        self.assertEqual(2, q.dequeue())
        self.assertEqual(0, q.size())
        self.assertTrue(q.is_empty())
        with self.assertRaises(EmptyQueueError):
            q.dequeue()

if __name__ == "__main__":
    unittest.main()

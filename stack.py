class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def peek(self):
        self.__validate_not_empty()
        return self.items[len(self.items)-1]
    def pop(self):
        self.__validate_not_empty()
        return self.items.pop()
    def is_empty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def __validate_not_empty(self):
        if self.is_empty():
            raise EmptyStackError()

class EmptyStackError(Exception):
    pass

import unittest
class StackTest(unittest.TestCase):
    def test_stack(self):
        # []
        stack = Stack()
        self.assertTrue(stack.is_empty())
        self.assertEqual(0, stack.size())
        with self.assertRaises(EmptyStackError):
            stack.peek()
        with self.assertRaises(EmptyStackError):
            stack.pop()
        # [1]
        stack.push(1)
        self.assertEqual(1, stack.peek())
        self.assertFalse(stack.is_empty())
        self.assertEqual(1, stack.size())
        # [1, 2]
        stack.push(2)
        self.assertEqual(2, stack.peek())
        self.assertFalse(stack.is_empty())
        self.assertEqual(2, stack.size())
        # [1, 2, 3]
        stack.push(3)
        self.assertEqual(3, stack.size())
        self.assertFalse(stack.is_empty())
        self.assertEqual(3, stack.size())
        # [1, 2] 3 popped
        popped = stack.pop()
        self.assertEqual(3, popped)
        self.assertFalse(stack.is_empty())
        self.assertEqual(2, stack.size())
        # [1] 2 popped
        popped = stack.pop()
        self.assertEqual(2, popped)
        self.assertFalse(stack.is_empty())
        self.assertEqual(1, stack.size())
        # [] 1 popped
        popped = stack.pop()
        self.assertEqual(1, popped)
        self.assertTrue(stack.is_empty())
        self.assertEqual(0, stack.size())
        with self.assertRaises(EmptyStackError):
            stack.peek()
        with self.assertRaises(EmptyStackError):
            stack.pop()

if __name__ == "__main__":
    unittest.main()

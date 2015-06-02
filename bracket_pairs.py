from stack import Stack

def are_brackets_paired(string):
    brackets_stack = Stack()
    for letter in string:
        if letter == "(":
            brackets_stack.push("(")
        if letter == ")":
            if brackets_stack.is_empty():
                return False
            popped = brackets_stack.pop()
            if popped != "(":
                return False
    return brackets_stack.is_empty()

import unittest
class BracketPairsTest(unittest.TestCase):
    def test_brackets_paired(self):
        self.assertTrue(are_brackets_paired("abcde"))
        self.assertTrue(are_brackets_paired("()((())((())))"))
        self.assertTrue(are_brackets_paired("()(bs((asf))((()a)d))"))
    def test_brackets_not_paired(self):
        self.assertFalse(are_brackets_paired("(()(("))
        self.assertFalse(are_brackets_paired(")()(("))

if __name__ == "__main__":
    unittest.main()

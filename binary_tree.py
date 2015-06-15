class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
    def insert_left(self, value):
        new_node = BinaryTree(value)
        if self.left_child is not None:
            new_node.left_child = self.left_child
            self.left_child = new_node
            return
        self.left_child = new_node
    def insert_right(self, value):
        new_node = BinaryTree(value)
        if self.right_child is not None:
            new_node.right_child = self.right_child
            self.right_child = new_node
            return
        self.right_child = new_node
    def get_left_child(self):
        return self.left_child
    def get_right_child(self):
        return self.right_child
    def get_value(self):
        return self.value
    def set_value(self, value):
        self.value = value
    def traverse_preorder(self, processor):
        processor(self.get_value())
        if self.left_child is not None:
            self.left_child.traverse_preorder(processor)
        if self.right_child is not None:
            self.right_child.traverse_preorder(processor)
    def traverse_postorder(self, processor):
        if self.left_child is not None:
            self.left_child.traverse_postorder(processor)
        if self.right_child is not None:
            self.right_child.traverse_postorder(processor)
        processor(self.get_value())
    def traverse_inorder(self, processor):
        if self.left_child is not None:
            self.left_child.traverse_inorder(processor)
        processor(self.get_value())
        if self.right_child is not None:
            self.right_child.traverse_inorder(processor)

def traverse_preorder(binary_tree, processor):
    if not binary_tree:
        return
    processor(binary_tree.get_value())
    traverse_preorder(binary_tree.get_left_child(), processor)
    traverse_preorder(binary_tree.get_right_child(), processor)

def traverse_postorder(binary_tree, processor):
    if not binary_tree:
        return
    traverse_postorder(binary_tree.get_left_child(), processor)
    traverse_postorder(binary_tree.get_right_child(), processor)
    processor(binary_tree.get_value())

def traverse_inorder(binary_tree, processor):
    if binary_tree is None:
        return
    traverse_inorder(binary_tree.get_left_child(), processor)
    processor(binary_tree.get_value())
    traverse_inorder(binary_tree.get_right_child(), processor)

import unittest
class BinaryTreeTest(unittest.TestCase):
    def test_binary_tree(self):
        '''
          1
          |
        -----
        |   |
        x   x
        '''
        t = BinaryTree(1)
        self.assertIsNone(t.get_left_child())
        self.assertIsNone(t.get_right_child())
        self.assertEqual(1, t.get_value())
        '''
                1
                |
            --------
            |      |
            2      3
            |      |
          -----  -----
          |   |  |   |
          x   x  x   x
        '''
        t.insert_left(2)
        t.insert_right(3)
        self.assertEqual(1, t.get_value())
        self.assertEqual(2, t.get_left_child().get_value())
        self.assertEqual(3, t.get_right_child().get_value())
        self.assertIsNone(t.get_left_child().get_left_child())
        self.assertIsNone(t.get_left_child().get_right_child())
        self.assertIsNone(t.get_right_child().get_left_child())
        self.assertIsNone(t.get_right_child().get_right_child())
        '''
                1
                |
            --------
            |      |
            4      3
            |      |
          -----  -----
          |   |  |   |
          x   x  x   x
        '''
        t.get_left_child().set_value(4)
        self.assertEqual(1, t.get_value())
        self.assertEqual(4, t.get_left_child().get_value())
        self.assertEqual(3, t.get_right_child().get_value())
        self.assertIsNone(t.get_left_child().get_left_child())
        self.assertIsNone(t.get_left_child().get_right_child())
        self.assertIsNone(t.get_right_child().get_left_child())
        self.assertIsNone(t.get_right_child().get_right_child())
        '''
                        1
                        |
                 ---------------
                 |             |
                 4             3
                 |             |
              --------      --------
              |      |      |      |
              5      6      7      x
              |      |      |
            -----  -----  -----
            |   |  |   |  |   |
            x   8  x   x  9   x
                |         |
               ---       ---
               | |       | |
               x x       x x
        '''
        t.get_left_child().insert_left(5)
        t.get_left_child().get_left_child().insert_right(8)
        t.get_left_child().insert_right(6)
        t.get_right_child().insert_left(7)
        t.get_right_child().get_left_child().insert_left(9)
        self.assertEqual(1, t.get_value())
        self.assertEqual(4, t.get_left_child().get_value())
        self.assertEqual(3, t.get_right_child().get_value())
        self.assertEqual(5, t.get_left_child().get_left_child().get_value())
        self.assertIsNone(t.get_left_child().get_left_child().get_left_child())
        self.assertEqual(8, t.get_left_child()
                             .get_left_child()
                             .get_right_child()
                             .get_value())
        self.assertIsNone(t.get_left_child()
                           .get_left_child()
                           .get_right_child()
                           .get_left_child())
        self.assertIsNone(t.get_left_child()
                           .get_left_child()
                           .get_right_child()
                           .get_right_child())
        self.assertEqual(6, t.get_left_child().get_right_child().get_value())
        self.assertIsNone(t.get_left_child().get_right_child().get_left_child())
        self.assertIsNone(t.get_left_child()
                           .get_right_child()
                           .get_right_child())
        self.assertEqual(7, t.get_right_child().get_left_child().get_value())
        self.assertEqual(9, t.get_right_child()
                             .get_left_child()
                             .get_left_child()
                             .get_value())
        self.assertIsNone(t.get_right_child()
                           .get_left_child()
                           .get_left_child()
                           .get_left_child())
        self.assertIsNone(t.get_right_child()
                           .get_left_child()
                           .get_left_child()
                           .get_right_child())
        self.assertIsNone(t.get_right_child()
                           .get_left_child()
                           .get_right_child())
        self.assertIsNone(t.get_right_child()
                           .get_right_child())
        # Traversal
        order = []
        def processor(value):
            order.append(value)
        # Preorder traversal
        expected_preorder = [1, 4, 5, 8, 6, 3, 7, 9]
        t.traverse_preorder(processor)
        self.assertEqual(expected_preorder, order)
        order = []
        traverse_preorder(t, processor)
        self.assertEqual(expected_preorder, order)
        # Postorder traversal
        expected_postorder = [8, 5, 6, 4, 9, 7, 3, 1]
        order = []
        t.traverse_postorder(processor)
        self.assertEqual(expected_postorder, order)
        order = []
        traverse_postorder(t, processor)
        self.assertEqual(expected_postorder, order)
        # Inorder traversal
        expected_inorder = [5, 8, 4, 6, 1, 9, 7, 3]
        order = []
        t.traverse_inorder(processor)
        self.assertEqual(expected_inorder, order)
        order = []
        traverse_inorder(t, processor)
        self.assertEqual(expected_inorder, order)

if __name__ == "__main__":
    unittest.main()

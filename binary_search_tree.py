class TreeNode:
    def __init__(self, key, value, left = None, right = None, parent = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
    def has_left_child(self):
        return self.left is not None
    def has_right_child(self):
        return self.right is not None
    def is_root(self):
        return self.parent is None
    def is_left_child(self):
        return not self.is_root() and self.parent.left is self
    def is_right_child(self):
        return not self.is_root() and self.parent.right is self
    def is_leaf(self):
        return not self.has_left_child() and not self.has_right_child()
    def has_any_children(self):
        return self.has_left_child() or self.has_right_child()
    def has_both_children(self):
        return self.has_left_child() and self.has_right_child()
    def set_node_data(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
        if self.has_left_child():
            self.left.parent = self
        if self.has_right_child():
            self.right.parent = self

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.items_count = 0
    def size(self):
        return self.items_count
    def put(self, key, value):
        self.items_count += 1
        if self.root is None:
            self.root = TreeNode(key, value)
            return
        self._put(self.root, key, value)
    def _put(self, parent, key, value):
        if not parent.has_left_child() and key < parent.key:
            parent.left = TreeNode(key, value, None, None, parent)
            return
        if not parent.has_right_child() and key > parent.key:
            parent.right = TreeNode(key, value, None, None, parent)
            return
        if key < parent.key:
            return self._put(parent.left, key, value)
        return self._put(parent.right, key, value)
    def __setitem__(self, key, value):
        self.put(key, value)
    def get(self, key):
        if self.root is None:
            return None
        node = self._get(self.root, key)
        if node is not None:
            return node.value
        return None
    def _get(self, node, key):
        if node.key == key:
            return node
        if key < node.key and node.has_left_child():
            return self._get(node.left, key)
        if key > node.key and node.has_right_child():
            return self._get(node.right, key)
        return None
    def __contains__(self, key):
        return self.get(key) is not None
    def delete(self, key):
        if self.size() == 0:
            raise KeyNotFoundError()
        node = self._get(self.root, key)
        if node is None:
            raise KeyNotFoundError()
        if not node.has_any_children():
            if self.root is node:
                self.root = None
            elif node.is_left_child():
                node.parent.left = None
                node.parent = None
            else:
                node.parent.right = None
                node.parent = None
            self.items_count -= 1
            return
        if node.has_both_children():
            min_child = self._min_child(node.right)
            if min_child.parent is node:
                min_child.parent = node.parent
                if node is self.root:
                    self.root = min_child
                elif node.is_left_child():
                    node.parent.left = min_child
                else:
                    node.parent.right = min_child
                min_child.left = node.left
                self.items_count -= 1
                node.left = None
                node.parent = None
                node.right = None
                return
            if min_child.has_right_child():
                min_child.right.parent = min_child.parent
            min_child.parent.left = min_child.right
            node.left.parent = min_child
            min_child.left = node.left
            node.right.parent = min_child
            min_child.right = node.right
            min_child.parent = node.parent
            if node is self.root:
                self.root = min_child
            elif node.is_left_child():
                node.parent.left = min_child
            else:
                node.parent.right = min_child
            node.left = None
            node.right = None
            node.parent = None
            self.items_count -= 1
            return
        if node.has_left_child():
            if node is self.root:
                self.root = node.left
            elif node.is_left_child():
                node.parent.left = node.left
            else:
                node.parent.right = node.left
            node.left.parent = node.parent
            node.parent = None
            node.left = None
            self.items_count -= 1
            return
        if node.has_right_child():
            if node is self.root:
                self.root = node.right
            elif node.is_left_child():
                node.parent.left = node.right
            else:
                node.parent.right = node.right
            node.right.parent = node.parent
            node.parent = None
            node.right = None
            self.items_count -= 1
            return
        raise KeyNotFoundError()
    def _min_child(self, node):
        if not node.has_left_child():
            return node
        return self._min_child(node.left)
    def __delitem__(self, key):
        self.delete(key)

class KeyNotFoundError(Exception):
    pass

import unittest
class BinarySearchTreeTest(unittest.TestCase):
    def test_tree_node(self):
        # Empty binary search tree
        bst = BinarySearchTree()
        self.assertEqual(0, bst.size())
        self.assertIsNone(bst.get(0))
        self.assertFalse(0 in bst)
        '''
                 (0, "0")
                    |
            -----------------
            |               |
            x               x
        '''
        bst.put(0, "0")
        self.assertEqual(1, bst.size())
        self.assertEqual("0", bst.get(0))
        self.assertIsNone(bst.get(-10))
        self.assertTrue(0 in bst)
        self.assertFalse(-10 in bst)
        '''
                      (0, "0")
                         |
                 -----------------
                 |               |
            (-10, "-10")         x
                 |
        ---------------------
        |                   |
        x                   x
        '''
        bst.put(-10, "-10")
        self.assertEqual(2, bst.size())
        self.assertEqual("0", bst.get(0))
        self.assertEqual("-10", bst.get(-10))
        self.assertIsNone(bst.get(10))
        self.assertTrue(0 in bst)
        self.assertTrue(-10 in bst)
        self.assertFalse(10 in bst)
        '''
                           (0, "0")
                              |
                 --------------------------
                 |                        |
            (-10, "-10")              (10, "10")
                 |                        |
        ---------------------    -------------------
        |                   |    |                 |
        x                   x    x                 x
        '''
        bst.put(10, "10")
        self.assertEqual(3, bst.size())
        self.assertEqual("0", bst.get(0))
        self.assertEqual("-10", bst.get(-10))
        self.assertEqual("10", bst.get(10))
        self.assertIsNone(bst.get(-100))
        self.assertTrue(0 in bst)
        self.assertTrue(-10 in bst)
        self.assertTrue(10 in bst)
        self.assertFalse(-100 in bst)
        '''
                                   (0, "0")
                                      |
                         --------------------------
                         |                        |
                    (-10, "-10")              (10, "10")
                         |                        |
                ---------------------    -------------------
                |                   |    |                 |
          (-100, "-100")            x    x                 x
                |
        ---------------------
        |                   |
        x                   x
        '''
        bst[-100] = "-100"
        self.assertEqual(4, bst.size())
        self.assertEqual("0", bst.get(0))
        self.assertEqual("-10", bst.get(-10))
        self.assertEqual("10", bst.get(10))
        self.assertEqual("-100", bst.get(-100))
        self.assertIsNone(bst.get(100))
        self.assertTrue(0 in bst)
        self.assertTrue(-10 in bst)
        self.assertTrue(10 in bst)
        self.assertTrue(-100 in bst)
        self.assertFalse(100 in bst)
        '''
                                   (0, "0")
                                      |
                         --------------------------
                         |                        |
                    (-10, "-10")              (10, "10")
                         |                        |
                ---------------------    -------------------
                |                   |    |                 |
          (-100, "-100")            x    x            (100, "100")
                |                                          |
        ---------------------                     --------------------
        |                   |                     |                  |
        x                   x                     x                  x
        '''
        bst[100] = "100"
        self.assertEqual(5, bst.size())
        self.assertEqual("0", bst.get(0))
        self.assertEqual("-10", bst.get(-10))
        self.assertEqual("10", bst.get(10))
        self.assertEqual("-100", bst.get(-100))
        self.assertEqual("100", bst.get(100))
        self.assertIsNone(bst.get(1000))
        self.assertTrue(0 in bst)
        self.assertTrue(-10 in bst)
        self.assertTrue(10 in bst)
        self.assertTrue(-100 in bst)
        self.assertTrue(100 in bst)
        self.assertFalse(1000 in bst)
        '''
                                   (0, "0")
                                      |
                         --------------------------
                         |                        |
                    (-10, "-10")              (10, "10")
                         |                        |
                ----------------      -------------------
                |              |      |                 |
          (-100, "-100")       x   (5, "5")        (100, "100")
                |                     |                 |
        ---------------------      -----------      ----------
        |                   |      |         |      |        |
        x                   x   (2, "2")  (7, "7")  x        x
                                   |         |
                              --------      ---------
                              |      |      |       |
                              x   (3, "3") (6, "6") x
                                     |      |
                                  -------- ---
                                  |      | | |
                                  x      x x x
        '''
        bst[5] = "5"
        bst[2] = "2"
        bst[3] = "3"
        bst[7] = "7"
        bst[6] = "6"
        self.assertEqual(10, bst.size())
        self.assertEqual("0", bst.get(0))
        self.assertEqual("-10", bst.get(-10))
        self.assertEqual("10", bst.get(10))
        self.assertEqual("-100", bst.get(-100))
        self.assertEqual("100", bst.get(100))
        self.assertEqual("5", bst.get(5))
        self.assertEqual("2", bst.get(2))
        self.assertEqual("3", bst.get(3))
        self.assertEqual("7", bst.get(7))
        self.assertEqual("6", bst.get(6))
        self.assertIsNone(bst.get(1000))
        self.assertTrue(0 in bst)
        self.assertTrue(-10 in bst)
        self.assertTrue(10 in bst)
        self.assertTrue(-100 in bst)
        self.assertTrue(100 in bst)
        self.assertTrue(5 in bst)
        self.assertTrue(2 in bst)
        self.assertTrue(3 in bst)
        self.assertTrue(7 in bst)
        self.assertTrue(6 in bst)
        self.assertFalse(1000 in bst)
        '''
                                   (0, "0")
                                      |
                         --------------------------
                         |                        |
                    (-10, "-10")              (10, "10")
                         |                        |
                ----------------      -------------------
                |              |      |                 |
          (-100, "-100")       x   (6, "6")        (100, "100")
                |                     |                 |
        ---------------------      -----------      ----------
        |                   |      |         |      |        |
        x                   x   (2, "2")  (7, "7")  x        x
                                   |         |
                              --------      ---------
                              |      |      |       |
                              x   (3, "3")  x       x
                                     |
                                  --------
                                  |      |
                                  x      x
        '''
        del bst[5]
        self.assertEqual(9, bst.size())
        self.assertEqual("0", bst.get(0))
        self.assertEqual("-10", bst.get(-10))
        self.assertEqual("10", bst.get(10))
        self.assertEqual("-100", bst.get(-100))
        self.assertEqual("100", bst.get(100))
        self.assertEqual("2", bst.get(2))
        self.assertEqual("3", bst.get(3))
        self.assertEqual("7", bst.get(7))
        self.assertEqual("6", bst.get(6))
        self.assertIsNone(bst.get(5))
        self.assertTrue(0 in bst)
        self.assertTrue(-10 in bst)
        self.assertTrue(10 in bst)
        self.assertTrue(-100 in bst)
        self.assertTrue(100 in bst)
        self.assertTrue(2 in bst)
        self.assertTrue(3 in bst)
        self.assertTrue(7 in bst)
        self.assertTrue(6 in bst)
        self.assertFalse(5 in bst)
        '''
                                   (0, "0")
                                      |
                         --------------------------
                         |                        |
                    (-10, "-10")              (10, "10")
                         |                        |
                ----------------      -------------------
                |              |      |                 |
          (-100, "-100")       x   (7, "7")        (100, "100")
                |                     |                 |
        ---------------------      -----------      ----------
        |                   |      |         |      |        |
        x                   x   (2, "2")     x      x        x
                                   |
                              --------
                              |      |
                              x   (3, "3")
                                     |
                                  --------
                                  |      |
                                  x      x
        '''
        del bst[6]
        self.assertEqual(8, bst.size())
        self.assertEqual("0", bst.get(0))
        self.assertEqual("-10", bst.get(-10))
        self.assertEqual("10", bst.get(10))
        self.assertEqual("-100", bst.get(-100))
        self.assertEqual("100", bst.get(100))
        self.assertEqual("2", bst.get(2))
        self.assertEqual("3", bst.get(3))
        self.assertEqual("7", bst.get(7))
        self.assertIsNone(bst.get(6))
        self.assertTrue(0 in bst)
        self.assertTrue(-10 in bst)
        self.assertTrue(10 in bst)
        self.assertTrue(-100 in bst)
        self.assertTrue(100 in bst)
        self.assertTrue(2 in bst)
        self.assertTrue(3 in bst)
        self.assertTrue(7 in bst)
        self.assertFalse(6 in bst)
        '''
                                   (0, "0")
                                      |
                         --------------------------
                         |                        |
                    (-10, "-10")              (10, "10")
                         |                        |
                ----------------      -------------------
                |              |      |                 |
          (-100, "-100")       x   (2, "2")        (100, "100")
                |                     |                 |
        ---------------------      -----------      ----------
        |                   |      |         |      |        |
        x                   x      x      (3, "3")  x        x
                                             |
                                          --------
                                          |      |
                                          x      x
        '''
        del bst[7]
        self.assertEqual(7, bst.size())
        self.assertEqual("0", bst.get(0))
        self.assertEqual("-10", bst.get(-10))
        self.assertEqual("10", bst.get(10))
        self.assertEqual("-100", bst.get(-100))
        self.assertEqual("100", bst.get(100))
        self.assertEqual("2", bst.get(2))
        self.assertEqual("3", bst.get(3))
        self.assertIsNone(bst.get(7))
        self.assertTrue(0 in bst)
        self.assertTrue(-10 in bst)
        self.assertTrue(10 in bst)
        self.assertTrue(-100 in bst)
        self.assertTrue(100 in bst)
        self.assertTrue(2 in bst)
        self.assertTrue(3 in bst)
        self.assertFalse(7 in bst)
        '''
                                   (0, "0")
                                      |
                         --------------------------
                         |                        |
                    (-10, "-10")              (10, "10")
                         |                        |
                ----------------      -------------------
                |              |      |                 |
          (-100, "-100")       x   (3, "3")        (100, "100")
                |                     |                 |
        ---------------------      -----------      ----------
        |                   |      |         |      |        |
        x                   x      x         x      x        x
        '''
        del bst[2]
        self.assertEqual(6, bst.size())
        self.assertEqual("0", bst.get(0))
        self.assertEqual("-10", bst.get(-10))
        self.assertEqual("10", bst.get(10))
        self.assertEqual("-100", bst.get(-100))
        self.assertEqual("100", bst.get(100))
        self.assertEqual("3", bst.get(3))
        self.assertIsNone(bst.get(2))
        self.assertTrue(0 in bst)
        self.assertTrue(-10 in bst)
        self.assertTrue(10 in bst)
        self.assertTrue(-100 in bst)
        self.assertTrue(100 in bst)
        self.assertTrue(3 in bst)
        self.assertFalse(2 in bst)
        '''
                                   (0, "0")
                                      |
                         --------------------------
                         |                        |
                  (-100, "-100")              (10, "10")
                         |                        |
                ----------------      -------------------
                |              |      |                 |
                x              x   (3, "3")        (100, "100")
                                      |                 |
                                   -----------      ----------
                                   |         |      |        |
                                   x         x      x        x
        '''
        del bst[-10]
        self.assertEqual(5, bst.size())
        self.assertEqual("0", bst.get(0))
        self.assertEqual("10", bst.get(10))
        self.assertEqual("-100", bst.get(-100))
        self.assertEqual("100", bst.get(100))
        self.assertEqual("3", bst.get(3))
        self.assertIsNone(bst.get(-10))
        self.assertTrue(0 in bst)
        self.assertTrue(10 in bst)
        self.assertTrue(-100 in bst)
        self.assertTrue(100 in bst)
        self.assertTrue(3 in bst)
        self.assertFalse(-10 in bst)
        '''
                                   (0, "0")
                                      |
                         --------------------------
                         |                        |
                  (-100, "-100")             (100, "100")
                         |                        |
                ----------------      -------------------
                |              |      |                 |
                x              x   (3, "3")             x
                                      |
                                   -----------
                                   |         |
                                   x         x
        '''
        del bst[10]
        self.assertEqual(4, bst.size())
        self.assertEqual("0", bst.get(0))
        self.assertEqual("-100", bst.get(-100))
        self.assertEqual("100", bst.get(100))
        self.assertEqual("3", bst.get(3))
        self.assertIsNone(bst.get(10))
        self.assertTrue(0 in bst)
        self.assertTrue(-100 in bst)
        self.assertTrue(100 in bst)
        self.assertTrue(3 in bst)
        self.assertFalse(10 in bst)
        '''
                                   (0, "0")
                                      |
                         --------------------------
                         |                        |
                  (-100, "-100")               (3, "3")
                         |                        |
                ----------------      -------------------
                |              |      |                 |
                x              x      x                 x
        '''
        del bst[100]
        self.assertEqual(3, bst.size())
        self.assertEqual("0", bst.get(0))
        self.assertEqual("-100", bst.get(-100))
        self.assertEqual("3", bst.get(3))
        self.assertIsNone(bst.get(100))
        self.assertTrue(0 in bst)
        self.assertTrue(-100 in bst)
        self.assertTrue(3 in bst)
        self.assertFalse(100 in bst)
        '''
                                   (0, "0")
                                      |
                         --------------------------
                         |                        |
                  (-100, "-100")                  x
                         |
                ----------------
                |              |
                x              x
        '''
        del bst[3]
        self.assertEqual(2, bst.size())
        self.assertEqual("0", bst.get(0))
        self.assertEqual("-100", bst.get(-100))
        self.assertIsNone(bst.get(3))
        self.assertTrue(0 in bst)
        self.assertTrue(-100 in bst)
        self.assertFalse(3 in bst)
        '''
          (-100, "-100")
                 |
        ----------------
        |              |
        x              x
        '''
        del bst[0]
        self.assertEqual(1, bst.size())
        self.assertEqual("-100", bst.get(-100))
        self.assertIsNone(bst.get(0))
        self.assertTrue(-100 in bst)
        self.assertFalse(0 in bst)
        '''
                                (-100, "-100")
                                      |
                      -------------------------------
                      |                             |
                (-200, "-200")                   (0, "0")
                      |                             |
                -------------                   -------------------
                |           |                   |                 |
          (-300, "-300")(-150, "-150")     (-50, "-50")      (100, "100")
                |             |                 |                 |
          ------------   -----------        ----------       -----------
          |          |   |         |        |        |       |         |
          x          x   x         x        x  (-40, "-40")  x     (150, "150")
                                                     |                  |
                                                   -----             --------
                                                   |   |             |      |
                                                   x (-45, "-45")    x      x
                                                          |
                                                        -----
                                                        |   |
                                                        x   x
        '''
        bst[-200] = "-200"
        bst[-300] = "-300"
        bst[-150] = "-150"
        bst[0] = "0"
        bst[-50] = "-50"
        bst[-40] = "-40"
        bst[-45] = "-45"
        bst[100] = "100"
        bst[150] = "150"
        self.assertEqual(10, bst.size())
        self.assertEqual("-100", bst.get(-100))
        self.assertEqual("-200", bst.get(-200))
        self.assertEqual("-300", bst.get(-300))
        self.assertEqual("-150", bst.get(-150))
        self.assertEqual("0", bst.get(0))
        self.assertEqual("-50", bst.get(-50))
        self.assertEqual("-40", bst.get(-40))
        self.assertEqual("-45", bst.get(-45))
        self.assertEqual("100", bst.get(100))
        self.assertEqual("150", bst.get(150))
        self.assertIsNone(bst.get(300))
        self.assertTrue(-100 in bst)
        self.assertTrue(-200 in bst)
        self.assertTrue(-300 in bst)
        self.assertTrue(-150 in bst)
        self.assertTrue(0 in bst)
        self.assertTrue(-50 in bst)
        self.assertTrue(-40 in bst)
        self.assertTrue(-45 in bst)
        self.assertTrue(100 in bst)
        self.assertTrue(150 in bst)
        self.assertFalse(300 in bst)
        '''
                                 (-50, "-50")
                                      |
                      -------------------------------
                      |                             |
                (-200, "-200")                   (0, "0")
                      |                             |
                -------------                   -------------------
                |           |                   |                 |
          (-300, "-300")(-150, "-150")     (-40, "-40")      (100, "100")
                |             |                 |                 |
          ------------   -----------        ----------       -----------
          |          |   |         |        |        |       |         |
          x          x   x         x        x  (-45, "-45")  x     (150, "150")
                                                     |                  |
                                                   -----             --------
                                                   |   |             |      |
                                                   x   x             x      x
        '''
        del bst[-100]
        self.assertEqual(9, bst.size())
        self.assertEqual("-200", bst.get(-200))
        self.assertEqual("-300", bst.get(-300))
        self.assertEqual("-150", bst.get(-150))
        self.assertEqual("0", bst.get(0))
        self.assertEqual("-50", bst.get(-50))
        self.assertEqual("-40", bst.get(-40))
        self.assertEqual("-45", bst.get(-45))
        self.assertEqual("100", bst.get(100))
        self.assertEqual("150", bst.get(150))
        self.assertIsNone(bst.get(-100))
        self.assertTrue(-200 in bst)
        self.assertTrue(-300 in bst)
        self.assertTrue(-150 in bst)
        self.assertTrue(0 in bst)
        self.assertTrue(-50 in bst)
        self.assertTrue(-40 in bst)
        self.assertTrue(-45 in bst)
        self.assertTrue(100 in bst)
        self.assertTrue(150 in bst)
        self.assertFalse(-100 in bst)
        '''
                                 (-40, "-40")
                                      |
                      -------------------------------
                      |                             |
                (-200, "-200")                   (0, "0")
                      |                             |
                -------------                   -------------------
                |           |                   |                 |
          (-300, "-300")(-150, "-150")     (-45, "-45")      (100, "100")
                |             |                 |                 |
          ------------   -----------        ----------       -----------
          |          |   |         |        |        |       |         |
          x          x   x         x        x        x       x     (150, "150")
                                                                       |
                                                                     --------
                                                                     |      |
                                                                     x      x
        '''
        del bst[-50]
        self.assertEqual(8, bst.size())
        self.assertEqual("-200", bst.get(-200))
        self.assertEqual("-300", bst.get(-300))
        self.assertEqual("-150", bst.get(-150))
        self.assertEqual("0", bst.get(0))
        self.assertEqual("-40", bst.get(-40))
        self.assertEqual("-45", bst.get(-45))
        self.assertEqual("100", bst.get(100))
        self.assertEqual("150", bst.get(150))
        self.assertIsNone(bst.get(-50))
        self.assertTrue(-200 in bst)
        self.assertTrue(-300 in bst)
        self.assertTrue(-150 in bst)
        self.assertTrue(0 in bst)
        self.assertTrue(-40 in bst)
        self.assertTrue(-45 in bst)
        self.assertTrue(100 in bst)
        self.assertTrue(150 in bst)
        self.assertFalse(-50 in bst)
        '''
                                 (-45, "-45")
                                      |
                      -------------------------------
                      |                             |
                (-200, "-200")                   (0, "0")
                      |                             |
                -------------                   -------------------
                |           |                   |                 |
          (-300, "-300")(-150, "-150")          x            (100, "100")
                |             |                                   |
          ------------   -----------                         -----------
          |          |   |         |                         |         |
          x          x   x         x                         x     (150, "150")
                                                                       |
                                                                     --------
                                                                     |      |
                                                                     x      x
        '''
        del bst[-40]
        self.assertEqual(7, bst.size())
        self.assertEqual("-200", bst.get(-200))
        self.assertEqual("-300", bst.get(-300))
        self.assertEqual("-150", bst.get(-150))
        self.assertEqual("0", bst.get(0))
        self.assertEqual("-45", bst.get(-45))
        self.assertEqual("100", bst.get(100))
        self.assertEqual("150", bst.get(150))
        self.assertIsNone(bst.get(-40))
        self.assertTrue(-200 in bst)
        self.assertTrue(-300 in bst)
        self.assertTrue(-150 in bst)
        self.assertTrue(0 in bst)
        self.assertTrue(-45 in bst)
        self.assertTrue(100 in bst)
        self.assertTrue(150 in bst)
        self.assertFalse(-40 in bst)
        '''
                                   (0, "0")
                                      |
                      -------------------------------
                      |                             |
                (-200, "-200")                 (100, "100")
                      |                             |
                -------------                   -------------------
                |           |                   |                 |
          (-300, "-300")(-150, "-150")          x            (150, "150")
                |             |                                   |
          ------------   -----------                         -----------
          |          |   |         |                         |         |
          x          x   x         x                         x         x
        '''
        del bst[-45]
        self.assertEqual(6, bst.size())
        self.assertEqual("-200", bst.get(-200))
        self.assertEqual("-300", bst.get(-300))
        self.assertEqual("-150", bst.get(-150))
        self.assertEqual("0", bst.get(0))
        self.assertEqual("100", bst.get(100))
        self.assertEqual("150", bst.get(150))
        self.assertIsNone(bst.get(-45))
        self.assertTrue(-200 in bst)
        self.assertTrue(-300 in bst)
        self.assertTrue(-150 in bst)
        self.assertTrue(0 in bst)
        self.assertTrue(100 in bst)
        self.assertTrue(150 in bst)
        self.assertFalse(-45 in bst)
        '''
                                 (100, "100")
                                      |
                      -------------------------------
                      |                             |
                (-200, "-200")                 (150, "150")
                      |                             |
                -------------                   -----------
                |           |                   |         |
          (-300, "-300")(-150, "-150")          x         x
                |             |
          ------------   -----------
          |          |   |         |
          x          x   x         x
        '''
        del bst[0]
        self.assertEqual(5, bst.size())
        self.assertEqual("-200", bst.get(-200))
        self.assertEqual("-300", bst.get(-300))
        self.assertEqual("-150", bst.get(-150))
        self.assertEqual("100", bst.get(100))
        self.assertEqual("150", bst.get(150))
        self.assertIsNone(bst.get(0))
        self.assertTrue(-200 in bst)
        self.assertTrue(-300 in bst)
        self.assertTrue(-150 in bst)
        self.assertTrue(100 in bst)
        self.assertTrue(150 in bst)
        self.assertFalse(0 in bst)
        '''
                                 (150, "150")
                                      |
                      -------------------------------
                      |                             |
                (-200, "-200")                      x
                      |
                -------------
                |           |
          (-300, "-300")(-150, "-150")
                |             |
          ------------   -----------
          |          |   |         |
          x          x   x         x
        '''
        del bst[100]
        with self.assertRaises(KeyNotFoundError):
            del bst[100]
        self.assertEqual(4, bst.size())
        self.assertEqual("-200", bst.get(-200))
        self.assertEqual("-300", bst.get(-300))
        self.assertEqual("-150", bst.get(-150))
        self.assertEqual("150", bst.get(150))
        self.assertIsNone(bst.get(100))
        self.assertTrue(-200 in bst)
        self.assertTrue(-300 in bst)
        self.assertTrue(-150 in bst)
        self.assertTrue(150 in bst)
        self.assertFalse(100 in bst)
        '''
                (-200, "-200")
                      |
                -------------
                |           |
          (-300, "-300")(-150, "-150")
                |             |
          ------------   -----------
          |          |   |         |
          x          x   x         x
        '''
        del bst[150]
        with self.assertRaises(KeyNotFoundError):
            del bst[150]
        self.assertEqual(3, bst.size())
        self.assertEqual("-200", bst.get(-200))
        self.assertEqual("-300", bst.get(-300))
        self.assertEqual("-150", bst.get(-150))
        self.assertIsNone(bst.get(150))
        self.assertTrue(-200 in bst)
        self.assertTrue(-300 in bst)
        self.assertTrue(-150 in bst)
        self.assertFalse(150 in bst)
        '''
                (-150, "-150")
                      |
                -------------
                |           |
          (-300, "-300")    x
                |
          ------------
          |          |
          x          x
        '''
        del bst[-200]
        with self.assertRaises(KeyNotFoundError):
            del bst[-200]
        self.assertEqual(2, bst.size())
        self.assertEqual("-300", bst.get(-300))
        self.assertEqual("-150", bst.get(-150))
        self.assertIsNone(bst.get(-200))
        self.assertTrue(-300 in bst)
        self.assertTrue(-150 in bst)
        self.assertFalse(-200 in bst)
        '''
          (-300, "-300")
                |
          ------------
          |          |
          x          x
        '''
        del bst[-150]
        with self.assertRaises(KeyNotFoundError):
            del bst[-150]
        self.assertEqual(1, bst.size())
        self.assertEqual("-300", bst.get(-300))
        self.assertIsNone(bst.get(-150))
        self.assertTrue(-300 in bst)
        self.assertFalse(-150 in bst)
        '''
        x
        '''
        del bst[-300]
        with self.assertRaises(KeyNotFoundError):
            del bst[-300]
        self.assertEqual(0, bst.size())
        self.assertIsNone(bst.get(-300))
        self.assertFalse(-300 in bst)

if __name__ == "__main__":
    unittest.main()

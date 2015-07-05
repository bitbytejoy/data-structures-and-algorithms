from graph import Graph

class DFSGraph(Graph):
    def __init__(self):
        super(DFSGraph, self).__init__()
        self.time = 0
    def dfs(self):
        for v in self:
            v.color = "white"
            v.distance = 0
        for v in self:
            if v.color == "white":
                self.dfs_visit(v)
    def dfs_visit(self, vertex):
        vertex.color = "gray"
        self.time += 1
        vertex.discovery_time = self.time
        for n_key in vertex.neighbours:
            n = self.get_vertex(n_key)
            if n.color != "white":
                continue
            n.predecessor = vertex
            n.distance = vertex.distance + 1
            self.dfs_visit(n)
        vertex.color = "black"
        self.time += 1
        vertex.finish_time = self.time

import unittest
class DFSGraphTest(unittest.TestCase):
    def test_dfs(self):
        g = DFSGraph()
        '''
          A B C D E F
        A   x   x
        B     x x
        C
        D         x
        E   x       x
        F     x
        '''
        g.add_edge('A', 'B')
        g.add_edge('A', 'D')
        g.add_edge('B', 'C')
        g.add_edge('B', 'D')
        g.add_edge('D', 'E')
        g.add_edge('E', 'B')
        g.add_edge('E', 'F')
        g.add_edge('F', 'C')
        g.dfs()
        v = g.get_vertex('A')
        self.assertIsNone(v.predecessor)
        self.assertEqual(0, v.distance)
        self.assertEqual(1, v.discovery_time)
        self.assertEqual(12, v.finish_time)
        self.assertEqual("black", v.color)
        v = g.get_vertex('B')
        self.assertEqual('A', v.predecessor.key)
        self.assertEqual(1, v.distance)
        self.assertEqual(2, v.discovery_time)
        self.assertEqual(11, v.finish_time)
        self.assertEqual("black", v.color)
        v = g.get_vertex('C')
        self.assertEqual('B', v.predecessor.key)
        self.assertEqual(2, v.distance)
        self.assertEqual(3, v.discovery_time)
        self.assertEqual(4, v.finish_time)
        self.assertEqual("black", v.color)
        v = g.get_vertex('D')
        self.assertEqual('B', v.predecessor.key)
        self.assertEqual(2, v.distance)
        self.assertEqual(5, v.discovery_time)
        self.assertEqual(10, v.finish_time)
        self.assertEqual("black", v.color)
        v = g.get_vertex('E')
        self.assertEqual('D', v.predecessor.key)
        self.assertEqual(3, v.distance)
        self.assertEqual(6, v.discovery_time)
        self.assertEqual(9, v.finish_time)
        self.assertEqual("black", v.color)
        v = g.get_vertex('F')
        self.assertEqual('E', v.predecessor.key)
        self.assertEqual(4, v.distance)
        self.assertEqual(7, v.discovery_time)
        self.assertEqual(8, v.finish_time)
        self.assertEqual("black", v.color)

if __name__ == "__main__":
    unittest.main()


class Vertex:
	def __init__(self, key):
		self.key = key
		self.neighbours = {}
	def get_key(self):
		return self.key
	def add_neighbour(self, neighbour_key, weight = 0):
		self.neighbours[neighbour_key] = weight
	def get_neighbours(self):
		return self.neighbours.keys()
	def get_weight(self, neighbour_key):
		return self.neighbours.get(neighbour_key)
	def __str__(self):
		neighbours = str(self.neighbours.keys())
		return "{} connected to {}".format(self.key, neighbours)

class Graph:
	def __init__(self):
		self.vertices = {}
		self.vertices_count = 0
	def add_vertex(self, key):
		v = Vertex(key)
		self.vertices[key] = v
		self.vertices_count += 1
		return v
	def get_vertex(self, key):
		return self.vertices.get(key)
	def get_vertices(self):
		return self.vertices.keys()
	def add_edge(self, from_key, to_key, weight = 0):
		from_vertex = self.vertices.get(from_key)
		to_vertex = self.vertices.get(to_key)
		if from_vertex is None or to_vertex is None:
			raise VertexNotFoundError()
		from_vertex.add_neighbour(to_key, weight)
	def __contains__(self, key):
		return key in self.vertices
	def __iter__(self):
		return iter(self.vertices.values())

class VertexNotFoundError(Exception):
	pass

import unittest

class VertexTest(unittest.TestCase):
	def test_vertex(self):
		# { key:0, neighbours:{} }
		v = Vertex(0)
		self.assertEqual(0, v.get_key())
		self.assertEqual([], v.get_neighbours())
		self.assertIsNone(v.get_weight(1))
		# { key:0, neighbours:{1:1} }
		v.add_neighbour(1, 1)
		self.assertEqual(0, v.get_key())
		self.assertEqual([1], v.get_neighbours())
		self.assertEqual(1, v.get_weight(1))
		self.assertIsNone(v.get_weight(2))
		# { key:0, neighbours:{1:2} }
		v.add_neighbour(1, 2)
		self.assertEqual(0, v.get_key())
		self.assertEqual([1], v.get_neighbours())
		self.assertEqual(2, v.get_weight(1))
		self.assertIsNone(v.get_weight(2))
		# { key:0, neighbours:{1:2, 2:1} }
		v.add_neighbour(2, 1)
		self.assertEqual(0, v.get_key())
		connections = v.get_neighbours()
		for connection in connections:
			self.assertTrue(connection in [1, 2])
		self.assertEqual(2, v.get_weight(1))
		self.assertEqual(1, v.get_weight(2))
		self.assertIsNone(v.get_weight(3))

class GraphTest(unittest.TestCase):
	def test_graph(self):
		# Empty graph
		g = Graph()
		self.assertIsNone(g.get_vertex(0))
		self.assertEqual([], g.get_vertices())
		self.assertFalse(0 in g)
		'''
		  1 2 3
		1   1
		2     2
		3 3 4
		'''
		g.add_vertex(1)
		g.add_vertex(2)
		g.add_vertex(3)
		g.add_edge(1, 2, 1)
		g.add_edge(2, 3, 2)
		g.add_edge(3, 1, 3)
		g.add_edge(3, 2, 4)
		self.assertTrue(1 in g)
		self.assertTrue(2 in g)
		self.assertTrue(3 in g)
		self.assertFalse(4 in g)
		vertices = g.get_vertices()
		for vertex in vertices:
			self.assertTrue(vertex in [1, 2, 3])
		self.assertEqual([2], g.get_vertex(1).get_neighbours())
		self.assertEqual([3], g.get_vertex(2).get_neighbours())
		connections = g.get_vertex(3).get_neighbours()
		for connection in connections:
			self.assertTrue(connection in [1, 2])
		self.assertEqual(1, g.get_vertex(1).get_weight(2))
		self.assertEqual(2, g.get_vertex(2).get_weight(3))
		self.assertEqual(3, g.get_vertex(3).get_weight(1))
		self.assertEqual(4, g.get_vertex(3).get_weight(2))

if __name__ == "__main__":
	unittest.main()

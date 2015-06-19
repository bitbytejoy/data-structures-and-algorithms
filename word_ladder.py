from graph import Graph, Vertex
from queue import Queue

def build_graph(words):
	words_differed_by_a_letter = {}
	for word in words:
		for i in range(len(word)):
			word_with_wildcard = word[:i] + "_" + word[i + 1:]
			if word_with_wildcard in words_differed_by_a_letter:
				words_differed_by_a_letter[word_with_wildcard].append(word)
			else:
				words_differed_by_a_letter[word_with_wildcard] = [word]
	graph = Graph()
	for word_with_wildcard in words_differed_by_a_letter:
		for word1 in words_differed_by_a_letter[word_with_wildcard]:
			for word2 in words_differed_by_a_letter[word_with_wildcard]:
				if word1 != word2:
					graph.add_edge(word1, word2)
	return graph

def bfs(graph, start_vertex):
	start_vertex.distance = 0
	start_vertex.color = "gray"
	start_vertex.predecessor = None
	queue = Queue()
	queue.enqueue(start_vertex)
	while not queue.is_empty():
		vertex = queue.dequeue()
		for neighbour_key in vertex.get_neighbours():
			neighbour = graph.get_vertex(neighbour_key)
			if neighbour.color != "white":
				continue
			neighbour.distance = vertex.distance + 1
			neighbour.color = "gray"
			neighbour.predecessor = vertex
			queue.enqueue(neighbour)
		vertex.color = "black"

def traverse(graph, start_key, processor):
	vertex = graph.get_vertex(start_key)
	while vertex is not None:
		processor(vertex.key)
		vertex = vertex.predecessor

import unittest
class WordLadderTest(unittest.TestCase):
	def test_word_ladder(self):
		words = ["fool", "pool", "cool", "foil", "foul", "poll", "fail", "pole",
			     "pall", "pope", "pale", "page", "sale", "sage"]
		graph = build_graph(words)
		start_vertex = graph.get_vertex("fool")
		bfs(graph, start_vertex)
		expected = ["sage", "sale", "pale", "pole", "poll", "pool", "fool"]
		actual = []
		def processor(key):
			actual.append(key)
		traverse(graph, "sage", processor)
		self.assertEqual(expected, actual)

if __name__ == "__main__":
	unittest.main()

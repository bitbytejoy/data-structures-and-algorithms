from graph import Graph

def position_to_vertex_id(row, column, board_size):
	return row * board_size + column

def generate_next_moves(row, column, board_size):
	offsets = [(1, 2), (-1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1),
	           (-2, 1)]
	moves = []
	for offset in offsets:
		move = (row + offset[0], column + offset[1])
		if (move[0] < 0 or move[0] >= board_size or
			move[1] < 0 or move[1] >= board_size):
			continue
		moves.append(move)
	return moves

def generate_graph(board_size):
	graph = Graph()
	for row in range(board_size):
		for column in range(board_size):
			tile = position_to_vertex_id(row, column, board_size)
			moves = generate_next_moves(row, column, board_size)
			for move in moves:
				next_tile = position_to_vertex_id(move[0], move[1], board_size)
				graph.add_edge(tile, next_tile)
	return graph

def neighbours_keys_by_min_edges(graph, vertex_key):
	vertex = graph.get_vertex(vertex_key)
	neighbour_keys = vertex.get_neighbours()
	neighbours = []
	for neighbour_key in neighbour_keys:
		neighbour = graph.get_vertex(neighbour_key)
		neighbours.append((neighbour_key, len(neighbour.get_neighbours())))
	neighbours.sort(key=lambda k: k[1])
	return [e[0] for e in neighbours]

def knights_tour(graph, start_vertex_key, board_size, path = []):
	start_vertex = graph.get_vertex(start_vertex_key)
	start_vertex.color = "gray"
	path.append(start_vertex_key)
	if len(path) == board_size * board_size:
		return True
	done = False
	for neighbour_key in neighbours_keys_by_min_edges(graph, start_vertex_key):
		neighbour = graph.get_vertex(neighbour_key)
		if neighbour.color == "white":
			done = knights_tour(graph, neighbour_key, board_size, path)
			if not done:
				neighbour.color = "white"
				path.pop()
			else:
				return True
	return False

import unittest
class KnightsTourTest(unittest.TestCase):
	def test_knights_tour(self):
		# 4x4 board no solution
		board_size = 4
		graph = generate_graph(board_size)
		path = []
		start_vertex_key = position_to_vertex_id(0, 0, board_size)
		knights_tour(graph, start_vertex_key, board_size, path)
		self.assertEqual([start_vertex_key], path)
		# 5x5 board solution
		board_size = 5
		graph = generate_graph(board_size)
		path = []
		start_vertex_key = position_to_vertex_id(0, 0, board_size)
		knights_tour(graph, start_vertex_key, board_size, path)
		expected = [0, 11, 20, 17, 24, 13, 4, 7, 10, 1, 8, 19, 22, 15, 6, 3, 14,
		            23, 16, 5, 2, 9, 18, 21, 12]
		self.assertEqual(expected, path)
		# 8x8 board solution
		board_size = 8
		graph = generate_graph(board_size)
		path = []
		start_vertex_key = position_to_vertex_id(0, 0, board_size)
		knights_tour(graph, start_vertex_key, board_size, path)
		expected = [0, 17, 32, 49, 59, 53, 63, 46, 61, 55, 38, 23, 6, 12, 2, 8,
		            25, 40, 57, 51, 41, 56, 50, 60, 54, 39, 22, 7, 13, 3, 9, 24,
		            34, 19, 4, 14, 31, 37, 47, 62, 52, 58, 48, 33, 16, 1, 18,
		            35, 29, 44, 27, 10, 20, 5, 15, 30, 45, 28, 43, 26, 11, 21,
		            36, 42]
		self.assertEqual(expected, path)

if __name__ == "__main__":
	unittest.main()

class Maze:
    START = "S"
    EXIT = "E"
    WALKWAY = " "
    WALL = "x"
    def __init__(self, walls_file, tile_size):
        f = open(walls_file, "r")
        walls = f.read()
        f.close()
        self.map = []
        row = 0
        for i in range(0, len(walls)):
            c = walls[i]
            if i == 0:
                self.map.append([])
            if c == "\n":
                self.map.append([])
                row += 1
                continue
            if c == "F":
                break
            else:
                self.map[row].append(c)
        self.tile_size = tile_size
    def dimensions(self):
        return (len(self.map), len(self.map[0]))
    def is_walkway(self, coordinate):
        return self.map[coordinate[0]][coordinate[1]] == Maze.WALKWAY
    def is_wall(self, coordinate):
        return self.map[coordinate[0]][coordinate[1]] == Maze.WALL
    def is_exit(self, coordinate):
        return self.map[coordinate[0]][coordinate[1]] == Maze.EXIT
    def starting_tile(self):
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i])):
                if self.map[i][j] == Maze.START:
                    return (i, j)
    def _draw_square(self, turtle_brush, coordinate, color):
        corners = self._calculate_tile_corners(coordinate)
        turtle_brush.up()
        turtle_brush.goto(corners[0][0], corners[0][1])
        turtle_brush.color(color)
        turtle_brush.down()
        turtle_brush.begin_fill()
        for corner in corners:
            turtle_brush.goto(corner[0], corner[1])
        turtle_brush.end_fill()
        turtle_brush.up()
    def _calculate_tile_corners(self, coordinate):
        i = coordinate[0]
        j = coordinate[1]
        tile_width = self.tile_size
        tile_height = self.tile_size
        dimensions = self.dimensions()
        maze_height = dimensions[0] * tile_height
        maze_width = dimensions[1] * tile_width
        left_bound = -maze_width//2
        top_bound = maze_height//2
        nw_corner = (
            left_bound + j * tile_width,
            top_bound - i * tile_height
        )
        ne_corner = (
            left_bound + j * tile_width + tile_width,
            top_bound - i * tile_height
        )
        se_corner = (
            left_bound + j * tile_width + tile_width,
            top_bound - i * tile_height - tile_height
        )
        sw_corner = (
            left_bound + j * tile_width,
            top_bound - i * tile_height - tile_height
        )
        return [nw_corner, ne_corner, se_corner, sw_corner]
    def get_tile_midpoint(self, coordinate):
        corners = self._calculate_tile_corners(coordinate)
        nw_corner = corners[0]
        se_corner = corners[2]
        return (
            abs(nw_corner[0] - se_corner[0])//2 + nw_corner[0],
            abs(nw_corner[1] - se_corner[1])//2 + se_corner[1]
        )
    def draw(self, turtle_brush):
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i])):
                cell = self.map[i][j]
                if cell == Maze.WALL:
                    color = "orange"
                elif cell == Maze.WALKWAY:
                    color = "violet"
                elif cell == Maze.EXIT:
                    color = "green"
                elif cell == Maze.START:
                    color = "white"
                self._draw_square(turtle_brush, (i, j), color)
    def get_tile_size(self):
        return self.tile_size

class MazeExplorer:
    def __init__(self, maze, turtle_brush):
        self.maze = maze
        maze_dimensions = maze.dimensions()
        maze_height = maze_dimensions[0]
        maze_width = maze_dimensions[1]
        self.visited = []
        for i in range(0, maze_height):
            self.visited.append([False] * maze_width)
        self.movement_increment = maze.get_tile_size()
        starting_tile = maze.starting_tile()
        starting_coordinate = maze.get_tile_midpoint(starting_tile)
        turtle_brush.up()
        turtle_brush.goto(starting_coordinate[0], starting_coordinate[1])
        self.visited[starting_tile[0]][starting_tile[1]]
        self.position = starting_tile
        self.turtle_brush = turtle_brush
    def drop_breadcrumb(self, color):
        self.turtle_brush.dot(10, color)
    def goto_tile(self, coordinate):
        self.turtle_brush.up()
        tile_midpoint = self.maze.get_tile_midpoint(coordinate)
        self.turtle_brush.goto(tile_midpoint[0], tile_midpoint[1])
    def is_tile_visited(self, coordinate):
        return self.visited[coordinate[0]][coordinate[1]]
    def visit_tile(self, coordinate):
        self.visited[coordinate[0]][coordinate[1]] = True
    def find_exit(self, starting_position):
        if self.maze.is_exit(starting_position):
            return True
        northern_tile = (starting_position[0] - 1, starting_position[1])
        found = False
        if ((self.maze.is_walkway(northern_tile) or
            (self.maze.is_exit(northern_tile))) and
            not self.is_tile_visited(northern_tile) and
            not found):
            self.drop_breadcrumb("yellow")
            self.visit_tile(starting_position)
            self.goto_tile(northern_tile)
            found = self.find_exit(northern_tile)
        eastern_tile = (starting_position[0], starting_position[1] + 1)
        if ((self.maze.is_walkway(eastern_tile) or
            (self.maze.is_exit(eastern_tile))) and
            not self.is_tile_visited(eastern_tile) and
            not found):
            self.drop_breadcrumb("yellow")
            self.visit_tile(starting_position)
            self.goto_tile(eastern_tile)
            found = self.find_exit(eastern_tile)
        western_tile = (starting_position[0], starting_position[1] - 1)
        if ((self.maze.is_walkway(western_tile) or
            (self.maze.is_exit(western_tile))) and
            not self.is_tile_visited(western_tile) and
            not found):
            self.drop_breadcrumb("yellow")
            self.visit_tile(starting_position)
            self.goto_tile(western_tile)
            found = self.find_exit(western_tile)
        southern_tile = (starting_position[0] + 1, starting_position[1])
        if ((self.maze.is_walkway(southern_tile) or
            (self.maze.is_exit(southern_tile))) and
            not self.is_tile_visited(southern_tile) and
            not found):
            self.drop_breadcrumb("yellow")
            self.visit_tile(starting_position)
            self.goto_tile(southern_tile)
            found = self.find_exit(southern_tile)
        if found:
            self.goto_tile(starting_position)
            self.drop_breadcrumb("green")
        return found

import unittest
import os
import turtle
class MazeTest(unittest.TestCase):
    def test_maze_init(self):
        filename = "maze_walls.testdata"
        walls_file = open(filename, "w")
        content = (
            "xxxxx\n"
            "x   x\n"
            "x x x\n"
            "x xSx\n"
            "xExxxF"
        )
        walls_file.write(content)
        walls_file.close()
        maze = Maze(filename, 50)
        self.assertEqual((5, 5), maze.dimensions())
        self.assertTrue(maze.is_wall((3, 4)))
        self.assertTrue(maze.is_walkway((1, 1)))
        self.assertTrue(maze.is_exit((4, 1)))
        self.assertFalse(maze.is_exit((0, 0)))
        self.assertEqual((3, 3), maze.starting_tile())
        self.assertEqual((-100, 100), maze.get_tile_midpoint((0, 0)))
        turtle_brush = turtle.Turtle()
        slowest_speed = 1
        turtle_brush.speed(slowest_speed)
        screen = turtle.Screen()
        screen.tracer(0)
        maze.draw(turtle_brush)
        screen.tracer(1)
        maze_explorer = MazeExplorer(maze, turtle_brush)
        maze_explorer.find_exit(maze.starting_tile())
        turtle_brush.clear()
        walls_file = open(filename, "w")
        content = (
            "xxxxxxxxxxxxxxxxxxxxxExxxxxxxxxx\n"
            "x      xxx       xx            x\n"
            "x        xx xxxx  xxxxxxxx xxxxx\n"
            "x xSxx x          x    x       x\n"
            "x xxxx x          x xxxx       x\n"
            "x                              x\n"
            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxF"
        )
        walls_file.write(content)
        walls_file.close()
        maze = Maze(filename, 30)
        screen.tracer(0)
        maze.draw(turtle_brush)
        screen.tracer(1)
        maze_explorer = MazeExplorer(maze, turtle_brush)
        maze_explorer.find_exit(maze.starting_tile())
        os.remove(filename)
        screen.exitonclick()

if __name__ == "__main__":
    unittest.main()

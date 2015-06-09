def draw_triangle(points, turtle_brush, color):
    turtle_brush.up()
    turtle_brush.goto(points[0][0], points[0][1])
    turtle_brush.fillcolor(color)
    turtle_brush.down()
    turtle_brush.begin_fill()
    turtle_brush.goto(points[1][0], points[1][1])
    turtle_brush.goto(points[2][0], points[2][1])
    turtle_brush.goto(points[0][0], points[0][1])
    turtle_brush.end_fill()
    turtle_brush.up()

def mid_point(point1, point2):
    offset = point1[0] if point1[0] < point2[0] else point2[0]
    x_mid = abs(point1[0] - point2[0])/2 + offset
    offset = point1[1] if point1[1] < point2[1] else point2[1]
    y_mid = abs(point1[1] - point2[1])/2 + offset
    return (x_mid, y_mid)

def draw_sierpinski_triangle(points, depth, turtle_brush):
    colormap = ['yellow', 'orange', 'blue', 'red', 'violet', 'green', 'white']
    if depth <= 0:
        return
    color = colormap[depth % len(colormap)]
    draw_triangle(points, turtle_brush, color)
    subtriangle1 = [
        points[0],
        mid_point(points[0], points[1]),
        mid_point(points[0], points[2])
    ]
    draw_sierpinski_triangle(subtriangle1, depth - 1, turtle_brush)
    subtriangle2 = [
        points[1],
        mid_point(points[1], points[0]),
        mid_point(points[1], points[2])
    ]
    draw_sierpinski_triangle(subtriangle2, depth - 1, turtle_brush)
    subtriangle3 = [
        points[2],
        mid_point(points[2], points[0]),
        mid_point(points[2], points[1])
    ]
    draw_sierpinski_triangle(subtriangle3, depth - 1, turtle_brush)

import turtle
turtle_brush = turtle.Turtle()
screen = turtle.Screen()
starting_triangle_points = [(-100, -100), (100, -100), (0, 100)]
draw_sierpinski_triangle(starting_triangle_points, 4, turtle_brush)
screen.exitonclick()

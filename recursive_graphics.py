def draw_spiral(turtle_brush, line_length):
    if line_length == 0:
        return
    turtle_brush.forward(line_length)
    turtle_brush.right(90)
    draw_spiral(turtle_brush, line_length - 2)

def draw_tree(branch_length, turtle_brush):
    if branch_length < 5:
        return
    turtle_brush.forward(branch_length)
    turtle_brush.right(15)
    draw_tree(branch_length - 10, turtle_brush)
    turtle_brush.left(30)
    draw_tree(branch_length - 10, turtle_brush)
    turtle_brush.right(15)
    turtle_brush.backward(branch_length)

import turtle
brush = turtle.Turtle()
canvas = turtle.Screen()
# Spiral
brush.up()
brush.backward(300)
brush.left(90)
brush.down()
draw_spiral(brush, 50)
# Tree
brush.up()
brush.forward(300)
brush.right(90)
brush.backward(100)
brush.down()
draw_tree(50, brush)
canvas.exitonclick()

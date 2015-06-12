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

import random
def draw_tree_pretty(branch_length, turtle_brush):
    if branch_length < 2:
        return
    branch_width = branch_length // 5
    branch_color = "brown"
    if branch_length in range(1, 10):
        branch_color = "green"
        branch_width = branch_length
    rotation = random.randrange(15, 25, 1)
    turtle_brush.width(branch_width)
    turtle_brush.color(branch_color)
    turtle_brush.down()
    turtle_brush.forward(branch_length)
    turtle_brush.right(rotation)
    draw_tree_pretty(branch_length - random.randrange(5, 10, 1), turtle_brush)
    turtle_brush.left(rotation * 2)
    draw_tree_pretty(branch_length - random.randrange(5, 10, 1), turtle_brush)
    turtle_brush.up()
    turtle_brush.right(rotation)
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
brush.forward(150)
brush.right(90)
brush.backward(100)
brush.down()
draw_tree(50, brush)
# Pretty tree
brush.up()
brush.left(90)
brush.forward(300)
brush.left(90)
brush.backward(200)
fastest_brush_speed = 0
brush.speed(fastest_brush_speed)
brush.down()
draw_tree_pretty(60, brush)
canvas.exitonclick()

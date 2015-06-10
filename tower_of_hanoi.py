from stack import Stack
def pole_to_string(stack, size):
    tmp = Stack()
    stringed = ""
    while not stack.is_empty():
        tmp.push(stack.pop())
    while not tmp.is_empty():
        stringed += "{}".format(tmp.peek())
        stack.push(tmp.pop())
    stringed += "-" * size
    return stringed[0:size]

def solve_hanoi(height):
    poles = [Stack(), Stack(), Stack()]
    for i in range(0, height):
        poles[0].push("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[i])
    def move_disk(from_pole, to_pole, pole_height):
        poles[to_pole].push(poles[from_pole].pop())
        print "{}\n{}\n{}\n".format(
            pole_to_string(poles[0], pole_height),
            pole_to_string(poles[1], pole_height),
            pole_to_string(poles[2], pole_height))
    def move_tower(height, from_pole, to_pole, with_pole, pole_height):
        if height <= 0:
            return
        move_tower(height-1, from_pole, with_pole, to_pole, pole_height)
        move_disk(from_pole, to_pole, pole_height)
        move_tower(height-1, with_pole, to_pole, from_pole, pole_height)
    print "{}\n{}\n{}\n".format(
        pole_to_string(poles[0], height),
        pole_to_string(poles[1], height),
        pole_to_string(poles[2], height))
    move_tower(height, 0, 1, 2, height)

solve_hanoi(3)

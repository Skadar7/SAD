import turtle

turtle.speed('fastest')
screen = turtle.Screen()
undo = [(0, 0)]
redo = []


def line_func(x, y):
    turtle.goto(x, y)
    undo.append((x, y))


def undo_func():
    if len(undo) <= 1: return
    turtle.color('white')
    turtle.goto(undo[-2])
    redo.append(undo.pop(-1))
    turtle.color('black')
    print('undo')


def redo_func():
    turtle.goto(redo[-1])
    undo.append(redo.pop(-1))
    print('redo')


screen.onclick(line_func)
screen.onkey(undo_func, "u")
screen.onkey(redo_func, "r")
screen.listen()
screen.mainloop()
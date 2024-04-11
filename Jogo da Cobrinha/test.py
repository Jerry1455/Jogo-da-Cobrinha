from graphics import *

win = GraphWin("checkerboard", 400,400)
x, y = 0, 0
x2, y2 = 50, 50
numsquares = 64
obrec = Rectangle(Point(50,50), Point(0,0))

obrec.draw(win)
obrec.setFill("black")

for i in range(8):
    for j in range(8):
        grid = Rectangle(Point(x+50*i, y+50*j), Point(x2+50*i, y2+50*j))

grid.draw(win)

for count in range(numsquares):
    p1 = Point((((count // 64 ) + 1 * 50), ((numsquares // 8) + 1) * 50))
    p2 = Point((((count // 8) + 1) * 50), (50 *(numsquares // 8)))
    square = Rectangle(p1, p2)
    square.setFill("black")
square.draw(win)
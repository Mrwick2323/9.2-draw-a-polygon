from turtle import *
import math
sides=int(input('Think of a shape. How many sides does it have?'))
if sides!=4:
    print(f"Your shape is a{['n unknown shape!','n unknown shape!','n unknown shape!',' triangle!',' quadrilateral!',' Pentagon!',' Hexagon!'][sides]}") if sides<=6 else print('your shape is an unknown shape!')
else:
    if 'y' in input('does your shape have any parallel sides? ').lower():
        if 'y' in input('does your shape have two sets of parallel sides? ').lower():
            if 'y' in input('Are all sides the same length?').lower():
                print('Your shape is a square!')
                sides='s'
            if 'y' in input('are all the angles in your shape of equal measure?'):
                print('Your shape is a rectange!')
                sides='r'
            else:
                print('Your shape is a parallelogram!')
                sides='p'
        else:
            print('Your shape is a trapezoid!')
            sides='t'
    else:
        print('Your shape is an unknown quadrilateral!')
        sides='u'
screen=Screen()
turtle=Turtle()
turtle.speed(0)
turtle.pu()
def draw(turtle,s):
    if s=='s':
        s=4
    if type(s)==int:
        for i in range(s//2):
            turtle.left(360/s)
            turtle.forward(100)
        h=turtle.ycor()
        turtle.setpos(50,-h/2)
        turtle.pd()
        turtle.seth(0)
        for i in range(s):
            turtle.left(360/s)
            turtle.forward(100)
    elif s=='r':
        turtle.pu()
        turtle.setpos(-50,-25)
        turtle.pd()
        turtle.setpos(50,-25)
        turtle.setpos(50,25)
        turtle.setpos(-50,25)
        turtle.setpos(-50,-25)
    elif s=='p':
        turtle.pu()
        turtle.setpos(-50,-25)
        turtle.pd()
        turtle.setpos(50,-25)
        turtle.setpos(75,25)
        turtle.setpos(-25,25)
        turtle.setpos(-50,-25)
    elif s=='t':
        turtle.pu()
        turtle.setpos(-100,-25)
        turtle.pd()
        turtle.setpos(100,-25)
        turtle.setpos(75,25)
        turtle.setpos(-75,25)
        turtle.setpos(-100,-25)
    elif s=='u':
        turtle.pd()
        turtle.setpos(-100,-100)
        turtle.setpos(100,54)
        turtle.setpos(54,108)
        turtle.setpos(0,0)
draw(turtle,sides)
screen.mainloop()
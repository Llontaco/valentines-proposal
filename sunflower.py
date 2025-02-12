from turtle import *
from math import *

screen = Screen()
screen.title("Espero te guste, mi tortolita ❤️🌻") 
speed(0)
bgcolor("black")
goto(0,-40)

# Draw leaves
for i in range(16):
    for j in range(18):
        color('#FFA216'), rt(90)
        circle(150-j*6, 90), lt(90)
        circle(150-j*6, 90), rt(180)
    circle(40,24)

# Draw flower center
color('black') 
shape('circle')
shapesize(0.5)
fillcolor('#8B4513')
golden_ang = 137.508
phi = golden_ang*(pi/180)

for i in range(140):
    r = 4*sqrt(i)
    theta = i*phi
    x = r*cos(theta)
    y = r*sin(theta)
    penup(), goto(x, y)
    setheading(i*golden_ang)
    pendown(), stamp()

# Define points to draw letters
def point(x, y):
    penup(), goto(x, y), pendown()
    color('black'), fillcolor('#FFA216')
    begin_fill(), circle(4), end_fill()

# Function to draw 'A'
def draw_A(x, y):
    positions_a = [(x, y), (x+2, y+6), (x+4, y+12), (x+6, y+18),
             (x+8, y+24), (x+10, y+30),
             (x+12, y+24), (x+14, y+18), (x+16, y+12), (x+18, y+6),
             (x+20, y), (x+8, y+8), (x+12, y+8)]

    for pos in positions_a:
        point(*pos)

# Function to draw 'L'
def draw_L(x, y):
    positions_l = [(x, y+30), (x, y+24), (x, y+18), (x, y+12), (x, y+6),
                   (x, y), (x+4, y), (x+8, y), (x+12, y), (x+16, y)]

    for pos in positions_l:
        point(*pos)

# Function to draw 'E'
def draw_E(x, y):
    positions_e = [(x, y+30), (x, y+24), (x, y+18), (x, y+12), (x, y+6),
                   (x+4, y+30), (x+8, y+30), (x+12, y+30), (x+16, y+30),
                   (x+4, y+15), (x+8, y+15), (x+12, y+15), 
                   (x, y), (x+4, y), (x+8, y), (x+12, y), (x+16, y)]

    for pos in positions_e:
        point(*pos)

# Draw 'TÚ'
draw_A(-25, 0)
draw_L(10, 0)
draw_E(-5, -40)

hideturtle()
done()
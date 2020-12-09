# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# color_list = []
#
# for color in colors:
#     rgb = color.rgb
#     color_list.append((rgb.r, rgb.g, rgb.b))
#
# print(color_list)

import turtle as t
import random

INITIAL_X = -300
INITIAL_Y = -200
t.colormode(255)
turtle = t.Turtle()
turtle.speed("fastest")
turtle.penup()
turtle.setx(INITIAL_X)
turtle.sety(INITIAL_Y)
color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48),
              (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71),
              (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31),
              (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48),
              (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210),
              (65, 66, 56)]


for i in range(10):
    for j in range(10):
        turtle.color(random.choice(color_list))
        turtle.dot(20)
        turtle.penup()
        turtle.forward(50)
    INITIAL_Y += 50
    turtle.setx(INITIAL_X)
    turtle.sety(INITIAL_Y)

screen = t.Screen()
screen.exitonclick()

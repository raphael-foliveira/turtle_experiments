import turtle
from turtle import Turtle
from turtle import Screen
from random import choice, randint
from extract_colors import rgb_colors_list


color_list = ["blue", "red", "yellow3", "black", "green", "orange"]
heading_list = [0, 90, 180, 270]
turtle.colormode(255)
tim = Turtle()
tim.pensize(2)
tim.speed(0)


def draw_shape(num_of_sides):
    angle = 360 / num_of_sides
    tim.color(choice(color_list))
    for _ in range(num_of_sides):
        tim.forward(200)
        tim.right(angle)


def random_walk(num_of_steps, step_size):
    for _ in range(num_of_steps):
        color_tuple = (randint(0, 255), randint(0, 255), randint(0, 255))
        tim.color(color_tuple)
        tim.setheading(choice(heading_list))
        tim.forward(step_size)


def draw_spyrograph(steps):
    heading = 0
    for _ in range(360//steps):
        color_tuple = (randint(0, 255), randint(0, 255), randint(0, 255))
        tim.color(color_tuple)
        tim.circle(150)
        heading += steps
        tim.setheading(heading)


def make_painting(size, color, stepsize):
    tim.pu()
    tim.setpos(-300, -250)
    tim.setheading(0)
    for _ in range(10):
        for _ in range(20):
            tim.dot(size, choice(color))
            tim.forward(stepsize)
        tim.dot(size, choice(color))
        tim.setheading(90)
        tim.forward(stepsize)
        tim.setheading(180)
        for _ in range(20):
            tim.dot(size, choice(color))
            tim.forward(stepsize)
        tim.dot(size, choice(color))
        tim.setheading(90)
        tim.forward(stepsize)
        tim.setheading(0)


make_painting(20, rgb_colors_list, 30)


screen = Screen()
screen.exitonclick()

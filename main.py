import colorgram
from turtle import Turtle, Screen
import random

# Extract 100 colors from an image, add the rgb
colors = colorgram.extract('image.jpg', 1000)
color_list = [(color.rgb.r / 255, color.rgb.g / 255, color.rgb.b / 255) for color in colors]

champagnepapi = Turtle()
champagnepapi.up()
champagnepapi.shape('classic')
champagnepapi.speed(100)
champagnepapi.setx(-285)
champagnepapi.sety(-285)

for _ in range(40):
    for _ in range(40):
        color = random.choice(color_list)
        champagnepapi.color(color)
        champagnepapi.dot(10, color)
        champagnepapi.forward(15)

    champagnepapi.speed('fastest')
    champagnepapi.setx(-285)
    champagnepapi.sety(champagnepapi.ycor() + 15)
    champagnepapi.speed('slow')

champagnepapi.hideturtle()
screen = Screen()
screen.exitonclick()

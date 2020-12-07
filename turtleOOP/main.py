# from turtle import Turtle, Screen
#
#
# kasu_the_turtle = Turtle()
# kasu_the_turtle.shape("turtle")
# kasu_the_turtle.color("purple")
# kasu_the_turtle.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

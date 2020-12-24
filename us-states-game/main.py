from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("US state game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
correct_count = 0
is_game_on = True
while is_game_on:
    guess = screen.textinput(title="Guess the state", prompt="Guess names of US state!!")
    guess = guess.title()
    if guess in state_list:
        correct_count =
        new_turtle = Turtle()
        new_turtle.speed("slow")
        new_turtle.hideturtle()
        new_turtle.penup()
        state_data = data[data.state == guess]
        new_turtle.goto(int(state_data.x), int(state_data.y))
        new_turtle.write(guess)

screen.mainloop()

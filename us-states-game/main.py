from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("US state game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
correct_guess_list = []
learn_list = []
is_game_on = True

while is_game_on:
    guess = screen.textinput(title=f"{len(correct_guess_list)}/50 state correct", prompt="Guess names of US state!!")
    guess = guess.title()
    if guess == "Exit":
        break
    if guess in state_list:
        correct_guess_list.append(guess)
        new_turtle = Turtle()
        new_turtle.speed("slow")
        new_turtle.hideturtle()
        new_turtle.penup()
        state_data = data[data.state == guess]
        new_turtle.goto(int(state_data.x), int(state_data.y))
        new_turtle.write(guess)
    if len(correct_guess_list) == 50:
        is_game_on = False

for state in state_list:
    if state not in correct_guess_list:
        learn_list.append(state)

learn_dict = {
    "States": learn_list
}
df = pandas.DataFrame(learn_dict)
df.to_csv("to_learn.csv")
screen.mainloop()

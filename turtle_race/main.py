import turtle as t
import random

START_X = -300
FINISH_X = 300
COLORS = ["red", "blue", "green", "purple", "yellow"]
Y_POS = [-200, -100, 0, 100, 200]
screen = t.Screen()
screen.setup(width=650, height=600)
bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race?Red, Blue, Green, "
                                                  "Purple, Yellow")
bet = bet.lower()
turtle_list = []

for i in range(5):
    turtle = t.Turtle()
    turtle.color(COLORS[i])
    turtle.shape("turtle")
    turtle.penup()
    turtle.sety(Y_POS[i])
    turtle.setx(START_X)
    turtle_list.append(turtle)


def race():
    are_racing = True
    while are_racing:
        for tur in turtle_list:
            if tur.xcor() >= FINISH_X:
                are_racing = False
                print(f"Winner is {tur.color()[0]}")
                if bet == tur.color()[0]:
                    print(f"You bet: {bet}. You win!!")
                else:
                    print(f"You bet: {bet}. You loose!!")
                break
            else:
                tur.forward(random.randint(1, 10))


race()
screen.exitonclick()

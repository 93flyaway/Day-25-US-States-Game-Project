import turtle
import pandas

FONT = ("Courier", 10, "normal")

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

drawing_tool = turtle.Turtle()
drawing_tool.penup()
drawing_tool.hideturtle()
data = pandas.read_csv("50_states.csv")
answer_state = screen.textinput(title="Guess the State", prompt="Guess a state's name?").title()
correct_guesses = []
all_states = data.state.to_list()

while len(correct_guesses) < 50:
    if len(correct_guesses) != 0:
        answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                        prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    for state in data.state:
        if answer_state == state:
            if state not in correct_guesses:
                correct_guesses.append(state)
                relevant_row = data[data.state == state]
                drawing_tool.goto(x=relevant_row.x.item(), y=relevant_row.y.item())
                drawing_tool.write(arg=state, align="center", font=FONT)

for state in correct_guesses:
    all_states.remove(state)
missing_states = {
    "states": all_states
}
missing_states_df = pandas.DataFrame(missing_states)
# noinspection PyTypeChecker
missing_states_df.to_csv("missing_states.csv")

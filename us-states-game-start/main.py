import pandas
import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
t.shape(image)

states_df = pandas.read_csv("50_states.csv")


pen = turtle.Turtle()
pen.up()
pen.hideturtle()
guessed_states = []


while True:
    answer_state = screen.textinput(
        title="Guess A State", prompt=f"Type your state here. {len(guessed_states)}/{len(states_df.state)}")
    if answer_state == None:
        not_guessed = [x for x in states_df.state.values if x not in guessed_states]
        df = pandas.DataFrame(not_guessed)
        df.to_csv("study_these_states.csv")
        break
    answer_state = answer_state.title()
    if answer_state in states_df.state.values:
        row = states_df[states_df.state == answer_state]
        pen.goto(int(row.x), int(row.y))
        pen.write(answer_state)
        guessed_states.append(answer_state)


import turtle
import pandas

screen=turtle.Screen()
screen.title("Indian States")
image="india-map-gif-7.gif"
screen.addshape(image)

turtle.shape(image)
data=pandas.read_csv("States.csv")
states=data["State"].to_list()
guessed_states=[]
while len(guessed_states)<30:
    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 States Correct",prompt="What's state's name?").title()
    if answer_state=="Exit" or answer_state=="exit":
        missed_states=[state for state in states if state not in guessed_states]
        missed_data=pandas.DataFrame(missed_states)
        missed_data.to_csv("Missed_data.csv")
        break
#Compare answer
    if answer_state in states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.State==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)







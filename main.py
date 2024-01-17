import turtle
import pandas

screen = turtle.Screen()
image_path = "blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)
data = pandas.read_csv("50_states.csv")
states = data["state"].tolist()

all_states_found = False

while all_states_found == False:
    user_answer = screen.textinput(title="Guess a state", prompt="Type a state(Type 'exit' to exit.)")
    if user_answer.lower() == "exit":
        break
    for state in states:
        if str(state).lower() == user_answer.lower():
            row = data[data["state"] == state]
            x_cor = int(row.x.iloc[0])
            y_cor = int(row.y.iloc[0])
            write_turtle = turtle.Turtle()
            write_turtle.hideturtle()
            write_turtle.penup()
            write_turtle.goto(x_cor,y_cor)
            write_turtle.write(arg= user_answer,move=False, align="center", font=("Calibri",11,"normal"))
            states.remove(state)
            break
    if len(states) < 1:
        all_states_found = True
data_frame = pandas.DataFrame(states)
data_frame.to_csv("missed_states.csv")
if(all_states_found):
    end_turtle= turtle.Turtle()
    end_turtle.penup()
    end_turtle.hideturtle()
    end_turtle.goto(0,0)
    end_turtle.write(arg="You guessed every state correctly, well done!", move= False, align="center",font=("calibri",20,"bold"))
else:
    end_turtle = turtle.Turtle()
    end_turtle.penup()
    end_turtle.hideturtle()
    end_turtle.goto(0, 0)
    end_turtle.write(arg="You could not guessed all of them:( \n Check the created cvs file to see what states you missed.", move=False, align="center",
                     font=("calibri", 20, "bold"))
screen.exitonclick()

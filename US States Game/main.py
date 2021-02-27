#turle module only works with .gif  image extension
from turtle import Screen,Turtle
import pandas

screen=Screen()
turtle=Turtle()
tim=Turtle()

screen.title("U.S. States Game")
image="e:/Python Tutorials/programs/app brewery/Working with CSV Data and the Pandas Library/US States Game/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

tim.hideturtle()
tim.speed("fastest")

guesses=[]
#GIVES US THE CO-ORDINATES WHERE WE CLICK
# def get_mouse_click_coordinates(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coordinates)
# turtle.mainloop() #is the alternative of "exitonclick()" function.

data=pandas.read_csv("e:/Python Tutorials/programs/app brewery/Working with CSV Data and the Pandas Library/US States Game/50_states.csv")

states=data["state"].to_list()  #list

while len(guesses)<50:
    answer_state=screen.textinput(f"{len(guesses)}/50 States Correct" ,"What's the another state's name?").title()
    
    if answer_state=="Exit" or answer_state=="0" :
        # missing_states=[]
        # for state in states:
        #     if state not in guesses:
        #        missing_states.append(state)
        
        missing_states=[state for state in states if state not in guesses]
        new_data=pandas.DataFrame(missing_states)
        new_data.to_csv("remaining_states.csv")
        break

    if answer_state in states:
        guesses.append(answer_state) 
        x_cor=int(data[data["state"]==answer_state].x)
        y_cor=int(data[data["state"]==answer_state].y)
        tim.goto(x_cor,y_cor)
        tim.write(answer_state)


screen.exitonclick()
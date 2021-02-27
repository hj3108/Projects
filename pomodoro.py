#pomodora basically means tomato in italian.
#This technique uses a timer to break down work into intervals separated by short breaks.

import tkinter as tk
from tkinter import *
import time
import math
from tkinter import ttk
# from win10toast import ToastNotifier
from plyer import notification

# toast = ToastNotifier()

window=tk.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg="gold")
window.resizable(width=False,height=False)
window.iconbitmap("tomato.ico")

#Combobox
time_entry=ttk.Combobox(width=45,state='readonly')
time_entry['values']=("20","25","30","40","50","55","60","70","75","80","85","90")
time_entry.current(1)
time_entry.grid(row=0,column=1,columnspan=2,pady=2)

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = int(time_entry.get())
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer=None

#IN CANVAS WE USE "itemconfig()" to make change in canvas unlike just "config()" like in label.

def notifyMe(title,message):
    notification.notify(
        title=title,
        message=message,
        app_icon="tomato.ico",
        timeout=20 # time for the notification
    )

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    """Helps to rest timer back to Zero(0)."""
    window.after_cancel(timer) #stops the timer there only.
    canvas.itemconfig(timer_text,text="00:00")
    text_label.config(text="Timer",fg=GREEN)
    tick_label.config(text="")
    reps=0 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    """Helps to start the timer."""
    WORK_MIN = int(time_entry.get())
    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_break_sec=round(SHORT_BREAK_MIN*60,0)
    long_break_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        count_down(long_break_sec)  #get hold of seconds
        text_label.config(text="Break",fg=RED)
        # toast.show_toast("Pomodoro","It's your break time.",duration=20,icon_path="tomato.ico")
        notifyMe("Pomodoro","It's your long break time.Now you can relax!!")

    elif reps%2==0:
        count_down(short_break_sec)
        text_label.config(text="Break",fg=PINK)
        notifyMe("Pomodoro","It's your short break time.")
        
    elif reps==1:
        count_down(work_sec)
        text_label.config(text="Work",fg=GREEN)
        notifyMe("Pomodoro","You can start your work now.")

    else:
        count_down(work_sec)
        text_label.config(text="Work",fg=GREEN)
        notifyMe("Pomodoro","Now it's time to work again.")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    """Helps in managing timer."""
    global reps

    count_min= math.floor(count/60)
    count_sec=count%60

    if len(str(count_sec))<2:   #Dynamic Typing i.e. if we assign a variable with an int value and we can also dynamically change the datatype of the variable.
        count_sec="0"+str(count_sec)
    
    if len(str(count_min))<2:   #Dynamic Typing i.e. if we assign a variable with an int value and we can also dynamically change the datatype of the variable.
        count_min="0"+str(count_min)

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")

    if count>0:  #so that count value didn't get to below 0.
        global timer
        timer=window.after(1000,count_down, count-1)
    else:  #count=0
        start_timer()
        marks=""
        # work_sessions=math.floor(reps/2)
        # for _ in range (work_sessions):
        #     marks+="✔"
        # tick_label["text"]=marks
        for _ in range (int(reps/2)):
            marks+="✔"
        tick_label["text"]=marks


# ---------------------------- UI SETUP ------------------------------- #

# window=tk.Tk()
# window.title("Pomodoro")
# window.config(padx=100,pady=50,bg="gold")


# #Combobox
# time_entry=ttk.Combobox(width=45,state='readonly')
# time_entry['values']=("25","30","40","50")
# time_entry.current(1)
# time_entry.grid(row=0,column=1,columnspan=2,pady=2)

#Canvas
canvas=Canvas(width=200,height=224,bg="gold",highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=1)
# count_down(5)


#Labels
text_label=tk.Label(text="Timer", font=(FONT_NAME, 50,"bold"),fg=GREEN,bg="gold")
text_label.grid(row=1,column=1)

tick_label=tk.Label(font=("Arial", 20 ,"bold"),fg=GREEN,bg="gold")
tick_label.grid(row=4,column=1)

work_label=tk.Label(font=("Arial", 10 ,"bold"),fg="purple4",bg="gold",text="Set Work Time: ")
work_label.grid(row=0,column=0,padx=2)


#Buttons
start_button=tk.Button(text="Start",command=start_timer,bg="magenta",fg="blue4")
start_button.grid(row=3,column=0)

reset_button=tk.Button(text="Reset",command=reset_timer,bg="magenta",fg="blue4")
reset_button.grid(row=3,column=2)


window.mainloop()
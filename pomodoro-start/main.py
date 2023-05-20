from tkinter import *
import math
import pygame.mixer

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 45
SHORT_BREAK_MIN = 15
LONG_BREAK_MIN = 60

reps = 0
timer = None
remaining_time = None

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    checkmark.config(text="")
    status.config(text="Timer")
    

def countdown(count):
    mins = math.floor(count / 60)
    secs = f"{(count % 60):02}"
    canvas.itemconfig(timer_text, text=f"{mins}:{secs}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        checks = ""
        session = math.floor(reps/2)
        for _ in range(session):
            checks += " √"
        checkmark.config(text=checks)
        sound = pygame.mixer.Sound("/Users/bryangwin/Projects/python_projects/pomodoro-start/body-language_ah_vocals_one_shot_.wav.wav")
        sound.play()


def start_timer():
    global reps
    reps += 1
    if reps < 9 and reps in [1, 3, 5, 7]:
        status.config(text="Timer")
        countdown(WORK_MIN * 60)
    elif reps < 9 and reps in [2, 4, 6]:
        status.config(text="Break")
        countdown(SHORT_BREAK_MIN * 60)
    elif reps == 8:
        status.config(text="Break")
        countdown(LONG_BREAK_MIN * 60)




window = Tk()
pygame.mixer.init()

window.title("Work Timer")
canvas = Canvas(width=1000, height=1000)
clock_img = PhotoImage(file="/Users/bryangwin/Projects/python_projects/pomodoro-start/blankclock.png")
canvas.create_image(505, 500, image=clock_img)
timer_text = canvas.create_text(500, 500, text="00:00", font=(FONT_NAME, 100, "bold"))
canvas.pack()

status = Label(text="Timer", font=(FONT_NAME, 75, "bold"))
status.place(x=400, y=275)


checkmark = Label(text="", font=(FONT_NAME, 50,"bold"))
checkmark.place(x=400, y=725)


start = Button(text="Start", height=3, width=9, command=start_timer)
start.place(x=300, y=650)
reset = Button(text="Reset", height=3, width=9, command=reset_timer)
reset.place(x=600, y=650)

window.mainloop()




from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


LANG_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

csv_file = pandas.read_csv("data/french_words.csv")
dict = csv_file.to_dict(orient="records")




card_drawn = None


def new_flashcard():
    if len(dict) > 0:
        global card_drawn, timer
        window.after_cancel(timer)
        canvas.itemconfig(card_image, image=front_card)
        card_drawn = random.choice(dict)
        # print(card_drawn)
        canvas.itemconfig(language, text=f"{list(card_drawn.keys())[0]}")
        canvas.itemconfig(word, text=f"{card_drawn['French']}")
        timer = window.after(3000, flip_card)
        

    else:
        messagebox.showinfo("Info", "You have gone through all the words!")
        


def flip_card():
    canvas.itemconfig(card_image, image=back_card)
    canvas.itemconfig(language, text=f"{list(card_drawn.keys())[1]}", fill="white")
    canvas.itemconfig(word, text=f"{card_drawn['English']}", fill="white")

def remove_word():
    dict.remove(card_drawn)
    print(dict)
    
def right_button():
    remove_word()
    new_flashcard()
 

window = Tk()
timer = window.after(3000, flip_card)
window.title("Flashy")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)
canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, borderwidth=0, highlightthickness=0)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")
card_image = canvas.create_image(403, 280, image=front_card)
canvas.grid(column=0, row=0, columnspan=2)
language = canvas.create_text(403, 170, text="Language", font=LANG_FONT, fill="black")
word = canvas.create_text(403, 320, text="Word", font=WORD_FONT, fill="black")
timer_text = canvas.create_text(650,150, text="", font=("Arial", 100, "bold"), fill="gray")
canvas.itemconfig(card_image, image=front_card)

right_button = Button(image=right_img, borderwidth=0, highlightthickness=0, command=right_button)
right_button.grid(column=1, row=1)

wrong_button = Button(image=wrong_img, borderwidth=0, highlightthickness=0,relief=FLAT, command=new_flashcard)
wrong_button.grid(column=0, row=1)

new_flashcard()


window.mainloop()
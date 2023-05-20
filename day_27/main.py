import tkinter

def button_click():
    user_miles = entry.get()
    converted = int(user_miles) * 1.60934
    answer.config(text=round(converted, 2))

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)



label = tkinter.Label(text="is equal to")
label.grid(column=1, row=2)

button = tkinter.Button(text="Calculate", command=button_click)
button.grid(column=2, row=3)

miles = tkinter.Label(text="Miles")
miles.grid(column=3, row=1)

km = tkinter.Label(text="Km")
km.grid(column=3, row=2)

answer = tkinter.Label(text=0)
answer.grid(column=2, row=2)

entry = tkinter.Entry()
entry.grid(column=2, row=1)






window.mainloop()
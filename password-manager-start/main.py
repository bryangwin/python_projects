import string
import random
from tkinter import * 
from tkinter import messagebox
import json

FONT = ("Arial", 14, "normal")

def generate_password(length=12):
    """Uses random and string modules to generate a password."""
    characters = string.ascii_lowercase + \
        string. ascii_uppercase + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    print(type(password))
    entry_text.set(password)
    
def search_websites():
    ws = website_entry.get()
    try:
        with open("stored_data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo("Info", "No storage file has been created yet. Generate and add your first password to create the file.")
    else:
        if ws in data:
            pw = data[ws]["password"]
            un = data[ws]["email"]
            messagebox.showinfo(title="Password", message=f"Email: {un}\nPassword: {pw}")
        else:
            messagebox.showinfo("Does Not Exist", "That website was not found in your list of websites.")


def save_password():
    '''This will save your password to a text file.'''
    new_pw = password_entry.get()
    new_website = website_entry.get()
    new_un = email_entry.get()
    new_data = {
        new_website: {
            "email": new_un,
            "password": new_pw,
             }
        }

    if len(new_website) == 0 or len(new_pw) == 0:
        messagebox.showinfo(message="Please don't leave any fields empty!")
    else:
        try:
            with open("stored_data.json", "r") as data_file:
                saved_data = json.load(data_file)
        except FileNotFoundError:
            with open("stored_data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4 )
        else:
            saved_data.update(new_data)
            with open("stored_data.json", "w") as data_file:
                json.dump(saved_data, data_file, indent=4 )
        
    password_entry.delete(0, END)
    website_entry.delete(0, END)



window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(121, 100, image=lock_img)
canvas.grid(column=1, row=0)

entry_text = StringVar()

website = Label(text="Website:", font=FONT)
website.grid(column=0, row=1)

email_un = Label(text="Email/Username:", font=FONT)
email_un.grid(column=0, row=2)

pw = Label(text="Password:", font=FONT)
pw.grid(row=3, column=0)

website_entry = Entry()
website_entry.configure(width=22)
website_entry.grid(column=1, row=1,)
website_entry.focus()

email_entry = Entry()
email_entry.configure(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "bryangwin@gmail.com")

password_entry = Entry(textvariable=entry_text)
password_entry.configure(width=22)
password_entry.grid(column=1, row=3)

search_button = Button(text="Search", command=search_websites)
search_button.config(width=13)
search_button.grid(column=2, row=1)

gen_button = Button(text="Generate Password", command=generate_password)
gen_button.grid(column=2, row=3)

add = Button(text="Add", command=save_password)
add.configure(width=37)
add.grid(column=1, columnspan=2, row=4)

window.mainloop()

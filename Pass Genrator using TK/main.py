# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import json
from random import choice, randint, shuffle
import pyperclip

def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letter + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #   password += char
    password_label_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = web_entry.get()
    email = user_name_entry.get()
    password = password_label_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="please fill these blocks...")

    else:
        it_ok = messagebox.askokcancel(title="WebSite", message=f"These are details are you filled:\n{email}"
                                                         f"\nPassword: {password} \n Is it ok to save?")
        if it_ok:
            # with open("data.txt", "a") as data_file:
            #     data_file.write(f"{website} | {email} | {password}\n")
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                web_entry.delete(0, END)
                password_label_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)

user_name = Label(text="Email/Username: ")
user_name.grid(row=2, column=0)
user_name_entry = Entry(width=35)
user_name_entry.grid(row=2, column=1, columnspan=2)
user_name_entry.insert(0, "rushiG@gmail.com")

password_label = Label(text="Password: ")
password_label.grid(row=3, column=0)
password_label_entry = Entry(width=12)
password_label_entry.grid(row=3, column=1)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

gen_pass_btn = Button(text="Generate Password", width=18, command=generate_pass)
gen_pass_btn.grid(row=3, column=2)

add_pass_btn = Button(text="Add", width=30, command=save)
add_pass_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()
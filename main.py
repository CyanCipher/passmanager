from tkinter import *
from tkinter import messagebox
import random


# -------------------------------- Show Saved Passwords ----------------------------------#
PASSWORD = "abcd"


def show_list():
    window2 = Tk()
    window2.title("List")
    window2.minsize(400, 400)
    window2.config(padx=10, pady=5)

    def get_pass():
        with open("data.txt", "r") as file:
            for line in file:
                line_list = list(map(str, line.split(' | ')))
                pass_list.insert(END, f"{line_list[0]}\n")
                pass_list.insert(END, f"______> {line_list[1]}\n")
                pass_list.insert(END, f"______> {line_list[2]}\n")
                pass_list.insert(
                    END, "-------------------------------------\n")

    def pass_check():
        global PASSWORD
        password = pass_input.get()

        if password == PASSWORD:
            # Clearing all of the available text to avoid overwriting.
            pass_list.delete("1.0", "end")
            get_pass()
        else:
            messagebox.showerror(title="Oops!!!", message="Wrong Password")

    label = Label(window2, text="Please enter the password.",
                  font=("Courier", 10, "normal"))
    label.grid(column=0, row=0)

    pass_input = Entry(window2)
    pass_input.grid(column=1, row=0)

    ok_btn = Button(window2, text="Ok", command=pass_check)
    ok_btn.grid(column=2, row=0)
    ok_btn.config(padx=5)

    pass_list = Text(window2, width=60, height=25)
    pass_list.grid(column=0, row=1, columnspan=3)

    window2.mainloop()


# -------------------------------- ABOUT SECTION ----------------------------------#

def info():
    messagebox.showinfo(
        title="About", message="This product is designed and developed by Cyan Cipher...")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
           'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
characters = ['!', '@', '#', '%', '^', '&', '*', '(', ')']


def generator_rand():
    letterrand = random.randrange(4, 8)
    numberrand = random.randrange(4, 7)
    chararand = random.randrange(4, 7)

    letter_list = [random.choice(letters) for n in range(letterrand)]
    number_list = [random.choice(numbers) for n in range(numberrand)]
    character_list = [random.choice(characters) for n in range(chararand)]

    password_list1 = letter_list + number_list + character_list
    random.shuffle(password_list1)
    password = "".join(password_list1)
    password_input.delete(0, END)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    with open("data.txt", "a") as file:
        site = website_input.get()
        uname = username_input.get()
        password = password_input.get()

        if len(site) == 0 or len(uname) == 0 or len(password) == 0:
            messagebox.showerror(
                title="Oops!!!", message="Please don't leave any fields empty.")
        else:
            is_ok = messagebox.askokcancel(
                title="Save the details?", message=f"These are the details:\n Website: {site}\n Username: {uname}\n Password: {password}")

            if is_ok:
                text = f"{site} | {uname} | {password}\n"
                file.write(text)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=240, height=210)
photo = PhotoImage(file="logo.png")
canvas.create_image(120, 105, image=photo)
canvas.grid(column=1, row=1)

website_label = Label(text="Website", font=("Courier", 12, "normal"))
website_label.grid(column=0, row=2)

website_input = Entry(width=60)
website_input.grid(column=1, row=2, columnspan=2)

username_label = Label(text="Email/Username", font=("Courier", 12, "normal"))
username_label.grid(column=0, row=3)

username_input = Entry(width=60)
username_input.grid(column=1, row=3, columnspan=2)

password_label = Label(text="Password", font=("Courier", 12, "normal"))
password_label.grid(column=0, row=4)

password_input = Entry(width=41)
password_input.grid(column=1, row=4)

generator = Button(text="Generate Password", command=generator_rand)
generator.grid(column=2, row=4)

add_button = Button(text="Add", width=51, command=save)
add_button.grid(column=1, row=5, columnspan=2)

info_button = Button(text="ⓘ", font=(
    "Aerial", 12, "bold"), fg="blue", command=info)
info_button.grid(column=2, row=0)
info_button.config(padx=30)

show_list_button = Button(text="≡", font=(
    "Aerial", 14, "bold"), fg="blue", width=5, height=1, command=show_list)
show_list_button.grid(column=0, row=0)

window.mainloop()

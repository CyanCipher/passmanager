from tkinter import *
from tkinter import messagebox
import random
import json


# -------------------------------- Show Saved Passwords ----------------------------------#
PASSWORD = "abcd"


def overwrite():
    ask_win = Tk()
    ask_win.title("Please confirm...")
    ask_win.config(background="black")
    ask_win.minsize(width=100, height=100)
    ask_win.resizable(0,0)
    proceed_ans = 0

    def destruct():
        ask_win.destroy()

    def proceed():
        ask_win.destroy()

        site = website_input.get().lower()

        with open("data.json", "r") as file:
            data = json.load(file)
            for line in data.items():
                if line[0] == site:
                    data.pop(line[0])
                    with open("data.json", "w") as file:
                        json.dump(data, file, indent=4)
                        break

        save()

    prompt = Label(ask_win, text="The following site is already available in the database,\n do you want to overwrite the data?", font=(
        "Courier", 12, "normal"), background="black", fg="white")
    prompt.grid(row=0, column=0, columnspan=2)

    proceed_btn = Button(ask_win, text="OK", width=10,
                         command=proceed, background="grey", fg="white")
    proceed_btn.grid(row=1, column=0)
    proceed_btn.config(pady=5)

    cancel_btn = Button(ask_win, text="Cancel", width=10,
                        command=destruct, background="grey", fg="white")
    cancel_btn.grid(row=1, column=1)
    cancel_btn.config(pady=5)

    ask_win.mainloop()

    return proceed_ans


def check_site():
    is_available = False
    site = website_input.get().lower()
    to_go = 1

    with open("data.json", "r") as file:
        data = json.load(file)
        for line in data.items():
            if site == line[0]:
                is_available = True

    if is_available:
        to_go = overwrite()

    return to_go


def show_list():
    window2 = Tk()
    window2.title("List")
    window2.minsize(400, 400)
    window2.config(padx=10, pady=5, background="black")
    window2.resizable(0,0)

    def get_pass():
        with open("data.json", "r") as file:
            data = json.load(file)
            for line in data.items():
                uname = line[1]["Username"]
                passw = line[1]["Password"]
                pass_list.insert(END, f"{line[0]}\n")
                pass_list.insert(END, f"______> {uname}\n")
                pass_list.insert(END, f"______> {passw}\n")
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
                  font=("Courier", 10, "bold"), background="black", fg="white")
    label.grid(column=0, row=0)

    pass_input = Entry(window2, background="grey", fg="black")
    pass_input.grid(column=1, row=0)

    ok_btn = Button(window2, text="Ok", command=pass_check,
                    background="grey", fg="white")
    ok_btn.grid(column=2, row=0)
    ok_btn.config(padx=5)

    pass_list = Text(window2, width=60, height=25, background="light grey", font=(
        "Courier", 12, "bold"), fg="black")
    pass_list.grid(column=0, row=1, columnspan=3)

    window2.mainloop()


def search():
    with open("data.json", "r") as file:
        data = json.load(file)
        try:
            search_item = website_input.get().lower()
            uname = data[search_item]["Username"]
            passwd = data[search_item]["Password"]

            username_input.delete(0, END)
            password_input.delete(0, END)
            username_input.insert(0, uname)
            password_input.insert(0, passwd)

        except KeyError:
            messagebox.showerror(title="Password Not Found!",
                                 message="Please check the search item.")


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
    site = website_input.get().lower()
    uname = username_input.get()
    password = password_input.get()

    new_data = {
        site: {
            "Username": uname,
            "Password": password
        },
    }

    if len(site) == 0 or len(uname) == 0 or len(password) == 0:
        messagebox.showerror(
            title="Oops!!!", message="Please don't leave any fields empty.")
    else:
        try:
            if check_site():
                with open("data.json", "r") as file:
                    data = json.load(file)
                    data.update(new_data)

                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

                website_input.delete(0, END)
                username_input.delete(0, END)
                password_input.delete(0, END)

        except json.JSONDecodeError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, background="black")
window.resizable(0,0)
canvas = Canvas(width=240, height=210, background="black",
                highlightthickness=0, highlightbackground="black")
photo = PhotoImage(file="cc1.png")
canvas.create_image(120, 105, image=photo)
canvas.grid(column=1, row=1)

website_label = Label(text="Website :", font=(
    "Courier", 14, "bold"), fg="white", bg="black")
website_label.grid(column=0, row=2)

website_input = Entry(width=40, background="light grey",
                      fg="black", font=("Crourier", 8, "bold"))
website_input.grid(column=1, row=2)

search_btn = Button(text="Search", width=15, command=search,
                    background="grey", fg="white")
search_btn.grid(column=2, row=2)

username_label = Label(text="Email/Username :",
                       font=("Courier", 14, "bold"), fg="white", bg="black")
username_label.grid(column=0, row=3)

username_input = Entry(width=60, background="light grey",
                       fg="black", font=("Crourier", 8, "bold"))
username_input.grid(column=1, row=3, columnspan=2)

password_label = Label(text="Password", font=(
    "Courier", 14, "bold"), fg="white", bg="black")
password_label.grid(column=0, row=4)

password_input = Entry(width=41, background="light grey",
                       fg="black", font=("Crourier", 8, "bold"))
password_input.grid(column=1, row=4)

generator = Button(text="Generate Password",
                   command=generator_rand, background="grey", fg="white")
generator.grid(column=2, row=4)

add_button = Button(text="Add", width=51, command=save,
                    background="grey", fg="white")
add_button.grid(column=1, row=5, columnspan=2)

info_button = Button(text="ⓘ", font=(
    "Aerial", 12, "bold"), fg="blue", command=info, background="grey")
info_button.grid(column=2, row=0)
info_button.config(padx=30)

show_list_button = Button(text="≡", font=(
    "Aerial", 14, "bold"), fg="blue", width=5, height=1, command=show_list, background="grey")
show_list_button.grid(column=0, row=0)


window.mainloop()

from tkinter import *
from tkinter import messagebox
import json
import os

root = Tk()
root.title("Password Manager")
root.geometry("400x500")

def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    data = {
        "website": website,
        "username": username,
        "password": password
    }

    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            try:
                old_data = json.load(file)
            except:
                old_data = []
    else:
        old_data = []

    old_data.append(data)

    with open("passwords.json", "w") as file:
        json.dump(old_data, file, indent=4)

    saved_list.insert(END, f"{website} | {username}")

    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    messagebox.showinfo("Success", "Password Saved")

title = Label(root, text="Password Manager", font=("Arial", 20, "bold"))
title.pack(pady=10)

Label(root, text="Website/App").pack()
website_entry = Entry(root, width=35)
website_entry.pack(pady=5)

Label(root, text="Username/Email").pack()
username_entry = Entry(root, width=35)
username_entry.pack(pady=5)

Label(root, text="Password").pack()
password_entry = Entry(root, width=35, show="*")
password_entry.pack(pady=5)

save_btn = Button(root, text="Save Password", command=save_password)
save_btn.pack(pady=10)

Label(root, text="Saved Accounts", font=("Arial", 14)).pack()

saved_list = Listbox(root, width=45, height=10)
saved_list.pack(pady=10)

root.mainloop()

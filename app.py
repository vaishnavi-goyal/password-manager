from tkinter import *
from tkinter import messagebox
import json
import os
import re

# Main Window
root = Tk()
root.title("Password Manager")
root.geometry("500x550")

# Save Password Function
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Empty Field Check
    if website == "" or username == "" or password == "":
        messagebox.showwarning("Warning", "Please fill all fields")
        return

    # Password Validation
    if len(password) < 8:
        messagebox.showerror(
            "Weak Password",
            "Password must be at least 8 characters long"
        )
        return

    if not re.search("[A-Z]", password):
        messagebox.showerror(
            "Weak Password",
            "Password must contain an uppercase letter"
        )
        return

    if not re.search("[a-z]", password):
        messagebox.showerror(
            "Weak Password",
            "Password must contain a lowercase letter"
        )
        return

    if not re.search("[0-9]", password):
        messagebox.showerror(
            "Weak Password",
            "Password must contain a number"
        )
        return

    if not re.search("[@#$%^&*!_]", password):
        messagebox.showerror(
            "Weak Password",
            "Password must contain a special symbol"
        )
        return

    # Data Dictionary
    data = {
        "website": website,
        "username": username,
        "password": password
    }

    # Read Old Data
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            try:
                old_data = json.load(file)
            except:
                old_data = []
    else:
        old_data = []

    # Add New Data
    old_data.append(data)

    # Save Data
    with open("passwords.json", "w") as file:
        json.dump(old_data, file, indent=4)

    # Show in Listbox
    saved_list.insert(
        END,
        f"{website} | {username} | {password}"
    )

    # Clear Entries
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    messagebox.showinfo("Success", "Password Saved Successfully")


# Show / Hide Password
def toggle_password():
    if password_entry.cget('show') == '*':
        password_entry.config(show='')
        show_btn.config(text="Hide Password")
    else:
        password_entry.config(show='*')
        show_btn.config(text="Show Password")


# Heading
title = Label(
    root,
    text="Password Manager",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

# Website
Label(root, text="Website/App").pack()

website_entry = Entry(root, width=40)
website_entry.pack(pady=5)

# Username
Label(root, text="Username/Email").pack()

username_entry = Entry(root, width=40)
username_entry.pack(pady=5)

# Password
Label(root, text="Password").pack()

password_entry = Entry(root, width=40, show="*")
password_entry.pack(pady=5)

# Show Password Button
show_btn = Button(
    root,
    text="Show Password",
    command=toggle_password
)
show_btn.pack(pady=5)

# Save Button
save_btn = Button(
    root,
    text="Save Password",
    command=save_password
)
save_btn.pack(pady=10)

# Saved Passwords Label
Label(
    root,
    text="Saved Passwords",
    font=("Arial", 14)
).pack()

# Listbox
saved_list = Listbox(root, width=65, height=12)
saved_list.pack(pady=10)

# Run App
root.mainloop()

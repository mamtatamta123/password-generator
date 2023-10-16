import random
import string
from tkinter import *
from tkinter import ttk

def generate_password():
    password_length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(password_length))
    password_label.config(text="Generated Password: " + password)

root = Tk()
root.title("Password Generator")
root.geometry("400x200")

style = ttk.Style()
style.configure("TButton", padding=10, font=('Helvetica', 12))

length_label = Label(root, text="Password Length:")
length_label.pack()

length_entry = Entry(root)
length_entry.pack()

generate_button = ttk.Button(root, text="Generate Password", command=generate_password )
generate_button.pack()


password_label = Label(root, text="")
password_label.pack()
root.mainloop()



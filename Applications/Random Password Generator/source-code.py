import secrets
from tkinter import *
import string
from tkinter.font import Font

root = Tk()
root.geometry("250x200")
btn = Button(root, text="Generate Password", command=generate_password)
btn.place(relx=0.5, rely=0.2, anchor=N)
myFont = Font(family="Times New Roman", size=12)
lbl = Label(root, font=myFont)
lbl.place(relx=0.5, rely=0.5, anchor=CENTER)

def generate_password():
    password = []
    for i in range(3):
        alpha = secrets.choice(string.ascii_letters)
        symbol = secrets.choice(string.punctuation)
        numbers = secrets.choice(string.digits)
        password.append(alpha)
        password.append(symbol)
        password.append(numbers)
    y = "".join(str(x) for x in password)
    lbl.config(text=y)

root.mainloop()
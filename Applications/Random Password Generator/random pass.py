from tkinter import *
import random
import string

root = Tk()
root.geometry("400x200")

passstr = StringVar()
pwd_len = IntVar()

# function to generate the password
def get_pass():
    pass1 = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for x in range(pwd_len.get()): #loop to generate the user given length for password
        password = password + random.choice(pass1)
    passstr.set(password)

#tkinter command to generate the gui    
Label(root, text="Password Generator", font="calibri 18 bold").pack()
Label(root, text="Enter length of Password").pack(pady=9)
Entry(root, textvariable=pwd_len).pack(pady=2)
Button(root, text="Generate Password", command=generate).pack(pady=15)
Entry(root, textvariable=passstr).pack(pady=2)

root.mainloop()
from tkinter import *
import secrets
import string

root = Tk()
root.geometry("400x200")

passstr = StringVar()
pwd_len = IntVar()

# function to generate the password
def get_pass():
    # Validate password length is within reasonable bounds for security and performance
    pwd_length = pwd_len.get()
    
    # Security fix: validate input is numeric before conversion
    try:
        pwd_length = int(pwd_length)
    except (ValueError, TypeError):
        passstr.set("")
        return
    
    if pwd_length < 8 or pwd_length > 100:
        passstr.set("")
        return
    
    pass1 = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for x in range(pwd_length): #loop to generate the user given length for password
        password = password + secrets.choice(pass1)
    passstr.set(password)

#tkinter command to generate the gui    
Label(root, text="Password Generator", font="calibri 18 bold").pack()
Label(root, text="Enter length of Password").pack(pady=9)
Entry(root, textvariable=pwd_len).pack(pady=2)
Button(root, text="Generate Password", command=get_pass).pack(pady=15)
Entry(root, textvariable=passstr).pack(pady=2)

root.mainloop()
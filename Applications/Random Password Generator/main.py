import tkinter as tk
from utils import generate_password, check_strength

root = tk.Tk()
root.title("Password Generator")
root.geometry("420x400")
root.configure(bg="#1e1e2f")

# Variables
pwd_len = tk.IntVar(value=12)
passstr = tk.StringVar()
strength_var = tk.StringVar()

use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_symbols = tk.BooleanVar(value=True)

# Functions
def generate():
    length = pwd_len.get()

    if length <= 0:
        passstr.set("Invalid length")
        return

    password = generate_password(
        length,
        use_upper.get(),
        use_lower.get(),
        use_digits.get(),
        use_symbols.get()
    )

    passstr.set(password)
    strength_var.set("Strength: " + check_strength(password))


def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(passstr.get())


# UI
tk.Label(root, text="Password Generator", font=("Calibri", 18, "bold"), bg="#1e1e2f", fg="white").pack(pady=10)

tk.Label(root, text="Password Length", bg="#1e1e2f", fg="white").pack()
tk.Entry(root, textvariable=pwd_len).pack(pady=5)

# Options
tk.Checkbutton(root, text="Uppercase", variable=use_upper, bg="#1e1e2f", fg="white", selectcolor="#2e2e3f").pack()
tk.Checkbutton(root, text="Lowercase", variable=use_lower, bg="#1e1e2f", fg="white", selectcolor="#2e2e3f").pack()
tk.Checkbutton(root, text="Digits", variable=use_digits, bg="#1e1e2f", fg="white", selectcolor="#2e2e3f").pack()
tk.Checkbutton(root, text="Symbols", variable=use_symbols, bg="#1e1e2f", fg="white", selectcolor="#2e2e3f").pack()

# Buttons
tk.Button(root, text="Generate Password", command=generate).pack(pady=10)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

# Output
tk.Entry(root, textvariable=passstr, width=30).pack(pady=10)
tk.Label(root, textvariable=strength_var, bg="#1e1e2f", fg="lightgreen").pack()

root.mainloop()
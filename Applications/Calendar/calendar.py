from tkinter import *
import calendar

win = Tk()
win.title("GUI Calendar")

def text():
    year_str = year.get()
    month_str = month.get()
    year_int = int(year_str)
    month_int = int (month_str)
    cal = calendar.month(year_int, month_int)
    textfield.delete(0.0, END)
    textfield.insert(INSERT, cal)

label1 = Label(win, text = '{Year} ')
label1.grid(row = 0, column = 0)
label1 = Label(win, text = '{Month} ')
label1.grid(row = 0, column = 1)

year = Spinbox(win, from_= 1947, to = 2150, width = 24)
year.grid(row = 1, column = 0, padx = 16)
month = Spinbox(win, from_= 1, to = 12, width = 3)
month.grid(row = 1, column = 1)

button = Button(win, text = "{GO}", command = text)
button.grid(row = 1, column = 2)

textfield = Text(win, height = 10, width = 30, foreground = 'brown')
textfield.grid(row = 3, columnspan = 3)

win.mainloop()

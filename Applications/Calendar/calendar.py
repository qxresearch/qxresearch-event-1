from tkinter import *
from tkinter import ttk
import calendar
from datetime import datetime

win = Tk()
win.title("GUI Calendar")

def show_calendar(event=None):
    yr = int(year_var.get())
    mo = months.index(month_var.get()) + 1
    cal = calendar.month(yr, mo)
    textfield.delete(0.0, END)
    textfield.insert(INSERT, cal)

years = [str(y) for y in range(1947, 2151)]
months = [calendar.month_name[m] for m in range(1, 13)]

year_var = StringVar(value=str(datetime.now().year))
month_var = StringVar(value=calendar.month_name[datetime.now().month])

Label(win, text="Year:").grid(row=0, column=0)
year_combo = ttk.Combobox(win, textvariable=year_var, values=years, width=6)
year_combo.grid(row=1, column=0)

Label(win, text="Month:").grid(row=0, column=1)
month_combo = ttk.Combobox(win, textvariable=month_var, values=months, width=10)
month_combo.grid(row=1, column=1)

Button(win, text="Show Calendar", command=show_calendar).grid(row=1, column=2)
textfield = Text(win, height=10, width=30, fg='brown')
textfield.grid(row=3, columnspan=3)

win.bind('<Return>', show_calendar)

win.mainloop()

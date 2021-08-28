from tkinter import *
import wikipedia


def get_data():
    entry_value = entry.get()
    answer.delete(1.0, END)
    try:
        answer_value = wikipedia.summary(entry_value)
        answer.insert(INSERT, answer_value)
    except:
        answer.insert(INSERT, "ERROR! Invalid input or poor internet connection")

win = Tk()
win.title("Wikipedia Search")
topframe = Frame(win)
entry = Entry(topframe)
entry.pack()
button = Button(topframe, text="search", command=get_data)
button.pack()
topframe.pack(side = TOP)


bottomframe = Frame(win)
scroll = Scrollbar(bottomframe)
scroll.pack(side=RIGHT, fill=Y)
answer =  Text(bottomframe, width=50, height=20, yscrollcommand = scroll.set, wrap=WORD)
scroll.config(command=answer.yview)
answer.pack()
bottomframe.pack()

win.mainloop()

"""
If wikipedia module has not been installed previously, execute the following command - pip install wikipedia
"""
import tkinter as tk
from tkinter import messagebox, Scrollbar, Text
import wikipedia


def get_data():
    entry_value = entry.get().strip()
    answer.delete(1.0, tk.END)
    if not entry_value:
        answer.insert(tk.INSERT, "Please enter a valid search term.")
        return
    
    try:
        answer_value = wikipedia.summary(entry_value, sentences=3)  # Limit to a few sentences for faster response
        answer.insert(tk.INSERT, answer_value)
    except wikipedia.exceptions.DisambiguationError as e:
        answer.insert(tk.INSERT, f"Multiple results found. Did you mean: {str(e)}")  
    except wikipedia.exceptions.PageError:
        answer.insert(tk.INSERT, "ERROR! Page not found. Please try a different term.")
    except Exception as e:
        answer.insert(tk.INSERT, f"ERROR! {str(e)}")
        messagebox.showerror("Error", "An error occurred. Check your internet connection or input.")

win = tk.Tk()
win.title("Wikipedia Search")
win.geometry("600x400") 
win.resizable(True, True)

top_frame = tk.Frame(win, padx=10, pady=10)
entry = tk.Entry(top_frame, width=40)
entry.grid(row=0, column=0, padx=5)

button = tk.Button(top_frame, text="Search", command=get_data)
button.grid(row=0, column=1, padx=5)

top_frame.pack(side=tk.TOP)

bottom_frame = tk.Frame(win, padx=10, pady=10)
scroll = Scrollbar(bottom_frame)
answer = Text(bottom_frame, width=70, height=20, yscrollcommand=scroll.set, wrap=tk.WORD)
scroll.config(command=answer.yview)

scroll.pack(side=tk.RIGHT, fill=tk.Y)
answer.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

bottom_frame.pack(fill=tk.BOTH, expand=True)

win.mainloop()

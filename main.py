#Imports
import tkinter
from tkinter import ttk
import os

#Window definition
main_window = tkinter.Tk()
main_window.title("edredon")
main_window.geometry("1024x768")
main_window.iconbitmap("edredon.ico")
main_window.resizable(False, False)

#Functions definition
def view_entries():
    os.system('view_entries.py')

def add_entry():
    os.system('add_entry.py')

#Window and widgets layout
frame = tkinter.Frame(main_window)
frame.pack()

view_entries_button = tkinter.Button(frame, text="View entries", command=view_entries)
view_entries_button.grid(row=1, column=0, sticky="news", padx=20, pady=10)

add_entry_button = tkinter.Button(frame, text="Add entry", command=add_entry)
add_entry_button.grid(row=1, column=1, sticky="news", padx=20, pady=10)

main_window.mainloop()
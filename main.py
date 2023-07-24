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

def about():
    os.system('about.py')

#Window and widgets layout
frame = tkinter.Frame(main_window)
frame.pack()

menu_label = tkinter.LabelFrame(frame, text="MAIN MENU")
menu_label.grid(row=1, column=0)

view_entries_button = tkinter.Button(menu_label, text="View entries", command=view_entries)
view_entries_button.grid(row=0, column=0, sticky="news", padx=20, pady=10)

add_entry_button = tkinter.Button(menu_label, text="Add entry", command=add_entry)
add_entry_button.grid(row=1, column=0, sticky="news", padx=20, pady=10)

profiles_button = tkinter.Button(menu_label, text="Profiles", command=view_entries)
profiles_button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

about_button = tkinter.Button(menu_label, text="About", command=about)
about_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

main_window.mainloop()
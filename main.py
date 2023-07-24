#Imports
import tkinter
#from tkinter import ttk
from PIL import ImageTk, Image
import os

#Window definition
main_window = tkinter.Tk()
main_window.title("edredon")
main_window.geometry("800x600")
main_window.iconbitmap("data/images/edredon.ico")
main_window.resizable(False, False)
edredon = Image.open("data/images/edredon_bg.png")
background_image = ImageTk.PhotoImage(edredon)


#Functions definition
def profiles():
    profiles_window = tkinter.Toplevel()
    profiles_window.title("Manage profiles")
    profiles_window.geometry("640x480")
    profiles_window.iconbitmap("data/images/edredon.ico")
    profiles_window.resizable(False, False)
    profiles_window.mainloop()

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
menu_label.grid(row=1, column=0, sticky="w")

profiles_label = tkinter.LabelFrame(frame, bd=0, text="")
profiles_label.grid(row=1, column=1)

image_label = tkinter.Label(frame, image=background_image)
image_label.grid(row=2, column=1)

profiles_button = tkinter.Button(profiles_label, text="Profiles", command=profiles)
profiles_button.grid(row=0, column=0, sticky="news", padx=20, pady=10)

view_entries_button = tkinter.Button(menu_label, text="View entries", command=view_entries)
view_entries_button.grid(row=1, column=0, sticky="news", padx=20, pady=10)

add_entry_button = tkinter.Button(menu_label, text="Add entry", command=add_entry)
add_entry_button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

about_button = tkinter.Button(menu_label, text="About", command=about)
about_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

main_window.mainloop()
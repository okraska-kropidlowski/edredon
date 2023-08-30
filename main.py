#Imports
import tkinter
from tkinter import ttk
from PIL import ImageTk, Image
import os

#Window definition
main_window = tkinter.Tk()
main_window.title("edredon")
main_window.geometry("520x600")
main_window.iconbitmap("data/images/edredon.ico")
main_window.resizable(False, False)
edredon = Image.open("data/images/edredon_bg.png")
background_image = ImageTk.PhotoImage(edredon)

with open('data/profiles_list', encoding="UTF-8") as inFile:
    profiles_list = [line for line in inFile]
active_profile = ""

#Functions definition
def profiles():
    profiles_window = tkinter.Toplevel()
    profiles_window.title("Manage profiles")
    profiles_window.geometry("640x480")
    profiles_window.iconbitmap("data/images/edredon.ico")
    profiles_window.resizable(False, False)

    profiles_frame = tkinter.Frame(profiles_window)
    profiles_frame.pack()

    def profile_selection(profile):
        global active_profile
        profile = select_profile.get()
        active_profile = profile
        print(active_profile)
        view_entries_button.config(state="active")
        add_entry_button.config(state="active")
        profiles_window.destroy()

    #Profiles window and widgets layout
    profiles_window_label = tkinter.LabelFrame(profiles_frame, text="PROFILES LIST")
    profiles_window_label.grid(row=0, column=0)
    select_profile = ttk.Combobox(profiles_window_label, state="readonly", values=tuple(profiles_list))
    select_profile.current=""
    select_profile.grid(row=1, column=0)
    select_profile.bind("<<ComboboxSelected>>", profile_selection)
    profiles_window.mainloop()

def view_entries(profile):
    os.system('view_entries.py ' + profile)

def add_entry(profile):
    os.system('add_entry.py ' + profile)

def about():
    os.system('about.py')

#Window and widgets layout
frame = tkinter.Frame(main_window)
frame.pack()

profiles_label = tkinter.LabelFrame(frame, bd=0, text="")
profiles_label.grid(row=1, column=0, pady=50)

menu_label = tkinter.LabelFrame(frame, text="MAIN MENU")
menu_label.grid(row=2, column=0)

image_label = tkinter.Label(frame, image=background_image)
image_label.grid(row=1, column=1, padx=20, pady=50)

profiles_button = tkinter.Button(profiles_label, text="Profiles", command=profiles)
profiles_button.grid(row=0, column=0, sticky="news", padx=20, pady=10)

view_entries_button = tkinter.Button(menu_label, text="View entries", command=view_entries(active_profile), state="disabled")
view_entries_button.grid(row=1, column=0, sticky="news", padx=20, pady=10)

add_entry_button = tkinter.Button(menu_label, text="Add entry", command=lambda: add_entry(active_profile), state="disabled")
add_entry_button.grid(row=2, column=0, sticky="news", padx=20, pady=10)

about_button = tkinter.Button(menu_label, text="About", command=about)
about_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

main_window.mainloop()
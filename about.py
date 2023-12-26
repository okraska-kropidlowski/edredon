#Imports
import tkinter
from tkinter import ttk

#Window definition
about = tkinter.Tk()
about.title("About edredon")
about.iconbitmap("data/images/edredon.ico")
about.resizable(False, False)

info = tkinter.Label(about, text="edredon version 1.0\n\nFirst release with basic functionality:\n- Profile management\n- Entry adding/viewing\n\nCreated using:\n- TkinterMapView by Tom Schimansky\n- sqlite3 by Gerhard Häring\n\nList of bird species taken from:\nhttp://komisjafaunistyczna.pl/lista/\n")
info.config(justify=tkinter.LEFT, padx=20, pady=10, font=("Arial", 10))
info.pack()

about.mainloop()
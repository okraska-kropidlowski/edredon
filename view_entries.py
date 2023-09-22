#Imports
import tkinter
from tkinter import ttk
import sys

#Reading the user profile
user_profile = sys.argv[1]
print(user_profile)

#Window definition
view_entries = tkinter.Tk()
view_entries.title("View entries of " + user_profile)
view_entries.iconbitmap("data/images/edredon.ico")
#view_entries.resizable(False, False)

view_entries.mainloop()
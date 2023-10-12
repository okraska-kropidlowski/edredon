#Imports
import tkinter
from tkinter import ttk

#Window definition
profiles = tkinter.Tk()
profiles.title("Manage profiles")
profiles.iconbitmap("data/images/edredon.ico")
profiles.resizable(False, False)

with open ('data\profiles_list') as profiles_file:
    profiles_file_content = profiles_file.read()

#Functions definition
def add_profile():
    new_profile = add_profile_box.get('1.0', 'end-1c')
    with open('data\profiles_list', "a") as profiles_file:
        if profiles_file_content == '':
            profiles_file.write(new_profile)
            add_profile_box.delete('1.0', 'end')
        elif not profiles_file_content.endswith('\n'):
            profiles_file.write('\n')
            profiles_file.write(new_profile)
            add_profile_box.delete('1.0', 'end')

#Window and widgets layout
profiles_label = tkinter.LabelFrame(profiles, text="MANAGE PROFILES")
profiles_label.grid(column=0)

add_profile_box = tkinter.Text(profiles_label, height=1, width=20)
add_profile_box.grid(column=0, row=0)

add_button = tkinter.Button(profiles_label, text="Add profile", command=add_profile)
add_button.grid(column=1, row=0)

for widget in profiles_label.winfo_children():
    widget.grid_configure(sticky="news", padx=20, pady=10)

profiles.mainloop()
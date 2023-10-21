#Imports
import tkinter
from tkinter import ttk

#Window definition
profiles = tkinter.Tk()
profiles.title("Manage profiles")
profiles.iconbitmap("data/images/edredon.ico")
profiles.resizable(False, False)

#Load profiles list and analyse its contents
with open ('data/profiles_list') as profiles_file:
    profiles_file_content = profiles_file.read()
with open ('data/profiles_list') as profiles_file:
    profiles_list = [line for line in profiles_file]

#Functions definition
def add_profile():
    new_profile = add_profile_box.get('1.0', 'end-1c')
    with open('data/profiles_list', "a") as profiles_file:
        if profiles_file_content == '':
            profiles_file.write(new_profile)
            add_profile_box.delete('1.0', 'end')
        elif not profiles_file_content.endswith('\n'):
            profiles_file.write('\n')
            profiles_file.write(new_profile)
            add_profile_box.delete('1.0', 'end')

def profile_selection(profile):
    global to_be_deleted
    profile = remove_profile_list.get()
    to_be_deleted = profile
    print(to_be_deleted)

def remove_profile():
    with open('data\profiles_list', "r") as profiles_file:
        profiles_file_content = profiles_file.read()

    with open('data\profiles_list', "w") as profiles_file:
        removed_profile = profiles_file_content.replace(to_be_deleted, "")
        profiles_file.write(removed_profile)

#Window and widgets layout
profiles_label = tkinter.LabelFrame(profiles, text="MANAGE PROFILES")
profiles_label.grid(column=0)

add_profile_box = tkinter.Entry(profiles_label, width=50)
add_profile_box.grid(column=0, row=0)

add_button = tkinter.Button(profiles_label, text="Add profile", command=add_profile)
add_button.grid(column=1, row=0)

remove_profile_list = ttk.Combobox(profiles_label, state="readonly", values=tuple(profiles_list))
remove_profile_list.current=""
remove_profile_list.bind("<<ComboboxSelected>>", profile_selection)
remove_profile_list.grid(column=0, row=1)

remove_button = tkinter.Button(profiles_label, text="Remove profile", command=remove_profile)
remove_button.grid(column=1, row=1)

for widget in profiles_label.winfo_children():
    widget.grid_configure(sticky="news", padx=20, pady=10)

profiles.mainloop()
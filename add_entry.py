#Imports
import tkinter
from tkinter import ttk
import tkintermapview
from tkcalendar import DateEntry
import sys
import sqlite3

#Reading the user profile
user_profile = sys.argv[1]

#Reading the bird species list from a file and creating the Polish-Latin dictionary
species_list_raw = []
with open('data/species_list', encoding="UTF-8") as inFile:
    species_list_raw = [line for line in inFile]
species_list = [item.strip() for item in species_list_raw]
species_list_latin_raw = []
with open('data/species_list_latin') as inFile:
    species_list_latin_raw = [line for line in inFile]
species_list_latin = [item.strip() for item in species_list_latin_raw]

species_dictionary = {species_list[i]: species_list_latin[i] for i in range(len(species_list))}

#Window definition
new_entry = tkinter.Tk()
new_entry.title("Add new entry")
new_entry.iconbitmap("data/images/edredon.ico")
new_entry.resizable(False, False)

saving_species = ""
saving_coordinates = ""

#Functions definition
def allow_saving():
    global saving_species
    global saving_coordinates
    print(saving_species, saving_coordinates)
    if (saving_coordinates != "" and saving_species != ""):
        save_button.config(state="active")

def open_location():
    global location
    location_window = tkinter.Toplevel()
    location_window.title("Observation location")
    location_window.geometry("800x600")
    location_window.iconbitmap("data/images/edredon.ico")
    location_window.resizable(False, False)

    def select_location(coordinates):
        global saving_coordinates
        global coordinates_simple
        global latitude, longitude
        coordinates_simple = tuple([float("{0:.5f}".format(n)) for n in coordinates])
        (latitude, longitude) = coordinates_simple
        location.config(text=coordinates_simple)
        saving_coordinates = coordinates_simple
        allow_saving()
        location_window.destroy()

    map_widget = tkintermapview.TkinterMapView(location_window, width=800, height=600, corner_radius=0)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    map_widget.set_position(51.77674, 19.45469)
    map_widget.set_zoom(50)
    map_widget.add_right_click_menu_command(label="Set location", command=select_location, pass_coords=True)
    location_window.mainloop()

def list_selection(bird):
    global latin_bird
    global saving_species
    bird = select_species.get()
    latin_bird = species_dictionary[bird]
    latin_species.config(text=latin_bird)
    saving_species = bird
    allow_saving()

def save_entry():
    global date
    global species
    species = select_species.get()
    latin_species = latin_bird
    latitude_string = str(latitude)
    longitude_string = str(longitude)
    location_string = "(" + latitude_string + ", "+ longitude_string + ")"
    date = date_button.get_date()
    date_string = str(date)
    #Create table in db
    conn = sqlite3.connect('database/' + user_profile + '.db')
    table_create_query = '''CREATE TABLE IF NOT EXISTS Observation (species TEXT, species_latin TEXT, location TEXT, date TEXT)'''
    conn.execute(table_create_query)   
    #Insert data into the table
    data_insert_query = '''INSERT INTO Observation (species, species_latin, location, date) VALUES (?, ?, ?, ?)'''
    data_insert_tuple = (species, latin_species, location_string, date_string)
    cursor = conn.cursor()
    cursor.execute(data_insert_query, data_insert_tuple)
    conn.commit()
    conn.close()
    new_entry.destroy()

#Window and widgets layout
frame = tkinter.Frame(new_entry)
frame.pack()

species_label = tkinter.LabelFrame(frame, text="OBSERVED SPECIES")
species_label.grid(row=1, column=0)
latin_label = tkinter.LabelFrame(frame, text="LATIN NAME")
latin_label.grid(row=1, column=1)

select_species = ttk.Combobox(species_label, state="readonly", values=tuple(species_list))
select_species.current=""
select_species.grid(row=1, column=0)
select_species.bind("<<ComboboxSelected>>", list_selection)
latin_species = tkinter.Label(latin_label, text="")
latin_species.grid(row=1, column=1)

location_date_label = tkinter.LabelFrame(frame, text="LOCATION AND DATE")
location_date_label.grid(row=2)

select_location = tkinter.LabelFrame(location_date_label, text="Select observation location:")
select_location.grid(row=2, column=0)
location_button = tkinter.Button(select_location, text="Open map view", command=open_location)
location_button.grid(column=0)

show_location = tkinter.LabelFrame(location_date_label, text="Observation location:")
show_location.grid(row=2, column=1)
location = tkinter.Label(show_location, text="")
location.grid(column=0)

select_date = tkinter.LabelFrame(location_date_label, text="Select observation date:")
select_date.grid(row=2, column=2)
date_button = DateEntry(select_date, date_pattern='dd.mm.yyyy')
date_button.grid(column=0)

#Entry saving
save_button = tkinter.Button(frame, text="Add observation", command=save_entry, state="disabled")
save_button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

new_entry.mainloop()
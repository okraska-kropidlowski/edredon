#Imports
import tkinter
from tkinter import ttk
import tkintermapview
from tkcalendar import Calendar, DateEntry

#Reading the bird species list from a file
species = []
with open('species_list') as inFile:
    species = [line for line in inFile]
#species = [tuple(map(lambda x: x.encode(encoding = 'UTF-8', errors = 'strict'), bird)) for bird in species]
species_latin = []
with open('species_list_latin') as inFile:
    species_latin = [line for line in inFile]

#Window definition
new_entry = tkinter.Tk()
new_entry.title("Add new entry")
new_entry.geometry("1024x768")
new_entry.resizable(False, False)

#Functions definition
def open_location():
    global location
    location_window = tkinter.Toplevel()
    location_window.title("Observation location")
    location_window.geometry("800x600")
    location_window.resizable(False, False)

    def select_location(coordinates):
        print("Observation location:", coordinates)
        coordinates_simple = tuple([float("{0:.5f}".format(n)) for n in coordinates])
        location.config(text=coordinates_simple)
        location_window.destroy()

    map_widget = tkintermapview.TkinterMapView(location_window, width=800, height=600, corner_radius=0)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    map_widget.set_position(51.77674, 19.45469)
    map_widget.set_zoom(50)
    map_widget.add_right_click_menu_command(label="Set location", command=select_location, pass_coords=True)

    location_window.mainloop()

#Window and widgets layout
frame = tkinter.Frame(new_entry)
frame.pack()

species_label = tkinter.LabelFrame(frame, text="OBSERVED SPECIES")
species_label.grid(row=1)

select_species = ttk.Combobox(species_label, state="readonly", values=tuple(species))
select_species.current=""
select_species.grid(row=1, column=0)

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

new_entry.mainloop()
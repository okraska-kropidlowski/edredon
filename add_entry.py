import tkinter
import tkintermapview

new_entry = tkinter.Tk()
new_entry.title("Add new entry")
new_entry.geometry("1024x768")
new_entry.resizable(False, False)

def open_location():
    global location
    location_window = tkinter.Toplevel()
    location_window.title("Observation location")
    location_window.geometry("800x600")
    location_window.resizable(False, False)

    def select_location(coordinates):
        print("Observation location:", coordinates)
        location.config(text=coordinates)
        location_window.destroy()

    map_widget = tkintermapview.TkinterMapView(location_window, width=800, height=600, corner_radius=0)
    map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
    map_widget.set_position(51.77674, 19.45469)
    map_widget.set_zoom(50)
    map_widget.add_right_click_menu_command(label="Set location", command=select_location, pass_coords=True)

    location_window.mainloop()

frame = tkinter.Frame(new_entry)
frame.pack()

select_location = tkinter.LabelFrame(frame, text="Select observation location:")
select_location.grid(row=0)

location_button = tkinter.Button(select_location, text="Open map view", command=open_location)
location_button.grid(column=0)

show_location = tkinter.LabelFrame(frame, text="Observation location:")
show_location.grid(row=1)

location = tkinter.Label(show_location, text="")
location.grid(column=0)

new_entry.mainloop()
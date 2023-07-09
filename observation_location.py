import tkinter
import tkintermapview

location = tkinter.Tk()
location.title("Observation location")
location.geometry("800x600")
location.resizable(False, False)

def select_location(coordinates):
    print("Observation location:", coordinates)
    location.destroy()

map_widget = tkintermapview.TkinterMapView(location, width=800, height=600, corner_radius=0)
map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
map_widget.set_position(51.77674, 19.45469)
map_widget.set_zoom(50)
map_widget.add_right_click_menu_command(label="Set location", command=select_location, pass_coords=True)

location.mainloop()
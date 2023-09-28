#Imports
import tkinter
from tkinter import ttk
import sys
import sqlite3

#Reading the user profile
user_profile = sys.argv[1]

#Window definition
view_entries = tkinter.Tk()
view_entries.title("View entries of " + user_profile)
view_entries.iconbitmap("data/images/edredon.ico")
#view_entries.resizable(False, False)

conn = sqlite3.connect('database/' + user_profile + '.db')
table_create_query = '''CREATE TABLE IF NOT EXISTS Observation (species TEXT, species_latin TEXT, location TEXT, date TEXT)'''
conn.execute(table_create_query)
cursor = conn.cursor()
cursor.execute('SELECT * FROM "Observation"')
entries_list = cursor.fetchall()

title_label = tkinter.Label(view_entries, text="Observations record of " + user_profile, font=("Arial", 15))
title_label.grid(row=0, columnspan=3)
columns = ('Species name', 'Species name latin', 'Observation location', 'Observation date')
entries_table = ttk.Treeview(view_entries, columns=columns, show='headings')

for i, (name, latin_name, location, date) in enumerate(entries_list, start=1):
    entries_table.insert("", "end", values=(name, latin_name, location, date))

for column in columns:
    entries_table.heading(column, text=column)    
entries_table.grid(row=1, column=0, columnspan=2)

close_button = tkinter.Button(view_entries, text="Close", width=15, command=exit)
close_button.grid(row=4, column=1)

view_entries.mainloop()
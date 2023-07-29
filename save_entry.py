import sqlite3
import sys

#Reading the args from add_entry.py
db_name = sys.argv[1]
species = sys.argv[2]
species_latin = sys.argv[3]
location = sys.argv[4]
date = sys.argv[5]

# Create Table
conn = sqlite3.connect(db_name + '.db')
table_create_query = '''CREATE TABLE IF NOT EXISTS Observation (species TEXT, species_latin TEXT, location TEXT, date TEXT)'''
conn.execute(table_create_query)
            
# Insert Data
data_insert_query = '''INSERT INTO Observation (species, species_latin, location, date) VALUES (?, ?, ?, ?)'''
data_insert_tuple = (species, species_latin, location, date)
cursor_text = conn.cursor()
cursor_text.execute(data_insert_query, data_insert_tuple)

conn.commit()
conn.close()
import sqlite3
import sys

#This will be changed, to tage args from add_enry.py
db_name = "TEST"
species = "TESCIAK TESTOWY"
species_latin = "TESTUS VULGARIS"
location = "SOMEWHERE"
date = "SOMEDAY"

# Create Table
conn = sqlite3.connect(db_name + '.db')
table_create_query = '''CREATE TABLE IF NOT EXISTS Student_Data (species TEXT, species_latin TEXT, location TEXT, date TEXT)'''
conn.execute(table_create_query)
            
# Insert Data
data_insert_query = '''INSERT INTO Student_Data (species, species_latin, location, date) VALUES (?, ?, ?, ?)'''
data_insert_tuple = (species, species_latin, location, date)
cursor = conn.cursor()
cursor.execute(data_insert_query, data_insert_tuple)
conn.commit()
conn.close()
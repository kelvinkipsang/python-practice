import sqlite3

#creating connection to db/create db if it doesnt exist
with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()                                             #define cursor (for db interaction) & assign var c to it
    c.execute("CREATE TABLE posts(title TEXT, description TEXT)")   #create new table(posts) 2 columns title &text
    c.execute('INSERT INTO posts VALUES ("kelvin","a quiet guy")')      #add data to posts
import sqlite3

#create database
conn = sqlite3.connect('DB_Assignment.db')

#with connection open insert cursor
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS table_assignment(\
                ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                file_name TEXT\
                )")
    conn.commit()
conn.close()


#reconnect and insert data
conn = sqlite3.connect('DB_Assignment.db')
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO table_assignment(file_name) VALUES ('Hello.txt')")
    cur.execute("INSERT INTO table_assignment(file_name) VALUES ('World.txt')")
    conn.commit()
conn.close()

#list to pull from 
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

#reconnect using endswith instead of SELECT
for x in fileList:
    if x.endswith(".txt"):
        print(x)

"""#reconnect and print qualifying files
conn = sqlite3.connect('DB_Assignment.db')
with conn:
    cur = conn.cursor()
    #select data with matching criteria
    cur.execute("SELECT ID, file_name FROM table_assignment WHERE file_name = '%txt'")
    varStorage = cur.fetchall() #stores selected data as var
    for item in varStorage:
        displayVar = "The following files have been found with the .txt extension: {}, {}.".format(item[0], item[1])
    print(displayVar)"""
    


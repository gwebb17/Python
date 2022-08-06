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

"""
#reconnect and insert data
conn = sqlite3.connect('DB_Assignment.db')
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO table_assignment(file_name) VALUES ('Hello.txt')")
    cur.execute("INSERT INTO table_assignment(file_name) VALUES ('World.txt')")
    conn.commit()
conn.close()"""

#list to pull from 
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')



for x in fileList:
    if x.endswith(".txt"):
        conn = sqlite3.connect('DB_Assignment.db')
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO table_assignment(file_name) VALUES (?)", (x,))#the ? tells python that this is where the variable will go (x)
            conn.commit()
        conn.close()
            
conn = sqlite3.connect('DB_Assignment.db')
with conn:
    cur = conn.cursor() #must be put before any statement including cur.
    cur.execute("SELECT file_name FROM table_assignment")
    varStorage = cur.fetchall() #this now retrieves the result from above SELECT statement
    for item in varStorage:
        displayVar = "The following files have been found with the .txt extension: {}.".format(item)
        print(displayVar)
conn.close() #math indentation with intial with 

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
    


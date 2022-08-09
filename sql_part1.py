import sqlite3
#this will actually create the db we are naming below though it doesn't exist yet
connection = sqlite3.connect('C:/Users/Machine/Documents/GitHub/Python/db_sql_part1.db')

c = connection.cursor() #basic cursor instantiation but now we're calling it c for shorthand

#creates table with three columns
#c.execute("CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT)")


#single' denotes string in SQL
#double " denotes the sql statement begin/end
c.execute("INSERT INTO People VALUES('Ron', 'Obvious', 42)") 
connection.commit() #save changes or won't be saved
connection.close() #close conn once done with connection


#for practice db can use ':memory:' to do temporary one
connection = sqlite3.connect(':memory:')


#use with keyword to say "while this is true/while we have our connection"
with sqlite3.connect("db_sql_part1.db") as connection:
    c = connection.cursor()
    c.execute("INSERT INTO People VALUES('Ron', 'Burgundy', 34)")
    connection.commit()
    connection.close()


#to run multiple lines of SQL at a time you can use executescript() method and use big string
#with multiple instructions. ; separates statements but use multiline string for readability
import sqlite3
with sqlite3.connect('db_sql_part1.db') as connection:
    c = connection.cursor()
    c.executescript("""DROP TABLE IF EXISTS People;
                    CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT);
                    INSERT INTO People VALUES('Ron', 'Burdungy', 35);
                    """)

#To run similar statements without repeating same command using executemany
#first write out the tuples as a variable with the same amount of parameters needed (below are 3)
peopleValues = (('Luigi', 'Vercotti', 54), ('Arthur', 'Belling', 24))
#then insert all the people to the table at once using a single line
c = connection.cursor()
c.executemany("INSERT INTO People VALUES(?, ?, ?)", peopleValues)
                

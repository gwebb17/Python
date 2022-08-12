import sqlite3


#define tableValues that we will INSERT to columns at once instead of one by one
tableValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ("Ak'not", 'Mangalore', -5))


#the with statement gives us our connection to memory for all of the instructions/Says while we have our connection execute:
with sqlite3.connect(':memory:') as connection:
    c = connection.cursor() #saves our connection as variable
    c.execute("CREATE TABLE IF NOT EXISTS Roster(ID integer PRIMARY KEY AUTOINCREMENT, \
          Name TEXT, Species TEXT, IQ INT)") #first statement creating table
    c.executemany("INSERT INTO Roster (Name,Species,IQ) VALUES(?,?,?)", tableValues) #inserts values from variable we defined
    c.execute("UPDATE Roster SET Species='Human' WHERE Name='Korben Dallas'") #updates sepcified values
    c.execute("SELECT Name,IQ FROM Roster WHERE species='Human'") #grabs specified info from table
    for item in c.fetchall():  #this will print our most recent SELECT statement (the one immediately above) where data matches
        print(item)
    c.close()



    #below is original idea of solving problem. The above is superior in several ways:
    #1. above is much more concise and easy to read
    #2. above keeps connection to ':memory:' database while ALL execute statements are done instead of opening/closing each time
    #3. below won't work using ':memory:' (temp RAM) unsure why but maybe because it handles connection differently
    
    """
connection = sqlite3.connect(':memory:')
#create shorthand for connection
c = connection.cursor()

#create table
c.execute("CREATE TABLE IF NOT EXISTS Roster(ID integer PRIMARY KEY AUTOINCREMENT, \
          Name TEXT, Species TEXT, IQ INT)")
connection.commit()


#populate table with values using executemany
tableValues = (('Jean-Baptiste Zorg', 'Human', 122), ('Korben Dallas', 'Meat Popsicle', 100), ("Ak'not", 'Mangalore', -5))
c = connection.cursor()
c.executemany("INSERT INTO Roster (Name,Species,IQ) VALUES(?,?,?)", tableValues)
connection.commit()

#update value
#connection = sqlite3.connect(':memory:')
#c = connection.cursor()
c.execute("UPDATE Roster SET Species='Human' WHERE Name='Korben Dallas'")
connection.commit()
connection.close()

"""

import sqlite3

#get personal data from user
firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))    #way to convert to int in same line?
personData = (firstName, lastName, age)
#personData saves all above info as one var, this way you can insert it into placeholders (?)
#this avoids errors like names with ' in them being confused in the INSERT statement

connection = sqlite3.connect(':memory:')

#execute insert statement for supplied person data
with sqlite3.connect(':memory:') as connection:
    c = connection.cursor()
    c.execute("INSERT INTO ':memory:' VALUES (?,?,?)",personData)

c.execute("UPDATE :memory: SET Age=? WHERE FirstName=? AND LastName=?",
         (45, 'Luigi', 'Vercotti'))

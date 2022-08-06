import sqlite3


def practice_database_Function():
    conn = sqlite3.connect('practice_database.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS practice_table(\
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                    Mode_Name TEXT, \
                    Mode_Formulae TEXT, \
                    Mode_Mood TEXT \
                    )")
        # might need: conn.commit()
        cur.execute("INSERT INTO practice_table(Mode_Name, Mode_Formulae, Mode_Mood)\
                    VALUES (?, ?, ?)", \
                    ('Ionian', '1 2 3 4 5 6 7', 'Happy'))
        cur.execute("INSERT INTO practice_table(Mode_Name, Mode_Formulae, Mode_Mood)\
                    VALUES (?, ?, ?)", \
                    ('Dorian', '1 2 b3 4 5 6 b7', 'Inquiring/Misleading'))
        cur.execute("INSERT INTO practice_table(Mode_Name, Mode_Formulae, Mode_Mood)\
                    VALUES (?, ?, ?)", \
                    ('Phyrigan', '1 b2 b3 4 5 b6 b7', 'Impending/Foreboding'))
        cur.execute("INSERT INTO practice_table(Mode_Name, Mode_Formulae, Mode_Mood)\
                    VALUES (?, ?, ?)", \
                    ('Lydian', '1 2 3 #4 5 6 7', 'Floating/Whimsical'))
        cur.execute("INSERT INTO practice_table(Mode_Name, Mode_Formulae, Mode_Mood)\
                    VALUES (?, ?, ?)", \
                    ('Mixolydian', '1 2 3 4 5 6 b7', 'Happy/Island/Blues'))
        cur.execute("INSERT INTO practice_table(Mode_Name, Mode_Formulae, Mode_Mood)\
                    VALUES (?, ?, ?)", \
                    ('Aeolian', '1 2 b3 4 5 b6 b7', 'Sad/Powerful/Angry'))
        cur.execute("INSERT INTO practice_table(Mode_Name, Mode_Formulae, Mode_Mood)\
                    VALUES (?, ?, ?)", \
                    ('Locrian', '1 b2 b3 4 b5 b6 b7', 'Twisted/Bitter'))
        conn.commit()
    conn.close()

practice_database_Function()
                    
    

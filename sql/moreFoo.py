import sqlite3

# with nie dziala!
db = sqlite3.connect(':memory:')
db.row_factory = sqlite3.Row

cursor = db.cursor()
cursor.execute('''CREATE TABLE Pies(
    id INTEGER PRIMARY KEY, 
    imie VARCHAR(30), 
    wiek INTEGER)
    ''')

piesely = [('Azor',12),('Fafik', 2),('Dziku',4),('Kurczak', 5)]    
cursor.executemany('INSERT INTO Pies(imie, wiek) VALUES(?,?)',
                   piesely)


# for i in cursor.execute('SELECT * FROM Pies'):
results = cursor.execute('SELECT * FROM Pies').fetchall()
for i in results:
    # print(i['imie'])
    print(dict(i))


db.close()



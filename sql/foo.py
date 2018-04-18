import sqlite3

db = sqlite3.connect(':memory:')

cursor = db.cursor()
cursor.execute('CREATE TABLE Pies(imie varchar(30), wiek integer)')
cursor.execute('''INSERT INTO Pies(imie, wiek) VALUES('Fafix', 11)''')
cursor.execute('''INSERT INTO Pies(imie, wiek) VALUES('Azor', 5)''')
cursor.execute('''INSERT INTO Pies(imie, wiek) VALUES('Reksio', 3)''')

cursor.execute('''INSERT INTO Pies(imie, wiek) VALUES(:name, :wiek)''',
    {'name': 'DzikiPies', 'wiek': 100})

cursor.execute('''INSERT INTO Pies(imie, wiek) VALUES(?,?)''',
    ('Kurczak', 2))
       
cursor.execute('SELECT * from Pies')
wynik = cursor.fetchall()

for w in wynik:
    print(w)

print("\nPsy o wieku <=6:")
cursor.execute('SELECT * FROM Pies WHERE wiek<=?', str(6))
wynik = cursor.fetchall()
for w in wynik:
    print(w)


print("\ninny select")
db.row_factory = sqlite3.Row
cursor.execute('SELECT * FROM Pies')
for row in cursor:
    print('{},{}'.format(row[0], row[1]))
    
db.close()



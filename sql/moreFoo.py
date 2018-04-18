import sqlite3

def createPies():
    return 'CREATE TABLE Pies(imie varchar(30), wiek integer)'

def populatePieses():
    return [('Azor',12),('Fafik', 2),('Dziku',4),('Kurczak', 5)]

def readAllPiesels():
    return 'SELECT * FROM Pies'

# with nie dziala!
db= sqlite3.connect(':memory:')

cursor = db.cursor()
cursor.execute(createPies())
    
piesely = populatePieses()
cursor.executemany('INSERT INTO Pies(imie, wiek) VALUES(?,?)',
                   piesely)

for i in cursor.execute(readAllPiesels()):
    print(i)

db.close()



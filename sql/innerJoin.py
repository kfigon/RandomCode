import sqlite3

def dodajDoWozka(cursor, idx, nazwa, idWozka):
    cursor.execute('''INSERT INTO cart_item(id, nazwa, cart_id) VALUES
                    (?,?,?)''', (idx, nazwa, idWozka))

def dajWozki(cursor):
    cursor.execute('SELECT * from cart')
    return cursor.fetchall()

def dajElementyZWozka(cursor, wozekId):
    cursor.execute('''SELECT * from cart_item ci
            INNER JOIN cart c on c.id=ci.cart_id
            WHERE ci.cart_id=?''', str(wozekId))
    return cursor.fetchall()

def initBaze(c):
    c.execute('CREATE TABLE cart(id int, nazwa varchar(30))')
    c.execute('CREATE TABLE cart_item(id int, nazwa varchar(30), cart_id int)')

    c.execute('INSERT INTO cart(id, nazwa) VALUES (1, "wozek sklepowy")')
    c.execute('INSERT INTO cart(id, nazwa) VALUES (2, "wozek widlowy")')

    dodajDoWozka(c, 1, 'Chleb', 1)
    dodajDoWozka(c, 2, 'Pasta', 1)
    dodajDoWozka(c, 3, 'Mieso', 1)

    dodajDoWozka(c, 1, 'WAGON', 2)
    dodajDoWozka(c, 2, 'KONTENER', 2)
    dodajDoWozka(c, 3, 'Chomiki', 2)

#####################################

db = sqlite3.connect(':memory:')
db.row_factory = sqlite3.Row
c = db.cursor()
initBaze(c)

print("Wozki:")
wozki = dajWozki(c)
for w in wozki:
    idWozka = w['id']
    nazwaWozka = w['nazwa']
    print("{} (id {}) ma w srodku:".format(nazwaWozka, str(idWozka)))
    wyniki = dajElementyZWozka(c, idWozka)
    for i in wyniki:
          print("{} (id {})".format(i['nazwa'], str(i['id'])))
    print()

c.close()
db.close()

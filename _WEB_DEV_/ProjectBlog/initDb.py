import sqlite3

b = sqlite3.connect('baza.db')
b.row_factory = sqlite3.Row
c = b.cursor()

c.execute('DROP TABLE IF EXISTS post')
c.execute("CREATE TABLE post(id integer primary key, tytul varchar(30), tresc varchar(200))")


dane = [
        {'tytul': 'Bylem wczoraj tutaj', 'tresc': 'bylo awesome!'},
        {'tytul': 'Nowi avengersi', 'tresc': 'nie podobaja mi sie'},
        {'tytul': 'taki sobie wpis', 'tresc': 'ale bez tresci...'}
    ]

c.executemany('insert into post(tytul, tresc) values(:tytul, :tresc)', dane)

b.commit()

c.close()
b.close()
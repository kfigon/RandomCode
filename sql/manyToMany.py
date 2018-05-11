import sqlite3

baza = sqlite3.connect(':memory:')
c = baza.cursor()

c.execute('create table pies(id integer primary key, name varchar(30))')
c.execute('insert into pies(name) values("Azor")')
c.execute('insert into pies(name) values("Fafik")')
c.execute('insert into pies(name) values("Piesel")')
c.execute('insert into pies(name) values("Zwierzak")')


c.execute('create table zabawka(id integer primary key, name varchar(30))')
c.execute('insert into zabawka(name) values("Piszczalka")')
c.execute('insert into zabawka(name) values("Kosc")')
c.execute('insert into zabawka(name) values("Pilka")')
c.execute('insert into zabawka(name) values("Kurczak")')
c.execute('insert into zabawka(name) values("DzikiDzik")')


c.execute('create table zabawka_pies(id integer primary key, id_psa integer, id_zabawki integer)')
c.execute('insert into zabawka_pies(id_psa,id_zabawki) values(1,1)')
c.execute('insert into zabawka_pies(id_psa,id_zabawki) values(1,2)')
c.execute('insert into zabawka_pies(id_psa,id_zabawki) values(1,3)')

c.execute('insert into zabawka_pies(id_psa,id_zabawki) values(2,2)')
c.execute('insert into zabawka_pies(id_psa,id_zabawki) values(2,3)')
c.execute('insert into zabawka_pies(id_psa,id_zabawki) values(2,5)')


query = \
'''Select p.name, z.name from zabawka_pies zp join pies p on zp.id_psa=p.id 
join zabawka z on zp.id_zabawki=z.id
'''
for i in c.execute(query):
    print(i)

c.close()
baza.close()
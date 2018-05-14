__author__ = 'kamil'
from flask import Flask, render_template, request,json,g
import sqlite3

DATABASE = 'baza.db'
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def dodajPost(tytul, tresc):
    with app.app_context():
        db= get_db()
        c =db.cursor()
        c.execute('INSERT INTO post(tytul, tresc) VALUES(?,?)', (tytul,tresc))
        db.commit()

def czytajPosty():
    with app.app_context():
        return get_db().cursor().execute('SELECT * FROM post').fetchall()

def czytajPost(id):
    with app.app_context():
        cur = get_db().cursor()
        cur.execute('SELECT tytul,tresc FROM post where id=?', str(id))
        return cur.fetchone()

@app.route('/')
@app.route('/index')
def dawajStart():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/posty')
def posty():
    return render_template('posty.html', posty=czytajPosty())

@app.route('/post/<int:id>')
def post(id):
    post = czytajPost(id)
    return render_template('post.html', post = post)

@app.route('/newpost', methods=['GET', 'POST'])
def nowy():
    if request.method == 'GET':
        return render_template('newpost.html')
    elif request.method == 'POST':
        r = request.get_json()
        if(r['tytul'] =='' or r['tresc']==''):
            return json.dumps({'success':False}), 500, {'ContentType':'application/json'}

        dodajPost(r['tytul'], r['tresc'])
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 

if __name__=='__main__':
    app.run(debug=True)

__author__ = 'kamil'
from flask import Flask, render_template, request,json

app = Flask(__name__)
dane = [
        {'id': 1, 'tytul': 'Bylem wczoraj tutaj', 'tresc': 'bylo awesome!'},
        {'id': 2, 'tytul': 'Nowi avengersi', 'tresc': 'nie podobaja mi sie'},
        {'id': 3, 'tytul': 'taki sobie wpis', 'tresc': 'ale bez tresci...'}
    ]

def dodajPost(tresc, tytul):
    dane.append({
        'id': len(dane)+1,
        'tytul': tytul,
        'tresc': tresc
    })

def czytajPosty():
    return dane

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
    posty = czytajPosty()
    post = None
    for p in posty:
        if(p['id'] == id):
            post = p
            break

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

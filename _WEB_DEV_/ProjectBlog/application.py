__author__ = 'kamil'
from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

def czytajPosty():
    return [
        {'id': 1, 'tytul': 'Bylem wczoraj tutaj', 'tresc': 'bylo awesome!'},
        {'id': 2, 'tytul': 'Nowi avengersi', 'tresc': 'nie podobaja mi sie'},
        {'id': 3, 'tytul': 'taki sobie wpis', 'tresc': 'ale bez tresci...'}
    ]

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

@app.route('/post/<string:id>')
def post(id):
    posty = czytajPosty()
    post = None
    for p in posty:
        if(p['id'] == int(id)):
            post = p
            break

    return render_template('post.html', post = post)

@app.route('/newpost', methods=['GET', 'POST'])
def nowy():
    return 'ok'

if __name__=='__main__':
    app.run(debug=True)

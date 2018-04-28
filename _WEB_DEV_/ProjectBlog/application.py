__author__ = 'kamil'
from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

def czytajPosty():
    return [
        {'tytul': 'Bylem wczoraj tutaj', 'tresc': 'bylo awesome!'},
        {'tytul': 'Nowi avengersi', 'tresc': 'nie podobaja mi sie'},
        {'tytul': 'taki sobie wpis', 'tresc': 'ale bez tresci...'}
    ]

@app.route('/')
@app.route('/index')
def dawajStart():
    posty = czytajPosty()
    return render_template('index.html',
    posty=posty)

if __name__=='__main__':
    app.run(debug=True)

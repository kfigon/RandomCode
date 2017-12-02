__author__ = 'kamil'
from flask import Flask

app = Flask(__name__)


@app.route('/')
def foo():
    return '<h1>' \
           'Witaj swiecie,<br> ' \
           'kliknij tu <a href="/piesek">KLIK!</a> ' \
           '</h1>' \

@app.route('/piesek')
def pies():
    return "hello piesek, wpisz adres /gosc/IMIE albo /gosc/LICZBA"

#http://127.0.0.1:5000/gosc/stasiek
@app.route('/gosc/<uzutkownik>')
def userzy(uzutkownik):
    return 'witaj %s' % uzutkownik

#http://127.0.0.1:5000/gosc/456
@app.route('/gosc/<int:dane>')
def dawajDane(dane):
    return 'wpisales: %d' % dane

if __name__=='__main__':
    #app.run(debug=True)
    app.run()
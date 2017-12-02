__author__ = 'kamil'
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def foo():
    return '<h1>' \
           'Witaj swiecie,<br> ' \
           'uzyta metoda: %s<br>' \
           'kliknij tu zeby zrobic post <a href="/piesek">KLIK!</a> ' \
           '</h1>' \
           % request.method

# domyslnie jest GET zawsze, a ta strona moze tez POST
@app.route('/piesek', methods=['GET','POST'])
def pies():
    if(request.method == "GET"):
        return 'uzywamy GET'
    else:
        return 'uzywamy POST'

if __name__=='__main__':
    #app.run(debug=True)
    app.run()

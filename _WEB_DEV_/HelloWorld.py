__author__ = 'kamil'
from flask import Flask

# kontener
app = Flask(__name__)


# dekorator. Doda cala reszte (<html><head><body> itd)
# / strona domowa
@app.route('/')
def foo():
    return '<h1>Witaj swiecie</h1>'


if __name__=='__main__':
    #app.run(debug=True)
    app.run()
    # odpalanie tutaj: http://127.0.0.1:5000/
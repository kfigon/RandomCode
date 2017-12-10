__author__ = 'kamil'
from flask import Flask

# kontener
app = Flask(__name__)

# tip: ubicie procesu
#fuser nrPortu/tcp
#fuser 5000/tcp -k   <-- ubicie portu 5000


# dekorator. Doda cala reszte (<html><head><body> itd)
# / strona domowa
@app.route('/')
def foo():
    return '<h1>Witaj swiecie</h1>'


if __name__=='__main__':
    #app.run(debug=True)
    app.run()
    # odpalanie tutaj: http://127.0.0.1:5000/
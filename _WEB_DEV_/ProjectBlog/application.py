__author__ = 'kamil'
from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def dawajStart():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)

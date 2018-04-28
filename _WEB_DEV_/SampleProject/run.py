__author__ = 'kamil'
from flask import Flask, render_template, request,jsonify

app = Flask(__name__)

def generujPosty():
    return [{'tytulPosta':'tytulik','kontent':'smiesnzy tekst'},
            {'tytulPosta':'tytulik nr2','kontent':'jakis inny tekst'},
            {'tytulPosta':'oho, kolejny','kontent':'blabla'}]


@app.route('/')
@app.route('/index')
def dawajStart():
    user = {'nickname': "Kamil"}
    # render_template korzysta z plikow z katalogu templates!!!

    # podmieni bebechy z htmla dynamicznie
    # rozne frameworki roznie renderuja, flask korzysta z Jinja2
    # wiec sa konstrukcje {% if ... %}
    # albo {% for x in tab %}
    return render_template('index.html',
                           tytulStrony='Strona domowa',
                           user=user,
                           posts=generujPosty())

@app.route('/podstrona')
def dawajPodstrone():
    return render_template('podstrona.html')

@app.route('/wyslij/<napis>', methods=['POST'])
def wyslijDane(napis):
    return render_template('podstrona.html',
                    dodatkowyNapis=napis)

@app.route('/wyslijJsona', methods=['POST'])
def wyslanyJson():
    content = request.json
    print("serwer otrzymal jsona:")
    print(content)
    zwrotka = {'dane':'dziekuje pan javascript'}
    return jsonify(zwrotka)


if __name__=='__main__':
    #app.run(debug=True)
    app.run()
from flask import Flask, abort, render_template, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Exercice 1 & 2

@app.route('/')
def home():
    return render_template('index.html')

## Exercice 1

@app.route('/salutation/<nom>')
def salutation(nom):
    return f"Salut, {nom} !"

@app.route('/calcul/carre/<int:nombre>')
def calcul_carre(nombre):
    carre = nombre ** 2
    return f"Le carré de {nombre} est {carre}."


@app.route('/secret')
def acces_denied():
    abort(401)

@app.route('/status')
def status():
    return "Tout va bien", 200

## Exercice 2

@app.route('/profil/<user_name>')
def profil(user_name):
    user_age = 17
    return render_template('index.html',
                           name=user_name,
                           age=user_age)

@app.route('/utilisateurs')
def user():
    users_dic = ['Alice', 'Bob', 'Charlie', 'Diana']
    return render_template('utilisateurs.html',
                           users=users_dic)


@app.route('/recherche')
def search():
    payload = request.args.get('q')
    return render_template('search.html',
                           data=payload)


if __name__ == "__main__":
    app.run(debug=True)
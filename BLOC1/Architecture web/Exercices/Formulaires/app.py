from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_bootstrap import Bootstrap5
import random

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.secret_key = 'dev-secret-key'

# Route

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/finder')
def finder():
    target_number = random.randint(1, 100)
    session['target_number'] = target_number
    return render_template('finder.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/pizza')
def pizza():
    return render_template('pizzeria.html')

# Exercice 1: Calculatrice

@app.route('/calculatrice', methods=['GET', 'POST'])
def calculatrice():
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            print(num1)
            num2 = float(request.form['num2'])
            print(num2)
            operation = request.form['operation']

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2


            return render_template('index.html', result=result)

        except ValueError:
            return render_template('index.html', error="Invalid input. Please enter numeric values.")

    return render_template('index.html')


# Exercice 2 : Jeu du plus ou moins


    
@app.route('/find_number', methods=['GET', 'POST'])
def find_number():
    target_number = session.get('target_number')
    if target_number is None:
        flash("Début d'une nouvelle partie.")
        return redirect(url_for('finder'))

    if request.method == 'POST':
        try:
            guess_number = int(request.form.get('guess_number', ''))
        except ValueError:
            flash("Veuillez entrer un nombre entier.")
            return render_template('finder.html')

        if guess_number < target_number:
            message = "C'est plus !"
        elif guess_number > target_number:
            message = "C'est moins !"
        else:
            message = "Gagné !"
            session.pop('target_number')

        flash(message)
    return render_template('finder.html')



# Exercice 3
@app.route('/send_message', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message = request.form.get('message', '').strip()

        if not all((name, email, message)):
            flash("Tous les champs sont requis", "error")
        else:
            flash("Message envoyé !", "success")
        
    return redirect(url_for('contact'))

        
# Exercice 4
@app.route('/commander_pizza', methods=['GET', 'POST'])
def commander_pizza():
    if request.method == 'POST':
        taille = request.form.get('taille')
        ingredients = request.form.getlist('ingredients')


        flash(f'Taille :{taille}, Ingrédients : {ingredients}')
    
    return render_template('pizzeria.html')


if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, abort, render_template, request
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

# Exercice #

@app.route('/')
def home():
    return render_template('index.html')

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

if __name__ == "__main__":
    app.run(debug=True)
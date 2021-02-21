from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from flask import flash
import func

app = Flask(__name__)
app.config['SECRET_KEY'] = "oh-so-secret"

@app.route('/', methods=['GET'])
def get_form():
    return render_template('index.html')

# @app.route('/', methods=['POST'])
# def post_form():
#     amount_to = request.form['amountto']
#     amount_from = request.form['amountfrom']
#     amount = request.form['amount']
#     result = func.convert(amount_from, amount_to, amount)
#     return render_template('result.html', converted_amount=result)
@app.route('/result')
def post_form():
    amount_to = request.args['amountto']
    amount_from = request.args['amountfrom']
    print(amount_from)
    amount = request.args['amount']
    try:
        result = func.convert(amount_from, amount_to, amount)
    except:
        flash("INVALID INPUT")
        return render_template('index.html')
    return render_template('result.html', converted_amount=result)
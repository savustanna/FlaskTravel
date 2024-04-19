from flask import Flask, render_template, request, flash
import flask
from .data import tours, title
from model import LoginForm
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcd'

@app.route('/')
def index():
    return render_template('index.html', title=title, tours=tours, status="Log In")

@app.route('/departure/<departure>')
def departure(departure):
    tours = dict(filter(lambda tour: tour[1]["departure"] == departure, data.tours.items()))
    if tours:
        return render_template('departure.html', departure=departure, tours=tours)

@app.route('/tour/<int:id>/')
def tour(id):
    return render_template('tour.html', tour=tours[id], title=title, status="Log In")



@app.route('/login/', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if flask.request.method == "GET":
        return render_template('login.html', form=form, status="Log In")

    if flask.request.method == 'POST':
        with open('users.json', 'r') as file:
            users = json.load(file)
            while users:
                for user in users:
                    if user['login'] == form.login.data and user['password'] == form.password.data:
                        return render_template('index.html', title=title, tours=tours, status=user['login'])

            else:
                flash("Incorrect login credentials!")  #?
                return render_template('login.html', form=form, status="Log In")

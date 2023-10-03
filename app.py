from flask import Flask, render_template, request, redirect, url_for, session, make_response
from requesto import Requesto
import utils.logs as logger
from utils import registrationHandler
from utils.loginHandler import loggingIn
from utils.registrationHandler import registration

db = Requesto.db

app = Flask(__name__)


logger.data(registration("St1zy3", "bastardcom1@gmail.com", "AcrobaTick14@"))


@app.route('/', methods=['POST', 'GET'])
def mainPage():
    if request.method == "POST":
        pass
    else:
        if True:
            redirect(url_for("landing"))
        return render_template("mainPage.html")


@app.route('/signIn', methods=['POST', 'GET'])
def signIn():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        response = loggingIn(login, password)
    else:
        return render_template("loginPage.html")


@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        email = request.form['email']
        response = registration(login, email, password)
        if response != 0:
            pass

    else:
        return render_template("registerPage.html")


@app.route('/landing', methods=['POST', 'GET'])
def landing():
    if request.method == "POST":
        pass
    else:
        return render_template("landing.html")


app.run(debug=False)

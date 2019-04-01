from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

#workers
def is_empty(val):
    if val == '':
        return True
    else:
        return False

def validate_info(data):
    if len(data) < 3 or len(data) > 20 or ' ' in data:
        return False
    else:
        return True

def is_email(email):
    if '@' in email and '.' in email:
        if ' ' in email:
            return False
        return True
    else:
        return False

@app.route("/")
def index():
    return render_template('home.html')

@app.route("/", methods=["POST"])
def validate_user():
    username = request.form['username']
    password = request.form['password']
    valid_pass = request.form['verify-password']
    email = request.form['email']

    name_error = ''
    password_error = ''
    valid_pass_error = ''
    email_error = ''

    if is_empty(username):
        name_error = "Please enter a username"
    elif not validate_info(username):
        name_error = """Please enter a valid username
        (between 3 and 20 characters without spaces"""

    if is_empty(password):
        password_error = "Please enter a password"
    elif not validate_info(password):
        password_error = """Please enter a valid password
        (between 3 and 20 characters without spaces"""

    if is_empty(valid_pass):
        valid_pass_error = "Please verify your password"
    elif valid_pass != password:
        valid_pass_error = "Please make sure both password fields match"

    if email != '':
        if not is_email(email):
            email_error = "Please enter a valid email"

    if not name_error and not password_error and not valid_pass_error and not email_error:
        return render_template('welcome.html', title="Welcome!", message="Welcome, ", username=username)
    else:
        return render_template('home.html', title="Signup", message="Whoops! Got a problem here.", 
        name_error=name_error, password_error=password_error, 
        valid_pass_error=valid_pass_error, email_error=email_error, 
        username=username, email=email)

app.run()
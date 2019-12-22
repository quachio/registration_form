from flask import Flask, render_template, redirect, session, request, flash, get_flashed_messages
import re
import time
from datetime import date

NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$')
BIRTHDATE_REGEX = re.compile(r'^\d{4}[-]\d{2}[-]\d{2}$')

app = Flask(__name__)
app.secret_key = '7VL9f(u]ksirecbW4YMfBmAt37Tb@7MfEk;)i(eeaJMXqi2M2,nD+ya+aD&6gz3P'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register_user():
    print(request.form)

    print(request.form['date'][5:7])
    year = int(request.form['date'][0:4])
    month = int(request.form['date'][5:7])
    day = int(request.form['date'][8:10])

    today = date.today()

    bday = date(year, month, day)    

    print(bday, today)

    # print(today, year, month, day)

    # Validate Email
    if len(request.form['email']) < 1: 
        flash(f"email cannot be blank", 'email')
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!", 'email')
    # Validate First Name
    if len(request.form['first_name']) < 1:
        flash(f'first name cannot be blank', 'first_name')
    elif not NAME_REGEX.match(request.form['first_name']):
        flash(f'first name can only contain letter', 'first_name')
    # Validate Last Name
    if len(request.form['last_name']) < 1:
        flash(f'last name cannot be blank', 'last_name')
    elif not NAME_REGEX.match(request.form['last_name']):
        flash(f'last name cannot be blank', 'last_name')
    # Validate Password
    if len(request.form['password']) < 1:
        flash(f'password cannot be blank', 'password')
    elif len(request.form['password']) < 8:
        flash(f'password should be at least 8 character', 'password')
    elif request.form['password'] != request.form['confirmed_password']:
        flash(f'password and confirm password must match.', 'password')
    elif not PASSWORD_REGEX.match(request.form['password']):
        flash(f'password must contain at least 1 number and 1 capital letter')
    # Validate Confirmed Password
    if len(request.form['confirmed_password']) < 1:
        flash(f'confirmed_password cannot be blank', 'confirmed_password')
    elif len(request.form['confirmed_password']) < 8:
        flash(f'confirmed password should be at least 8 character', 'confirmed_password')
    elif request.form['password'] != request.form['confirmed_password']:
        flash(f'password and confirm password must match.', 'confirmed_password')

    if not BIRTHDATE_REGEX.match(request.form['date']):
        flash(f'please enter proper date format', 'date')
    elif bday > today:
        flash('birthday must be from the past', 'date')



    if '_flashes' in session.keys():
        print(session['_flashes'])
        return redirect('/')
    else:
        return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)
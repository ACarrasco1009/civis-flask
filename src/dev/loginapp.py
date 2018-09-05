from flask import Flask, render_template, redirect, url_for, request
import os
import civis
import hashlib
import uuid

app = Flask(__name__)

@app.route("/")
def home():
    return "Hi!"

@app.route("/new")
def new():
    return "User Created!"

def hash_pword(pword):
    """
    When creating user
    """
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + pword.encode()).hexdigest() + ':' + salt

def validate_pword(hashed_pword, provided_pword):
    """
    When logging in
    """
    _hashedText, salt = hashed_pword.split(':')
    return _hashedText == hashlib.sha256(salt.encode() + provided_pword.encode()).hexdigest()

def get_pword(login):
    if login == '':
        raise IndexError
    client = civis.APIClient(api_key=os.environ['CIVIS_API_KEY'])
    return civis.io.read_civis_sql(sql=f"SELECT pword FROM users.creds WHERE LOWER(login) = '{login.lower()}'",
                                   database='HRC',
                                   client=client,
                                   hidden=True)[1][0]

def create_user(login, pword):
    client = civis.APIClient(api_key=os.environ['CIVIS_API_KEY'])
    try:
        civis.io.read_civis_sql(sql=f"SELECT login FROM users.creds WHERE LOWER(login) = '{login.lower()}'",
                                database='HRC',
                                client=client,
                                hidden=True)[1][0]
        raise ValueError
    except civis.base.EmptyResultError:
        return civis.io.query_civis(sql=f"INSERT INTO users.creds VALUES ({login}, {hash_pword(pword)})",
                                    database='HRC',
                                    client=client,
                                    hidden=True)

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['submit'] == 'Login':
            try:
                hashed_pword = get_pword(request.form['username'])
                if validate_pword(hashed_pword, request.form['password']):
                    return redirect(url_for('home'))
                else:
                    error = 'Invalid pword'
            except IndexError:
                error = 'No user'
        elif request.form['submit'] == 'Create User':
            try:
                create_user(request.form['username'], request.form['password'])
                return redirect(url_for('new'))
            except ValueError:
                error = 'User exists'
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(port=3838)



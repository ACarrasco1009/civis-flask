from flask import Flask, request, render_template, url_for, redirect
from database import db
from config import Config
import models
import os

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


def phone_number_exists(phone_number):
    return models.MobileCommonsProfile.query.filter(models.MobileCommonsProfile.phone_number == phone_number).count() != 0

@app.route("/")
def home():
    return render_template('button.html')

@app.route('/welcome_series', methods=['GET', 'POST'])
def welcome_series_trigger():
    phone_number = request.args.get('phone_number') or ''

    if phone_number_exists(phone_number):
        retval = 'Existing'
    else:
        retval = 'New'
    return retval

if __name__ == '__main__':
    app.run(port=3838)
